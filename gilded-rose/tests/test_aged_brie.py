# -*- coding: utf-8 -*-
import unittest

import src.models as m
from src.gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_increasing_quality(self):
        # "Aged Brie" actually increases in Quality the older it gets
        sell_in = 2
        quality = 2
        items = [Item(m.AGED_BRIAR, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 1, items[0].quality)

    def test_quality_less_than_fifty(self):
        # The Quality of an item is never more than 50
        sell_in = 2
        quality = m.MAX_QUALITY
        items = [Item(m.AGED_BRIAR, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality, items[0].quality)


if __name__ == "__main__":
    unittest.main()
