def get_matrix(rows, cols, name="Matrix"): # deh function m7taga dimension mn el user 3l4an td5al el matrix
    print(f"Enter elements for {name} ({rows}x{cols}):")
    matrix = [] # empty matrix
    for i in range(rows): # deh loop hat4t8al l7d 3dd el rows mslan 2x3 yb2a ht run 2 times
        while True:
            row_input = input(f"Row {i + 1}: ").split() # hena by2ol ll user d5aly el arkam bta3t el matrix w bytla3lo rkm el row
            if len(row_input) != cols: # dah bet check enak d5alt el matrix cols zy el dimension el enta mdeholo
                print(f"Please enter exactly {cols} numbers.") # dah by2olak en lazm tda5l el arkam el matrix cols s7
                continue
            try:
                rows = [float(x) for x in row_input]# lw 3dd rows = ll for each inputs break
                break
            except ValueError:
                print("Invalid input. Enter numeric values only.")
        matrix.append(rows) # save el matrix
    return matrix

def print_matrix(matrix, name="Matrix"):# deh function bt print el matrix w esm el operation el tamt 3liha
    print(f"\n{name}:")# esm el operation
    for row in matrix:# l kol row fl matrix hat3ml dah 👇👇
        print(" ".join(str(x) for x in row)) # [for x in row bt3ml separate ll int] w [" ".join(str(x) bt5li el int string w bt3ml split ]

#a = get_matrix(2,2 )
#print_matrix(a)





def add_matrices(A, B):# deh function ll addtion bt3ml ll two matrices add
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))] # for i in range(len(A)) --> l kol index(5ana) f kol row ///  for j in range(len(A[0])) --> l kol index(5ana) f kol cols /// w y3mlhom add
                                                                                  # men el a5ir bt loop 3la kol el index bta3t el row ,cols /// w len(A) gives the number of rows /// len(A[0]) gives the number of columns
def subtract_matrices(A, B):# deh function ll subtraction bt3ml ll two matrices subtract
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))] # nfs el 7aga hyro7 l kol [i][j] f matrix A w B bs hy3ml subtraction



def multiply_matrices(A, B):# el function deh bt3ml multiply ll two matrices
    rows_A, cols_A = len(A), len(A[0])# hena by3raf en el rows_A = len(A) w cols_A = len(A[0])
    rows_B, cols_B = len(B), len(B[0])# hena by3raf en el rows_B = len(B) w cols_B = len(B[0])

    if cols_A != rows_B:# check if cols_A = rows_B 3lan fl multiply lazm tb2a keda --> A (2×3) × B (3×4) = ✅ A (2×3) × B (2×4) = ❌
        print("Error: Cannot multiply, incompatible dimensions.")
        return None

    result = [[0 for col in range(cols_B)] for row in range(rows_A)] # bt3ml create l new zero matrix mn 7asl 3mlyt el darb /// if A is 2x3 and B is 3x4 → result will be a 2x4

    for i in range(rows_A):# i is a regular loop variable. It takes the values: 0, 1, 2, ..., el loop deh ht run 3la 7sab el rows bta3 el A mslan A = 2x3 y3ni ht run 2 times
        for j in range(cols_B):# j is a regular loop variable. It takes the values: 0, 1, 2, ..., el loop deh ht run 3la 7sab el cols bta3 el B mslan B = 3x2 y3ni ht run 2 times
            for k in range(cols_A):# k is a regular loop variable. It takes the values: 0, 1, 2, ..., el loop deh ht run 3la 7sab el cols bta3 el A aw el rows bta3t el B mslan B = 3x2 y3ni ht run 3 times
                result[i][j] += A[i][k] * B[k][j] # result[0][0] = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0]) + (A[0][2] * B[2][0])

    return result


def transpose_matrix(A):# deh function el transpose
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] # l kol index f awl col hatt7wl l awl row w b3d keda tro7 l kol index f tany col t7wlha l tany row



def determinant(matrix):# el function deh et3mlt 3l4an nst3mlha fl inverse function
    if len(matrix) != len(matrix[0]):# deh btt check en 3dd el rows howa 3dd el cols
        print("Error: Determinant is only defined for square matrices.")
        return None

    if len(matrix) == 2:# lw el matrix 2x2
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]# 1 2  --> 1x4 -3x2
                                                                        # 3 4
    if len(matrix) == 3:# lw el matrix 3x3
        return (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
    return None


def inverse_matrix(A):# deh function el inverse b tre2t el adj/det el hya cofactor.trans/det
    if len(A) != len(A[0]): # check en el rows = cols
        print("Error: Inverse is only defined for square matrices.")
        return None

    det = determinant(A)
    if det == 0:# dah be check en el determinant m4 = zero 3l4an y3rf y3ml inverse
        print("Error: The matrix is singular (det = 0) and does not have an inverse.")
        return None

    if len(A) == 2:# if matrix 2x2 using the special case
        return [[A[1][1] / det, -A[0][1] / det],
                [-A[1][0] / det, A[0][0] / det]]# Flip A[0][0] and A[1][1] // Change the signs of A[0][1] and A[1][0]

    if len(A) == 3:# if matrix 3x3 we use the adj/det el hya cofactor.trans/det method
        cofactors = [
            [((-1) ** (i + j)) * determinant([row[:j] + row[j + 1:] for row in (A[:i] + A[i + 1:])]) for j in range(3)]# (**) means power to get the correct sign (+/-) for each cofactor
            for i in range(3)]# b3d keda bt7sb determinant 3l4an ht remove one row w one column hytb2a det 2x2 dah el minor el det hy7sbo w el (**) ht7tlo el sign bta3to w hakaza
        #htla2i voice 3la el telegram
        adjugate = transpose_matrix(cofactors)
        inverse = [[adjugate[i][j] / det for j in range(3)] for i in range(3)]# e3ml loop 3l i i[0] w e3ml for loop 3l j tlat mrat i[0]j[0] , i[0]j[1] , i[0]j[2]  w erg3 a3ml loop 3l i tany i[1] etc...
        return inverse


def main():
    while True:
        try:
            dimensions = input("Enter matrix dimensions (max 3x3, format: rows cols or rowsxcols): ").strip() # deh bta5od el dimensions w el strip bt4el ay space zyada
            if "x" in dimensions:
                parts = dimensions.split("x") # dah by3tbr el "x" bt split
            else:
                parts = dimensions.split() # dah lw mafe4 "x" be split lwa7do
            if len(parts) != 2: # dah be check eno tlat amaken zy 3x3 aw 3 3
                print("Error: Please enter both rows and columns.")
                continue
            rows = int(parts[0]) # dah by7dd en el row tb2a awl rkam
            cols = int(parts[1]) # dah by7dd en el cols tb2a tany rkam
            if 1 <= rows <= 3 and 1 <= cols <= 3: # dah by5ali el matrix 3x3 max
                break
            else:
                print("Error: Dimensions must be between 1x1 and 3x3.")
        except ValueError:
            print("Error: Please enter valid numbers.")

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
