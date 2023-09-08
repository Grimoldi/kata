# -*- coding: utf-8 -*-
import unittest

import src.models as m
from src.gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_standard_quality_degradation(self):
        # "Conjured" items degrade in Quality twice as fast as normal items
        sell_in = 1
        quality = 4
        items = [Item(m.CONJURED_BREAD, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality - 2, items[0].quality)

    def test_double_quality_degradation(self):
        # "Conjured" items degrade in Quality twice as fast as normal items
        sell_in = 0
        quality = 4
        items = [Item(m.CONJURED_BREAD, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality - 4, items[0].quality)

    def test_positive_quality(self):
        # The Quality of an item is never negative
        sell_in = 0
        quality = 2
        items = [Item(m.CONJURED_BREAD, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == "__main__":
    unittest.main()
