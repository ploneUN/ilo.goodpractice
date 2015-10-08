from z3c.form.interfaces import NO_VALUE
from Products.CMFPlone.utils import safe_unicode

def render_value_patch(self, obj):
        """Gets the value to render in excel file from content value
        """
        value = self.get_value(obj)
        if not value or value == NO_VALUE:
            return ""

        text = safe_unicode(self._get_text(value))

        return text