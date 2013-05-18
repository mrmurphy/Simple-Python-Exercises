import operator


def is_bomb(cell, row, bombs):
    for bomb in bombs:
        if bomb[0] == cell and bomb[1] == row:
            return True
    return False


def near_bombs(cell, row, bombs):
    near_count = 0
    for bomb in bombs:
        if cell - 1 <= bomb[0] <= cell + 1 and \
                row - 1 <= bomb[1] <= row + 1:
            near_count += 1
    return near_count


def find_state_2_cells(givenlines):
    width = int(givenlines[0][0])
    height = int(givenlines[0][1])
    bombs = givenlines[1:]
    state_2_cells = []

    for row in range(height):
        for cell in range(width):
            if not is_bomb(cell, row, bombs):
                b = near_bombs(cell, row, bombs)
                if b:
                    state_2_cells.append((cell, row, b))

    return sorted(state_2_cells, key=operator.itemgetter(0, 1))


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
    state_2_cells = find_state_2_cells(givenlines)
    write_file("newout{num}.txt".format(num=num), state_2_cells)

if __name__ == '__main__':
    for i in (2, 3):
        run_test(i)
