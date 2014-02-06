from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from ilo.goodpractice import MessageFactory as _


# Interface class; used to define content-type schema.

class IILOGoodPracticeForm(form.Schema, IImageScaleTraversable):
    """
    Good Practice Form
    """
    title = schema.TextLine(
        title=_(u'Evaluation Title'),
        description=u'',
        required=True,
        )

    description = schema.Text(
        title=_(u'Brief summary of the good practice'),
        description=_(u'Brief summary of the good practice (link to'
                      u' project goal or specific deliverable, background,'
                      u' purpose, etc.'),
        required=True,
        )

    start = schema.Date(
        title=_(u'Project start'),
        description=u'',
        required=True,
        )

    end = schema.Date(
        title=_(u'Project end'),
        description=u'',
        required=True,
        )

    goodpractice_project = schema.TextLine(
        title=_(u'Project TC/SYMBOL'),
        description=u'',
        required=True,
        )

    goodpractice_evaluator = schema.TextLine(
        title=_(u'Evaluator'),
        description=u'Name of Evaluator',
        required=True,
        )

    goodpractice_context = schema.Text(
        title=_(u'Relevant conditions and Context'),
        description=_(u'Relevant conditions and Context: limitations or advice'
                      u' in terms of applicability  and replicability'),
        required=True,
        )

    goodpractice_cause_effect = schema.Text(
        title=_(u'Cause-effect relationship'),
        description=_(u'Establish a clear cause-effect relationship'),
        required=True,
        )

    goodpractice_indicator = schema.Text(
        title=_(u'Measurable impact'),
        description=_(u'Indicate measurable impact and targeted'
                      u' beneficiaries'),
        required=True,
        )

    goodpractice_replication = schema.Text(
        title=_(u'Potential for replication'),
        description=_(u'Potential for replication and by whom'),
        required=True,
        )

    goodpractice_link = schema.Text(
        title=_(u'Upward links to higher ILO Goals'),
        description=_(u'Upward links to higher ILO Goals (DWCPs,'
                      u" Country Programme Outcomes or ILO's Strategic"
                      u' Programme Framework)'),
        required=True,
        )

    goodpractice_comment = schema.Text(
        title=_(u'Other documents'),
        description=_(u'Other documents or relevant comments'),
        required=True,
        )


alsoProvides(IILOGoodPracticeForm, IFormFieldProvider)
