def get_matrix(rows, cols, name="Matrix"):
    print(f"Enter elements for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} numbers.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))
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
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Error: Determinant is only defined for square matrices.")
        return None

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if len(matrix) == 3:
        return (
                matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
    return None


def inverse_matrix(A):
    if len(A) != len(A[0]):
        print("Error: Inverse is only defined for square matrices.")
        return None

    det = determinant(A)
    if det == 0:
        print("Error: The matrix is singular (det = 0) and does not have an inverse.")
        return None

    if len(A) == 2:
        return [[A[1][1] / det, -A[0][1] / det],
                [-A[1][0] / det, A[0][0] / det]]

    if len(A) == 3:
        cofactors = [
            [((-1) ** (i + j)) * determinant([row[:j] + row[j + 1:] for row in (A[:i] + A[i + 1:])]) for j in range(3)]
            for i in range(3)]
        adjugate = transpose_matrix(cofactors)
        inverse = [[adjugate[i][j] / det for j in range(3)] for i in range(3)]
        return inverse


def main():
    while True:
        try:
            dimensions = input("Enter matrix dimensions (max 3x3, format: rows cols): ").strip()
            if "x" in dimensions:
                rows, cols = map(int, dimensions.split("x"))
            else:
                rows, cols = map(int, dimensions.split())

            if 1 <= rows <= 3 and 1 <= cols <= 3:
                break
            else:
                print("Error: Dimensions must be between 1x1 and 3x3.")
        except ValueError:
            print("Error: Please enter valid numbers in the format 'rows cols' (e.g., 2x3).")

    A = get_matrix(rows, cols, "Matrix A")
    B = get_matrix(rows, cols, "Matrix B")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (A + B)")
        print("2. Subtraction (A - B)")
        print("3. Multiplication (A * B)")
        print("4. Transpose (A^T and B^T)")
        print("5. Inverse (A^-1 and B^-1) (Only for square matrices)")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

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
            if rows == cols:
                inv_A = inverse_matrix(A)
                if inv_A:
                    print_matrix(inv_A, "Inverse of A")
                inv_B = inverse_matrix(B)
                if inv_B:
                    print_matrix(inv_B, "Inverse of B")
            else:
                print("Error: Inverse is only possible for square matrices (e.g., 2x2 or 3x3).")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1-6.")


main()
