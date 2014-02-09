from five import grok
from Products.CMFCore.interfaces import IContentish
from Products.CMFPlone.utils import safe_unicode
import csv, codecs, cStringIO


class DownloadCSV(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('download_csv')

    def render(self):

        
       
        #Column Headings
        headings = [  'Good Practice',
                      'Creator',
                      'Start Date',
                      'End Date',
                      'Summary',
                      'Context',
                      'Cause/Effect',
                      'Indicators',
                      'Replication',
                      'Links',
                      'Keywords',
                      'Comments',
                    ]
        
        #Rows
        brains = self.context.results()

        for brain in brains:
            obj = brain.getObject()
            row = []
            row.append(obj.title)
            row.append(obj.Creator()) #XXX need to covert to fullname
            row.append(obj.start.isoformat()) #
            row.append(obj.end.isoformat()) ###XXX needs to be formatted as string
            row.append(obj.description)
            row.append(obj.goodpractice_context)
            row.append(obj.goodpractice_cause_effect)
            row.append(obj.goodpractice_indicator)
            row.append(obj.goodpractice_replication)
            row.append(obj.goodpractice_link)
            row.append(obj.goodpractice_keywords)
            row.append(obj.goodpractice_comment)
        

        out = cStringIO.StringIO()

        import ipdb; ipdb.set_trace()

        writer = UnicodeWriter(self, out)  

        filename = "good_practice.csv"
        self.request.response.setHeader('Content-Type', 'text/csv')
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)

        return out.getvalue()

class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)