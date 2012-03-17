
from .paragraph import Paragraph
from . import text


def factory(cls):
    def __init__(self, string, y_offset=0):
        return super(self.__class__, self).__init__(str(string), y_offset)
    space = {'__init__': __init__}
    return type(cls.__name__, (cls, ), space)


Italic = factory(text.Italic)
Oblique = factory(text.Italic)

Bold = factory(text.Bold)
Light = factory(text.Bold)

Underline = factory(text.Bold)

Superscript = factory(text.Superscript)
Subscript = factory(text.Subscript)

SmallCaps = factory(text.SmallCaps)


##class Bibliography(Paragraph):
##    def __init__(self, items):
##        return super().__new__(self, items, style=None)
