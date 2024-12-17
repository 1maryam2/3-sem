from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np
from termcolor import colored

def main():
    rec = Rectangle("синий", 13, 13)
    cir = Circle("зеленый", 13)
    sq = Square("красный", 13)
    print(colored(rec, 'blue'))
    print(colored(cir, 'green'))
    print(colored(sq, 'red'))
    a = np.array([rec, cir, sq])
    print(a)

if __name__ == "__main__":
    main()
