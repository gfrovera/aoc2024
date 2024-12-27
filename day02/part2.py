from typing import Iterator


tst_slice = None
InputList = list[list[int]]
SafetyList = list[bool]

tst_input = [1, 2, 7, 8, 9]
tst_input2 = [1, 3, 6, 7, 9]


def input_splitter(input_path: str) -> InputList:

    list_of_lists = []

    with open(input_path, 'r') as file:
        for line in file:
            list_of_lists.append(list(map(int, line.split())))

    return list_of_lists


class FloorSafetyEvaluator:

    def __init__(self, floor_list: InputList) -> None:
        self.floor_list = floor_list

    def floor_evaluator(self, input: list[int]) -> bool:
        '''Evaluates if single floor: list[int] is Safe/Unsafe'''

        if all(0 < (input[i] - input[i-1]) < 4 for i in range(1, len(input))):
            return True
        elif all(-4 < (input[i] - input[i-1]) < 0 for i in range(1, len(input))):
            return True
        else:
            return False

    def evaluate_all_floors(self) -> SafetyList:
        '''Evaluate all floor lists in the input list of lists'''

        floor_sts_list = []

        for idx, lst in enumerate(self.floor_list):
            floor_sts_list.append(self.floor_evaluator(lst))

        return floor_sts_list


class FloorReEvaluator(FloorSafetyEvaluator):

    def __init__(self,  floor_list: InputList) -> None:
        super().__init__(floor_list)

    def mark_floor_unsafe(self) -> Iterator[tuple[bool, list[int]]]:
        initial_results = self.evaluate_all_floors()
        floors_with_status = zip(initial_results, self.floor_list)
        return floors_with_status

    def extract_unsafe(self, results: Iterator[tuple[bool, list[int]]]) -> InputList:
        recheck_list: InputList = []
        for sts, lst in results:
            if not sts:
                recheck_list.append(lst)
        
        return recheck_list
    
    def create_recheck_list(self) -> InputList:

        recheck_list = (
            self.extract_unsafe(
                self.mark_floor_unsafe()
                )
            )

        return recheck_list

    def recheck_floor_status(self, recheck_list: InputList) -> SafetyList:
        
        iter_results = []

        for idx, lst in enumerate(recheck_list):
            inner_results = []
            for idy, flr in enumerate(lst):
                retest_lst =  lst[:idy]  + lst[idy+1:]
                if self.floor_evaluator(retest_lst):
                    inner_results.append(True)
                else:
                    inner_results.append(False)
            
            iter_results.append(inner_results)

        return iter_results
    
    def final_safe_flr_cnt(self, iter_result_list: list[list[bool]]) -> int:

        add_safe_floors = []
        for val in iter_result_list:
            add_safe_floors.append(any(val))
        
        return sum(add_safe_floors)
        
        

if __name__ == '__main__':
 
    input_list = input_splitter('part1_input.txt')
    floor_evaluator = FloorReEvaluator(input_list)
    safe_floor_list = floor_evaluator.evaluate_all_floors()
    print('...')



    safe_floor_list = floor_evaluator.mark_floor_unsafe()
    recheck_list = floor_evaluator.create_recheck_list()
    inner_checks = floor_evaluator.recheck_floor_status(recheck_list)
    additional_flr_lst = floor_evaluator.final_safe_flr_cnt(inner_checks)
    part_two_answer = sum(safe_floor_list) + additional_flr_lst
    print(part_two_answer)