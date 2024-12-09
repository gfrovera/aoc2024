
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

def pop_sorter(input: list[list[int], list[int]]) -> int:
    '''Sorts lists in list of lists, converts all differences
    of list values into the absolute values and finally sums all
    items in list.
    '''
    l = sorted(input[0])
    r = sorted(input[1])

    diffs = [lv - rv for lv, rv in zip(l, r)]
    abs_list = list(map(abs, y))

    return sum(abs_list)
    

if __name__ == "__main__":
    x = input_splitter('./part_01_input.txt')
    pop_sorter(x)
