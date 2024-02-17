import numpy as np
numbers = [1.2, 1.0, 25.0, 43.25, 76.76, 987.173, 4.0, 42.0]
arr = np.array(numbers)
def double_this(arr): #(1 задача)
    return arr*2
print(double_this(arr))
def select_even(arr): #(2 задача)
    arr1 = arr[np.where(arr%2==0)]
    return arr1
print(select_even(arr))
def wipe_even(arr, target_value, in_place): #(задача 3)
    def f(arr, target_value):
        arr[arr % 2 == 0] = target_value
        return arr
    if not (target_value):
        target_value = 0
    if in_place == False:
        arr2 = arr.copy()
        arr2 = f(arr2, target_value)
        return arr2
    else:
        f(arr, target_value)
        return arr
print(wipe_even(arr, 888, True))
normalize = 0
def weighted_sum(weights, grades, normalize): #(задача 4)
    weights = np.array(weights)
    grades = np.array(grades)
    c = weights * grades
    normalize = np.sum(c)
    return normalize
print(weighted_sum(([0.9, 0.1, 0.8]), ([19, 45, 9]), normalize))
def mean_by_gender(grades1, genders): #(задача 5)
    grades1 = np.array(grades1)
    genders = np.array(genders)
    c = grades1[genders == "male"]
    d = grades1[genders == "female"]
    p = np.mean(c)
    v = np.mean(d)
    s = {"male": p, "female": v}
    return s
print(mean_by_gender(([3, 2, 5, 5, 1]), (["female", "female", "male", "male", "female"])))
doh = np.array([11, 6435, 87439857, 938, 54, 231, 879, 12324]) #(задача 6)
def calculate_tax(doh):
    c = np.cumsum(doh)
    d = c[c <= 1000]
    v = c[c > 1000]
    l = d * 0
    l[0] = v[0]
    m = sum(np.concatenate([d, l])*0.13)
    s = sum(v[1:]*0.2)
    return m+s
print(calculate_tax(doh))

