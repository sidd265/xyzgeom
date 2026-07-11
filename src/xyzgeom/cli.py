"""Command-line interface for xyzgeom."""

from __future__ import annotations

import argparse
import sys

from xyzgeom.geometry import angle, center_of_mass, distance, radius_of_gyration
from xyzgeom.parser import parse_xyz


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="xyzgeom",
        description="Compute basic geometry from a .xyz molecular coordinate file.",
    )
    parser.add_argument("xyz_file", help="path to a .xyz coordinate file")
    parser.add_argument(
        "--distance",
        nargs=2,
        type=int,
        metavar=("I", "J"),
        help="print the distance (Angstroms) between atoms I and J (0-indexed)",
    )
    parser.add_argument(
        "--angle",
        nargs=3,
        type=int,
        metavar=("I", "J", "K"),
        help="print the angle (degrees) I-J-K, vertex at J (0-indexed)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        mol = parse_xyz(args.xyz_file)

        if args.distance is not None:
            i, j = args.distance
            print(f"{distance(mol, i, j):.4f}")
            return 0

        if args.angle is not None:
            i, j, k = args.angle
            print(f"{angle(mol, i, j, k):.2f}")
            return 0

        com = center_of_mass(mol)
        rg = radius_of_gyration(mol)
        print(f"Atoms: {len(mol.symbols)}")
        print(f"Center of mass: ({com[0]:.4f}, {com[1]:.4f}, {com[2]:.4f})")
        print(f"Radius of gyration: {rg:.4f} A")
        return 0

    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
