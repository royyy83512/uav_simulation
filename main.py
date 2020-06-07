# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from uav_class import *
import copy

MAP_SIZE = [1000, 1000]
NUMBER_GROUP = 5
MAX_SPEED = 60
UAV_LIST = []
FPS = 30
START = [400, 400]
END = [1000, 1000]
'''
FORBID = [[(800, 800), (800, 400), (1000, 400), (1000, 800), (800, 800)],
            [(0, 1600), (1, 1600), (1, 1500), (0, 1500), (0, 1600)]]
'''
FORBID = []


def main():
    route = [[400, 400], [800, 800]]
    cur = copy.copy(route[0])

    # set each UAV
    uav0 = UAV(0, 5, [400, 400], [800, 800], [0, 0], 'leader', [1], 0)
    UAV_LIST.append(uav0)
    uav1 = UAV(1, 5, [350, 400], [750, 800], [0, 0], 'default', [0], 0)
    UAV_LIST.append(uav1)

    # direction consensus of all UAV
    # temporarily set up by current point and goal point
    consensus_direction = displacement(uav0.cur, uav0.goal, uav0.vel)
    for uav in UAV_LIST:
        uav.vec = consensus_direction

    while True:
        for uav in UAV_LIST:
            if uav.completed is not True:
                if uav.level == 'leader':
                    # leader's direction may change due to decisions

                    if uav.cur[0] > 600:
                        uav.vec = [0, 5]
                    uav.cur[0] += uav.vec[0]
                    uav.cur[1] += uav.vec[1]
                else:
                    # TODO: neighbor may be more than one
                    neighbor = UAV_LIST[uav.neighbor[0]]

                    # update vec depends on its neighbors
                    uav.vec[0] = (uav.vec[0] + neighbor.vec[0])/2
                    uav.vec[1] = (uav.vec[1] + neighbor.vec[1])/2
                    uav.cur[0] += uav.vec[0]
                    uav.cur[1] += uav.vec[1]

            # check if uav arrives the goal
            if dis(uav.cur, uav.goal) < 10:
                uav.completed = True

        show(MAP_SIZE, UAV_LIST, START, END, FORBID)
        plt.pause(1/FPS)
        plt.cla()

        if all_complete(UAV_LIST):
            break


if __name__ == '__main__':
    main()

# end of file
