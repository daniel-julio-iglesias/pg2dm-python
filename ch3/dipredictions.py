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

    # print("band1, band2, similarity ==> ", band1, band2, similarity)
    
    return similarity



def normalizeRatings(user, userRatings):
    # print("user ==> ", user)
    # print("userRatings[user].items() ==> ", userRatings[user].items())
    # print("userRatings[user].keys() ==> ", userRatings[user].keys())
    # print("userRatings[user].values() ==> ", userRatings[user].values())
    # print("min(userRatings[user].values()) ==> ", min(userRatings[user].values()))    
    # print("max(userRatings[user].values()) ==> ", max(userRatings[user].values()))    

    nr_u = {}  # normalized ratings for user
    nr = 0
    min_r = min(userRatings[user].values())
    max_r = max(userRatings[user].values())
    
    for (band, rating) in userRatings[user].items():
        if max_r == min_r:
            nr = -1
        else:
            nr = (2* (rating - min_r) - (max_r - min_r))/(max_r - min_r)
        # print("nr ==> ", nr)
        nr_u.setdefault(band, nr)
            
    # print("nr_u ==> ", nr_u)
    return nr_u


def predictRating(user, item, userRatings):
    # print("user, item ==> ", user, item)
    nr_u = normalizeRatings(user, users3)
    # print("nr_u ==> ", nr_u)
    # print("userRatings[user].items() ==> ", userRatings[user].items())

    np = 0 # normalized prediction
    num = 0
    dem = 0

    min_r = min(userRatings[user].values())
    max_r = max(userRatings[user].values())

    for (band, rating) in userRatings[user].items():
        num += computeSimilarity(item, band, userRatings) * nr_u[band]
        dem += abs(computeSimilarity(item, band, userRatings))

    if dem == 0:
        np = 0
    else:
        np = num / dem

    # print("min_r ==> ", min_r)
    # print("max_r ==> ", max_r)
    # print("num ==> ", num)
    # print("dem ==> ", dem)
    # print("np ==> ", np)

    prediction = 0.5 *((np + 1) * (max_r - min_r)) + min_r

    print("prediction ==> ", prediction)
    return prediction



def main():
    # computeSimilarity("Kacey Musgraves", "Imagine Dragons", users3)
    # computeSimilarity("Kacey Musgraves", "Lorde", users3)
    # computeSimilarity("Imagine Dragons", "Lorde", users3)
    # computeSimilarity("Daft Punk", "Lorde", users3)
    # computeSimilarity("Kacey Musgraves", "Daft Punk", users3)


    predictRating("David", "Kacey Musgraves", users3)



if __name__ == '__main__':
    main()
