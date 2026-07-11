"""Parser for standard .xyz molecular coordinate files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class Molecule:
    """Atom symbols and their 3D coordinates (Angstroms)."""

    symbols: list[str]
    coords: np.ndarray  # shape (n_atoms, 3)


def parse_xyz(path: str | Path) -> Molecule:
    """Read a standard .xyz file into a Molecule.

    Format: first line is the atom count, second line is a comment,
    then one line per atom: ``Symbol x y z``.
    """
    lines = Path(path).read_text().splitlines()
    if len(lines) < 2:
        raise ValueError(f"{path}: file too short to be a valid .xyz file")

    try:
        n_atoms = int(lines[0].strip())
    except ValueError as exc:
        raise ValueError(f"{path}: first line must be an atom count") from exc

    atom_lines = lines[2 : 2 + n_atoms]
    if len(atom_lines) != n_atoms:
        raise ValueError(
            f"{path}: expected {n_atoms} atom lines, found {len(atom_lines)}"
        )

    symbols: list[str] = []
    coords = np.empty((n_atoms, 3), dtype=float)
    for i, line in enumerate(atom_lines):
        parts = line.split()
        if len(parts) != 4:
            raise ValueError(f"{path}: malformed atom line {i + 3!r}: {line!r}")
        symbol, x, y, z = parts
        symbols.append(symbol)
        try:
            coords[i] = (float(x), float(y), float(z))
        except ValueError as exc:
            raise ValueError(f"{path}: non-numeric coordinate on line {i + 3}") from exc

    return Molecule(symbols=symbols, coords=coords)
