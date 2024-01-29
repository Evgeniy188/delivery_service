# 106143761
def delivery_service(weight_robot_list: list, limit: int) -> int:
    """Функция для определения минимального количества транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве"""
    weight_robot_list_sort = sorted(weight_robot_list)
    count_platform = 0
    left_pointer = 0
    right_pointer = len(weight_robot_list_sort) - 1
    while left_pointer <= right_pointer:
        current_sum = (weight_robot_list_sort[left_pointer] +
                       weight_robot_list_sort[right_pointer])
        if current_sum <= limit:
            left_pointer += 1
            right_pointer -= 1
            count_platform += 1
        else:
            right_pointer -= 1
            count_platform += 1
    return count_platform


if __name__ == '__main__':
    weight_robot_list = [int(x) for x in input().split(' ')]
    limit = int(input())
    print(delivery_service(weight_robot_list, limit))
