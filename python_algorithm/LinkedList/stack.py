# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.imtes == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.imtems.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
