# -*- coding: utf-8 -*-

import random
from astrobox.core import Drone
from hangar_2022.strategy_osadchy.strategy_interface import StrategyInterface


class ResourceCollector(StrategyInterface):
    """Сборщик ресурсов"""

    def __init__(self, unit: Drone):
        super().__init__(unit)

    def action(self):
        if self.unit.health != 100:
            self.unit.move_at(self.unit.mothership)

    def on_stop_at_asteroid(self, asteroid):
        asteroids_list = self.unit.search_for_asteroids()
        if asteroid.payload != 0:
            self.unit.turn_to(self.unit.mothership)
            self.unit.load_from(asteroid)
        elif asteroids_list:
            self.unit.move_at(random.choice(asteroids_list))
        else:
            self.unit.move_at(self.unit.mothership)

    def on_load_complete(self):
        if self.unit.fullness == 1.0:
            self.unit.move_at(self.unit.mothership)
        elif self.unit.fullness != 1.0:
            asteroids_list = self.unit.search_for_asteroids()
            if asteroids_list:
                self.unit.move_at(random.choice(asteroids_list))
            else:
                self.unit.move_at(self.unit.mothership)

    def on_stop_at_mothership(self, mothership):
        asteroids_list = self.unit.search_for_asteroids()
        if mothership is self.unit.mothership:
            if asteroids_list:
                self.unit.turn_to(random.choice(asteroids_list))
            self.unit.unload_to(mothership)

    def on_unload_complete(self):
        self.unit.enable_protection = False
        asteroids_list = self.unit.search_for_asteroids()
        if asteroids_list:
            self.unit.move_at(random.choice(asteroids_list))
        else:
            self.unit.enable_protection = True

    def on_wake_up(self):
        self.on_unload_complete()


class CollectBaseResources(StrategyInterface):
    """Забрать Ресурсы Базы"""

    def __init__(self, unit: Drone):
        super().__init__(unit)

        self.destroyed_base = self.unit.get_destroyed_base()
        if self.destroyed_base:
            self.unit.move_at(self.destroyed_base)

    def action(self):
        pass

    def on_stop_at_mothership(self, mothership):
        if mothership is not self.unit.mothership and mothership.payload != 0:
            self.unit.load_from(mothership)
        elif mothership is self.unit.mothership:
            self.unit.unload_to(mothership)

    def on_load_complete(self):
        if self.unit.fullness == 1.0:
            self.unit.move_at(self.unit.mothership)
        elif self.unit.fullness != 1.0:
            self.unit.move_at(self.unit.mothership)

    def on_unload_complete(self):
        if self.destroyed_base and self.destroyed_base.payload != 0:
            self.unit.move_at(self.destroyed_base)

    def on_wake_up(self):
        self.unit.move_at(self.unit.mothership)


class DroneResourceGathering(StrategyInterface):
    """Сбор Ресурса Дрона"""

    def __init__(self, unit: Drone):
        super().__init__(unit)

    def action(self):
        """действие"""
        target = self.find_destroyed_enemy_drones()
        if target:
            self.unit.move_at(target)
        if target and round(self.unit.x) == round(target.x) and round(self.unit.y) == round(target.y) and target.payload != 0:
            self.unit.load_from(target)
        if self.unit.fullness == 1.0:
            self.unit.move_at(self.unit.mothership)
        if self.unit.fullness != 1.0 and not target:
            self.unit.move_at(self.unit.mothership)
            self.unit.broken_drones_elyrium_zero = True
        if not target:
            self.unit.move_at(self.unit.mothership)
            self.unit.broken_drones_elyrium_zero = True
        if target and round(self.unit.x) == round(target.x) and round(self.unit.y) == round(target.y) and self.unit.fullness == 1.0:
            self.unit.move_at(self.unit.mothership)
        elif target and round(self.unit.x) == round(target.x) and round(self.unit.y) == round(target.y) and self.unit.fullness != 1.0:
            self.unit.move_at(self.unit.mothership)

    def find_destroyed_enemy_drones(self):
        """найти унечтоженные вражеские дроны"""
        for enemy in self.unit.scene.drones:
            if not enemy.is_alive and self.unit.mothership.distance_to(enemy) < self.unit.distance_to_destroyed_drones and enemy.payload != 0:
                return enemy

    def on_stop_at_mothership(self, mothership):
        if mothership is self.unit.mothership:
            self.unit.unload_to(mothership)

    def on_wake_up(self):
        self.action()


class AdditionalElyriumGathering(StrategyInterface):
    """Дополнительный Сбор Элириума"""

    def __init__(self, unit: Drone):
        super().__init__(unit)
        asteroids_list = self.unit.search_for_asteroids()
        if asteroids_list:
            self.unit.move_at(random.choice(asteroids_list))

    def action(self):
        if self.unit.health != 100:
            self.unit.move_at(self.unit.mothership)

    def on_stop_at_asteroid(self, asteroid):
        asteroids_list = self.unit.search_for_asteroids()
        if asteroid.payload != 0:
            self.unit.turn_to(self.unit.mothership)
            self.unit.load_from(asteroid)
        elif asteroids_list:
            self.unit.move_at(random.choice(asteroids_list))
        else:
            self.unit.move_at(self.unit.mothership)

    def on_load_complete(self):
        if self.unit.fullness == 1.0:
            self.unit.move_at(self.unit.mothership)
        elif self.unit.fullness != 1.0:
            asteroids_list = self.unit.search_for_asteroids()
            if asteroids_list:
                self.unit.move_at(random.choice(asteroids_list))
            else:
                self.unit.move_at(self.unit.mothership)

    def on_stop_at_mothership(self, mothership):
        asteroids_list = self.unit.search_for_asteroids()
        if mothership is self.unit.mothership:
            if asteroids_list:
                self.unit.turn_to(random.choice(asteroids_list))
            self.unit.unload_to(mothership)

    def on_unload_complete(self):
        self.unit.enable_protection = False
        asteroids_list = self.unit.search_for_asteroids()
        if asteroids_list:
            self.unit.move_at(random.choice(asteroids_list))
        elif not asteroids_list:
            self.unit.no_asteroids = True

    def on_wake_up(self):
        self.on_unload_complete()
