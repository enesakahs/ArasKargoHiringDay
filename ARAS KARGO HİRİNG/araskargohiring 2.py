#Bu kodlar, iki farklı sayı dizisi arasındaki kesişimi (yani aynı elemanları) bulmayı ve ardından bu kesişim elemanlarını sıralamayı amaçlayan bir Python programıdır.
#Program, kullanıcıdan ilk dizinin eleman sayısını ve ardından bu dizinin elemanlarını alır. 
#Daha sonra, kullanıcıdan ikinci dizinin eleman sayısını ve elemanlarını alır. Ardından, iki dizinin kesişimini hesaplar ve sıralar. 
#Son olarak, bu kesişim elemanlarını çıktı olarak verir.
import math
import os
import random
import re
import sys


def sortIntersect(volcanic, nonVolcanic):
    # Find the intersection of the two arrays
    intersection = set(volcanic) & set(nonVolcanic)
    # Sort the intersection in descending order
    sorted_intersection = sorted(list(intersection), reverse=True)
    return sorted_intersection


# Initialize result array
    result = []

# Loop through both arrays and find the intersection
    i = 0
    j = 0
    while i < len(volcanic) and j < len(nonVolcanic):
        if volcanic[i] == nonVolcanic[j]:
            result.append(volcanic[i])
            i += 1
            j += 1
        elif volcanic[i] < nonVolcanic[j]:
            i += 1
        else:
            j += 1

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    volcanic_count = int(input().strip())

    volcanic = []

    for _ in range(volcanic_count):
        volcanic_item = int(input().strip())
        volcanic.append(volcanic_item)

    nonVolcanic_count = int(input().strip())

    nonVolcanic = []

    for _ in range(nonVolcanic_count):
        nonVolcanic_item = int(input().strip())
        nonVolcanic.append(nonVolcanic_item)

    result = sortIntersect(volcanic, nonVolcanic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()