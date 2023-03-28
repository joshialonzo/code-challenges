def index_all(search_list, number):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == number:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], number):
                indices.append([i]+index)
    return indices


def print_index_all(lst, number):
    print(f"Inp: {lst},{number} - Out: {index_all(lst, number)}")


def main():
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print_index_all(example, 2)


if __name__ == "__main__":
    main()
