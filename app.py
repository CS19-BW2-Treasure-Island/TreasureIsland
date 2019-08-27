from room import Room
from player import Player
from world import World

import random
import json
import requests

world = World()
player = Player('Name', world.startingRoom)

def get_init():
    url = ('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/')
    headers = {'Authorization' : 'Token a0243e3f1036125e5d2a0e5ffe7c64fcfa3bc126'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return json.loads(r.text)
    else:
        return None

# init_info = get_init()

# if init_info is not None:
#     print(f'here is the res {init_info}')
# else:
#     print('Error during request')


    
traversal_path = []

my_map = {}

reversed_path = []

reverse_direction = {'w':'e', 'e':'w', 's':'n', 'n':'s'}

my_map[player.currentRoom.id] = player.currentRoom.getExits()

while len(my_map) < 500 - 1:

    if player.currentRoom.id not in my_map:
        my_map[player.currentRoom.id] = player.currentRoom.getExits()
        last_direction = reversed_path[-1]
        my_map[player.currentRoom.id].remove(last_direction)
    
    while len(my_map[player.currentRoom.id]) == 0:
        reverse_direction = reversed_path.pop()
        traversal_path.append(reverse_direction)
        player.travel(reverse_direction)
    
    direction_move = my_map[player.currentRoom.id].pop(0)
    traversal_path.append(direction_move)
    reversed_path.append(reverse_direction[direction_move])
    player.travel(direction_move)

visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == 500:
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{500 - len(visited_rooms)} unvisited rooms")