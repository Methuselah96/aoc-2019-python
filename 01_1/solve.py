def solve_single(number):
    return int(number / 3) - 2


def solve_all():
    with open('input') as f:
        print(sum([solve_single(int(x)) for x in f]))


if __name__ == '__main__':
    solve_all()
