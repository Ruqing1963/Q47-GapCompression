#!/usr/bin/env python3
"""
Compute the Bateman-Horn singular series S(Q) for Q(n) = n^47 - (n-1)^47.

S(Q) = prod_p (1 - omega_Q(p)/p) / (1 - 1/p)

where omega_Q(p) = 0 for p not equiv 1 (mod 47), and omega_Q(p) = 46
for p equiv 1 (mod 47).

Author: Ruqing Chen
Repository: https://github.com/Ruqing1963/Q47-GapCompression
"""

import csv
import os


MAX_PRIME = 100000


def sieve_primes(n: int) -> list:
    """Sieve of Eratosthenes up to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def omega_Q(p: int) -> int:
    """Return omega_Q(p): number of roots of Q(n) mod p."""
    if (p - 1) % 47 == 0 and p != 47:
        return 46
    return 0


def main():
    print("=" * 60)
    print("  Singular Series S(Q) for Q(n) = n^47 - (n-1)^47")
    print(f"  Computing partial products up to p = {MAX_PRIME}")
    print("=" * 60)
    print()

    primes = sieve_primes(MAX_PRIME)
    print(f"Total primes up to {MAX_PRIME}: {len(primes)}")

    partial = 1.0
    n_shielding = 0
    n_splitting = 0

    for p in primes:
        w = omega_Q(p)
        factor = (1 - w / p) / (1 - 1 / p)
        partial *= factor
        if w == 0:
            n_shielding += 1
        else:
            n_splitting += 1

    print(f"\nShielding primes (omega=0): {n_shielding}")
    print(f"Splitting primes (omega=46): {n_splitting}")
    print(f"\nS(Q) = {partial:.6f}")
    print(f"Compression factor: {partial:.2f}x")
    print(f"Effective degree: 46 / {partial:.2f} = {46/partial:.2f}")

    # Save CSV
    os.makedirs("data", exist_ok=True)
    partial = 1.0
    with open("data/convergence.csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["prime_p", "omega_Q_p", "local_factor",
                      "partial_product_S"])
        for p in primes:
            w = omega_Q(p)
            factor = (1 - w / p) / (1 - 1 / p)
            partial *= factor
            wr.writerow([p, w, f"{factor:.8f}", f"{partial:.6f}"])

    print("\n  Saved to data/convergence.csv")
    print("  [DONE]")


if __name__ == "__main__":
    main()
