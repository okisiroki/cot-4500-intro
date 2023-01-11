# Intro To Python Assignment
# Jordan Sirokie 3831723

import numpy as np

def matrix_one() ->  np.array:
    # returns 3x3 array: 1 if i==j, 0 elsewhere
    array = np.zeros((3,3))
    for i in range(0,3):
        for j in range(0,3):
            if i == j: 
                array[i][j] = 1
    return array


def matrix_two(array: np.array) -> np.array:
    # returns array_one + 3 where i != j
    for i in range(0,3):
        for j in range(0,3):
            if i != j: 
                array[i][j] += 3
    return array


def matrix_three(array: np.array) -> np.array:
    # drops last column from array_two
    return np.delete(array, 2, 1)


if __name__ == "__main__":
    # main program to print arrays
    array_one = matrix_one()
    for i in range(0,3):
        print(f"{array_one[i][0]} {array_one[i][1]} {array_one[i][2]}")

    array_two = matrix_two(array_one)
    print("\n")
    for i in range(0,3):
        print(f"{array_two[i][0]} {array_two[i][1]} {array_two[i][2]}")

    array_three = matrix_three(array_two)
    print("\n")
    for i in range(0,3):
        print(f"{array_three[i][0]} {array_three[i][1]}")
