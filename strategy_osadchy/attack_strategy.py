# -*- coding: utf-8 -*-


from astrobox.core import Drone
from robogame_engine.geometry import Point
from hangar_2022.strategy_osadchy.strategy_interface import StrategyInterface


class SpaceMap:
    """Косимческая Карта"""

    """статус сектора после атаки: если True
       - значит сектор чист"""
    sector_1_status = False
    sector_2_status = False
    sector_3_status = False

    """12 позиций от моей базы в трёх направлениях"""
    route_1_attack_position_x_1 = {}
    route_1_attack_position_y_1 = {}
    route_1_attack_position_x_2 = {}
    route_1_attack_position_y_2 = {}
    route_1_attack_position_x_3 = {}
    route_1_attack_position_y_3 = {}
    route_1_attack_position_x_4 = {}
    route_1_attack_position_y_4 = {}
    route_1_attack_position_x_5 = {}
    route_1_attack_position_y_5 = {}
    route_1_attack_position_x_6 = {}
    route_1_attack_position_y_6 = {}
    route_1_attack_position_x_7 = {}
    route_1_attack_position_y_7 = {}
    route_1_attack_position_x_8 = {}
    route_1_attack_position_y_8 = {}
    route_1_attack_position_x_9 = {}
    route_1_attack_position_y_9 = {}
    route_1_attack_position_x_10 = {}
    route_1_attack_position_y_10 = {}
    route_1_attack_position_x_11 = {}
    route_1_attack_position_y_11 = {}
    route_1_attack_position_x_12 = {}
    route_1_attack_position_y_12 = {}

    route_2_attack_position_x_1 = {}
    route_2_attack_position_y_1 = {}
    route_2_attack_position_x_2 = {}
    route_2_attack_position_y_2 = {}
    route_2_attack_position_x_3 = {}
    route_2_attack_position_y_3 = {}
    route_2_attack_position_x_4 = {}
    route_2_attack_position_y_4 = {}
    route_2_attack_position_x_5 = {}
    route_2_attack_position_y_5 = {}
    route_2_attack_position_x_6 = {}
    route_2_attack_position_y_6 = {}
    route_2_attack_position_x_7 = {}
    route_2_attack_position_y_7 = {}
    route_2_attack_position_x_8 = {}
    route_2_attack_position_y_8 = {}
    route_2_attack_position_x_9 = {}
    route_2_attack_position_y_9 = {}
    route_2_attack_position_x_10 = {}
    route_2_attack_position_y_10 = {}
    route_2_attack_position_x_11 = {}
    route_2_attack_position_y_11 = {}
    route_2_attack_position_x_12 = {}
    route_2_attack_position_y_12 = {}

    route_3_attack_position_x_1 = {}
    route_3_attack_position_y_1 = {}
    route_3_attack_position_x_2 = {}
    route_3_attack_position_y_2 = {}
    route_3_attack_position_x_3 = {}
    route_3_attack_position_y_3 = {}
    route_3_attack_position_x_4 = {}
    route_3_attack_position_y_4 = {}
    route_3_attack_position_x_5 = {}
    route_3_attack_position_y_5 = {}
    route_3_attack_position_x_6 = {}
    route_3_attack_position_y_6 = {}
    route_3_attack_position_x_7 = {}
    route_3_attack_position_y_7 = {}
    route_3_attack_position_x_8 = {}
    route_3_attack_position_y_8 = {}
    route_3_attack_position_x_9 = {}
    route_3_attack_position_y_9 = {}
    route_3_attack_position_x_10 = {}
    route_3_attack_position_y_10 = {}
    route_3_attack_position_x_11 = {}
    route_3_attack_position_y_11 = {}
    route_3_attack_position_x_12 = {}
    route_3_attack_position_y_12 = {}

    drones_counter = []   # для метода attack_start()


