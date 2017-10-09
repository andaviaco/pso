import lib

from swarm import Swarm


def main():
    swarm_sphere = Swarm(10, 10, lib.sphere, fn_lb=[-5, -5], fn_ub=[5, 5])
    swarm_ackley = Swarm(10, 10, lib.ackley, fn_lb=[-20, -20], fn_ub=[20, 20])
    swarm_rastrigin = Swarm(10, 10, lib.rastrigin, fn_lb=[-5, -5], fn_ub=[5, 5])

    min_x, min_y = swarm_sphere.optimize()
    print(f'Sphere min: x={min_x}, y={min_y}')

    min_x, min_y = swarm_ackley.optimize()
    print(f'Ackley min: x={min_x}, y={min_y}')

    min_x, min_y = swarm_rastrigin.optimize()
    print(f'Rastrigin min: x={min_x}, y={min_y}')

if __name__ == '__main__':
    main()
