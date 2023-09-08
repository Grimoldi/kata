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
        if item.name != m.AGED_BRIAR and item.name != m.BACKSTAGE_PASS:
            if item.name != m.SULFURAS:
                self._decrease_quality(item)
        else:
            self._increase_quality(item)
            if item.name == m.BACKSTAGE_PASS:
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1
        if item.name != m.SULFURAS:
            self._decrease_sellin_date(item)
        if item.sell_in < 0:
            if item.name != m.AGED_BRIAR:
                if item.name != m.BACKSTAGE_PASS:
                    if item.quality > 0:
                        if item.name != m.SULFURAS:
                            self._decrease_quality(item)
                else:
                    self._drop_quality(item)
            else:
                self._increase_quality(item)

    def _decrease_quality(self, item: Item, amount: int = 1) -> None:
        item.quality = max(0, item.quality - amount)

    def _increase_quality(self, item: Item, amount: int = 1) -> None:
        item.quality = min(m.MAX_QUALITY, item.quality + amount)

    def _decrease_sellin_date(self, item: Item) -> None:
        item.sell_in -= 1

    def _drop_quality(self, item: Item) -> None:
        item.quality = 0
