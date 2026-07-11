from pathlib import Path

import pytest

from xyzgeom.parser import parse_xyz

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_water_atom_count_and_symbols():
    mol = parse_xyz(FIXTURES / "water.xyz")
    assert mol.symbols == ["O", "H", "H"]
    assert mol.coords.shape == (3, 3)


def test_parse_methane_multi_atom():
    mol = parse_xyz(FIXTURES / "methane.xyz")
    assert mol.symbols == ["C", "H", "H", "H", "H"]
    assert mol.coords.shape == (5, 3)
    assert mol.coords[0].tolist() == [0.0, 0.0, 0.0]


def test_parse_malformed_file_raises():
    with pytest.raises(ValueError, match="malformed atom line"):
        parse_xyz(FIXTURES / "malformed.xyz")


def test_parse_missing_file_raises():
    with pytest.raises(OSError):
        parse_xyz(FIXTURES / "does_not_exist.xyz")
