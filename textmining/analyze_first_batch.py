__author__ = 'matjaz'

'''
    CALCULATE FREQUENCY OF DOMAIN SUFFIXES
'''

''' I split big aaaa.csv file by using bash split command:
    split -l 10000 -d aaaa.csv  newfile - splits in files with 10000 lines each or
    split -n10 -d aaaa.csv newfile - splits into 10 files of equal sizes
'''

from collections import Counter
from pprint import pprint
# import matplotlib

file_source = '/home/matjaz/Computer_stuff/CS/CS_Masters/MSProject/dnscensus_to_play_with/'\
              'records/aaaa_split_into_10000_line_files/aaaa_split_tenthousand_00'

def suffix_frequency(file_source):

    data=file_source
    with open(data, 'r') as file:

        li=[]
        for line in file:
            line =line.strip('\n').split(',')

            # get suffixes
            l = line[0].split('.')

            if len(l) > 1:
                li.append(l[1])

        freqs = Counter(li)
        return freqs

pprint(suffix_frequency(file_source))


