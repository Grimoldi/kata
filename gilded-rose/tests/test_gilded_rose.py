# -*- coding: utf-8 -*-
import unittest

import src.models as m
from src.gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


if __name__ == "__main__":
    unittest.main()
