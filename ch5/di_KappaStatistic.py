# Kappa Statistic and interpret

# A commonly cited* scale on how to interpret Kappa
# < 0: less than chance performance
# 0.01-0.20 slightly good
# 0.21-0.40 fair performance
# 0.41-0.60 moderate performance
# 0.61-0.80 substantially good performance
# 0.81-1.00 near perfect performance
# * Landis, JR, Koch, GG. 1977. The measurement of observer
# agreement for categorical data. Biometrics 33:159-74




def calculateKappaStatistic(cmtx, Pc):
    Pr = 0.0 # accuracy_random_classifier
    k = 0.0  # kappa_statistic


    # calculate the percentages of instances

    total_predictions = {}
    total = 0
    pct_predictions = {}
    
    total_instances = {}    

    for major in cmtx:
        # print('major => ', major)
        # print('cmtx[major] => ', cmtx[major])
        for predicted_major in cmtx[major]:
            total_predictions.setdefault(predicted_major, 0)
            total_predictions[predicted_major] += cmtx[major][predicted_major]
            total += cmtx[major][predicted_major]
            
    # print('total_predictions => ', total_predictions)
    print('total => ', total)

    for predicted_major in total_predictions:
        pct_predictions.setdefault(predicted_major, 0.0)
        pct_predictions[predicted_major] += total_predictions[predicted_major]/total

    print('pct_predictions => ', pct_predictions)        

    tot_ok = 0.0
    for major in cmtx:
        total_instance = sum(cmtx[major].values())
        # print('total_instance => ', total_instance)
        tot_ok += pct_predictions[major] * total_instance
        # print('tot_ok => ', tot_ok)
        

    # calculate acurracy_random_classifier

    Pr = tot_ok / total
    print('Pr => ', Pr)


    if Pr != 1.0:
        k = (Pc - Pr) / (1.0 - Pr)
        
    return k


def getKappaInterpretation(k):


    kappa_matrix = {
                    (-1.0,0.0): 'less than chance performance',
                    (0.01,0.20): 'slightly good',
                    (0.21,0.40): 'fair performance',
                    (0.41,0.60): 'moderate performance',
                    (0.61,0.80): 'substantially good performance',
                    (0.81,1.00): 'near perfect performance'
                    }


    interpretation = ''

    # return interpretation
    
    for interval in kappa_matrix:
        # print(interval[0], interval[1])
        if k >= interval[0] and k <= interval[1]:
            interpretation = kappa_matrix[interval]
            # print('interpretation => ', interpretation)
            return interpretation

    return interpretation

def main():
    

    confusion_matrix = {
        'cs': {'cs': 50, 'ed': 8, 'eng': 15, 'psych': 7},
        'ed': {'cs': 0, 'ed': 75, 'eng': 12, 'psych': 33},
        'eng': {'cs': 5, 'ed': 12, 'eng': 123, 'psych': 30},
        'psych': {'cs': 5, 'ed': 25, 'eng': 30, 'psych': 170}
        }

    
    accuracy_real_classifier = 0.697

    kappa_statistic = calculateKappaStatistic(confusion_matrix, accuracy_real_classifier)

    
    print('kappa_statistic => ', kappa_statistic)
    # 0.5722352941176471
    interpretation = getKappaInterpretation(kappa_statistic)
    print('interpretation ==> ', interpretation)


if __name__ == '__main__':
    main()
