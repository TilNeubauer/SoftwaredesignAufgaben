from itertools import accumulate
from operator import add, mul


def main() -> None:
    print(f"{list(accumulate([1, 2, 3, 4, 5], add)) = }")
    print(f"{list(accumulate([1, 2, 3, 4, 5], mul)) = }")
    
    # c6.1: Compute a running maximum
    print(f"{list(accumulate([1, 2, 3, 6, 5], max)) = }") 

    # C6.2: loan with interst of 5% and pyments 100
    loan = [1000] *11
    loan_interest = list(accumulate(loan, lambda x, y: (x*1.05) - 100))
    loan_interest = list(map(lambda e: round(e,2), loan_interest))
    print(f"{loan_interest = }")
    
if __name__ == "__main__":
    main()
