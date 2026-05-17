#!/usr/bin/env python3
"""Validate the local UI Skills plugin."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ui-skills"


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def assert_no_todo(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "TODO" in text or "[TODO" in text:
        raise AssertionError(f"placeholder remains in {path}")


def assert_file(path: Path) -> None:
    if not path.is_file():
        raise AssertionError(f"missing file: {path}")


def assert_dir(path: Path) -> None:
    if not path.is_dir():
        raise AssertionError(f"missing directory: {path}")


def main() -> None:
    manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"

    manifest = read_json(manifest_path)
    marketplace = read_json(marketplace_path)

    assert manifest["name"] == "ui-skills"
    assert manifest["skills"] == "./skills/"
    assert manifest["interface"]["displayName"] == "UI Skills"
    assert_no_todo(manifest_path)
    assert_no_todo(marketplace_path)

    entries = {entry["name"]: entry for entry in marketplace["plugins"]}
    assert "ui-skills" in entries
    assert entries["ui-skills"]["source"]["path"] == "./plugins/ui-skills"
    assert entries["ui-skills"]["policy"]["installation"] == "AVAILABLE"
    assert entries["ui-skills"]["policy"]["authentication"] == "ON_INSTALL"

    assert_file(PLUGIN / "skills" / "ui-craft" / "SKILL.md")
    assert_file(PLUGIN / "skills" / "ui-audit" / "SKILL.md")
    assert_file(PLUGIN / "skills" / "ui-craft" / "scripts" / "search.py")
    assert_dir(PLUGIN / "skills" / "ui-craft" / "data" / "stacks")
    assert_file(PLUGIN / "docs" / "source-review.md")
    assert_file(PLUGIN / "docs" / "third-party-notices.md")
    assert_file(PLUGIN / "docs" / "LICENSE.ui-ux-pro-max")

    print("ui-skills plugin validation passed")


if __name__ == "__main__":
    main()
