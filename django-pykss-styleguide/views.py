from pykss.contrib.django.views import StyleguideView

from collections import OrderedDict


class StyleguideMixin(object):
    def get_ordered_sections(self, sections):
        sections = OrderedDict(sorted(sections.items(), key=lambda t: t[0]))
        return sections

    def get_ordered_section_headers(self, sections):
        headers = []
        ordered_sections = self.get_ordered_sections(sections)
        for section in ordered_sections:
            section_name = section
            if len(section_name.split('.')) == 1:
                # Found the next section
                headers.append((section_name, ordered_sections[section].description,))
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
        # section headers is 0 indexed
        page_title = section_headers[section_id - 1][1]
        context.update({
            'section_headers': section_headers,
            'page_title': page_title})
        return context
