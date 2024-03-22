class Remote():
    pass

class Player():
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()        # object set a variable name = class name and ()
player1 = Player()

if(remote1.isleftPressed()):
    player1.moveleft()