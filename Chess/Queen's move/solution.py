def can_queen_move(x1: int, y1: int, x2: int, y2: int) -> bool:
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return dx == 0 or dy == 0 or dx == dy


def main() -> None:
    x1, y1, x2, y2 = map(int, input().split())
    print("YES" if can_queen_move(x1, y1, x2, y2) else "NO")


if __name__ == "__main__":
    main()
