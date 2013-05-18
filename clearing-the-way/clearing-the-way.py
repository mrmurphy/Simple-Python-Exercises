import operator

WIDTH = 0
HEIGHT = 0
BOMBS = []


def is_bomb(cell, row):
    for bomb in BOMBS:
        if bomb[0] == cell and bomb[1] == row:
            return True
    return False


def near_bombs(cell, row):
    near_count = 0
    for bomb in BOMBS:
        if cell - 1 <= bomb[0] <= cell + 1 and \
                row - 1 <= bomb[1] <= row + 1:
            near_count += 1
    return near_count


def recursive_reveal(square, visited=[]):
    visited.append(square)
    if is_bomb(square[0], square[1]):
        yield
    elif near_bombs(square[0], square[1]):
        yield square
    else:
        yield square
        for i in range(-1, 2):
            for j in range(-1, 2):
                cell, row = square[0] + i, square[1] + j
                if 0 <= cell < WIDTH and 0 <= row < HEIGHT \
                        and [cell, row] not in visited:
                    for row in recursive_reveal([cell, row], visited):
                        yield row


def find_unobscured_cells(givenlines):
    global WIDTH, HEIGHT, BOMBS
    WIDTH = int(givenlines[0][0])
    HEIGHT = int(givenlines[0][1])
    BOMBS = givenlines[1:-1]
    clicked = givenlines[-1]
    unobscured = []

    if is_bomb(clicked[0], clicked[1]) or near_bombs(clicked[0], clicked[1]):
        return [clicked]
    else:
        unobscured = [i for i in recursive_reveal(clicked)]

    return sorted(unobscured, key=operator.itemgetter(0, 1))


def parse_file(filename):
    givenlines = []
    f = open(filename)
    for line in f.read().split("\n"):
        if line.strip():
            parsedline = list(map(int, line.split(" ")))
            givenlines.append(parsedline)
    f.close()
    return givenlines


def write_file(filename, data):
    f = open(filename, 'w')
    for line in data:
        f.write("{line}\n".format(line=" ".join(map(str, line))))
    f.close()


def run_test(num):
    givenlines = parse_file("stdin{num}.txt".format(num=num))
    unobscured_cells = find_unobscured_cells(givenlines)
    write_file("newout{num}.txt".format(num=num), unobscured_cells)

if __name__ == '__main__':
    for i in (1,):
        run_test(i)
