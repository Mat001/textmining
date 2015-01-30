__author__ = 'matjaz'

from textmining.analyze_first_batch import suffix_frequency

# test if correct number of elements is produced in the frequency list
def test_suffix_frequency():
    data_path= '/home/matjaz/Computer_stuff/CS/CS_Masters/MSProject/dnscensus_to_play_with/' \
          'records/aaaa_split_into_10000_line_files/aaaa_split_tenthousand_00'

    assert len(suffix_frequency(data_path)) == 122

# test that function 'suffix_frequency(data_path)' produces correct number of elements on a different-test file (6)
def test_suffix_frequency_on_different_file():
    data_path= '/home/matjaz/PycharmProjects/textmining/textmining/test/'\
                'test_analyze_first_batch_testtext.csv'
    assert len(suffix_frequency(data_path)) == 6

