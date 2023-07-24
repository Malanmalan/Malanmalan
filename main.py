import numpy as np
from dataclasses import dataclass

# pi = np.pi

# x_deck = [7, 6, 5, 4, 3, 2, 1, -1, -2, -3]
# y_deck = [6.514]
# z_deck = [2.4]

# y_tower = [36.1, 35.5, 34.9, 34.2, 33.5, 32.7, 31.4, 31.4, 32.7, 33.5]

# sea_level = 6.514
# cable_spacing = 8.5

# tower_angle = 5 * pi/ 180


# x_coordinates = np.array(x_deck) * cable_spacing
# y_coordinates = np.round(np.array(y_tower) - sea_level, 3)

# x_tower = np.round(np.array(-y_coordinates) * np.tan(tower_angle),3)

# m_x = list(x_coordinates)
# m_y = list(y_coordinates)
# m_x_tower = list(x_tower)
# m_y_tower = list(y_tower)
# #print("the x coordinates:", m_x)
# #print("\n\nthe y coordinates:", m_y)
# #print("\n\nthe x tower:", m_x_tower)
# #print("\n\nthe y tower", m_y_tower)

# #x_cable = x_coordinates - m_x_tower
# #print("x_cable:", x_cable)
# print(y_coordinates)
# print(m_y_tower)
# y_cable = y_coordinates - m_y_tower
# print("\ny_cable:", y_cable)
deck_length = 8.5
pylon_top = 37.869

@dataclass
class Cable:
    x1: float
    y1: float
    x2: float
    y2: float
    angle: float
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

cables_left = [ Cable((7-index)*deck_length,0, 999, 999) for index in range(0, 7)]

for index, cable in enumerate(cables_left):
    cable.x2 = 0
    cable.y2 = pylon_top
    cable.angle = np.tanh((cable.y2 - cable.y1)/(cable.x2 - cable.x1))  * (360/2 * np.pi)

print(cables_left)
