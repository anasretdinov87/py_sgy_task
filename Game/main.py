#🌲🌊🚁🟩🔥🏥💛🛢️🏫🏆⚡☁️

from map import Map
import time
import os

TICK_SLEEP = 0.40
TREE_UPDATE = 50

tmp = Map(9, 10)
tmp.generate_forest(3, 10)
tmp.generate_river(10)
tmp.generate_river(10)
tmp.print_map()

tick = 1

while True:
    os.system("cls")
    print("TICK", tick)
    tmp.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree()
