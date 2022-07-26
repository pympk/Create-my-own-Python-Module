'''An example file that imports some of the installed modules'''
import sys
from platform import python_version
import hello as ho
from hello import people, world

print("python_path:    ", sys.executable)
print("python_version: ", python_version())
print("hello_version:  ", ho.__version__)
if __name__ == "__main__":
    # If the modules can't be imported, the following print won't happen
    print("Successfully imported the modules!", "\n")

people.say_hello(['Trevor', 'Elias'])
world.World('World').hello()
