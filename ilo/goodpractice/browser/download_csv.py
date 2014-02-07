from five import grok
from Products.CMFCore.interfaces import IContentish
import csv
from cStringIO import StringIO

class DownloadCSV(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('download_csv')

    def render(self):


        out = StringIO()
        writer = csv.writer(out)
       
        #Column Headings
        headings = ['Good Practice',
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

        writer.writerow(headings)
        
        #Rows
        brains = self.context.results()

        for brain in brains:
            obj = brain.getObject()
            row = []
            row.append(obj.title)
            row.append(obj.Creator()) #XXX need to covert to fullname
            row.append(obj.start)
            row.append(obj.end)
            row.append(obj.description)
            row.append(obj.goodpractice_context)
            row.append(obj.goodpractice_cause_effect)
            row.append(obj.goodpractice_indicator)
            row.append(obj.goodpractice_replication)
            row.append(obj.goodpractice_link)
            row.append(obj.goodpractice_keywords)
            row.append(obj.goodpractice_comment)
            writer.writerow(row)
    
        filename = "good_practice.csv"
        self.request.response.setHeader('Content-Type', 'text/csv')
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)

        return out.getvalue()
