from math import sqrt


gals = {
    "Yun L": {"age": 35, "salary": 75000},
    "Allie C": {"age": 52, "salary": 55000},
    "Daniela C": {"age": 27, "salary": 45000},
    "Rita A": {"age": 37, "salary": 115000}
    }


guys = {
    "Brian A": {"age": 53, "salary": 70000},
    "Abdullah K": {"age": 25, "salary": 105000},
    "David A": {"age": 35, "salary": 69000},
    "Michael W": {"age": 48, "salary": 43000}
    }


tracks = {
    "Power/Marcus Miller": {"play count": 21},
    "I Breathe In, I Breathe Out/ Chris Cagle": {"play count": 15},
    "Blessed / Jill Scott": {"play count": 12},
    "Europa/Santana": {"play count": 3},
    "Santa Fe/ Beirut": {"play count": 7}
    }



class recommender:

    def __init__(self, data=0):
        """ initialize recommender
        currently, if data is dictionary the recommender is initialized
        to it.
        For all other data types of data, no initialization occurs
        """

        #
        # if data is dictionary set recommender data to it
        #
        # if type(data).__name__ == 'dict':
        self.data = data

        # Values to calculate z-scores / Standard Scores
        self.genes = []
        self.totals = {}
        self.cardinalities = {}
        self.means = {}
        self.medians = {}
        self.standardDeviations = {}
        self.absoluteStandardDeviations = {}
        self.zScores = {}
        

        # for Absolute Standard Deviations
        self.genes_lists = {}
        self.mss = {}
        

        # print('self.data => ', self.data)


    def calculateStandardDeviations(self):
        # print('self.data => ', self.data)
        
        # calculate means
        for user in self.data:
            for gene in self.data[user]:
                if gene not in self.genes:
                    self.genes.append(gene)
                self.totals.setdefault(gene, 0.0)
                self.totals[gene] += self.data[user][gene]
                self.cardinalities.setdefault(gene, 0)
                self.cardinalities[gene] += 1


        for gene in self.totals.keys():
            self.means.setdefault(gene, 0.0)
            self.means[gene] = self.totals[gene] / self.cardinalities[gene]
            
        
        # print('self.genes => ', self.genes)
        # print('self.totals => ', self.totals)
        # print('self.cardinalities => ', self.cardinalities)
        # print('self.means => ', self.means)

        
        for gene in self.genes:
            num = 0
            for user in self.data:
                # print('self.data[user][gene] => ', self.data[user][gene])
                num += (self.data[user][gene] - self.means[gene]) ** 2
            self.standardDeviations.setdefault(gene, 0.0)
            self.standardDeviations[gene] = sqrt(num / self.cardinalities[gene])
            
                
        # print('self.standardDeviations => ', self.standardDeviations)


        for user in self.data:
            self.zScores.setdefault(user, {})
            for gene in self.genes:
                each_value = self.data[user][gene]
                mean = self.means[gene]
                standard_deviation = self.standardDeviations[gene]
                if standard_deviation != 0:
                    self.zScores[user].setdefault(gene, (each_value - mean) / standard_deviation)
                else:
                    self.zScores[user].setdefault(gene, 0.0)

        # print('self.zScores => ', self.zScores)
                


    def calculateMedian(self, a = [0]):
        """
        len([0,1,2,3])== 4
        len([0,1,2,3,4]) == 5
        """
        median = 0.0
        b = sorted(a)
        if len(a) == 0:
            pass
        elif len(a) % 2 != 0:
            median = b[int(len(a) / 2)]
        else:
            median = (b[int(len(a) / 2) - 1 ] + b[int(len(a) / 2)]) / 2

        # print('Median => ', median)

        return median
    
        

    def calculateAbsoluteStandardDeviations(self):
        # print('self.data => ', self.data)
        
        # calculate medians
        for user in self.data:
            for gene in self.data[user]:
                if gene not in self.genes:
                    self.genes.append(gene)
                # self.totals.setdefault(gene, 0.0)
                # self.totals[gene] += self.data[user][gene]
                self.cardinalities.setdefault(gene, 0)
                self.cardinalities[gene] += 1
                self.genes_lists.setdefault(gene, [])
                self.genes_lists[gene].append(self.data[user][gene])


        for gene in self.genes:
            self.medians.setdefault(gene, 0.0)
            self.medians[gene] = self.calculateMedian(self.genes_lists[gene])
            
        
        # print('self.genes => ', self.genes)
        # print('self.cardinalities => ', self.cardinalities)
        print('self.medians => ', self.medians)

        
        for gene in self.genes:
            num = 0
            for user in self.data:
                # print('self.data[user][gene] => ', self.data[user][gene])
                num += abs(self.data[user][gene] - self.medians[gene])
            self.absoluteStandardDeviations.setdefault(gene, 0.0)
            self.absoluteStandardDeviations[gene] = num / self.cardinalities[gene]
            
                
        print('self.absoluteStandardDeviations => ', self.absoluteStandardDeviations)


        for user in self.data:
            self.mss.setdefault(user, {})
            for gene in self.genes:
                each_value = self.data[user][gene]
                median = self.medians[gene]
                absolute_standard_deviation = self.absoluteStandardDeviations[gene]
                if absolute_standard_deviation != 0:
                    self.mss[user].setdefault(gene, (each_value - median) / absolute_standard_deviation)
                else:
                    self.mss[user].setdefault(gene, 0.0)

        # print('self.mss => ', self.mss)
                





    def getZScore(self, user, gene):
        return self.zScores[user][gene]

    def get_mss(self, user, gene):
        return self.mss[user][gene]

        

def main():
    # https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
    	
    # How can I merge two Python dictionaries in a single expression?
    # For dictionaries x and y, z becomes a merged dictionary with values from y replacing those from  x.

    # In Python 3.5 or greater, :
    # z = {**x, **y}
    # In Python 2, (or 3.4 or lower) write a function:

    # def merge_two_dicts(x, y):
    #    z = x.copy()   # start with x's keys and values
    #     z.update(y)    # modifies z with y's keys and values & returns None
    #     return z
    # and
    # z = merge_two_dicts(x, y)


    # z = {**gals, **guys}

    # z = gals.copy()
    # z.update(guys)


    # r = recommender(z)
    
    # print(z)
    # r.calculateStandardDeviations()

    # r.calculateAbsoluteStandardDeviations()

    # print("r.getZScore('Yun L', 'salary') => ", r.getZScore('Yun L', 'salary'))
    # print("r.getZScore('Allie C', 'salary') => ", r.getZScore('Allie C', 'salary'))
    # print("r.getZScore('Daniela C', 'salary') => ", r.getZScore('Daniela C', 'salary'))
    # print("r.getZScore('Rita A', 'salary') => ", r.getZScore('Rita A', 'salary'))


    # r.calculateMedian([0,1,2,3]) ==> 1.5
    # r.calculateMedian([0,1,2,3,4]) ==> 2
    # r.calculateMedian([2,4,0,3,1]) ==> 2
    # r.calculateMedian() ==> 0


    # print("r.get_mss('Yun L', 'salary') => ", r.get_mss('Yun L', 'salary'))


    z = tracks.copy()
    r = recommender(z)
    r.calculateAbsoluteStandardDeviations()
    print("r.get_mss('Power/Marcus Miller', 'play count') => ", r.get_mss('Power/Marcus Miller', 'play count'))

    for track in z:
        for gene in z[track]:
            print("track, gene, r.get_mss(track, gene) => ", track, gene, r.get_mss(track, gene))


if __name__ == '__main__':
    main()


