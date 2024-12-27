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

3. Calculate the diff between n[i] - n[i]+1
  * This was my initial thought of evaluating the differences. If they were between 1 and 3. This didnt work with lists that had an increase _and_ a decrease. Problem summary stated that the _all_ have to increase or decrease. This method masked that.

4. Just evaluate if all elements are increasing or decreasing by no more than 3 or less than 1.
  * Found that I could utilize all() to evaluate the change accross all elements. if they all meet the criteria then append `True` to a list. If they dont all increase or decrease then append `False` to a list.
  * Once list of `bool` is returned, `sum` all `True` values in list to get the answer?


## Part Two Notes

### Problem Summary

What if each list was allowed to have 1 value that fell outside of the step 1's rules. If this is done how many `True` results are there.

#### Examples

- 7 6 4 2 1: Safe without removing any level.
- 1 2 7 8 9: Unsafe regardless of which level is removed.
- 9 7 6 2 1: Unsafe regardless of which level is removed.
- 1 3 2 4 5: Safe by removing the second level, 3.
- 8 6 4 4 1: Safe by removing the third level, 4.
- 1 3 6 7 9: Safe without removing any level.

#### Steps

- Change to create two seperate lists. `safe_floors` is a list of all `True` floors, and `double_check` will be a list that evaluted `False`.
- Check `double_check` list to see if any can be changed to `True` be removing 1 item from the list'