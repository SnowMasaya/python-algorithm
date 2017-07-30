# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from typing import Any


class LinkedList(object):

    def __init__(self, current_node: str=None,
                 next_node: Any=None)-> None:
        self.current = current_node
        self.next = next_node

    def __str__(self) -> str:
        return str(self.current)

