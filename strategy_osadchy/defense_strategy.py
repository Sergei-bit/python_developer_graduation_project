# -*- coding: utf-8 -*-

from astrobox.core import Drone
from robogame_engine.geometry import Point
from hangar_2022.strategy_osadchy.strategy_interface import StrategyInterface


class DefensePosition:
    """Позиция Защиты"""
    position_on_x = {}
    position_on_y = {}
    additional_position_x = {}
    additional_position_y = {}


class Protection(StrategyInterface):
    """Защита"""

    def __init__(self, unit: Drone):
        super().__init__(unit)

        self.field_width = self.unit.scene.field[0]      # ширина поля
        self.field_height = self.unit.scene.field[1]     # высота поля

        """выход на позиции"""
        if self.unit.mothership.x < self.field_width / 2 and self.unit.mothership.y < self.field_height / 2:
            DefensePosition.position_on_x = dict(
                zip(self.unit.list_of_my_drones(), list(range(50, 325, 55))))
            DefensePosition.position_on_y = dict(
                zip(self.unit.list_of_my_drones(), list(range(250, 50, -40))))
            self.unit.move_at(
                Point(
                    DefensePosition.position_on_x[self.unit],
                    DefensePosition.position_on_y[self.unit]
                )
            )
        elif self.unit.mothership.x > self.field_width / 2 and self.unit.mothership.y < self.field_height / 2:
            DefensePosition.position_on_x = dict(zip(self.unit.list_of_my_drones(), list(
                range(self.field_width - 50, self.field_width - 325, -55))))
            DefensePosition.position_on_y = dict(
                zip(self.unit.list_of_my_drones(), list(range(250, 50, -40))))
            self.unit.move_at(
                Point(
                    DefensePosition.position_on_x[self.unit],
                    DefensePosition.position_on_y[self.unit]
                )
            )
        elif self.unit.mothership.x < self.field_width / 2 and self.unit.mothership.y > self.field_height / 2:
            DefensePosition.position_on_x = dict(
                zip(self.unit.list_of_my_drones(), list(range(50, 325, 55))))
            DefensePosition.position_on_y = dict(zip(self.unit.list_of_my_drones(), list(
                range(self.field_height - 250, self.field_height, 40))))
            self.unit.move_at(
                Point(
                    DefensePosition.position_on_x[self.unit],
                    DefensePosition.position_on_y[self.unit]
                )
            )
        elif self.unit.mothership.x > self.field_width / 2 and self.unit.mothership.y > self.field_height / 2:
            DefensePosition.position_on_x = dict(zip(self.unit.list_of_my_drones(), list(
                range(self.field_width - 50, self.field_width - 325, -55))))
            DefensePosition.position_on_y = dict(zip(self.unit.list_of_my_drones(), list(
                range(self.field_height - 250, self.field_height, 40))))
            self.unit.move_at(
                Point(
                    DefensePosition.position_on_x[self.unit],
                    DefensePosition.position_on_y[self.unit]
                )
            )

    def action(self):
        """действие"""
        target = self.unit.turret()
        if round(self.unit.x) == DefensePosition.position_on_x[self.unit] and round(self.unit.y) == DefensePosition.position_on_y[self.unit]:
            self.unit.turn_to(
                Point(self.field_width / 2, self.field_height / 2))
        if round(self.unit.x) == DefensePosition.position_on_x[self.unit] and round(self.unit.y) == DefensePosition.position_on_y[self.unit]:
            if target:
                self.unit.turn_to(target)
                self.unit.gun.shot(target)
