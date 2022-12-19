from aocd import data, submit

SIZE = 5

lines = data.splitlines()

numbers = [int(n) for n in lines[0].split(",")]

boards = []
board = None
for line in lines[1:]:
    if line == "":
        if board is not None:
            boards.append(board)
        board = []
    else:
        print(line)
        board.append([int(n) for n in line.split()])

boards.append(board)


def remove(board, n):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == n:
                board[i][j] = None
                return


def won(board):
    rows = [True] * SIZE
    cols = [True] * SIZE

    for i in range(SIZE):
        for j in range(SIZE):
            rows[i] = rows[i] and board[i][j] == None
            cols[i] = cols[i] and board[j][i] == None

    for k in range(SIZE):
        if rows[k] or cols[k]:
            return True
    return False


def find():
    winners = []
    for number in numbers:
        for i in range(len(boards)):
            if boards[i] == None:
                continue
            remove(boards[i], number)
            if won(boards[i]):
                winners.append((boards[i], number))
                boards[i] = None
    return winners


def score(board):
    score = 0
    for row in board:
        for col in row:
            if col is not None:
                score += col
    return score


winners = find()

winner = winners[0]
loser = winners[-1]

submit(score(winner[0]) * winner[1], part="a")
submit(score(loser[0]) * loser[1], part="b")
