"""Basic geometry calculations on a parsed Molecule."""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

from xyzgeom.parser import Molecule

# Atomic masses (amu) for common elements. Extend as needed.
ATOMIC_MASSES: dict[str, float] = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "P": 30.974,
    "S": 32.06,
}


def distance(mol: Molecule, i: int, j: int) -> float:
    """Euclidean distance between atoms i and j (Angstroms)."""
    return float(np.linalg.norm(mol.coords[i] - mol.coords[j]))


def angle(mol: Molecule, i: int, j: int, k: int) -> float:
    """Angle i-j-k in degrees, with j as the vertex."""
    v1 = mol.coords[i] - mol.coords[j]
    v2 = mol.coords[k] - mol.coords[j]
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # guard float rounding past +/-1
    return float(np.degrees(np.arccos(cos_theta)))


def _masses(mol: Molecule) -> npt.NDArray[np.float64]:
    try:
        return np.array([ATOMIC_MASSES[s] for s in mol.symbols])
    except KeyError as exc:
        raise ValueError(f"no atomic mass known for element {exc}") from exc


def center_of_mass(mol: Molecule) -> npt.NDArray[np.float64]:
    """Mass-weighted average position of all atoms."""
    masses = _masses(mol)
    com: npt.NDArray[np.float64] = (masses[:, None] * mol.coords).sum(
        axis=0
    ) / masses.sum()
    return com


def radius_of_gyration(mol: Molecule) -> float:
    """Mass-weighted RMS distance of atoms from the center of mass."""
    masses = _masses(mol)
    com = center_of_mass(mol)
    sq_dev = np.sum((mol.coords - com) ** 2, axis=1)
    return float(np.sqrt(np.sum(masses * sq_dev) / masses.sum()))
