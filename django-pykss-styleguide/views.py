from pykss.contrib.django.views import StyleguideView

from collections import OrderedDict


class StyleguideMixin(object):
    def get_ordered_sections(self, sections):
        sections = OrderedDict(sorted(sections.items(), key=lambda t: t[0]))
        return sections

    def get_ordered_section_headers(self, sections):
        ordered_sections = self.get_ordered_sections(sections)
        headers = [(section, y[section].description)
                   for section in ordered_sections
                   if len(section.split('.')) == 1]
        return headers


class StyleguideSectionListView(StyleguideView, StyleguideMixin):
    def get_context_data(self, **kwargs):
        context = super(StyleguideSectionListView, self).get_context_data(**kwargs)
        d = context['styleguide'].sections
        context.update({'section_headers': self.get_ordered_section_headers(d)})
        return context


class StyleguideSectionView(StyleguideView, StyleguideMixin):
    def get_context_data(self, **kwargs):
        context = super(StyleguideSectionView, self).get_context_data(**kwargs)
        d = context['styleguide'].sections
        section_headers = self.get_ordered_section_headers(d)
        section_id = int(context['section_id'])
        # section headers is 0 indexed, styleguide starts at 1
        page_title = section_headers[section_id - 1][1]
        context.update({
            'section_headers': section_headers,
            'page_title': page_title})
        return context
