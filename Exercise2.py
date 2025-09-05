
# Write a Python function that takes a list of numbers as input and outputs
# the maximum, minimum and median values in the list.

from statistics import median

def func (list):
    list.sort()
    max = list[-1]
    min = list[0]
    med = median(list)
    return max, min, med

x = [4, 2, 6, 12, -4, 3]
res_max, res_min, res_med = func(x)
print("Max is:", res_max, "\nMin is:", res_min, "\nMed is:", res_med)

