import pandas as pd

#add to bad_chars words you don't want to be displayed
bad_chars = ['.' ,'Than','This', 'Make', 'Have ', 'By ', 'As ', '(', ')', 'On ', ',', '-',
 'Is ', 'Or ', ':', '\t', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Of', '|',
 '–', 'You ', 'We ', 'For ', 'About ', 'With ', 'That ', 'In ', 'Can ', 'And ', 'At ', 'All ',
 'Years', 'Life', 'Like', 'Do ', 'Are ', 'Any ', 'The ', 'To ', 'If ', 'Enough', 'Yet', 'Will ',
  'Them ', 'New ', 'Our ', 'More ', 'Many', 'Well', 'Not', 'But', 'Each', 'Age', 'Its', 'Per ', 'Inc', 'Via',
   'It ', 'Non ', 'End ', 'Bs ', 'Together', 'An ', '*', 'Into', 'Raise', 'Know', 'How', 'Using', 'Your', 'Both',
   'From', 'Help', 'Those', 'What', 'Way', 'User', 'Clearly', 'Their', 'Needs', "You’Ll", 'Role', 'Be ', 'Up ', 'Rely',
 'Us', 'Amazing', 'Self', 'Recommended']


#copypaste job description here
string_job = """



    """

#copypaste resume here
string_resume = """




    """



#takes a string and returns a frequency table of common words.
def word_list(string):
    #take a string and split it from spaces to a list
    for each in bad_chars:
        if each in string:
            string = string.replace(each, ' ')
            string = string.title()
    new_string = string.split(" ")

    #remove empty list items
    while '' in new_string:
        new_string.remove('')

    #create frequency table from cleaned list if item is longer than 1 character
    freq_table = {}
    for each in new_string:
        if len(each) >= 2:
            if each in freq_table:
                freq_table[each] += 1
            else:
                freq_table[each] = 1

    return freq_table

#checks if a word in job description is in resume and appends "OK" if the word is in resume
#prints word count, word coverage and frequency coverage
#returns a combined frequency table
def word_in_resume(freq_table_job, freq_table_resume):
    count_existing = 0
    count_missing = 0
    freq_existing = 0
    freq_missing = 0
    combined_dict = {}
    for each in freq_table_job:
        if each in freq_table_resume:
            combined_dict[each] = [freq_table_job[each], 'OK']
            count_existing += 1
            freq_existing += freq_table_job[each]
        else:
            combined_dict[each] = [freq_table_job[each], '']
            count_missing += 1
            freq_missing += freq_table_job[each]

    print('\nWords in description' )
    word_total = count_missing + count_existing
    print(word_total)

    print('\nWord coverage')
    resume_coverage = int(round((count_existing/(word_total))*100, 0))
    print(str(resume_coverage) + ' %')

    print('\nFrequency coverage')
    freq_coverage = int(round((freq_existing/(freq_missing+freq_existing))*100, 0))
    print(str(freq_coverage) + ' %')

    return combined_dict

#returns a Pandas DataFrame object sorted by frequency
def freq_table_sort(freq_table):
    data_frame = pd.DataFrame.from_dict(freq_table, orient='index', columns=['frequency', 'in_resume?'])
    data_frame = data_frame.sort_values(by=['frequency'], ascending=[False])
    return data_frame




freq_job = word_list(string_job)
freq_resume = word_list(string_resume)
combined_dict = word_in_resume(freq_job, freq_resume)
sorted_freq = freq_table_sort(combined_dict)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(sorted_freq)
