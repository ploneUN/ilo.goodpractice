from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class GoodPracticeListing(grok.View):
    grok.context(IContentish)
    grok.name('goodpracticelisting')
    grok.require('zope2.View')
    grok.template('goodpracticelisting')

    def goodpracticefields(self):
        data = [
            ('Title', 'Good Practice'),
            ('eval_theme', 'Themes'),
            ('Creator', 'Creator'),
            ('start', 'Start'),
            ('end', 'End'),
            ('description', 'Summary'),
            ('goodpractice_context', 'Context'),
            ('goodpractice_cause_effect', 'Cause/Effect'),
            ('goodpractice_indicator', 'Indicators'),
            ('goodpractice_replication', 'Replication'),
            ('goodpractice_link', 'Links'),
            ('goodpractice_keywords', 'Keywords'),
            ('goodpractice_comment', 'Comments'),
            ]
        return data
