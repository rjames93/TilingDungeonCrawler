import uuid

class Entity:
    def __init__(self, initx, inity,name):
        self.position = (initx,inity)
        self.uuid = uuid.uuid4()
        self.name = name


class animateEntity(Entity):
    def __init__(self, initx, inity, name):
        Entity.__init__(self, initx, inity, name)

# Pretty Obvious right? player, nature and ai
class playerEntity(animateEntity):
    def __init__(self, initx, inity, name):
        animateEntity.__init__(self, initx, inity, name)

class natureEntity(animateEntity):
    def __init__(self, initx, inity, name):
        animateEntity.__init__(self, initx, inity, name)

class aiEntity(animateEntity):
    def __init__(self, initx, inity, name):
        animateEntity.__init__(self, initx, inity, name)


# Pretty Obvious too. inanimateEntity at the moment is just a subclass for the itemEntity
class inanimateEntity(Entity):
    def __init__(self, initx, inity, name):
        Entity.__init__(self, initx, inity, name)

class itemEntity(inanimateEntity):
    def __init__(self, initx, inity, name):
        inanimateEntity(self, initx, inity, name)

