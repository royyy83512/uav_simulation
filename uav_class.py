# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from uav_math import *


class UAV:
    """
    UAV class variables:
    uid:       ID of each UAV (int)
    vel:       velocity of each UAV (int)
    current:   current position (list[x,y])
    goal:      goal position (list[x,y])
    level:     leader / default (char)
    neighbor:  neighbor(s) of each UAV (list[id, id, id...])
    completed: true if UAV arrives its goal (boolean)
    """
    def __init__(self, uid, vel, cur, goal, vec, level, neighbor, completed):
        self.uid = uid
        self.vel = vel
        self.cur = cur
        self.goal = goal
        self.vec = vec
        self.level = level
        self.neighbor = neighbor
        self.completed = completed


def detection(leader, forbid):
    uv = unit_vector(leader.current, leader.goal)
    ux, uy = uv[0], uv[1]

    backward_point = leader.current[0] - 100 * uv[0], leader.current[1] - 100 * uv[1]
    if dis(leader.current, leader.goal) < 200:
        forward_point = leader.goal
    else:
        forward_point = leader.current[0] + 200 * uv[0], leader.current[1] + 200 * uv[1]

    right_goal = [forward_point[0] + 40 * uy, forward_point[1] - 40 * ux]
    left_goal = [forward_point[0] - 40 * uy, forward_point[1] + 40 * ux]
    right_start = [backward_point[0] + 40 * uy, backward_point[1] - 40 * ux]
    left_start = [backward_point[0] - 40 * uy, backward_point[1] + 40 * ux]

    for i in range(len(forbid)):
        for j in range(len(forbid[i]) - 1):
            if (is_intersected(backward_point, forward_point, forbid[i][j], forbid[i][j + 1]) or
                    is_intersected(left_start, left_goal, forbid[i][j], forbid[i][j + 1]) or
                    is_intersected(right_start, right_goal, forbid[i][j], forbid[i][j + 1])):
                return True
    return False


def all_complete(uav_list):
    for uav in uav_list:
        if uav.completed == 0:
            return False
    return True


def show(map_size, uav_list, start, end, forbid):
    plt.grid(True)
    plt.xlim(0, map_size[0])
    plt.ylim(0, map_size[1])
    plt.plot(start[0], start[1], "^b")
    plt.plot(end[0], end[1], "^b")

    for i in range(len(forbid)):
        if i == 0:
            ov_x = list(zip(*forbid[i]))[0]
            ov_y = list(zip(*forbid[i]))[1]
            plt.plot(ov_x, ov_y, "-k")

    for uav in uav_list:
        plt.plot(uav.cur[0], uav.cur[1], ".r")

# end of file
