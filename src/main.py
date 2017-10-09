import lib

from swarm import Swarm


def main():
    swarm = Swarm(10, 10, lib.griewank)

    min_x, min_y = swarm.optimize()
    print(f'Mínimo: x={min_x}, y={min_y}')

if __name__ == '__main__':
    main()
