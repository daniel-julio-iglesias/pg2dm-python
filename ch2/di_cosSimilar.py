from math import sqrt

# "Clara": {"Blues Traveler": 4.75, "Norah Jones": 4.5, "Phoenix": 5, "The Strokes": 4.25, "Weird Al": 4},
# "Robert": {"Blues Traveler": 4, "Norah Jones": 3, "Phoenix": 5, "The Strokes": 2, "Weird Al": 1}

# "Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2, "Norah Jones": 4.5, "Phoenix": 5, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2},
# "Angelica": {"Blues Traveler": 3.5, "Norah Jones": 2.0, "Phoenix": 4.5, "Slightly Stoopid": 5.0, "The Strokes": 1.5, "Slightly Stoopid2": 2.5, "The Strokes2": 2.0},

users = {
        "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0},
        "Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2, "Norah Jones": 4.5, "Phoenix": 5, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2},
        "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
        "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
        "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
        "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
        "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
        "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
        "Clara": {"Blues Traveler": 4.75, "Norah Jones": 4.5, "Phoenix": 5, "The Strokes": 4.25, "Weird Al": 4},
        "Robert": {"Blues Traveler": 4, "Norah Jones": 3, "Phoenix": 5, "The Strokes": 2, "Weird Al": 1}
        }


def cos_similar(rating1, rating2):
    vec_length_1 = 0
    vec_length_2 = 0
    dot_product = 0

    include_all_occurrences(rating1, rating2)

    # print("rating1 ==> ", rating1)

    x,y = create_vectors(rating1, rating2)

    # print("x ==> ", x)
    # print("y ==> ", y)

    for rate in x:
        vec_length_1 += rate ** 2

    for rate in y:
        vec_length_2 += rate ** 2

    for rate1, rate2 in zip(x,y):
        dot_product += rate1 * rate2

    if vec_length_1 == 0 or vec_length_2 == 0:
        return 0

    # vec_length_1 = sqrt(vec_length_1)
    print("vec_length_1 before sqrt: ", vec_length_1)
    vec_length_1 = pow(vec_length_1, 1/2)
    print("vec_length_2 before sqrt: ", vec_length_2)
    vec_length_2 = sqrt(vec_length_2)
    similarity = dot_product / (vec_length_1 * vec_length_2)
    print("dot_product: ", dot_product)
    print("vec_length_1: ", vec_length_1)
    print("vec_length_2: ", vec_length_2)
    print("similarity: ", similarity)

    return similarity


def include_all_occurrences(rating1, rating2):
    vector_x = []
    vector_y = []

    for key in rating1:
        if key not in rating2:
            rating2.setdefault(key, 0)

    for key in rating2:
        if key not in rating1:
            rating1.setdefault(key, 0)

    # l1 = sorted(list(rating1.items()))
    # l2 = sorted(list(rating2.items()))

    # print(l1)
    # print(l2)

    return


def create_vectors(rating1, rating2):
    vector_x = []
    vector_y = []

    l1 = sorted(list(rating1.items()))
    l2 = sorted(list(rating2.items()))

    for (a,b) in l1:
        vector_x.append(b)

    for (a,b) in l2:
        vector_y.append(b)

    # print("vector_x ==> ", vector_x)
    # print("vector_y ==> ", vector_y)

    return vector_x, vector_y


def main():
    # cos_similar(users['Clara'], users['Robert'])
    cos_similar(users['Angelica'], users['Veronica'])
    # cos_similar(users['Veronica'], users['Angelica'])

    # include_all_occurrences(users['Angelica'], users['Veronica'])

    # print(sorted(users['Angelica'].items()))
    # print(sorted(users['Veronica'].items()))


if __name__ == '__main__':
    main()
