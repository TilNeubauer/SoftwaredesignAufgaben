import numpy as np
import copy

def examples_vec(arr: np.ndarray) -> None:
    #v = np.linspace(0, 19, 20)

    print(f"return the last 5 elements: {arr[-5:]}")
    print(f"return every second element: {arr[::2]}")
    print(f"reverse the vector: {arr[::-1]}")
    print(f"return element 1, 4 and 11: {arr[1]}, {arr[4]}, {arr[11]}")
    print(f"return all elements bigger than the mean: {arr[arr > arr.mean()]}")


def examples_mat(matrix, mat_big) -> None: 
    matrix_sawp = copy.copy(matrix)
    matrix_sawp[[1, 2]] = matrix_sawp[[2, 1]]
    print(f"flip the second and third row: \n{matrix_sawp}")
    
    addCol = np.matrix('10; 20; 30')
    matrix_addCol = copy.deepcopy(matrix)
    matrix_addCol = np.hstack((matrix, addCol))
    print(f"add the second column to the entire matrix: \n{matrix_addCol}")

    print(f"extract the sub matrix that only consists of odd rows and even columns: \n{matrix[0::2, 1::2]}")

    print(f"return the rows 1, 4, and 11: \n{mat_big[(1, 4, 11), ]}")


def main() -> None:
    v = np.linspace(0, 19, 20)
    examples_vec(v)

    matrix = np.matrix('1 2 3; 4 5 6; 7 8 9')
    mat_big = np.arange(12 * 12).reshape(12, 12)
    examples_mat(matrix, mat_big)

    

if __name__ == "__main__":
    main()