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
    "Robert": {"Blues Traveler": 4, "Norah Jones": 3, "Phoenix": 5, "The Strokes": 2, "Weird Al": 1},
    "Amanda" : {"Grey Wardens": 4.5, "Pearson": 0.5},
    "Eric" : {"Grey Wardens": 5, "Pearson": 0.7},
    "Sally" : {"Grey Wardens": 3.5, "Pearson": 0.8}
}


def select_occurrences(u, name="Grey Wardens", num=2):
    p = []

    for user in u:
        # print("user ==> ", user)
        # print("u[user] ==> ", u[user])
        d = u[user]
        # print("list(d.keys()) ==> ", list(d.keys()))

        if 'Pearson' in d.keys():
            # print("user: list(d.keys()) ==> ", user, ' : ', list(d.keys()))
            # print("d['Pearson'] ==> ", d['Pearson'])
            # print("user ==> ", user)
            t = (user, d['Pearson'], d[name])
            p.append(t)

    p.sort(key=lambda person_tuple: person_tuple[1], reverse=True)
    # print("p ==> ", p)

    r = []
    for n in range(num):
        r.append(p[n])
    # print("r ==> ", r)

    return r


def k_nearest():
    # k = 3
    k = 2
    title = "Grey Wardens"
    persons = select_occurrences(users, title, k)
    # print("persons ==> ", persons)

    sum_pearson = 0
    for person in persons:
        sum_pearson += person[1]
    # print("sum_pearson ==> ", sum_pearson)

    new_persons = []
    for person in persons:
        influence = person[1] / sum_pearson
        new_persons.append(person + (influence,))
    # print("persons ==> ", persons)
    # print("new_persons ==> ", new_persons)

    projected_rating = 0
    for person in new_persons:
        projected_rating += person[2]*person[3]
    print("projected_rating ==> ", projected_rating)


def main():
    k_nearest()


if __name__ == '__main__':
    main()
