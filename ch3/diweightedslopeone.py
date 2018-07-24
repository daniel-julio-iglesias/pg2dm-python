from math import sqrt
import pprint

users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
          "Ben": {"Taylor Swift": 5, "PSY": 2},
          "Clara": {"PSY": 3.5, "Whitney Houston": 4},
          "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}


def computeDeviation(item1, item2, userRatings):
    # print("userRatings.items() ==> ", userRatings.items())
    deviation = 0
    card = 0
    num = 0
    for user in userRatings:
        # pprint.pprint(userRatings[user])
        if item1 in userRatings[user] and item2 in userRatings[user]:
            card += 1
            num += userRatings[user][item1] - userRatings[user][item2]
    # print('card ==> ', card)
    # print('num ==> ', num)
    if card == 0:
        deviation = 0
    else:
        deviation = num/card
        
    # print("deviation ==> ", deviation)
    return deviation, card



def createDeviationsTable(userRatings):
    allItems = []
    for user in userRatings:
        # print('userRatings[user] ==> ', userRatings[user])
        # print('userRatings[user].keys() ==> ', userRatings[user].keys())
        for key in userRatings[user].keys():
            if key not in allItems:
                allItems.append(key)
    # print('allItems ==> ', allItems)

    # deviationsTable = []
    deviationsTable = {}
    
    for item1 in allItems:
        for item2 in allItems:
            # deviationsTable.append((item1, item2, computeDeviation(item1, item2, userRatings)))
            # deviationsTable.setdefault((item1, item2), computeDeviation(item1, item2, userRatings))
            deviationsTable.setdefault((item1, item2), (0.0, 0))
            deviationsTable[(item1, item2)] = computeDeviation(item1, item2, userRatings)
            
            

    pprint.pprint(deviationsTable)
    return deviationsTable


def calculatePwS1(user, item, deviations, userRatings):
    # Calculate numerator:
    num = 0
    dem = 0
    for artist, rating in userRatings[user].items():
        print('artist, rating ==> ', artist, rating)
        print('deviations[(item, artist)] ==> ', deviations[(item, artist)])
        # print('deviations[(item, artist)][0] ==> ', deviations[(item, artist)][0])
        # print('deviations[(item, artist)][1] ==> ', deviations[(item, artist)][1])
        deviation = deviations[(item, artist)][0]
        cardinality = deviations[(item, artist)][1]
        num += (rating + deviation) * cardinality
        dem += cardinality

    print('num ==> ', num)
    
    # Calculate denominator:
    # dem = 0

    print('dem ==> ', dem)

    if dem == 0:
        PwS1 = 0
    else:
        PwS1 = num / dem

    print('PwS1 ==> ', PwS1)
    return PwS1


def main():
    # print("computeDeviation('Taylor Swift', 'PSY', users2) ==> ", computeDeviation('Taylor Swift', 'PSY', users2))
    # print("computeDeviation('PSY', 'Taylor Swift', users2) ==> ", computeDeviation('PSY', 'Taylor Swift', users2))    

    deviationsTable = createDeviationsTable(users2)

    calculatePwS1('Ben', 'Whitney Houston', deviationsTable, users2)


if __name__ == '__main__':
    main()
