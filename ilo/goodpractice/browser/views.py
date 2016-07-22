from ilo.goodpractice.behavior.check_facetednavigation import CheckFacetedNavigation
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter

class IntegrationJavascriptHelper(grok.View):
    grok.context(Interface)
    grok.name('integration_javascript')
    
    def render(self):
        
        return self.context.unrestrictedTraverse('@@faceted_subtyper/is_faceted')