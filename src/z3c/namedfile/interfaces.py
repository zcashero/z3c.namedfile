# -*- coding: utf-8 -*-

# zope imports
from zope import schema
from zope.app.file.interfaces import IFile, IImage
from zope.interface import Interface
from zope.schema.interfaces import IObject

try:
    from z3c.blobfile.interfaces import IBlobFile, IBlobImage
    HAVE_BLOBS = True
except ImportError:
    HAVE_BLOBS = False


class INamed(Interface):
    """An item with a filename."""

    filename = schema.TextLine(title=u"Filename", required=False, default=None)


class INamedFile(INamed, IFile):
    """A non-BLOB file with a filename."""


class INamedImage(INamed, IImage):
    """A non-BLOB image with a filename."""


class INamedField(IObject):
    """Base field type."""


class INamedFileField(INamedField):
    """Field for storing INamedFile objects."""


class INamedImageField(INamedField):
    """Field for storing INamedImage objects."""


if HAVE_BLOBS:

    class IBlobby(Interface):
        """Marker interface for objects that support blobs."""
