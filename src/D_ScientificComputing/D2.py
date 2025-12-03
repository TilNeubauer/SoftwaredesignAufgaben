import numpy as np
import copy

def main() -> None:
    arr = np.arange(8)

    arr_4x2 = arr.reshape(4,2)
    print(f"{arr_4x2 = }")

    arr_2x4 = arr.reshape(4,2).reshape(2,4)
    print(f"{arr_2x4 = }")

    arr16 = np.arange(16)
    arr2X = arr16.reshape(2, -1)
    print(f"{arr2X = }")

    arr2X_2 = arr16.reshape(np.shape(arr2X))
    print(f"{arr2X_2 = }")

    if id(arr16) != id(arr2X):
        print("reshape creates a real copy, is not just linked to the original list\n")
    else:
        print("reshape is still linked to the original list")
    print(f"id arr16: {id(arr16)}\nid arr2X: {id(arr2X)}")

    arr2X_orig = arr2X.reshape(-1)
    print(f"{arr2X_orig = }")


    #print(f"{arr = }")

    

if __name__ == "__main__":
    main()