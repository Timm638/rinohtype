# This file is part of RinohType, the Python document preparation system.
#
# Copyright (c) Brecht Machiels.
#
# Use of this source code is subject to the terms of the GNU Affero General
# Public License v3. See the LICENSE file or http://www.gnu.org/licenses/.


from ...flowable import DummyFlowable
from ...text import SingleStyledText
from ..rst import BodyElement, BodySubElement, InlineElement, GroupingElement
from ..rst.nodes import AdmonitionBase


__all__ = ['Compact_Paragraph', 'Index', 'SeeAlso', 'Glossary']


class Compact_Paragraph(GroupingElement):
    pass


class Index(BodyElement, InlineElement):
    def build_styled_text(self):
        return SingleStyledText('')

    def build_flowable(self):
        return DummyFlowable()


class SeeAlso(AdmonitionBase):
    title = 'See also'


class Glossary(GroupingElement):
    pass
