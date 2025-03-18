def get_matrix(rows, cols, name="Matrix"):
    print(f"Enter elements for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} numbers.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(map(str, row)))


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Error: Cannot multiply, incompatible dimensions.")
        return None

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def transpose_matrix(A):
    rows, cols = len(A), len(A[0])
    return [[A[j][i] for j in range(rows)] for i in range(cols)]


def main():
    rows, cols = map(int, input("Enter matrix dimensions (rows cols): ").split())

    A = get_matrix(rows, cols, "Matrix A")
    B = get_matrix(rows, cols, "Matrix B")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (A + B)")
        print("2. Subtraction (A - B)")
        print("3. Multiplication (A * B)")
        print("4. Transpose (A^T and B^T)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            print_matrix(add_matrices(A, B), "Sum (A + B)")
        elif choice == "2":
            print_matrix(subtract_matrices(A, B), "Difference (A - B)")
        elif choice == "3":
            result = multiply_matrices(A, B)
            if result:
                print_matrix(result, "Multiplication (A * B)")
        elif choice == "4":
            print_matrix(transpose_matrix(A), "Transpose of A")
            print_matrix(transpose_matrix(B), "Transpose of B")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1-5.")


main()
