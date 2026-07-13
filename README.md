# xyzgeom

[![CI](https://github.com/sidd265/xyzgeom/actions/workflows/ci.yml/badge.svg)](https://github.com/sidd265/xyzgeom/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Basic geometry calculations — bond distance, bond angle, center of mass, and radius of gyration — from standard `.xyz` molecular coordinate files.

## What is .xyz?

`.xyz` is a plain-text format for molecular coordinates: a line with the atom count, a comment line, then one line per atom giving its element symbol and `x y z` position. It is one of the most widely supported formats in computational chemistry. `xyzgeom` reads an `.xyz` file and computes a handful of geometric quantities researchers commonly need as a quick sanity check on a structure, without requiring a full modeling suite.

## Requirements

- Python 3.10, 3.11, or 3.12

## Installation

```bash
git clone https://github.com/sidd265/xyzgeom.git
cd xyzgeom
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

This installs the `xyzgeom` command and the `xyzgeom` Python package.

## Quickstart

The repository includes a sample water molecule at `tests/fixtures/water.xyz`:

```
3
water molecule, experimental geometry (O-H 0.9584 A, H-O-H 104.45 deg)
O   0.000000   0.000000   0.117300
H   0.000000   0.757200  -0.469200
H   0.000000  -0.757200  -0.469200
```

Run the CLI for a geometry summary:

```bash
$ xyzgeom tests/fixtures/water.xyz
Atoms: 3
Center of mass: (0.0000, 0.0000, 0.0517)
Radius of gyration: 0.3136 A
```

Request a specific bond distance or angle by atom index (0-indexed, in the order the atoms appear in the file):

```bash
$ xyzgeom tests/fixtures/water.xyz --distance 0 1
0.9578

$ xyzgeom tests/fixtures/water.xyz --angle 1 0 2
104.48
```

## Using xyzgeom as a library

```python
from xyzgeom.parser import parse_xyz
from xyzgeom.geometry import distance, angle, center_of_mass, radius_of_gyration

mol = parse_xyz("water.xyz")
distance(mol, 0, 1)   # O-H bond length, in Angstroms
angle(mol, 1, 0, 2)   # H-O-H angle, vertex at atom 0, in degrees
center_of_mass(mol)   # mass-weighted average position, shape (3,)
radius_of_gyration(mol)
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution workflow.

## License

MIT — see [LICENSE](LICENSE).
