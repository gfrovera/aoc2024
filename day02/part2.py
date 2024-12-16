# Day Two: Part 1
# tst_slice = 2
tst_slice = None
ResultList = list[list[int]]
SafetyList = list[bool]

def input_splitter(input_path: str) -> ResultList:

    list_of_lists = []

    with open(input_path, 'r') as file:
        for line in file:
            list_of_lists.append(list(map(int, line.split())))

    return list_of_lists

def find_list_element_diff(input: ResultList ) -> ResultList:
    
    input_diffs = []

    for idx, lst in enumerate(input):
        diff_results = []
        for idxx in range(len(lst)-1):
            val_diffs = lst[idxx] - lst[idxx+1]
            diff_results.append(val_diffs)
        
        input_diffs.append(diff_results)

    return input_diffs
  
def evaluate_floor_saftey(input: ResultList) -> SafetyList:

    floor_status =[]

    for idx, lst in enumerate(input):
        if all(0 < (lst[i] - lst[i-1]) < 4 for i in range(1, len(lst))):
            floor_safe = True
        elif all(-4 < (lst[i] - lst[i-1]) < 0 for i in range(1, len(lst))):
            floor_safe = True
        else:
            floor_safe= False
        
        floor_status.append(floor_safe)

    return floor_status

def unsafe_floors(status_input: SafetyList, list_input: ResultList) -> ResultList:
    combined_inputs = zip(status_input, list_input)

    # Extract Unsafe (False) Lists
    dbl_check_list = []
    for sts, lst in combined_inputs:
        if not sts:
            dbl_check_list.append(lst)

    return dbl_check_list

if __name__ == '__main__':

    input_list: list[list[int]] = (
        input_splitter('test_input.txt')[:tst_slice]
        )
    safety_list = evaluate_floor_saftey(input_list)

    dbl_check_these = unsafe_floors(safety_list, input_list)


    print(len(safety_list))
    print(sum(safety_list))
    print(list(zip(safety_list, input_list)))
    print(dbl_check_these)
