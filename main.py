from random import randint

import pandas as pandas


def randList(N):
    a = []
    for i in range(N):
        a.append(randint(1, 1000))
    return(a)

def bubbleSortForCount(a):
    count = 0
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            count += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return(count)

def bubbleSort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return(a)

n = 10
counts = []
iterations = []

def arifmeric_progression():
    n = 10
    counts = []
    iterations = []
    for i in range(100):
        arr = randList(n)
        count = int(bubbleSortForCount(arr))
        counts.append(n)
        iterations.append(count)
        n += 10
    data = dict(len=counts, vhody=iterations)
    df = pandas.DataFrame(data)
    df.to_csv(r'iterationsArifmetic.csv', sep=';', index=False)

def geomtric_progression():
    n = 2
    counts = []
    iterations = []
    for i in range(15):
        arr = randList(n)
        count = int(bubbleSortForCount(arr))
        counts.append(n)
        iterations.append(count)
        n *= 2
    data = dict(len=counts, vhody=iterations)
    df = pandas.DataFrame(data)
    df.to_csv(r'iterationsGeometric.csv', sep=';', index=False)


if __name__ == '__main__':
    arifmeric_progression()
    geomtric_progression()
