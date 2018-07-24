from math import sqrt


users3 = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Matt":  {"Imagine Dragons": 3, "Daft Punk": 4,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Ben":   {"Kacey Musgraves": 4, "Imagine Dragons": 3,
                    "Lorde": 3, "Fall Out Boy": 1},
          "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
                    "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
          "Tori":  {"Kacey Musgraves": 5, "Imagine Dragons": 4,
                    "Daft Punk": 5, "Fall Out Boy": 3}}


def average_rating(rating):
    # print(rating)
    num = 0
    avg = 0
    for artist in rating:
        num += 1
        avg += rating[artist]
    if num != 0:
        avg /= num
    else:
        avg = 0

    return avg


def cos_similarity(artist1, artist2):
    selections = {}
    for user in users3:
        if artist1 in users3[user].keys():
            selection1 = user, artist1, users3[user][artist1]
        else:
            selection1 = False
        if artist2 in users3[user].keys():
            selection2 = user, artist2, users3[user][artist2]
        else:
            selection2 = False
        if selection1 and selection2:
            selections.setdefault(user, 'None')
            selections[user] = {'average rating': average_rating(users3[user]),
                                selection1[1]: selection1[2],
                                selection2[1]: selection2[2]}

    # print("selections ==> ", selections)

    # Result:
    # selections == > {
    #     'Ben': {'average rating': 2.75, 'Kacey Musgraves': 4, 'Imagine Dragons': 3},
    #     'Chris': {'average rating': 3.2, 'Kacey Musgraves': 4, 'Imagine Dragons': 4},
    #     'Tori': {'average rating': 4.25, 'Kacey Musgraves': 5, 'Imagine Dragons': 4}}

    numerator = 0
    for selection in selections:
        # print("selections[selection] ==> ", selections[selection])
        # print("selections[selection].values() ==> ", selections[selection].values())
        L = [v for k, v in selections[selection].items()
             if k != 'average rating']
        # print("L ==> ", L)
        average = selections[selection]['average rating']
        # print("average ==> ", average)
        l_numerator = 1
        for scale in L:
            l_numerator *= scale - average
        numerator += l_numerator
    # print("numerator ==> ", numerator)

    # Calculate the denominator for artist1
    denom_art1 = 0
    for selection in selections:
        scale = selections[selection][artist1]
        average = selections[selection]['average rating']
        # print("scale, average ==>", scale, average)
        denom_art1 += (scale - average) ** 2
    # print("denom_art1 ==> ", denom_art1)
        
        

    # Calculate the denominator for artist1    
    denom_art2 = 0
    for selection in selections:
        scale = selections[selection][artist2]
        average = selections[selection]['average rating']
        # print("scale, average ==>", scale, average)
        denom_art2 += (scale - average) ** 2
    # print("denom_art2 ==> ", denom_art2)

    if denom_art1 == 0 or denom_art2 == 0:
        similarity = 0
    else:
        similarity = numerator / (sqrt(denom_art1) * sqrt(denom_art2))
    print("similarity ==> ", artist1, artist2, similarity)
    


def computeSimilarity(band1, band2, userRatings):
    averages = {}
    for (key, ratings) in userRatings.items():
        averages[key] = (float(sum(ratings.values()))
                      / len(ratings.values()))

    num = 0  # numerator
    dem1 = 0 # first half of denominator
    dem2 = 0
    for (user, ratings) in userRatings.items():
        if band1 in ratings and band2 in ratings:
            avg = averages[user]
            num += (ratings[band1] - avg) * (ratings[band2] - avg)
            dem1 += (ratings[band1] - avg)**2
            dem2 += (ratings[band2] - avg)**2
    if dem1 == 0 or dem2 == 0:
        similarity = 0
    else:
        similarity = num / (sqrt(dem1) * sqrt(dem2))

    print("band1, band2, similarity ==> ", band1, band2, similarity)
    
    return similarity


def main():
    # cos_similarity("Kacey Musgraves", "Imagine Dragons")

    # cos_similarity("Kacey Musgraves", "Lorde")
    # cos_similarity("Imagine Dragons", "Lorde")
    # cos_similarity("Daft Punk", "Lorde")


    computeSimilarity("Kacey Musgraves", "Imagine Dragons", users3)

    computeSimilarity("Kacey Musgraves", "Lorde", users3)
    computeSimilarity("Imagine Dragons", "Lorde", users3)
    # computeSimilarity("Duft Punk", "Lorde", users3)    
    computeSimilarity("Daft Punk", "Lorde", users3)
    computeSimilarity("Kacey Musgraves", "Daft Punk", users3)


if __name__ == '__main__':
    main()
