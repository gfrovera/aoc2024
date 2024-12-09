


def input_splitter(path: str) -> list[list[int], list[int]]:

    result_lst = [[],[]]

    with open(path, 'r') as input:
        for line in input:
            line_parts = line.strip().split()
            l0, l1 = map(int, line_parts)

            result_lst[0].append(l0)
            result_lst[1].append(l1)
    return result_lst

def pop_sorter(input: list[list[int], list[int]]) -> list[int]:
    ...

if __name__ == "__main__":
    x = input_splitter('part_01_input.txt')

    print(f'first 10 of list 0 are: {x[0][:10]}')
    print(f'first 10 of list 1 are: {x[1][:10]}')

    # Sort list
    sx_one = sorted(x[0])
    sx_two = sorted(x[1])

    print(f'first 10 of list 0 are: {sx_one[:10]}')
    print(f'first 10 of list 1 are: {sx_two[:10]}') 

    print(enumerate(sx_one))
