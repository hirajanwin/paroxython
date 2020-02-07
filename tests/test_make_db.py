import json
from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.make_db import Database


def test_snapshot_simple_db(capsys):
    db = Database(["tests/data/simple"], ignore_timestamps=True)
    make_snapshot("snapshots/simple_db.json", db.get_json(), capsys)


def test_sqlite_simple_db(capsys):
    db = Database(["tests/data/simple"])
    db.write_sqlite("snapshots/simple_db.sqlite")
