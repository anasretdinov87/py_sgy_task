#🌲🌊🚁🟩🔥🏥💛🛢️🏫🏆⚡☁️

from map import Map
import time
import os
from helicopter import Helicopter as Helico
from pynput import keyboard

TICK_SLEEP = 1
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generate_forest(3, 10)
field.generate_river(10)
field.generate_river(10)


helico = Helico(MAP_W, MAP_H)

def process_key(key):
    print(key)
    if key.char == 'a' or key.char == 'A':
        print("Cool")
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

tick = 1

while True:
    os.system("clear")
    print("TICK", tick)
    field.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
