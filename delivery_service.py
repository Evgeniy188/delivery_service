import sys


def main():
    seq = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    limit = int(sys.stdin.readline().rstrip())
    print(delivery_service(seq, limit))


def delivery_service(seq: list, limit: int) -> int:
    """Функция для определения минимального количества транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве"""
    seq.sort()
    count_platform = 0
    right_pointer = len(seq) - 1
    while right_pointer > 0:
        current_sum = seq[0] + seq[right_pointer]
        if current_sum <= limit:
            seq.pop(right_pointer)
            seq.pop(0)
            count_platform += 1
            right_pointer = len(seq) - 1
            continue
        else:
            right_pointer -= 1
    count_platform += len(seq)
    return count_platform


if __name__ == '__main__':
    main()
