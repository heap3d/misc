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
    tags = scan_scene_tags()


def scan_scene_tags() -> dict[str, modo.Item]:
    ...


if __name__ == '__main__':
    main()
