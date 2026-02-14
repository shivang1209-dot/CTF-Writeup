#!/usr/bin/env python3

class SlotMachineLCG:
    def __init__(self, seed=None):
        self.M = 2147483647
        self.A = 48271
        self.C = 12345
        self.state = seed if seed is not None else 1

    def next(self):
        self.state = (self.A * self.state + self.C) % self.M
        return self.state

    def spin(self):
        return self.next() % 100


if __name__ == "__main__":
    print("Slot Machine LCG Test")
    print("=" * 40)

    lcg = SlotMachineLCG(seed=12345)

    print("First 10 spins:")
    for i in range(10):
        spin = lcg.spin()
        print(f"Spin {i+1:2d}: {spin:2d}")
