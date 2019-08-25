import logging

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from sorl_cropping import ImageCroppingMixin

from . import rr_api
from .models import Category, Episode, HighlightedPost, Post, Settings, Show

logger = logging.getLogger(__name__)


class ShowFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        shows = Show.objects.filter(archived=self.archived)
        return [(show.id, str(show)) for show in shows]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(show=self.value())
        else:
            return queryset


class ActiveShowFilter(ShowFilter):
    title = 'aktive programmer'
    parameter_name = 'show'
    archived = False


class ArchivedShowFilter(ShowFilter):
    title = 'arkiverte programmer'
    parameter_name = 'show'
    archived = True


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Brødtekst')

    class Meta:
        model = Post
        fields = '__all__'


class SettingsAdminForm(forms.ModelForm):
    about = forms.CharField(widget=CKEditorUploadingWidget(), label='Om Radio Revolt')
    privacy_policy = forms.CharField(widget=CKEditorUploadingWidget(), label='Personvernerklæring')

    class Meta:
        model = Settings
        fields = '__all__'


def get_show_options():
    try:
        shows = rr_api.get_shows()
    except Exception:
        logger.exception('Failed to fetch choices for Digas shows')
        return []

    def process_shows(predicate):
        filtered_shows = filter(predicate, shows)
        as_choices = map(lambda s: (s['id'], s['name']), filtered_shows)
        return tuple(as_choices)

    # Filter into archived and active
    old_shows = process_shows(lambda s: s['old'])
    active_shows = process_shows(lambda s: not s['old'])

    return (
        (None, '--------'),
        ('Aktive programmer', active_shows),
        ('Arkiverte programmer', old_shows),
    )


class ShowAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='small'), label='Lang beskrivelse')

    digas_id = forms.TypedChoiceField(
        coerce=int,
        empty_value=None,
        required=False,
        label='Tilhørende Digas-program',
        choices=get_show_options,
    )

    class Meta:
        model = Show
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ensure that the digas_id is not lost when the list of Digas shows is unavailable.
        # Inspired by
        # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html

        # What choices are available? Cast to list to evaluate the function
        digas_shows = list(self.fields['digas_id'].choices)

        if not digas_shows:
            # Failed to fetch shows, fall back to option with current value
            if 'digas_id' in self.data:
                # From submitted form data
                digas_id = self.data['digas_id']
            elif self.instance.digas_id:
                # From the Show model instance
                digas_id = self.instance.digas_id
            else:
                # No Digas show selected
                digas_id = None
            # Create the fallback choices list
            digas_shows = [(digas_id, 'Uforandret (fikk ikke hentet alternativer)')]

        # Update the choices (this way, we also evaluate the choices function only once)
        self.fields['digas_id'].choices = digas_shows


class EpisodeAdminForm(forms.ModelForm):
    # lead = forms.CharField(
    #   widget=CKEditorUploadingWidget(config_name='small'), label='Beskrivelse')

    class Meta:
        model = Episode
        fields = '__all__'


class HighlightedPostAdminForm(forms.ModelForm):
    def clean_posts(self):
        posts = self.cleaned_data['posts']
        if len(posts) > 5:
            raise forms.ValidationError("Du kan ikke fremheve mer enn 5 artikler.")
        return posts

    class Meta:
        model = HighlightedPost
        fields = '__all__'


@admin.register(Post)
class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at', 'ready_to_be_published', 'deleted')
    list_filter = ('deleted', 'publish_at', 'show')
    search_fields = ('title', 'show__name')
    form = PostAdminForm

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.show:
            show_episodes = Episode.objects.filter(show=obj.show)
            form.base_fields['episodes'].queryset = show_episodes
        return form

    # Set form field for "lead" to Textarea instead of Textinput
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'lead':
            formfield.widget = forms.Textarea(attrs={'cols': 60, 'rows': 5})
        return formfield


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Settings)
class SettingsAdmin(SingletonModelAdmin):
    form = SettingsAdminForm


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'archived', 'is_podcast')
    list_filter = ('archived', 'is_podcast')
    ordering = ('archived', 'name')
    search_fields = ('name', )
    form = ShowAdminForm
    actions = ('make_podcast', 'unmake_podcast')

    def make_podcast(self, request, queryset):
        return self._bulk_update_is_podcast(request, queryset, True, '{} program(mer) ble '
                                            'markert som podkast')

    make_podcast.short_description = 'Marker som podkast'

    def unmake_podcast(self, request, queryset):
        return self._bulk_update_is_podcast(request, queryset, False, '{} program(mer) er ikke '
                                            'lenger markert som podkast')

    unmake_podcast.short_description = 'Fjern podkast-markering'

    def _bulk_update_is_podcast(self, request, queryset, is_podcast, message):
        rows_updated = queryset.update(is_podcast=is_podcast)
        self.message_user(request, message.format(rows_updated))


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'show', 'publish_at')
    list_filter = (ActiveShowFilter, ArchivedShowFilter)
    search_fields = ('title', 'show__name')
    form = EpisodeAdminForm


@admin.register(HighlightedPost)
class HighlightedPostAdmin(SingletonModelAdmin):
    form = HighlightedPostAdminForm
