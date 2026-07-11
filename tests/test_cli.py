from pathlib import Path

from xyzgeom.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


def test_cli_summary(capsys):
    exit_code = main([str(FIXTURES / "water.xyz")])
    out = capsys.readouterr().out
    assert exit_code == 0
    assert "Atoms: 3" in out
    assert "Radius of gyration" in out


def test_cli_distance_flag(capsys):
    exit_code = main([str(FIXTURES / "water.xyz"), "--distance", "0", "1"])
    out = capsys.readouterr().out.strip()
    assert exit_code == 0
    assert float(out) == 0.9584 or abs(float(out) - 0.9584) < 1e-3


def test_cli_angle_flag(capsys):
    exit_code = main([str(FIXTURES / "water.xyz"), "--angle", "1", "0", "2"])
    out = capsys.readouterr().out.strip()
    assert exit_code == 0
    assert abs(float(out) - 104.45) < 0.1


def test_cli_malformed_file_exits_nonzero(capsys):
    exit_code = main([str(FIXTURES / "malformed.xyz")])
    err = capsys.readouterr().err
    assert exit_code == 1
    assert "error:" in err
