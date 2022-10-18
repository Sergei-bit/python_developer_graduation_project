# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from astrobox.core import Drone


class StrategyInterface(ABC):

    def __init__(self, unit: Drone):
        self.unit = unit

    @abstractmethod
    def action(self):
        pass

    def on_born(self):
        pass

    def on_stop_at_asteroid(self, asteroid):
        pass

    def on_load_complete(self):
        pass

    def on_stop_at_mothership(self, mothership):
        pass

    def on_unload_complete(self):
        pass

    def on_stop_at_point(self, target):
        pass

    def on_wake_up(self):
        pass

    def move_at(self):
        pass

    def on_stop_at_target(self, target):
        pass
