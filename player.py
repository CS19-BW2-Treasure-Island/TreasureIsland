import requests

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
    def travel(self, direction, showRooms = False):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if (showRooms):
                nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")
        url = ('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/')
        headers = {'Authorization' : 'Token a0243e3f1036125e5d2a0e5ffe7c64fcfa3bc126'}
        files = [('direction', nextRoom)]
        requests.post(url, headers=headers, files=files)





    