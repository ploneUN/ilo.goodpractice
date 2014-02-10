from five import grok
from Products.CMFCore.interfaces import IContentish
from Products.CMFPlone.utils import safe_unicode
import csv, codecs, cStringIO
from plone import api


class DownloadCSV(grok.View):
    grok.context(IContentish) #FIXME Limit to Collections
    grok.require('zope2.View')
    grok.name('download_csv')

    def render(self):        

        out = cStringIO.StringIO()
        writer = csv.writer(out)
       
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
        

        writer.writerow(headings)

        brains = self.context.results()

        # The following can be refactored into a single useful CSV cleanup library
        # given list of fields, check if None, int, date convert accordingly to string.
        # One might already exist 

        for brain in brains:
            obj = brain.getObject()
            row = []

            if obj.title:
                row.append(obj.title)

            if obj.Creator():
                user = api.user.get(username=obj.Creator())
                if user.fullname:
                    row.append(user.fullname)
                else:
                    row.append(obj.Creator())

            if obj.start:
                row.append(obj.start.isoformat())
            else:
                row.append("")
            
            if  obj.end:
                row.append(obj.end.isoformat())
            else:
                row.append("")
            
            if obj.description:
                row.append(obj.description)
            else:
                row.append("")
            
            if obj.goodpractice_context:
                row.append(obj.description)
            else:
                row.append("")
            
            if obj.goodpractice_cause_effect:
                row.append(obj.goodpractice_cause_effect)
            else:
                row.append("")
            
            if obj.goodpractice_indicator:
                row.append(obj.goodpractice_indicator)
            else:
                row.append("")
            
            if obj.goodpractice_replication:
                row.append(obj.goodpractice_replication)
            else:
                row.append("")
            
            if obj.goodpractice_link:
                row.append(obj.goodpractice_link)
            else:
                row.append("")

            if obj.goodpractice_keywords:
                row.append(obj.goodpractice_keywords)
            else:
                row.append("")

            if obj.goodpractice_comment:
                row.append(obj.goodpractice_comment)
            else:
                row.append("")
        
            writer.writerow([s.encode('utf-8') for s in row])

        filename = "good_practice.csv"
        self.request.response.setHeader('Content-Type', 'text/csv')
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)

        return out.getvalue()
