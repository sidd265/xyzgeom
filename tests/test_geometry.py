from pathlib import Path

import numpy as np
import pytest

from xyzgeom.geometry import angle, center_of_mass, distance, radius_of_gyration
from xyzgeom.parser import parse_xyz

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def water():
    return parse_xyz(FIXTURES / "water.xyz")


@pytest.fixture
def methane():
    return parse_xyz(FIXTURES / "methane.xyz")


def test_water_oh_bond_distance(water):
    # O is atom 0, H atoms are 1 and 2; both O-H bonds should be ~0.9584 A.
    assert distance(water, 0, 1) == pytest.approx(0.9584, abs=1e-3)
    assert distance(water, 0, 2) == pytest.approx(0.9584, abs=1e-3)


def test_water_hoh_angle(water):
    assert angle(water, 1, 0, 2) == pytest.approx(104.45, abs=0.1)


def test_methane_tetrahedral_angle(methane):
    # Any H-C-H angle in ideal methane is the tetrahedral angle.
    assert angle(methane, 1, 0, 2) == pytest.approx(109.47, abs=0.1)


def test_water_center_of_mass_closer_to_oxygen(water):
    com = center_of_mass(water)
    # Oxygen (17x heavier than H) should dominate; COM stays near atom 0.
    assert np.linalg.norm(com - water.coords[0]) < np.linalg.norm(com - water.coords[1])


def test_methane_center_of_mass_near_carbon(methane):
    com = center_of_mass(methane)
    assert com == pytest.approx([0.0, 0.0, 0.0], abs=1e-2)


def test_radius_of_gyration_positive(water, methane):
    assert radius_of_gyration(water) > 0
    assert radius_of_gyration(methane) > 0


def test_unknown_element_raises():
    from xyzgeom.parser import Molecule

    mol = Molecule(symbols=["Xx"], coords=np.zeros((1, 3)))
    with pytest.raises(ValueError, match="no atomic mass"):
        center_of_mass(mol)
