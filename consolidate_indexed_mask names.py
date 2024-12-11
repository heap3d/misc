#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# consolidate materials with indexed names
# ================================

import modo


def main():
    scene_tags = scan_scene_tags()
    consolidated_tags = get_consolidated_tags(scene_tags)


def scan_scene_tags() -> dict[str, list[modo.Item]]:
    ...


def get_consolidated_tags(tags: dict[str, list[modo.Item]]) -> dict[str, list[str]]:
    ...


if __name__ == '__main__':
    main()
