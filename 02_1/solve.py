def add(state, index):
    state[state[index + 3]] = state[state[index + 1]] + state[state[index + 2]]


def multiply(state, index):
    state[state[index + 3]] = state[state[index + 1]] * state[state[index + 2]]


def solve(state):
    index = 0
    op_code = state[0]
    while op_code != 99:
        if op_code == 1:
            add(state, index)
        elif op_code == 2:
            multiply(state, index)
        else:
            raise Exception(f'Unknown op code {op_code}')
        index += 4
        op_code = state[index]
    return state


def solve_file():
    with open('input') as f:
        state = [int(x) for x in f.readline().split(',')]
        state[1] = 12
        state[2] = 2
        print(solve(state)[0])


if __name__ == '__main__':
    solve_file()
