from five import grok
from plone.directives import dexterity, form
from ilo.goodpractice.content.ilo_good_practice_form import IILOGoodPracticeForm

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IILOGoodPracticeForm)
    grok.require('zope2.View')
    grok.template('ilo_good_practice_form_view')
    grok.name('view')

