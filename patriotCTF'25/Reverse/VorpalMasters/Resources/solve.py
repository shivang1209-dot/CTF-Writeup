#!/usr/bin/env python3
"""
Solver for Vorpal Masters license key challenge

From the decompiled code:
1. Format: xxxx-xxxx-xxxx (4 chars - integer - 10 chars)
2. First 4 chars must be "CCIA" (0x43, 0x43, 0x49, 0x41)
3. Integer must be between -5000 and 10000 (0xffffec78 to 0x2710)
4. Complex calculation check on the integer
5. Last 10 chars must be "PatriotCTF"
"""

def check_integer(n):
    """
    Check if integer n satisfies the complex calculation.
    
    From decompiled code:
    temp0_1:temp1_1 = var_20 + 0x16  (n + 22)
    
    The check is:
    temp1_1 - ((((var_20 + 0x16) * 0x96d4b1f) u>> 0x20).d s>> 6) - temp0_1) * 0x6ca
    == var_20 * 2 s% 0x7d0 * 6 + 9
    
    This is compiler-optimized modulo operation. The pattern:
    (x * magic) >> (32 + shift) computes floor(x / divisor)
    Then x - floor(x / divisor) * divisor = x % divisor
    
    So this is computing: (n + 22) % 0x6ca == (n * 2) % 0x7d0 * 6 + 9
    where 0x6ca = 1738 and 0x7d0 = 2000
    """
    # Right side: (n * 2) % 2000 * 6 + 9
    # Note: s% means signed modulo (C's % operator for signed ints)
    n_times_2 = n * 2
    right_side = ((n_times_2 % 2000) * 6 + 9)
    
    # Left side: (n + 22) % 1738
    # Implement the compiler-optimized modulo calculation
    temp = n + 22
    
    # The magic number calculation: (temp * 0x96d4b1f) >> (32 + 6)
    # This computes floor(temp / 1738) using compiler optimization
    magic = 0x96d4b1f
    
    # Handle signed arithmetic properly
    if temp < 0:
        temp_unsigned = (1 << 32) + temp
    else:
        temp_unsigned = temp
    
    # 64-bit multiplication
    product = (temp_unsigned * magic) & 0xFFFFFFFFFFFFFFFF
    
    # Get upper 32 bits
    upper = (product >> 32) & 0xFFFFFFFF
    
    # Arithmetic right shift by 6 (signed)
    if upper >= 0x80000000:
        upper_signed = upper - 0x100000000
    else:
        upper_signed = upper
    
    quotient = upper_signed >> 6
    
    # Compute modulo: temp - quotient * 1738
    left_side = temp - quotient * 0x6ca
    
    return left_side == right_side

def solve():
    """Find the valid license key"""
    print("Solving Vorpal Masters license key...")
    print()
    
    # First part is fixed: "CACI"
    # Memory layout: var_11='C', var_10='A', var_f='C', var_e='I'
    part1 = "CACI"
    
    # Third part is fixed: "PatriotCTF"
    part3 = "PatriotCTF"
    
    # Find valid integer in range [-5000, 10000]
    valid_integers = []
    
    print("Searching for valid integer in range [-5000, 10000]...")
    for n in range(-5000, 10001):
        if check_integer(n):
            valid_integers.append(n)
            print(f"Found valid integer: {n}")
    
    print()
    if valid_integers:
        print(f"Found {len(valid_integers)} valid integer(s):")
        for n in valid_integers:
            # Verify the calculation
            temp = n + 22
            left = temp % 1738
            right = ((n * 2) % 2000) * 6 + 9
            print(f"  n = {n}: ({n} + 22) % 1738 = {left}, (({n} * 2) % 2000) * 6 + 9 = {right}")
            
        print()
        print("Valid license keys:")
        for n in valid_integers:
            key = f"{part1}-{n}-{part3}"
            print(f"  {key}")
            print(f"  Flag format: CACI{{{key}}}")
    else:
        print("No valid integers found. Let me refine the check...")
        
        # Let's try a more careful analysis
        # The decompiled code shows:
        # temp0_1:temp1_1 = var_20 + 0x16
        # Then a complex calculation
        
        # Let me try to understand the modulo operation better
        # The pattern suggests: (n + 22) % 1738 == ((n * 2) % 2000) * 6 + 9
        
        # But wait, let me check if the right side can even be valid
        # (n * 2) % 2000 can be 0 to 1999
        # So right side can be: 9, 15, 21, ..., 9 + 1999*6 = 12003
        # But left side is (n + 22) % 1738, which is 0 to 1737
        
        # So we need: (n + 22) % 1738 == ((n * 2) % 2000) * 6 + 9
        # And ((n * 2) % 2000) * 6 + 9 must be < 1738
        # So ((n * 2) % 2000) * 6 + 9 < 1738
        # ((n * 2) % 2000) * 6 < 1729
        # ((n * 2) % 2000) < 288.17
        # So (n * 2) % 2000 < 289
        
        print("Refining search with additional constraints...")
        for n in range(-5000, 10001):
            if (n * 2) % 2000 < 289:  # Constraint from right side
                if check_integer(n):
                    valid_integers.append(n)
                    print(f"Found valid integer: {n}")

if __name__ == "__main__":
    solve()

