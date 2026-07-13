# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `.xyz` file parser (`xyzgeom.parser.parse_xyz`)
- Geometry functions: `distance`, `angle`, `center_of_mass`, `radius_of_gyration`
- `xyzgeom` command-line interface with `--distance` and `--angle` flags
- Test suite covering parser, geometry, and CLI, including a water-molecule
  correctness check against known experimental geometry
- Local tooling: ruff, mypy (strict), editorconfig, pre-commit
- GitHub Actions CI (lint, type check, test) on a Python 3.10-3.12 matrix
- Project governance and community files (README, LICENSE, CONTRIBUTING,
  SECURITY, issue/PR templates)
