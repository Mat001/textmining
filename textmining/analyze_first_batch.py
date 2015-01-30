__author__ = 'matjaz'

'''
    PREPROCESS AND EXTRACT DIFFERENT PARTS OF DOMAIN NAMES
    - name without suffix
    - suffix
    - frequency of name
    - frequency of suffix
    - how many names are alphanumerical
    - how many names are only numerical
    - how many names are only alphabetical

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

def get_all_suffixes(file_source):
    pass


def get_all_names(file_source):
    data = file_source
    with open(data, 'r') as file:

        # chop the list containing one long string of triples names-isotime-ipv6-s into a list of lists
        list_of_lines = [line.strip('\n').split(',') for line in file]

        # split lists of triples into names + suffix
        li = []
        for line in list_of_lines:
            # get suffixes
            l = line[0].split('.')

            # take name, ignore suffix
            if len(l) > 1:      # ignore column header 'name'
                li.append(l[0])

        # list all names
        return li



def get_names_frequency():
    freqs_names = Counter(get_all_names(file_source))
    return freqs_names



def get_name_roots(file_source):
    pass


def suffix_frequency(file_source):

    data=file_source
    with open(data, 'r') as file:

        # chop the list containing one long string of triples names-isotime-ipv6-s into a list of lists
        list_of_lines = [ line.strip('\n').split(',') for line in file ]

        # split lists of triples into names + suffix
        li = []
        for line in list_of_lines:
            # get suffixes
            l = line[0].split('.')

        # take suffix and ignore name
            if len(l) > 1:
                li.append(l[1])

        # calculate frequency of each suffix
        freqs = Counter(li)
        return freqs


# EXPERIMENTAL:
def get_all_names_in_all_files_alphanumerical():
    import os

    file_s = '/home/matjaz/Computer_stuff/CS/CS_Masters/MSProject/dnscensus_to_play_with/' \
                  'records/aaaa_split_into_10000_line_files/'
    listing = os.listdir(file_s)    # loop through all files in directory
    l = sorted([ i for i in listing ])
    #pprint(l)

    paths = [file_s + l[i] for i in range(89)]  # append file name to the path - list of paths
    #pprint(paths)

    result = ( get_all_names(y) for y in paths )    # generator expression - get iterator for all files
    for i in range(89):
        for x in next(result):
            if x.isalnum():       # if not x.isdigit() and not x.isalpha() and '-' not in x
                pprint(x)          # isalnum() method IS NOT WORKING!!!! Gives True for 'a'.isalnum() ans '1'.isalnum()!




get_all_names_in_all_files_alphanumerical()

#pprint(get_all_names(file_source))
#pprint(get_names_frequency())
#pprint(suffix_frequency(file_source))


