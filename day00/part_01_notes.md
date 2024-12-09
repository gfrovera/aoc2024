# 2024 Day 01


## Part One:

### Problem Summary:

-Pair up smallest number in left list (00) with the smallest number in right list (10).
  -The second smallest in left list (01) with smalles numbe right list (11) and so on...

- How far apart are the two numbers?  Difference between:
  - Add up all those distances

```txt
Always take lowest numbers in both lists
After calculating need to remove used numbers from both lists.
Resort to get next lowest until all are used.
Add up all differences for answer
```

---

## Part Two:

### Problem Summary

- Find how many times the number from left list appears in the right list.
- Multiply the left list number by frequency in right list
- Sum all values for output