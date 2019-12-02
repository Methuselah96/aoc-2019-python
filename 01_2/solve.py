def solve_single(number):
    fuel = int(number / 3) - 2
    return 0 if fuel <= 0 else fuel + solve_single(fuel)


def solve_all():
    with open('input') as f:
        print(sum([solve_single(int(x)) for x in f]))


if __name__ == '__main__':
    solve_all()
