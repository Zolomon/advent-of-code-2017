def parse(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [[int(number) for number in line.split('\t')] for line in lines]

def solve(lines):
    total_sum = sum(map(lambda line: max(line) - min(line), lines))
    print(total_sum)

if __name__ == '__main__':
    lines = parse('input-02.txt')
    solve(lines)