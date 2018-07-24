import codecs
import pprint as pp


class Classifier:

    def __init__(self, path='', filename=''):
        self.medianAndDeviation = []
        # self.data = {}


        if  path == '' or filename == '':
            print('path and filename are needed')
            return
        
        f = codecs.open(path + filename, 'r', 'ascii')
        lines = f.readlines()
        f.close()
        # print(lines)
        self.format = lines[0].strip().split('\t')
        # print(self.format)
        self.data = []
        for line in lines[1:]:
            # print(line)
            # fields = line.split('\t')
            fields = line.strip().split('\t')
            #print(fields)
            ignore = []
            vector = []
            for i in range(len(fields)):
                if self.format[i] == 'num':
                    vector.append(int(fields[i]))
                elif self.format[i] == 'comment':
                    ignore.append(fields[i])
                elif self.format[i] == 'class':
                    classification = fields[i]
            self.data.append((classification, vector, ignore))
        # pp.pprint(self.data)
        self.rawData = list(self.data)
        # pp.pprint(self.rawData)
      
        # get length of instance vector
        self.vlen = len(self.data[0][1])
        # pp.pprint(self.data)
        # print(self.data[0][1])
        # print(range(self.vlen))
        # now normalize the data
        for i in range(self.vlen):
            self.normalizeColumn(i)

        # pp.pprint(self.data)
        # print(self.medianAndDeviation)

            
    
    ##################################################
    ###
    ###  FINISH THE FOLLOWING TWO METHODS

    def getMedian(self, alist):
        """return median of alist"""
        # """TO BE DONE"""
        # return 0
    
        # len([0,1,2,3])== 4
        # len([0,1,2,3,4]) == 5

        median = 0.0
        b = sorted(alist)
        if len(b) == 0:
            pass
        elif len(b) % 2 != 0:
            median = b[int(len(b) / 2)]
        else:
            median = (b[int(len(b) / 2) - 1 ] + b[int(len(b) / 2)]) / 2

        # print('median => ', median)

        return median
        
        

    def getAbsoluteStandardDeviation(self, alist, median):
        """given alist and median return absolute standard deviation"""
        # """TO BE DONE"""
        # return 0


        asd = 0.0
        for item in alist:
            asd += abs(item - median)
        asd /= len(alist)

        return asd




    def normalizeColumn(self, columnNumber):
        # print(columnNumber)
        alist = [data[1][columnNumber] for data in self.data]

        # print(alist)
        median = self.getMedian(alist)
        asd = self.getAbsoluteStandardDeviation(alist, median)
        # print("Median: %f ASD = %f" % (median, asd))
        self.medianAndDeviation.append((median, asd))

        for data in self.data:
            data[1][columnNumber] = (data[1][columnNumber] - median) / asd

        # print(self.medianAndDeviation)


    def normalizeVector(self, v):
        vector = list(v)
        for i in range(len(vector)):
            (median, asd) = self.medianAndDeviation[i]
            vector[i] = (vector[i] - median) / asd

        # print(vector)
        return vector



    def manhattanDistance(self, vector1, vector2):
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



    def nearestNeighbor(self, itemVector):
        """creates a sorted list of items based on their distance to item"""
        # "Chris Cagle/ I Breathe In. I Breathe Out" [1, 5, 2.5, 1, 1, 5, 1]

        # [('Gymnastics', [-1.93277, -1.21842], ['Asuka Teramoto']),
        # ('Basketball', [1.09243, 1.63447], ['Brittainey Raven']),
        # ('Basketball', [2.10084, 2.88261], ['Chen Nan']),
        # ('Gymnastics', [-2.77311, -0.50520], ['Gabby Douglas']),
        # ('Track', [-0.08403, -0.23774], ['Helalia Johannes']),
        # ('Track', [-0.42017, -0.02972], ['Irina Miketenko']),

        distances = []
        for data in self.data:
            distance = self.manhattanDistance(itemVector, data[1])
            distances.append((data[0], distance))
        # sort based on distance -- closest first
        distances.sort()
        distances.sort(key=lambda sportTuple: sportTuple[1],
                     reverse = False)
        pp.pprint(distances)
        return distances
            

    def classify(self, itemVector):
        """Return class we think item Vector is in"""
        return(self.nearestNeighbor(self.normalizeVector(itemVector))[1][0])

    
    ###
    ### 
    ##################################################



def unitTest():
    list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54]
    list2 = [54, 72, 78, 49, 65, 63, 75, 67, 54, 68]
    list3 = [69]
    list4 = [69, 72]
    classifier = Classifier('..\\data\\ch4\\', 'athletesTrainingSet.txt')
    m1 = classifier.getMedian(list1)
    m2 = classifier.getMedian(list2)
    m3 = classifier.getMedian(list3)
    m4 = classifier.getMedian(list4)
    asd1 = classifier.getAbsoluteStandardDeviation(list1, m1)
    asd2 = classifier.getAbsoluteStandardDeviation(list2, m2)
    asd3 = classifier.getAbsoluteStandardDeviation(list3, m3)
    asd4 = classifier.getAbsoluteStandardDeviation(list4, m4)
    assert(round(m1, 3) == 65)
    assert(round(m2, 3) == 66)
    assert(round(m3, 3) == 69)
    assert(round(m4, 3) == 70.5)
    # assert(asd1 == 8)
    assert(round(asd1, 3) == 8)
    assert(round(asd2, 3) == 7.5)
    assert(round(asd3, 3) == 0)
    assert(round(asd4, 3) == 1.5)
    
    print("getMedian and getAbsoluteStandardDeviation work correctly")


def main():
    # c = Classifier("..\\data\\ch4\\", "athletesTrainingSet.txt")
    # c = Classifier()

    # classifier = Classifier('..\\data\\ch4\\', 'athletesTrainingSet.txt')
    # list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54]
    # m1 = classifier.getMedian(list1)


    c = Classifier('..\\data\\ch4\\', 'athletesTrainingSet.txt')
    # heights = [54, 72, 78, 49, 65, 63, 75, 67, 54]
    # median = c.getMedian(heights)
    # print(median)

    # asd = c.getAbsoluteStandardDeviation(heights, median)
    # print(asd)

    # v = [70, 140]
    v = [70, 170]
    # c.normalizeVector(v)
    print(c.classify(v))
    
    # unitTest()
    

if __name__ == '__main__':
    main()
