import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

def get_count(sequence) :
    count={}
    for x in sequence :
        if 'tz' in x : count[x['tz']]=count.get(x['tz'],0)+1
    sorted(count)
    return count

def count_from_top (input, n=10) :
    dict=[(count, tz) for tz, count in input.items()]
    dict.sort()
    return dict[-n:]


path='usagov_bitly_data2012-03-16-1331923249.txt'

records=[json.loads(line) for line in open(path)]
dict_count=get_count(records)

count_from_top(dict_count)


#the above may be done in the below
from collections import Counter
count=Counter([rec['tz'] for rec in records if 'tz' in rec])
count.most_common(10)