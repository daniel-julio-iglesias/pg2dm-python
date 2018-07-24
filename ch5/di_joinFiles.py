import os, codecs
import pprint as pp


def joinbuckets(currentdir, outfilename, bucketName):
    # filenames = ['file1.txt', 'file2.txt', ...]
    # pimaSmall-01, ... , pimaSmall-10
    # '..\\data\\ch5\\pimaSmall\\pimaSmall\\'
    # 'pimaSmall.txt'

    # f = open("%s-%02i" % (bucketName, bNum + 1), 'w')
    # f = codecs.open(currentdir + '/' + file, 'r', 'iso8859-1')
    # f = open("%s-%02i" % (bucketName, bNum + 1), 'w')

    # with open('path/to/file', 'w') as outfile:
    #     for fname in filenames:
    #         with open(fname) as infile:
    #             for line in infile:
    #                 outfile.write(line)


    with open(currentdir + '/' + outfilename, 'w') as outfile:
        filenames = os.listdir(currentdir)
        # pp.pprint(filenames)
        #filter out files that are not files
        filenames = [filename for filename in filenames
                           if os.path.isfile(currentdir + '/' + filename)
                     and filename.find(bucketName) != -1
                     and filename.find(bucketName + '.txt') == -1 ]


        # pp.pprint(filenames)
        # print(bucketName)

        # filenames = [filename for filename in filenames
        #                   if filename.find(bucketName) != -1 and filename.find(bucketName + '.txt') == -1 ]

        pp.pprint(filenames)
        
       
        for fname in filenames:
            with codecs.open(currentdir + '/' + fname, 'r', 'iso8859-1') as infile:
                for line in infile:
                    outfile.write(line)


def main():
    # workdir = '../data/ch5/pimaSmall/pimaSmall'
    # outputfilename = 'pimaSmall.txt'
    # bucketName = 'pimaSmall'


    workdir = '../data/ch5/mpgData/mpgData'
    outputfilename = 'mpgData.txt'
    bucketName = 'mpgData'

    joinbuckets(workdir, outputfilename, bucketName)

if __name__ == '__main__':
    main()

