from collective.grok import gs
from ilo.goodpractice import MessageFactory as _

@gs.importstep(
    name=u'ilo.goodpractice', 
    title=_('ilo.goodpractice import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.goodpractice.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
