# Queen's Move

## Problem

On an empty 8 × 8 chessboard, determine whether a queen can move between two distinct squares in one move. Read four integers `x1 y1 x2 y2` from 1 to 8. Print `YES` if the move is possible and `NO` otherwise.

## Idea

Compute the absolute differences `dx = |x2 − x1|` and `dy = |y2 − y1|`. The squares share a column when `dx = 0`, a row when `dy = 0`, or a diagonal when `dx = dy`. Each case gives the queen a straight path on the empty board.

## Complexity

The solution takes `O(1)` time and `O(1)` extra space.

## Examples

| Input | Output | Move |
|---|---|---|
| `5 2 5 8` | `YES` | Vertical |
| `6 5 2 5` | `YES` | Horizontal |
| `1 1 2 2` | `YES` | Diagonal |
| `1 1 2 3` | `NO` | Unreachable in one move |

[Python solution](solution.py) · [Test cases](tests.txt)
