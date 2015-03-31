from django.conf.urls import include, patterns, url

from .views import StyleguideSectionListView, StyleguideSectionView


styleguide_patterns = patterns('',  # NOQA
    url(r'^styleguide/index/$', StyleguideSectionListView.as_view(
        template_name='django-pykss-styleguide/styleguide_list.html'), name='styleguide_list'),
    url(r'^styleguide/section/(?P<section_id>\d+)/$', StyleguideSectionView.as_view(
        template_name='django-pykss-styleguide/styleguide.html'), name='styleguide'),
)

urlpatterns = patterns('',  # NOQA
    url(r'^', include(styleguide_patterns)),
)
