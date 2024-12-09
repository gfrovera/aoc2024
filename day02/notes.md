# Day Two

## Part One Notes

### Problem Summary

- Input is one `report` per line
- Each `report` is a list of int called `levels`
- Find which `reports` are `safe`
  - all increasing
  - all decreasing
  - any two adjacent levels differ by `at least one`
  - any two adjacent levels differ by `at most three`

#### Examples
- 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
- 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
- 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
- 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
- 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
- 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

#### Steps

1. Import each line in input as list element in a list of lists
2. For each line (_floor_) determine if criteria for _safe_ is met
3. Build binary list of safe/unsafe where safe is 1
4. Sum up all items in list to determine # of safe floors.