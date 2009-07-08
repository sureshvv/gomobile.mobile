__license__ = "GPL 2.1"
__copyright__ = "2009 Twinapex Research"

from zope.component import getUtility, queryUtility

from Products.CMFCore.Skinnable import SkinnableObjectManager
from Products.CMFCore.utils import getToolByName

from interfaces import IMobileUtility

# Apply monkeypatches
import monkeypatch

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
