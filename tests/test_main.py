from pathlib import Path
from unittest import mock

import pytest
from typer.testing import CliRunner

from main import app


@pytest.fixture
def runner():
    yield CliRunner()


def test_version(runner: CliRunner):
    with runner.isolated_filesystem():
        result = runner.invoke(app, "version")
        assert result.exit_code == 0
        assert result.stdout == "Version: 0.1.0\n"


def test_build(runner: CliRunner):
    with runner.isolated_filesystem() as path:
        result = runner.invoke(app, "build")
        assert result.exit_code == 0
        index = Path(path) / "dist" / "index.html"
        assert index.exists()


def test_clean(runner: CliRunner):
    with runner.isolated_filesystem() as path:
        path = Path(path) / "dist"
        path.mkdir()

        result = runner.invoke(app, "clean")
        assert result.exit_code == 0
        assert not path.exists()


def test_serve(runner: CliRunner):
    with mock.patch("main.serve") as mock_serve:
        result = runner.invoke(app, "serve")
        assert result.exit_code == 0
        mock_serve.assert_called_once_with()