class Attack(StrategyInterface):
    """Атака"""

    def __init__(self, unit: Drone):
        super().__init__(unit)

        self.field_width = self.unit.scene.field[0]
        self.field_height = self.unit.scene.field[1]

        self.space_map = SpaceMap

        """Стартовая позиция"""
        if self.unit.mothership.x < self.field_width / 2 and self.unit.mothership.y < self.field_height / 2:
            self.unit.move_at(
                Point(round(self.unit.mothership.x + 70), round(self.unit.mothership.y + 70)))
        elif self.unit.mothership.x > self.field_width / 2 and self.unit.mothership.y < self.field_height / 2:
            self.unit.move_at(
                Point(round(self.unit.mothership.x - 70), round(self.unit.mothership.y + 70)))
        elif self.unit.mothership.x < self.field_width / 2 and self.unit.mothership.y > self.field_height / 2:
            self.unit.move_at(
                Point(round(self.unit.mothership.x + 70), round(self.unit.mothership.y - 70)))
        elif self.unit.mothership.x > self.field_width / 2 and self.unit.mothership.y > self.field_height / 2:
            self.unit.move_at(
                Point(round(self.unit.mothership.x - 70), round(self.unit.mothership.y - 70)))

        """Создание позиций на карте по x, y"""
        self.create_attack_positions()

        """Выйти на стартовую позицию атаки"""
        self.attack_starting_position = 50
        self.unit.move_at(
            Point(
                round(self.unit.mothership.x + self.attack_starting_position) if self.unit.mothership.x < self.field_width /
                2 else round(self.unit.mothership.x - self.attack_starting_position),
                round(self.unit.mothership.y + self.attack_starting_position) if self.unit.mothership.y < self.field_height /
                2 else round(self.unit.mothership.y - self.attack_starting_position)
            )
        )

    def create_attack_positions(self):
        """создать позиции атаки"""
        my_base = self.unit.mothership
        if my_base.x < self.field_width / 2 and my_base.y < self.field_height / 2:
            self.space_map.route_1_attack_position_x_1 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 200), round(my_base.y + 210)))))
            self.space_map.route_1_attack_position_x_2 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 230), round(my_base.y + 235)))))
            self.space_map.route_1_attack_position_x_3 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 260), round(my_base.y + 365)))))
            self.space_map.route_1_attack_position_x_4 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 290), round(my_base.y + 395)))))
            self.space_map.route_1_attack_position_x_5 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 320), round(my_base.y + 325)))))
            self.space_map.route_1_attack_position_x_6 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 350), round(my_base.y + 355)))))
            self.space_map.route_1_attack_position_x_7 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 350), round(my_base.y + 355)))))
            self.space_map.route_1_attack_position_x_8 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 380), round(my_base.y + 385)))))
            self.space_map.route_1_attack_position_x_9 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 410), round(my_base.y + 415)))))
            self.space_map.route_1_attack_position_x_10 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 450), round(my_base.y + 455)))))
            self.space_map.route_1_attack_position_x_11 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 500), round(my_base.y + 505)))))
            self.space_map.route_1_attack_position_x_12 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 550), round(my_base.y + 555)))))

            self.space_map.route_2_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 201), round(my_base.x + 210)))))
            self.space_map.route_2_attack_position_y_1 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 230), round(my_base.x + 235)))))
            self.space_map.route_2_attack_position_y_2 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 260), round(my_base.x + 265)))))
            self.space_map.route_2_attack_position_y_3 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 290), round(my_base.x + 295)))))
            self.space_map.route_2_attack_position_y_4 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 320), round(my_base.x + 325)))))
            self.space_map.route_2_attack_position_y_5 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 350), round(my_base.x + 355)))))
            self.space_map.route_2_attack_position_y_6 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 380), round(my_base.x + 385)))))
            self.space_map.route_2_attack_position_y_7 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 410), round(my_base.x + 415)))))
            self.space_map.route_2_attack_position_y_8 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 450), round(my_base.x + 455)))))
            self.space_map.route_2_attack_position_y_9 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 500), round(my_base.x + 505)))))
            self.space_map.route_2_attack_position_y_10 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 550), round(my_base.x + 555)))))
            self.space_map.route_2_attack_position_y_11 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 600), round(my_base.x + 605)))))
            self.space_map.route_2_attack_position_y_12 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))

            self.space_map.route_3_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 100), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 130), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 160), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 190), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 250), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2), round(0), -50))))

        if my_base.x > self.field_width / 2 and my_base.y < self.field_height / 2:
            self.space_map.route_1_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 200), round(my_base.y + 210)))))
            self.space_map.route_1_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 230), round(my_base.y + 235)))))
            self.space_map.route_1_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 260), round(my_base.y + 365)))))
            self.space_map.route_1_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 290), round(my_base.y + 395)))))
            self.space_map.route_1_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 320), round(my_base.y + 325)))))
            self.space_map.route_1_attack_position_x_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 350), round(my_base.y + 355)))))
            self.space_map.route_1_attack_position_x_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 380), round(my_base.y + 385)))))
            self.space_map.route_1_attack_position_x_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 410), round(my_base.y + 415)))))
            self.space_map.route_1_attack_position_x_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 450), round(my_base.y + 455)))))
            self.space_map.route_1_attack_position_x_10 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 480), round(my_base.y + 485)))))
            self.space_map.route_1_attack_position_x_11 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 510), round(my_base.y + 515)))))
            self.space_map.route_1_attack_position_x_12 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y + 550), round(my_base.y + 555)))))

            self.space_map.route_2_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 210), round(my_base.x - 200)))))
            self.space_map.route_2_attack_position_y_1 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 235), round(my_base.x - 230)))))
            self.space_map.route_2_attack_position_y_2 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 265), round(my_base.x - 260)))))
            self.space_map.route_2_attack_position_y_3 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 295), round(my_base.x - 290)))))
            self.space_map.route_2_attack_position_y_4 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 325), round(my_base.x - 320)))))
            self.space_map.route_2_attack_position_y_5 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 355), round(my_base.x - 350)))))
            self.space_map.route_2_attack_position_y_6 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 385), round(my_base.x - 380)))))
            self.space_map.route_2_attack_position_y_7 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 415), round(my_base.x - 410)))))
            self.space_map.route_2_attack_position_y_8 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 455), round(my_base.x - 450)))))
            self.space_map.route_2_attack_position_y_9 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 505), round(my_base.x - 500)))))
            self.space_map.route_2_attack_position_y_10 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 555), round(my_base.x - 550)))))
            self.space_map.route_2_attack_position_y_11 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))
            self.space_map.route_2_attack_position_x_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 585), round(my_base.x - 580)))))
            self.space_map.route_2_attack_position_y_12 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_height), 70))))

            self.space_map.route_3_attack_position_x_1 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 100), round(0), -70))))
            self.space_map.route_3_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_2 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 130), round(0), -70))))
            self.space_map.route_3_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_3 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 160), round(0), -70))))
            self.space_map.route_3_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_4 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 190), round(0), -70))))
            self.space_map.route_3_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 100), round(0), -50))))
            self.space_map.route_3_attack_position_x_5 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 250), round(0), -70))))
            self.space_map.route_3_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2), round(0), -50))))

        if my_base.x < self.field_width / 2 and my_base.y > self.field_height / 2:
            self.space_map.route_1_attack_position_x_1 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 200), round(my_base.y + 210)))))
            self.space_map.route_1_attack_position_x_2 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 230), round(my_base.y + 235)))))
            self.space_map.route_1_attack_position_x_3 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 260), round(my_base.y + 365)))))
            self.space_map.route_1_attack_position_x_4 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 290), round(my_base.y + 395)))))
            self.space_map.route_1_attack_position_x_5 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 320), round(my_base.y + 325)))))
            self.space_map.route_1_attack_position_x_6 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 350), round(my_base.y + 355)))))
            self.space_map.route_1_attack_position_x_7 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 350), round(my_base.y + 355)))))
            self.space_map.route_1_attack_position_x_8 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 380), round(my_base.y + 385)))))
            self.space_map.route_1_attack_position_x_9 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 410), round(my_base.y + 415)))))
            self.space_map.route_1_attack_position_x_10 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 450), round(my_base.y + 455)))))
            self.space_map.route_1_attack_position_x_11 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 500), round(my_base.y + 505)))))
            self.space_map.route_1_attack_position_x_12 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(50), round(self.field_width), 70))))
            self.space_map.route_1_attack_position_y_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 550), round(my_base.y + 555)))))

            self.space_map.route_2_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 201), round(my_base.x + 210)))))
            self.space_map.route_2_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 230), round(my_base.x + 235)))))
            self.space_map.route_2_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 260), round(my_base.x + 265)))))
            self.space_map.route_2_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 290), round(my_base.x + 295)))))
            self.space_map.route_2_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 320), round(my_base.x + 325)))))
            self.space_map.route_2_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 350), round(my_base.x + 355)))))
            self.space_map.route_2_attack_position_y_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 380), round(my_base.x + 385)))))
            self.space_map.route_2_attack_position_y_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 410), round(my_base.x + 415)))))
            self.space_map.route_2_attack_position_y_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 450), round(my_base.x + 455)))))
            self.space_map.route_2_attack_position_y_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 500), round(my_base.x + 505)))))
            self.space_map.route_2_attack_position_y_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 550), round(my_base.x + 555)))))
            self.space_map.route_2_attack_position_y_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 600), round(my_base.x + 605)))))
            self.space_map.route_2_attack_position_y_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))

            self.space_map.route_3_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 100), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 130), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 160), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 190), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x + 250), round(self.field_width), 70))))
            self.space_map.route_3_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2), round(0), -50))))

        if my_base.x > self.field_width / 2 and my_base.y > self.field_height / 2:
            self.space_map.route_1_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 200), round(my_base.y + 210)))))
            self.space_map.route_1_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 230), round(my_base.y + 235)))))
            self.space_map.route_1_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 260), round(my_base.y + 365)))))
            self.space_map.route_1_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 290), round(my_base.y + 395)))))
            self.space_map.route_1_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 320), round(my_base.y + 325)))))
            self.space_map.route_1_attack_position_x_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 350), round(my_base.y + 355)))))
            self.space_map.route_1_attack_position_x_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 380), round(my_base.y + 385)))))
            self.space_map.route_1_attack_position_x_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 410), round(my_base.y + 415)))))
            self.space_map.route_1_attack_position_x_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 450), round(my_base.y + 455)))))
            self.space_map.route_1_attack_position_x_10 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 500), round(my_base.y + 505)))))
            self.space_map.route_1_attack_position_x_11 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(self.field_width - 50), round(0), -70))))
            self.space_map.route_1_attack_position_y_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 550), round(my_base.y + 555)))))
            self.space_map.route_1_attack_position_x_12 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(self.field_width - 50), round(0), -75))))
            self.space_map.route_1_attack_position_y_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.y - 600), round(my_base.y + 605)))))

            self.space_map.route_2_attack_position_x_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 201), round(my_base.x + 210)))))
            self.space_map.route_2_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 230), round(my_base.x + 235)))))
            self.space_map.route_2_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 260), round(my_base.x + 265)))))
            self.space_map.route_2_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 290), round(my_base.x + 295)))))
            self.space_map.route_2_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 320), round(my_base.x + 325)))))
            self.space_map.route_2_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 350), round(my_base.x + 355)))))
            self.space_map.route_2_attack_position_y_6 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 380), round(my_base.x + 385)))))
            self.space_map.route_2_attack_position_y_7 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 410), round(my_base.x + 415)))))
            self.space_map.route_2_attack_position_y_8 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 450), round(my_base.x + 455)))))
            self.space_map.route_2_attack_position_y_9 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 500), round(my_base.x + 505)))))
            self.space_map.route_2_attack_position_y_10 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 550), round(my_base.x + 555)))))
            self.space_map.route_2_attack_position_y_11 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))
            self.space_map.route_2_attack_position_x_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(my_base.x - 600), round(my_base.x + 605)))))
            self.space_map.route_2_attack_position_y_12 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height - 50), round(0), -70))))

            self.space_map.route_3_attack_position_x_1 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 100), round(0), -70))))
            self.space_map.route_3_attack_position_y_1 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_2 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 130), round(0), -70))))
            self.space_map.route_3_attack_position_y_2 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_3 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 160), round(0), -70))))
            self.space_map.route_3_attack_position_y_3 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_4 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 190), round(0), -70))))
            self.space_map.route_3_attack_position_y_4 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 + 100), round(self.field_height), 50))))
            self.space_map.route_3_attack_position_x_5 = dict(zip(
                self.unit.list_of_my_drones(), list(range(round(my_base.x - 250), round(0), -70))))
            self.space_map.route_3_attack_position_y_5 = dict(zip(self.unit.list_of_my_drones(
            ), list(range(round(self.field_height / 2 - 280), round(0), -70))))

    def base_explorer(self):
        """исследователь баз:
        возвращает ближайщего дрона к моей базе
        """
        drones = {}
        for enemy_drone in self.unit.scene.drones:
            if not isinstance(enemy_drone, self.unit.__class__) and enemy_drone.is_alive:
                drones[round(self.unit.mothership.distance_to(
                    enemy_drone))] = enemy_drone
        if drones:
            return drones

    def drone_explorer(self):
        """исследователь дронов:
        возращает ближайшего вражеского дрона к моему дрону
        """
        for enemy_drone in self.unit.scene.drones:
            if not isinstance(enemy_drone, self.unit.__class__) and enemy_drone.is_alive:
                if self.unit.distance_to(enemy_drone) < 600:
                    return enemy_drone

    def attack_start(self):
        """старт атаки"""
        self.space_map.drones_counter.clear()
        for drone in self.unit.scene.drones:
            if isinstance(drone, self.unit.__class__) and drone.is_alive:
                if round(drone.x) == round(self.unit.mothership.x + 50 if self.unit.mothership.x < self.field_width / 2 else self.unit.mothership.x - 50) and round(drone.y) == round(self.unit.mothership.y + 50 if self.unit.mothership.y < self.field_height / 2 else self.unit.mothership.y - 50):
                    self.space_map.drones_counter.append(drone)
        if len(self.space_map.drones_counter) == len(self.find_my_drones()):
            return True

    def find_my_drones(self):
        """найти моих дронов"""
        drone_list = []
        for drone in self.unit.scene.drones:
            if isinstance(drone, self.unit.__class__) and drone.is_alive:
                drone_list.append(drone)
        return drone_list

    def check_positions(self, positions_x, positions_y):
        """проверить позиции:
        проверить количество дронов на позиции
        """
        drone_list = []
        for drone in self.find_my_drones():
            if round(drone.x) == positions_x[drone] and round(drone.y) == positions_y[drone]:
                drone_list.append(drone)
        if drone_list:
            if len(drone_list) == len(self.find_my_drones()):
                return True
            elif len(drone_list) != len(self.find_my_drones()):
                return False

    def nearest_enemy_base(self):
        """ближайшая база врага"""
        for enemy_base in self.unit.scene.motherships:
            if enemy_base is not self.unit.mothership and enemy_base.is_alive:
                if self.unit.distance_to(enemy_base) < 600:
                    return enemy_base

    def action(self):
        """действие"""
        target_near_the_base = self.nearest_enemy_base()
        target = self.drone_explorer()
        start_attack = self.attack_start()
        if start_attack and self.space_map.sector_1_status is False:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_1[self.unit],
                    self.space_map.route_1_attack_position_y_1[self.unit]
                )
            )

        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_1[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_1[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_1[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_1[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_2[self.unit],
                    self.space_map.route_1_attack_position_y_2[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_2[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_2[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_2[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_2[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_3[self.unit],
                    self.space_map.route_1_attack_position_y_3[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_3[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_3[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_3[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_3[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_4[self.unit],
                    self.space_map.route_1_attack_position_y_4[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_4[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_4[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_4[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_4[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_5[self.unit],
                    self.space_map.route_1_attack_position_y_5[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_5[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_5[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_5[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_5[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_6[self.unit],
                    self.space_map.route_1_attack_position_y_6[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_6[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_6[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_6[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_6[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_7[self.unit],
                    self.space_map.route_1_attack_position_y_7[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_7[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_7[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_7[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_7[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_8[self.unit],
                    self.space_map.route_1_attack_position_y_8[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_8[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_8[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_8[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_8[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_9[self.unit],
                    self.space_map.route_1_attack_position_y_9[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_9[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_9[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_9[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_9[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_10[self.unit],
                    self.space_map.route_1_attack_position_y_10[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_10[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_10[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_10[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_10[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_11[self.unit],
                    self.space_map.route_1_attack_position_y_11[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_11[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_11[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_1_attack_position_x_11[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_11[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_1_attack_position_x_12[self.unit],
                    self.space_map.route_1_attack_position_y_12[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_1_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_12[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if not target and target_near_the_base and round(self.unit.x) == self.space_map.route_1_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_12[self.unit]:
            self.unit.turn_to(target_near_the_base)
            self.unit.gun.shot(target_near_the_base)
        if not target_near_the_base and round(self.unit.x) == self.space_map.route_1_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_12[self.unit]:
            self.space_map.sector_status_1 = True

        if start_attack and self.space_map.sector_1_status and self.space_map.sector_2_status is False:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_1[self.unit],
                    self.space_map.route_2_attack_position_y_1[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_1[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_1[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_1[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_1[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_2[self.unit],
                    self.space_map.route_2_attack_position_y_2[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_2[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_2[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_2[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_2[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_3[self.unit],
                    self.space_map.route_2_attack_position_y_3[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_3[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_3[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_3[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_3[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_4[self.unit],
                    self.space_map.route_2_attack_position_y_4[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_4[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_4[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_4[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_4[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_5[self.unit],
                    self.space_map.route_2_attack_position_y_5[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_5[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_5[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_5[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_5[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_6[self.unit],
                    self.space_map.route_2_attack_position_y_6[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_6[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_6[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_6[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_6[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_7[self.unit],
                    self.space_map.route_2_attack_position_y_7[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_7[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_7[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_7[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_7[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_8[self.unit],
                    self.space_map.route_2_attack_position_y_8[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_8[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_8[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_8[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_8[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_9[self.unit],
                    self.space_map.route_2_attack_position_y_9[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_9[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_9[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_9[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_9[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_10[self.unit],
                    self.space_map.route_2_attack_position_y_10[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_10[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_10[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_10[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_10[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_11[self.unit],
                    self.space_map.route_2_attack_position_y_11[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_11[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_11[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_11[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_11[self.unit] and target is None:
            self.unit.move_at(
                Point(
                    self.space_map.route_2_attack_position_x_12[self.unit],
                    self.space_map.route_2_attack_position_y_12[self.unit]
                )
            )
        if target and round(self.unit.x) == self.space_map.route_2_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_12[self.unit]:
            self.unit.turn_to(target)
            self.unit.gun.shot(target)
        if not target and target_near_the_base and round(self.unit.x) == self.space_map.route_2_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_12[self.unit]:
            self.unit.turn_to(target_near_the_base)
            self.unit.gun.shot(target_near_the_base)
        if not target_near_the_base and round(self.unit.x) == self.space_map.route_2_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_12[self.unit]:
            self.space_map.sector_status_2 = True

        if self.unit.health < 65:
            self.unit.move_at(
                Point(
                    round(self.unit.mothership.x + self.attack_starting_position) if self.unit.mothership.x < self.field_width /
                    2 else round(self.unit.mothership.x - self.attack_starting_position),
                    round(self.unit.mothership.y + self.attack_starting_position) if self.unit.mothership.y < self.field_height /
                    2 else round(self.unit.mothership.y - self.attack_starting_position)
                )
            )

        if round(self.unit.x) == self.space_map.route_1_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_1_attack_position_y_12[self.unit] and target is None and target_near_the_base is None:
            self.space_map.sector_1_status = True
            self.unit.move_at(
                Point(
                    round(self.unit.mothership.x + self.attack_starting_position) if self.unit.mothership.x < self.field_width /
                    2 else round(self.unit.mothership.x - self.attack_starting_position),
                    round(self.unit.mothership.y + self.attack_starting_position) if self.unit.mothership.y < self.field_height /
                    2 else round(self.unit.mothership.y - self.attack_starting_position)
                )
            )
        if round(self.unit.x) == self.space_map.route_2_attack_position_x_12[self.unit] and round(self.unit.y) == self.space_map.route_2_attack_position_y_12[self.unit] and target is None and target_near_the_base is None:
            self.space_map.sector_2_status = True
            self.unit.move_at(
                Point(
                    round(self.unit.mothership.x + self.attack_starting_position) if self.unit.mothership.x < self.field_width /
                    2 else round(self.unit.mothership.x - self.attack_starting_position),
                    round(self.unit.mothership.y + self.attack_starting_position) if self.unit.mothership.y < self.field_height /
                    2 else round(self.unit.mothership.y - self.attack_starting_position)
                )
            )

    def on_wake_up(self):
        self.action()
