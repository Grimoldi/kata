from typing import Protocol

import src.models as m
from src.item import Item


class ItemUpdater(Protocol):
    def update_sellin(self, item: Item) -> None:
        ...

    def update_quality(self, item: Item) -> None:
        ...


class DefaultUpdater:
    """
    All items have a SellIn value which denotes the number of days we have to sell the item
    All items have a Quality value which denotes how valuable the item is
    At the end of each day our system lowers both values for every item
    Once the sell by date has passed, Quality degrades twice as fast
    The Quality of an item is never negative
    """

    def update_sellin(self, item: Item) -> None:
        _decrease_sellin_date(item)

    def update_quality(self, item: Item) -> None:
        if item.sell_in > 0:
            amount = 1
        else:
            amount = 2
        _decrease_quality(item, amount)


class AgedBrieUpdater:
    """Aged Brie actually increases in Quality the older it gets"""

    def update_sellin(self, item: Item) -> None:
        _decrease_sellin_date(item)

    def update_quality(self, item: Item) -> None:
        _increase_quality(item)


class BackstagePassUpdater:
    """
    Backstage passes, like aged brie, increases in Quality as its SellIn value approaches;
    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert
    """

    def update_sellin(self, item: Item) -> None:
        _decrease_sellin_date(item)

    def update_quality(self, item: Item) -> None:
        if item.sell_in <= 0:
            _drop_quality(item)
        elif item.sell_in < 6:
            _increase_quality(item, 3)
        elif item.sell_in < 11:
            _increase_quality(item, 2)
        else:
            _increase_quality(item)


class ConjuredUpdater:
    """Conjured items degrade in Quality twice as fast as normal items"""

    def update_sellin(self, item: Item) -> None:
        _decrease_sellin_date(item)

    def update_quality(self, item: Item) -> None:
        if item.sell_in > 0:
            amount = 2
        else:
            amount = 4
        _decrease_quality(item, amount)


class SulfurasUpdater:
    """Sulfuras, being a legendary item, never has to be sold or decreases in Quality"""

    def update_sellin(self, item: Item) -> None:
        pass

    def update_quality(self, item: Item) -> None:
        pass


def _decrease_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(m.MIN_QUALITY, item.quality - amount)


def _increase_quality(item: Item, amount: int = 1) -> None:
    item.quality = min(m.MAX_QUALITY, item.quality + amount)


def _decrease_sellin_date(item: Item) -> None:
    item.sell_in -= 1


def _drop_quality(item: Item) -> None:
    item.quality = m.MIN_QUALITY
