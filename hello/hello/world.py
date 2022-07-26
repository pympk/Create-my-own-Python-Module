class World:
    def __init__(self, world_name):
        self.name = world_name

    def hello(self):
        print("Hello, " + self.name + "!" + " Wow, I made my first module!")