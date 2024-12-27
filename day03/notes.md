## 2024 Day 3


### Notes:
- multiply some numbers
    - `mul(X, Y)` where `X` and `Y` are 1-3 digit ints.
- Input is "corrupted" and some `mul()` instructions have characters instead of ints.
    - `mul(4*`, `mul(6,9!)`, `?(12,34)`, or `mul ( 2 , 4 )`

### Example of corrupted memory (test input)

- x**mul(2,4)**%&mul[3,7]!@^do_not_**mul(5,5)**+mul(32,64]then(**mul(11,8)mul(8,5)**)`
    - Only the four bold sections are real `mul` instructions.
    - Sum all results produces `161 = (2*4 + 5*5 + 11*8 + 8*5)`

### Part 1 

- Use all "uncorrecupted' `mul()` instructions. What do you get if you sum all of the `mul()` results?
