from aocd import data, submit
import math

input = data


def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])


def turtle():
    x = 0
    y = 0
    a = 0
    for line in input.splitlines():
        action = line[0]
        value = int(line[1:])

        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "W":
            x -= value
        elif action == "E":
            x += value
        elif action == "L":
            a += math.radians(value)
        elif action == "R":
            a -= math.radians(value)
        elif action == "F":
            x += round(math.cos(a) * value)
            y += round(math.sin(a) * value)
    return x, y


def waypoint():
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1
    for line in input.splitlines():
        action = line[0]
        value = int(line[1:])

        if action == "N":
            waypoint_y += value
        elif action == "S":
            waypoint_y -= value
        elif action == "W":
            waypoint_x -= value
        elif action == "E":
            waypoint_x += value
        elif action == "L":
            r = math.radians(value)

            _waypoint_x = waypoint_x * math.cos(r) - waypoint_y * math.sin(r)
            _waypoint_y = waypoint_x * math.sin(r) + waypoint_y * math.cos(r)

            waypoint_x = round(_waypoint_x)
            waypoint_y = round(_waypoint_y)
        elif action == "R":
            r = -math.radians(value)

            _waypoint_x = waypoint_x * math.cos(r) - waypoint_y * math.sin(r)
            _waypoint_y = waypoint_x * math.sin(r) + waypoint_y * math.cos(r)

            waypoint_x = round(_waypoint_x)
            waypoint_y = round(_waypoint_y)
        elif action == "F":
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value
    return ship_x, ship_y


submit(manhattan(turtle()), part='a')
submit(manhattan(waypoint()), part='b')
