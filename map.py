import requests
from player import Player

headers = {
    'Authorization': 'Token 8462b8d16624f572bdc0d8402680ae5245449f4d',
    'Content-Type': 'application/json',
}

data = '{"direction":"n"}'

newMap = {}

response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=data)

print(response.text)


# algorithm

oppositeDirection = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
traversalPath = []
reversalPath = [None]
rooms = {}
roomsDictionary = {}
roomGraph = {}

#maze algorithm

#initialize first room by appending each exit
rooms[0] = player.currentRoom.getExits()
roomsDictionary[0] = player.currentRoom.getExits()

while len(rooms) < len(roomGraph)-1:
    if player.currentRoom.id not in rooms:
        rooms[player.currentRoom.id] = player.currentRoom.getExits()
        roomsDictionary[player.currentRoom.id] = player.currentRoom.getExits()
        lastDirection = reversalPath[-1]
        roomsDictionary[player.currentRoom.id].remove(lastDirection)
    while len(roomsDictionary[player.currentRoom.id]) < 1: 
        reverse = reversalPath.pop()
        traversalPath.append(reverse)
        player.travel(reverse)
    exit_dir = roomsDictionary[player.currentRoom.id].pop(0)
    traversalPath.append(exit_dir)
    reversalPath.append(oppositeDirection[exit_dir])
    player.travel(exit_dir)
    if len(roomGraph) - len(rooms) ==1:
        rooms[player.currentRoom.id] = player.currentRoom.getExits()