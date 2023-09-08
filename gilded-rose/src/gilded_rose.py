# -*- coding: utf-8 -*-
import src.models as m
from src.item import Item


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            self._update_quality_of_single_item(item)

    def _update_quality_of_single_item(self, item: Item) -> None:
        if item.name == m.AGED_BRIAR:
            self._increase_quality(item)
            self._decrease_sellin_date(item)

        elif item.name == m.BACKSTAGE_PASS:
            if item.sell_in <= 0:
                self._drop_quality(item)
            elif item.sell_in < 6:
                self._increase_quality(item, 3)
            elif item.sell_in < 11:
                self._increase_quality(item, 2)
            else:
                self._increase_quality(item)
            self._decrease_sellin_date(item)

        elif item.name == m.SULFURAS:
            pass

        else:
            self._decrease_quality(item)
            if item.sell_in <= 0:
                self._decrease_quality(item)
            self._decrease_sellin_date(item)

    def _decrease_quality(self, item: Item, amount: int = 1) -> None:
        item.quality = max(0, item.quality - amount)

    def _increase_quality(self, item: Item, amount: int = 1) -> None:
        item.quality = min(m.MAX_QUALITY, item.quality + amount)

    def _decrease_sellin_date(self, item: Item) -> None:
        item.sell_in -= 1

    def _drop_quality(self, item: Item) -> None:
        item.quality = 0
