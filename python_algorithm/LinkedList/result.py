# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from LinkedList import LinkedList


class Result(object):
    def __init__(self, node: LinkedList, result: bool):
        self.node = node
        self.result = result
