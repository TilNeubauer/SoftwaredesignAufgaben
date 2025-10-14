from B5 import in_unit_circle

def estimate_pi(N: int, fkt_M=in_unit_circle) -> float:
    # estimats pi with the formular 
    # with formular pi ~= A_circle / A_square
    # A_circle ^= M
    # A_square ^= N
    
    M = fkt_M(N)

    return 4*M/N


print(estimate_pi(1000))