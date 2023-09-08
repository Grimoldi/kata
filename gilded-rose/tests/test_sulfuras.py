# -*- coding: utf-8 -*-
import unittest

import src.models as m
from src.gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_unchange_quality(self):
        """Sulfuras, being a legendary item, never has to be sold or decreases in Quality"""
        sell_in = 2
        quality = 25
        items = [Item(m.SULFURAS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality, items[0].quality)

    def test_sulfuras_unchange_sellin(self):
        """Sulfuras, being a legendary item, never has to be sold or decreases in Quality"""
        sell_in = 2
        quality = 25
        items = [Item(m.SULFURAS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in, items[0].sell_in)


if __name__ == "__main__":
    unittest.main()
