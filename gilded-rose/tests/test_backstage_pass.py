# -*- coding: utf-8 -*-
import unittest

import src.models as m
from src.gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_backstage_quality_default_increase(self):
        """Backstage passes, like aged brie, increases in Quality as its SellIn value approaches;"""
        sell_in = 20
        quality = 25
        items = [Item(m.BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 1, items[0].quality)

    def test_backstage_quality_default_increase_le_fifty(self):
        """
        Backstage passes, like aged brie, increases in Quality as its SellIn value approaches;
        The Quality of an item is never more than 50
        """
        sell_in = 20
        quality = m.MAX_QUALITY
        items = [Item(m.BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(m.MAX_QUALITY, items[0].quality)

    def test_backstage_quality_double_increase(self):
        """Quality increases by 2 when there are 10 days or less"""
        sell_in = 10
        quality = 25
        items = [Item(m.BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 2, items[0].quality)

    def test_backstage_quality_double_increase_le_fifty(self):
        """
        Quality increases by 2 when there are 10 days or less
        The Quality of an item is never more than 50
        """
        sell_in = 10
        quality = m.MAX_QUALITY - 1
        items = [Item(m.BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(m.MAX_QUALITY, items[0].quality)

    def test_backstage_quality_triple_increase(self):
        """Quality increases by 3 when there are 5 days or less"""
        sell_in = 5
        quality = 25
        items = [Item(m.BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 3, items[0].quality)

    def test_backstage_quality_triple_increase_le_fifty(self):
        """Quality increases by 3 when there are 5 days or less
        The Quality of an item is never more than 50
        """
        sell_in = 5
        quality = m.MAX_QUALITY - 2
        items = [Item(m.BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(m.MAX_QUALITY, items[0].quality)

    def test_backstage_quality_drop(self):
        """Quality drops to 0 after the concert"""
        sell_in = 0
        quality = 25
        items = [Item(m.BACKSTAGE_PASS, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == "__main__":
    unittest.main()
