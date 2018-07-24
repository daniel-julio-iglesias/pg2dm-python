# Nearest Neighbor Classifier
import pprint as pp

music = {
        "Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5, "blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
        "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1, "rap": 1},
        "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2, "guitar": 4, "backup vocals": 1, "rap": 1},
        "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5, "beat": 4, "blues": 4, "guitar": 1, "backup vocals": 5, "rap": 1},
        "The Black Keys/Magic Potion": {"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5, "backup vocals": 1, "rap": 1},
        "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5, "beat": 3.5, "blues": 3, "guitar":4, "backup vocals": 5, "rap": 1},
        "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1, "backup vocals": 1, "rap": 1},
        "Mike Posner": {"piano": 2.5, "vocals": 4, "beat": 4, "blues": 1, "guitar": 1, "backup vocals": 1, "rap": 1},
        "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5, "beat": 5, "blues": 1, "guitar": 2, "backup vocals": 2, "rap": 4},
        "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3, "blues": 2, "guitar": 1, "backup vocals": 2, "rap": 1}
        }


#
# the item vector represents the attributes: piano, vocals,
# beat, blues, guitar, backup vocals, rap
#
items = {
        "Dr Dog/Fate": [2.5, 4, 3.5, 3, 5, 4, 1],
        "Phoenix/Lisztomania": [2, 5, 5, 3, 2, 1, 1],
        "Heartless Bastards/Out at Sea": [1, 5, 4, 2, 4, 1, 1],
        "Todd Snider/Don't Tempt Me": [4, 5, 4, 4, 1, 5, 1],
        "The Black Keys/Magic Potion": [1, 4, 5, 3.5, 5, 1, 1],
        "Glee Cast/Jessie's Girl": [1, 5, 3.5, 3, 4, 5, 1],
        "La Roux/Bulletproof": [5, 5, 4, 2, 1, 1, 1],
        "Mike Posner": [2.5, 4, 4, 1, 1, 1, 1],
        "Black Eyed Peas/Rock That Body": [2, 5, 5, 1, 2, 2, 4],
        "Lady Gaga/Alejandro": [1, 5, 3, 2, 1, 2, 1]
        }


users = {"Angelica": {"Dr Dog/Fate": "L", "Phoenix/Lisztomania": "L",
                    "Heartless Bastards/Out at Sea": "D",
                    "Todd Snider/Don't Tempt Me": "D",
                    "The Black Keys/Magic Potion": "D",
                    "Glee Cast/Jessie's Girl": "L",
                    "La Roux/Bulletproof": "D",
                    "Mike Posner": "D",
                    "Black Eyed Peas/Rock That Body": "D",
                    "Lady Gaga/Alejandro": "L"},
        "Bill": {"Dr Dog/Fate": "L", "Phoenix/Lisztomania": "L",
                "Heartless Bastards/Out at Sea": "L",
                "Todd Snider/Don't Tempt Me": "D",
                "The Black Keys/Magic Potion": "L",
                "Glee Cast/Jessie's Girl": "D",
                "La Roux/Bulletproof": "D", "Mike Posner": "D",
                "Black Eyed Peas/Rock That Body": "D",
                "Lady Gaga/Alejandro": "D"}
         }


def manhattan(vector1, vector2):
    """Computes the Manhattan distance."""
    distance = 0
    # total = 0
    n = len(vector1)
    # print('vector1 => ', vector1)
    # print('vector2 => ', vector2)

    # print('vector1[0] => ', vector1[0])
    # print('vector1[1] => ', vector1[1])
    
    for i in range(n):
        # print('vector1[i] => ', vector1[i])
        # print('vector2[i] => ', vector2[i])
        distance += abs(vector1[i] - vector2[i])
    return distance


def computeNearestNeighbor(itemName, itemVector, items):
    """creates a sorted list of items based on their distance to item"""
    # "Chris Cagle/ I Breathe In. I Breathe Out" [1, 5, 2.5, 1, 1, 5, 1]
    distances = []
    for otherItem in items:
        if otherItem != itemName:
            # print('itemVector =>', itemVector)
            # print('items[otherItem] =>', items[otherItem])
            distance = manhattan(itemVector, items[otherItem])
            distances.append((distance, otherItem))
    # sort based on distance -- closest first
    distances.sort()
    return distances


def classify(user, itemName, itemVector):
    """Classify the itemName based on user ratings
    Should really have items and users as parameters"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(itemName, itemVector, items)[0][1]
    rating = users[user][nearest]
    return rating


def main():
    # print(manhattan(items['Dr Dog/Fate'], items['Mike Posner']))

    # vector1 =  [1, 5, 2.5, 1, 1, 5, 1]
    # vector2 =  [2.5, 4, 3.5, 3, 5, 4, 1]

    # print(manhattan(vector1, vector2))


    item = {'name': "Chris Cagle/ I Breathe In. I Breathe Out",
            'vector': [1, 5, 2.5, 1, 1, 5, 1]}

    # print(item['name'], item['vector'])
    # print(items)

    # pp.pprint(computeNearestNeighbor(item['name'], item['vector'], items))

    # [(4.5, 'Lady Gaga/Alejandro'),
    #  (6.0, "Glee Cast/Jessie's Girl"),
    #  (7.5, "Todd Snider/Don't Tempt Me"),
    #  (8.0, 'Mike Posner'),
    #  (9.5, 'Heartless Bastards/Out at Sea'),
    #  (10.5, 'Black Eyed Peas/Rock That Body'),
    #  (10.5, 'Dr Dog/Fate'),
    #  (10.5, 'La Roux/Bulletproof'),
    #  (10.5, 'Phoenix/Lisztomania'),
    #  (14.0, 'The Black Keys/Magic Potion')]


    # pp.pprint(classify('Angelica', 'Cagle', [1, 5, 2.5, 1, 1, 5, 1]))
    pp.pprint(classify('Angelica', item['name'], item['vector']))

if __name__ == "__main__":
    main()
