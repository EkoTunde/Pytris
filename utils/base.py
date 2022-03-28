from typing import Tuple


def relocate(
    coords: Tuple[int, int],
    up=0,
    right=0,
    down=0,
    left=0,
) -> Tuple[int, int]:
    """Returns a new Tuple with the coordinates relocated."""
    return (coords[0] + up - down, coords[1] + right - left)
