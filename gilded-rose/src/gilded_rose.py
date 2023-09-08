# -*- coding: utf-8 -*-

import models as m
import updater as u
from item import Item

updater_mapping = {
    m.AGED_BRIAR: u.AgedBrieUpdater(),
    m.BACKSTAGE_PASS: u.BackstagePassUpdater(),
    m.SULFURAS: u.SulfurasUpdater(),
    m.CONJURED: u.ConjuredUpdater(),
}


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            self._update_quality_of_single_item(item)

    def _update_quality_of_single_item(self, item: Item) -> None:
        updater = self._get_updater(item)
        updater.update_quality(item)
        updater.update_sellin(item)

    def _get_updater(self, item: Item) -> u.ItemUpdater:
        return updater_mapping.get(item.name, u.DefaultUpdater())
