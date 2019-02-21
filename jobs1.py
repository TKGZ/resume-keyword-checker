from flask import Flask
import pandas as pd
import time
app = Flask(__name__)

bad_chars = ['.' ,'Than','This', 'Make', 'Have ', 'By ', 'As ', '(', ')', 'On ', ',', '-',
 'Is ', 'Or ', ':', '\t', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Of', '|',
 '–', 'We ', 'For ', 'About ', 'With ', 'That ', 'In ', 'Can ', 'And ', 'At ', 'All ',
 'Years', 'Life', 'Like', 'Do ', 'Are ', 'Any ', 'The ', 'To ', 'If ', 'Enough', 'Yet', 'Will ',
  'Them ', 'New ', 'Our ', 'More ', 'Many', 'Well', 'Not', 'But', 'Each', 'Age', 'Its', 'Per ', 'Inc', 'Via',
   'It ', 'Non ', 'End ', 'Bs ', 'Together', 'An ', '*', 'Into', 'Raise', 'Know', 'How', 'Using', 'Your', 'Both',
   'From', 'Help', 'Those', 'What', 'Way', 'User', 'Clearly', 'Their', 'Needs', "You’Ll", 'Role', 'Be ', 'Up ', 'Rely',
 'Us', 'Amazing', 'Self', 'Recommended', 'People',  'A ', '’S', '?', 'You’Re', 'You', 'We’Ve']
#bad_chars does not capture all the adjectives.



@app.route("/")
#takes a string and returns a cleaned pandas df with one column
def word_list(string):
    #take a string and split it from spaces to a list
    for each in bad_chars:
        if each in string:
            string = string.replace(each, ' ')
            string = string.title()
    new_list = string.split(" ")

    for each in new_list:
        if len(each) < 2:
            new_list.remove(each)

    series = pd.DataFrame(data=new_list, columns=['frequency'])
    return series

#return pandas series (frequency table)
def series_to_freq(series):
    df = series['frequency'].value_counts(ascending=False)
    return df

#takes two series as input and returns dataframe with word check
#this algorithm contributes to doubling of the running time
def in_resume(job_ser, resume):
#    start = time.time()
    df = job_ser.to_frame()
    for each in resume["frequency"]:
        if each in df.index:
            df.loc[each, "in_resume"] = 'OK'
#    end = time.time()
#    print(end-start)
    df.index.name = 'word'
    df = df.sort_values(by=['frequency','word'], ascending=[False, True])
    return df



def counts(df):
    count_existing = df["in_resume"].notna().sum()
    count_missing = df["in_resume"].isna().sum()
    freq_existing = df["frequency"][df["in_resume"] == 'OK'].sum()
    freq_total = df["frequency"].sum()


    print('\nWords in description' )
    words = df.shape
    print(words[0])

    print('\nWord coverage')
    resume_coverage = int(round((count_existing/(words[0]))*100, 0))
    print(str(resume_coverage) + ' %')

    print('\nFrequency coverage')
    freq_coverage = int(round((freq_existing/(freq_total))*100, 0))
    print(str(freq_coverage) + ' %')

#job description
string_job = """



    """

#resume
string_resume = """ 



    """

cleaned_job = word_list(string_job)
resume = word_list(string_resume)

job_freq = series_to_freq(cleaned_job)
comb = in_resume(job_freq, resume)
counts(comb)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(comb)
