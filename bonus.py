# ==========================
# Linear Algebra Solver
# Gauss Elimination & Gauss-Jordan
# Shows steps + final matrix
# ==========================

def print_matrix(matrix, title="Matrix"):
    print("\n" + title)
    for row in matrix:
        print("  ".join(f"{val:8.4f}" for val in row))
    print()


def get_augmented_matrix(n):
    print("\nYou must enter", n+1, "numbers per row (coefficients + constant):")
    matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Row {i+1}: ").split()
            if len(row_input) != n+1:
                print("❌ ERROR: Enter exactly", n+1, "numbers! Try again.")
                continue
            try:
                row = list(map(float, row_input))
                matrix.append(row)
                break
            except ValueError:
                print("❌ ERROR: Only numeric values allowed! Try again.")
    return matrix


# ==========================================
# Detect system type
# ==========================================
def detect_solution_type(matrix, n):
    zero_row = [0]*n
    for row in matrix:
        # 0 0 0 | c   (c ≠ 0)
        if row[:n] == zero_row and abs(row[n]) > 1e-9:
            return "NO_SOLUTION"

    rankA = sum(1 for row in matrix if row[:n] != zero_row)

    if rankA < n:
        return "INFINITE"

    return "UNIQUE"


# ==========================================
# Back Substitution
# ==========================================
def back_substitution(matrix, n):
    x = [0]*n
    for i in range(n-1, -1, -1):
        if abs(matrix[i][i]) < 1e-9:
            return None
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i-1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]
    return x


# ==========================================
# Gauss Elimination (Forward) + step display
# ==========================================
def gauss_elimination(matrix, n):
    step = 1
    print_matrix(matrix, "Initial Matrix")

    for i in range(n):
        # Pivot fix
        if abs(matrix[i][i]) < 1e-9:
            for k in range(i+1, n):
                if abs(matrix[k][i]) > 1e-9:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break

        pivot = matrix[i][i]
        if abs(pivot) > 1e-9:
            for j in range(i, n+1):
                matrix[i][j] /= pivot

        print_matrix(matrix, f"After normalizing pivot (Step {step})")
        step += 1

        # eliminate below
        for k in range(i+1, n):
            factor = matrix[k][i]
            for j in range(i, n+1):
                matrix[k][j] -= factor * matrix[i][j]

            print_matrix(matrix, f"After eliminating row {k+1} (Step {step})")
            step += 1

    return matrix


# ==========================================
# Gauss–Jordan + step display
# ==========================================
def gauss_jordan(matrix, n):
    step = 1
    print_matrix(matrix, "Initial Matrix")

    for i in range(n):
        pivot = matrix[i][i]

        if abs(pivot) < 1e-9:
            for k in range(i+1, n):
                if abs(matrix[k][i]) > 1e-9:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    pivot = matrix[i][i]
                    break

        # normalize pivot
        for j in range(i, n+1):
            matrix[i][j] /= pivot
        
        print_matrix(matrix, f"After normalizing pivot (Step {step})")
        step += 1

        # eliminate all other rows
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n+1):
                    matrix[k][j] -= factor * matrix[i][j]
                print_matrix(matrix, f"After eliminating row {k+1} (Step {step})")
                step += 1

    return matrix


# ==========================================
# MAIN PROGRAM LOOP
# ==========================================
while True:
    print("\nChoose Method:")
    print("1. Gauss Elimination")
    print("2. Gauss–Jordan")

    choice = input("Enter choice (1 or 2): ")

    if choice not in ("1", "2"):
        print("❌ Invalid choice!")
        continue

    n = int(input("Enter number of equations: "))

    matrix = get_augmented_matrix(n)

    print("\nProcessing...\n")

    if choice == "1":
        mat = gauss_elimination(matrix, n)

        print_matrix(mat, "Final Reduced Matrix (Row-Echelon Form)")

        system = detect_solution_type(mat, n)

        if system == "NO_SOLUTION":
            print("🚫 No solution (inconsistent system).")
        elif system == "INFINITE":
            print("♾️ Infinite solutions (free variables exist).")
        else:
            x = back_substitution(mat, n)
            print("\n✅ Unique solution:")
            for i in range(n):
                print(f"x{i+1} = {x[i]}")

    else:
        mat = gauss_jordan(matrix, n)
        print_matrix(mat, "Final Reduced Matrix (RREF)")

        system = detect_solution_type(mat, n)

        if system == "NO_SOLUTION":
            print("🚫 No solution.")
        elif system == "INFINITE":
            print("♾️ Infinite solutions (free variables).")
        else:
            print("\n✅ Unique solution:")
            for i in range(n):
                print(f"x{i+1} = {mat[i][n]}")

    again = input("\nDo you want to solve another system? (y/n): ").lower()
    if again != "y":
        print("\nThank you! Goodbye 😊")
        break
