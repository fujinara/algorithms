def solve():
    input()
    board = []
    for _ in range(8):
        board.append(input())
    for i in range(1, 7):
        for j in range(1, 7):
            if (board[i - 1][j - 1] == board[i - 1][j + 1] == '#' and
                board[i + 1][j - 1] == board[i + 1][j + 1] == '#'):
                print(i + 1, j + 1)


t = int(input())
for _ in range(t):
    solve()