# Q47-GapCompression

**The Bateman–Horn Constant as a Compression Factor: Prime Density Enhancement in the Titan Polynomial**

**Author:** Ruqing Chen, GUT Geoservice Inc., Montreal, Canada

---

## Overview

The Titan polynomial $Q(n) = n^{47} - (n-1)^{47}$ has an anomalously large Bateman–Horn singular series constant $\mathfrak{S}(Q) \approx 8.70$, driven by the **Shielding Property**: all 60 primes below 283 contribute a factor $p/(p-1) > 1$ to the Euler product because $\omega_Q(p) = 0$ for every $p < 283$.

## Key Result

| Model | Constant $\mathfrak{S}$ | Degree | Expected Gap $H^*$ | Relative |
|-------|:-----------------------:|:------:|:------------------:|:--------:|
| Generic degree-46 | ≈ 1.0 | 46 | 1,059,196 | 100% |
| **Titan $Q(n)$** | **8.70** | **46** | **121,781** | **11.5%** |
| Integers (ref) | 1.0 | 1 | 23,026 | — |

At $n \approx 10^{10000}$, the expected gap between prime-producing arguments is compressed **8.7×** compared to a generic polynomial of the same degree. The Titan polynomial effectively behaves like a polynomial of degree $\approx 5.3$ in terms of prime density.

## Repository Structure

```
Q47-GapCompression/
├── README.md
├── LICENSE
├── .gitignore
├── paper/
│   ├── GapCompression_TitanPolynomial.tex      # LaTeX source (4 pages)
│   └── GapCompression_TitanPolynomial.pdf      # Compiled paper
├── figures/
│   ├── figure1_convergence.pdf                 # Convergence of S(Q) to ≈ 8.70
│   └── figure2_stress.pdf                      # Gap compression at n = 10^10000
├── data/
│   ├── convergence.csv                         # Partial products for all primes ≤ 10^5
│   ├── gap_compression.csv                     # Table 1 data
│   └── summary.csv                             # Summary statistics
└── scripts/
    ├── compute_singular_series.py              # Compute S(Q) up to p = 10^5
    └── generate_figures.py                     # Reproduce Figures 1 and 2
```

## Quick Start

### Compute Singular Series
```bash
python scripts/compute_singular_series.py
```
Runs in seconds. Computes the Euler product for all 9,592 primes up to 100,000.

### Generate Figures
```bash
python scripts/generate_figures.py
```
Requires `matplotlib` and `numpy`. Reads `data/convergence.csv`.

## Companion Papers

1. **Titan paper** (local root structure, bounded gap conjecture):
   [Zenodo](https://zenodo.org/records/18521551)

2. **Bateman–Horn constant** ($C_Q \approx 8.68$, detailed computation):
   [Zenodo](https://zenodo.org/records/18526470)

3. **Null–Sparse Decomposition** (Bombieri–Vinogradov):
   [Zenodo](https://zenodo.org/records/18521778)

4. **Admissible Shifts** (fixed divisor analysis):
   [GitHub](https://github.com/Ruqing1963/Q47-Admissible-Shifts)

5. **Exponential Sums** (monodromy, Katz–Sarnak):
   [GitHub](https://github.com/Ruqing1963/Q47-ExponentialSums)

6. **Landau–Siegel paper** (15.4M primes, spectral gap):
   [Zenodo](https://zenodo.org/records/18315796)

## Citation

```bibtex
@article{chen2026gapcompression,
  title   = {The Bateman--Horn Constant as a Compression Factor:
             Prime Density Enhancement in the Titan Polynomial},
  author  = {Chen, Ruqing},
  year    = {2026},
  note    = {Preprint, \url{https://github.com/Ruqing1963/Q47-GapCompression}}
}
```

## License

MIT License. See [LICENSE](LICENSE) for details.
