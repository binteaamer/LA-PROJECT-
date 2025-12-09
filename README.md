# Linear Algebra Project  
## Gauss Elimination & Gauss–Jordan Solver (Python)

This project is a Python-based program that solves systems of linear equations using:

- **Gauss Elimination Method**
- **Gauss–Jordan Method**

It shows **step-by-step matrix transformations**, detects the **type of solution**, and prints the final results clearly.

---

##  Features

### 🔹 1. Method Selection
The user can choose:
- **Gauss Elimination**
- **Gauss–Jordan**

### 🔹 2. User Input
The program asks for:
- Number of equations
- Augmented matrix values entered **row-wise**

### 🔹 3. Step-by-Step Output
The program displays:
- Matrix after each pivot normalization  
- Matrix after every elimination step  
- Final matrix (REF or RREF)

### 🔹 4. Solution Type Detection
The program automatically detects:
- ✔ **Unique Solution**
- ✔ **No Solution** (inconsistent system)
- ✔ **Infinite Solutions** (dependent system with free variables)

### 🔹 5. Final Results
Depending on the system:
- **Unique** → Prints numerical solution  
- **Infinite** → Displays dependent system  
- **No Solution** → Shows contradiction

---

## How It Works

- Gauss Elimination reduces the matrix to **Row-Echelon Form (REF)** and applies **back-substitution**.
- Gauss–Jordan reduces it to **Reduced Row-Echelon Form (RREF)**.
- The code includes checks for:
  - Zero rows
  - Contradictions like `[0 0 0 | c]` where `c ≠ 0`
  - Rank comparison for detecting infinite solutions

---

## Input Format

For a system with **n equations**, enter **n + 1 numbers per row**  
(coefficients + constant term).

Example for 3 equations:

