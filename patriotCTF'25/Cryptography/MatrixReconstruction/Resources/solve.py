#!/usr/bin/env python3
"""
Matrix Reconstruction CTF Challenge Solver

Given: S[n+1] = A*S[n] XOR B over GF(2)
We need to recover A (32x32 matrix) and B (32-bit vector) from leaked states.
"""

import numpy as np
from numpy.linalg import solve

def int_to_bits(n, bits=32):
    """Convert integer to bit vector (little-endian)"""
    return np.array([(n >> i) & 1 for i in range(bits)], dtype=np.uint8)

def bits_to_int(bits):
    """Convert bit vector to integer"""
    return sum(int(bits[i]) << i for i in range(len(bits)))

def read_states(filename):
    """Read leaked states from file"""
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

def read_ciphertext(filename):
    """Read ciphertext as bytes"""
    with open(filename, 'rb') as f:
        return f.read()

def recover_matrix_and_vector(states):
    """
    Recover A and B from consecutive states.
    For each pair (S[i], S[i+1]): S[i+1] = A*S[i] XOR B
    This can be written as: S[i+1] = A*S[i] + B (over GF(2))
    
    We need to solve for A and B. Since A is 32x32, we need 32 independent equations.
    """
    n = len(states) - 1  # Number of pairs
    if n < 32:
        raise ValueError(f"Need at least 32 state pairs, got {n}")
    
    # Convert states to bit vectors
    state_vectors = [int_to_bits(s) for s in states]
    
    # Set up system of equations: S[i+1] = A*S[i] + B
    # For each output bit j, we have:
    # S[i+1][j] = sum_k(A[j,k] * S[i][k]) + B[j]
    # This is a linear system over GF(2)
    
    # We'll solve for each row of A and corresponding bit of B independently
    A = np.zeros((32, 32), dtype=np.uint8)
    B = np.zeros(32, dtype=np.uint8)
    
    # For each output bit position
    for j in range(32):
        # Set up linear system: S[i+1][j] = sum_k(A[j,k] * S[i][k]) + B[j]
        # We have n equations and 33 unknowns (32 for A[j,:] + 1 for B[j])
        
        # Build coefficient matrix: [S[i][0], S[i][1], ..., S[i][31], 1]
        # and target vector: S[i+1][j]
        coeffs = []
        targets = []
        
        for i in range(n):
            # Coefficient vector: [S[i][0], S[i][1], ..., S[i][31], 1]
            coeff = list(state_vectors[i]) + [1]
            coeffs.append(coeff)
            targets.append(state_vectors[i+1][j])
        
        # Convert to numpy array
        coeff_matrix = np.array(coeffs, dtype=np.uint8)
        target_vector = np.array(targets, dtype=np.uint8)
        
        # Solve over GF(2) using Gaussian elimination
        # We need to find x such that coeff_matrix @ x = target_vector (mod 2)
        solution = solve_gf2(coeff_matrix, target_vector)
        
        if solution is None:
            # Try with more states if available
            print(f"Warning: Could not solve for row {j}, trying with all available states")
            continue
        
        # Extract A[j,:] and B[j] from solution
        A[j, :] = solution[:32]
        B[j] = solution[32]
    
    return A, B

def solve_gf2(A, b):
    """
    Solve Ax = b over GF(2) using Gaussian elimination
    Returns solution vector x or None if no solution
    """
    # Augmented matrix [A | b]
    n, m = A.shape
    aug = np.hstack([A, b.reshape(-1, 1)]).astype(np.uint8)
    
    # Gaussian elimination over GF(2)
    row = 0
    for col in range(m):
        # Find pivot
        pivot_row = None
        for r in range(row, n):
            if aug[r, col] == 1:
                pivot_row = r
                break
        
        if pivot_row is None:
            continue  # No pivot in this column
        
        # Swap rows
        if pivot_row != row:
            aug[[row, pivot_row]] = aug[[pivot_row, row]]
        
        # Eliminate
        for r in range(n):
            if r != row and aug[r, col] == 1:
                aug[r] = (aug[r] + aug[row]) % 2
        
        row += 1
        if row >= n:
            break
    
    # Check for consistency and extract solution
    solution = np.zeros(m, dtype=np.uint8)
    
    # Back substitution
    for i in range(min(row, n)):
        # Find the first non-zero entry in row i
        pivot_col = None
        for j in range(m):
            if aug[i, j] == 1:
                pivot_col = j
                break
        
        if pivot_col is None:
            # Check if this is an inconsistent equation
            if aug[i, m] == 1:
                return None  # Inconsistent system
            continue
        
        # Set solution[pivot_col] = aug[i, m] - sum of other terms
        # Since we're in GF(2), this is simpler
        val = aug[i, m]
        for j in range(pivot_col + 1, m):
            val = (val + aug[i, j] * solution[j]) % 2
        solution[pivot_col] = val
    
    # Verify solution
    if np.all((A @ solution) % 2 == b):
        return solution
    
    return None

def generate_keystream(A, B, initial_state, length):
    """Generate keystream from recovered A and B"""
    keystream = []
    state = int_to_bits(initial_state)
    
    for _ in range(length):
        # Extract lowest byte (bits 0-7)
        keystream_byte = sum(int(state[i]) << i for i in range(8))
        keystream.append(keystream_byte)
        
        # Update state: S[n+1] = A*S[n] XOR B
        new_state = (A @ state) % 2
        new_state = (new_state + B) % 2
        state = new_state
    
    return bytes(keystream)

def main():
    # Read inputs
    print("Reading leaked states...")
    states = read_states('keystream_leak.txt')
    print(f"Read {len(states)} states")
    
    print("Reading ciphertext...")
    ciphertext = read_ciphertext('cipher.txt')
    print(f"Ciphertext length: {len(ciphertext)} bytes")
    
    # Recover A and B
    print("\nRecovering matrix A and vector B...")
    A, B = recover_matrix_and_vector(states)
    
    print("Matrix A recovered:")
    print(A)
    print(f"\nVector B recovered: {bits_to_int(B)} (0x{bits_to_int(B):08x})")
    
    # Generate keystream starting from the first leaked state
    print("\nGenerating keystream...")
    initial_state = states[0]
    keystream = generate_keystream(A, B, initial_state, len(ciphertext))
    
    # Decrypt
    print("\nDecrypting...")
    plaintext = bytes(a ^ b for a, b in zip(ciphertext, keystream))
    
    print(f"Plaintext: {plaintext}")
    print(f"Plaintext (hex): {plaintext.hex()}")
    
    # Try to decode as text
    try:
        text = plaintext.decode('utf-8', errors='ignore')
        print(f"Plaintext (text): {text}")
    except:
        pass

if __name__ == '__main__':
    main()

