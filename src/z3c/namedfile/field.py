# -*- coding: utf-8 -*-

# zope imports
from zope.interface import implements
from zope.schema import Object

# local imports
from z3c.namedfile.file import NamedFile as FileValueType
from z3c.namedfile.file import NamedImage as ImageValueType
from z3c.namedfile.interfaces import (HAVE_BLOBS, INamedFile, INamedFileField,
    INamedImage, INamedImageField)

if HAVE_BLOBS:
    pass


class NamedFile(Object):
    """A NamedFile field."""
    implements(INamedFileField)

    _type = FileValueType
    schema = INamedFile

    def __init__(self, **kw):
        if 'schema' in kw:
            self.schema = kw.pop('schema')
        super(NamedFile, self).__init__(schema=self.schema, **kw)


class NamedImage(Object):
    """A NamedImage field."""
    implements(INamedImageField)

    _type = ImageValueType
    schema = INamedImage

    def __init__(self, **kw):
        if 'schema' in kw:
            self.schema = kw.pop('schema')
        super(NamedImage, self).__init__(schema=self.schema, **kw)
