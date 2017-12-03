def parse(filename):
    with open(filename) as f:
        return [int(c) for c in f.read().strip()]

def main(data):
    current = data[0]
    sum = 0

    for i in range(1, len(data)):
        tmp = data[i]
        if current == tmp:
            sum += int(current)
        else:
            current = tmp

    if current == data[0]:
        sum += int(current)

    print(sum)

if __name__ == '__main__':
    data = parse('input-01.txt')
    main(data)