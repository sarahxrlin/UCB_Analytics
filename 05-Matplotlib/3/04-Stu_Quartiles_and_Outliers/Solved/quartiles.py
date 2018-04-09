#!usr/bin/python


def lower_quartile(arr):
    index = len(arr) // 4
    return (index, arr[index])


def upper_quartile(arr):
    index = 3 * len(arr) // 4
    return (index, arr[index])


def iqr(arr):
    (_, lower) = lower_quartile(arr)
    (_, upper) = upper_quartile(arr)
    return upper - lower
