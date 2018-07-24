"""
Pearson implementation
>>> pearson(users['Angelica'], users['Bill'])
-0.90405349906826993
>>> pearson(users['Angelica'], users['Hailey'])
0.42008402520840293
>>> pearson(users['Angelica'], users['Jordyn'])
0.76397486054754316
"""

from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0},
         "Clara": {"Blues Traveler": 4.75, "Norah Jones": 4.5, "Phoenix": 5, "The Strokes": 4.25, "Weird Al": 4},
         "Robert": {"Blues Traveler": 4, "Norah Jones": 3, "Phoenix": 5, "The Strokes": 2, "Weird Al": 1}
        }


def pearson(rating1, rating2):
    """Computes the Pearson coefficient. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    # First expression for numerator
    num_sum_mult = 0
    for key in rating1:
        if key in rating2:
            num_sum_mult += (rating1[key] * rating2[key])
    print('num_sum_mult: ', num_sum_mult)
    # Numerator - rest expression
    num_sum_rat1 = 0
    num_sum_rat2 = 0
    num = 0
    for key in rating1:
        if key in rating2:
            num_sum_rat1 += rating1[key]
            num += 1
    for key in rating1:
        if key in rating2:
            num_sum_rat2 += rating2[key]
    num_rest = (num_sum_rat1 * num_sum_rat2) / num
    print('num_sum_rat1: ', num_sum_rat1)
    print('num_sum_rat2: ', num_sum_rat2)
    print('num: ', num)
    print('num_rest: ', num_rest)
    # Numerator
    numerator = num_sum_mult - num_rest
    print('numerator: ', numerator)

    # Denominator - rating 1 - sum of squares
    denom_rat1_sum_sqrs = 0
    for key in rating1:
        if key in rating2:
            denom_rat1_sum_sqrs += (rating1[key] ** 2)
    print('denom_rat1_sum_sqrs: ', denom_rat1_sum_sqrs)
    # denom - rating 1 - sum divided number
    den_rat1_rest =  (num_sum_rat1 ** 2) / num
    print("den_rat1_rest: ", den_rat1_rest)
    # denom - rat1 - sqrt
    den_rat1_sqr = sqrt(denom_rat1_sum_sqrs - den_rat1_rest)
    print("den_rat1_sqr: ", den_rat1_sqr)

    # Denominator - rating 2 - sum of squares
    denom_rat2_sum_sqrs = 0
    for key in rating1:
        if key in rating2:
            denom_rat2_sum_sqrs += (rating2[key] ** 2)
    print('denom_rat2_sum_sqrs: ', denom_rat2_sum_sqrs)
    # denom - rating 2 - sum divided number
    den_rat2_rest =  (num_sum_rat2 ** 2) / num
    print("den_rat2_rest: ", den_rat2_rest)
    # denom - rat2 - sqrt
    den_rat2_sqr = sqrt(denom_rat2_sum_sqrs - den_rat2_rest)
    print("den_rat2_sqr: ", den_rat2_sqr)

    # denominator
    denominator =  den_rat1_sqr * den_rat2_sqr
    print("denominator: ", denominator)

    # Pearson r
    r = 0
    if denominator != 0:
        r = numerator / denominator

    print("Pearson coefficient: ", r)

    return r


def main():
    # pearson(users['Clara'], users['Robert'])

    # pearson(users['Angelica'], users['Bill'])
    # pearson(users['Angelica'], users['Hailey'])
    pearson(users['Angelica'], users['Jordyn'])


if __name__ == '__main__':
    main()
