import sys
import importlib
import cache
import module

car = None

if __name__ == "__main__":
    while True:
        if not car:
            car = cache.loadCar()
        module.drive(car)
        print ("Press enter to re-run the script, CTRL-C to exit")
        sys.stdin.readline()
        importlib.reload(module)