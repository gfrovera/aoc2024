import re

# test_input = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

RawMuls = list[tuple[str,str]]
IntMuls = list[tuple[int,int]]

def skibity_whitespace(input_sting: str) -> str:
    return ''.join(input_sting.split())

def convert_to_int(input_list: RawMuls) -> IntMuls:
    str_as_int = [(int(x), int(y)) for x, y in input_list]
    return str_as_int

def mul(x: int, y: int) -> int:
    return x * y

def solver() -> int:

    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    with open('part1_input.txt', 'r') as input_file:
        input_data = input_file.read().replace('\n','')


    mul_matches = re.findall(mul_pattern, skibity_whitespace(input_data))
    mul_ints = convert_to_int(mul_matches)

    return sum([mul(x, y) for x, y in mul_ints])




if __name__ == '__main__':
    answer = solver()
    print(answer)
