import random
import math

def in_unit_circle(N):
    # counts how many random N are under the unitcircle  
    M = 0

    for _ in range(N):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1.0:
            M += 1

    return M

def estimate_pi(N):
    # estimats pi with the formular 
    #   pi = 4 * M/N
    #       N: random points 
    #       M: random points under the unitsircle 

    M = in_unit_circle(N)

    return 4*M/N  


def get_accuracy(N):

    est_pi = estimate_pi(N)

    return abs(est_pi - math.pi)


print(f"delta pi{get_accuracy(1000)}")
print(f"pi {estimate_pi(1000)}")