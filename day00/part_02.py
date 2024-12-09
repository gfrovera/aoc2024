from collections import defaultdict

def input_splitter(path: str) -> list[list[int], list[int]]:
    '''Takes the challenge input and creates a list of lists.
    Each "column" in txt file becomes a list in the list of lists
    '''
    result_lst = [[],[]]

    with open(path, 'r') as input:
        for line in input:
            line_parts = line.strip().split()
            l0, l1 = map(int, line_parts)

            result_lst[0].append(l0)
            result_lst[1].append(l1)
    
    return result_lst

def part_one(input: list[list[int], list[int]]) -> int:
    '''Sorts lists in list of lists, converts all differences
    of list values into the absolute values and finally sums all
    items in list.
    '''
    l = sorted(input[0])
    r = sorted(input[1])

    diffs = [lv - rv for lv, rv in zip(l, r)]
    abs_list = list(map(abs, diffs))

    return sum(abs_list)

def part_two(input: list[list[int], list[int]]) -> int:
    '''Finds frequency of list 1 values in list 2.
    Multiplies list 1 value by its list 2 frequency
    Sums the resulting list of integers
    '''

    dd = defaultdict(int)

    for val in x[1]:
        dd[val] += 1

    product_lst = []

    for idx, val in enumerate(x[0]):
        if val in dd.keys():
            product_lst.append(val * dd[val])
        else:
            product_lst.append(0)

    return sum(product_lst)

if __name__ == "__main__":
    x = input_splitter('./part_01_input.txt')
    # x = input_splitter('./test_input.txt')
    
    y = part_one(x)
    print(y)

    z = part_two(x)
    print(z)

