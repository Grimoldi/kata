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

    def test_standard_quality_degradation(self):
        # At the end of each day our system lowers both values for every item
        sell_in = 1
        quality = 2
        items = [Item("foo", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality - 1, items[0].quality)

    def test_double_quality_degradation(self):
        # Once the sell by date has passed, Quality degrades twice as fast
        sell_in = 0
        quality = 2
        items = [Item("foo", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality - 2, items[0].quality)

    def test_positive_quality(self):
        # The Quality of an item is never negative
        sell_in = 0
        quality = 0
        items = [Item("foo", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == "__main__":
    unittest.main()
