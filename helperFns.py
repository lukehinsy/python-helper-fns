import numpy as np
import pandas as pd
from collections import Counter
from IPython.display import Audio, display
from numpy import linalg

def dfSummary(df):
    print('Note: This command is NOT very performant, and can take quite long on large dataframes!')
    output = []
    for col in df.columns:
        nonNull = len(df) - np.sum(pd.isna(df[col]))
        unique = df[col].nunique()
        colType = str(df[col].dtype)
        output.append([col, nonNull, unique, colType])
    output = pd.DataFrame(output)
    output.columns = ['colName', 'non-null values', 'unique values', 'dtype']
    with pd.option_context('display.max_rows', None): display(output)
        
def propCounter(vec, num = 25, cumul = False):
    l = vec
    c = Counter(l)
    output = [(i, count, c[i] / len(l) * 100.0) for i, count in c.most_common(num)]
    output = pd.DataFrame(output, columns = ['Value', 'Count', 'Percent'])
    if cumul == True:
        output['CumulativePercent'] = output['Percent'].cumsum()
    return output.style.hide_index()

def allDone():
    display(Audio(url = 'https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', autoplay = True))