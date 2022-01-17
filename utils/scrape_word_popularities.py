# %%
from http.client import TOO_MANY_REQUESTS
import requests
import json
import pandas as pd
from time import sleep

from wordle_vocab import dictionary as vocab

####################################################################################
#
# USER SETTINGS
######################################################################################

#Script is a bit fragile so may fall over. Will want to rerun without losing progress
#So set this to true only if you intend to start from scratch
RESTART_DICT=False


#I would recomment your base sleep time be 0.1 second.
#This script is poorly written so it does take 2/3 runs to actually get all words
#when you have very few words left, set sleep to ~1 second or so to avoid rejected requests
WORD_TIME_GAP=0.1

#Occasionally, Google says too many requests, try again later (status 429)
#we just wait a bit longer before continuing, only do this so many times for a word
TOO_MANY_REQUESTS_PAUSE=5
MAX_ATTEMPTS_PER_WORD=5

####################################################################################
# SCRIPT - ONLY MAKE CHANGES BELOW IF YOU KNOW WHAT YOU'RE DOING
####################################################################################

if RESTART_DICT:
    df=pd.DataFrame(columns=["word","case"]+list(range(1970,2020)))
else:
    df=pd.read_csv("word_popularity_data.csv.zip",compression="zip")

def make_query_url(word):
    """Quickly turn a word into the appropriate Google Books url

    Args:
        word (str): Any word

    Returns:
        str: Google Books url for the word's popularity from 1970 to 2019
    """
    return f"https://books.google.com/ngrams/json?content={word}&year_start=1970&year_end=2019&corpus=26&smoothing=0&case_insensitive=true#"

def make_ngram_lists(word):
    """Queries Google Books for a word, using the case insensitive settings. Retrieves the popularity
    of the word from 1970 to 2019 for the case insensitive and lower case versions of the word.

    Args:
        word (str): a word to query

    Returns:
        list: list of up to two lists containing ngram results for case insensitive
        and lower case version of the word.
    """
    response=requests.get(make_query_url(word))
    
    #too many requests results in status 429. Pause and ask again in a bit
    attempts=0
    while (response.status_code==429) and (attempts<MAX_ATTEMPTS_PER_WORD):
        sleep(TOO_MANY_REQUESTS_PAUSE)
        response=requests.get(make_query_url(word))
    if response.status_code==200:
        response=json.loads(response.content)
        
        if len(response)>1:   
            #then take the case insensitive and lower case results and add to dataframe
            for i in [0,1]:
                ngram=response[i]
                df.loc[len(df)]=[ngram["ngram"].split()[0]]+["Insensitive" if i==0 else "lower"]+ngram["timeseries"]
        elif len(response)==1:
            i=0
            ngram=response[i]
            df.loc[len(df)]=[ngram["ngram"].split()[0]]+["Insensitive" if i==0 else "lower"]+ngram["timeseries"]
        else:
            df.loc[len(df)]=[word]+["Insensitive"]+([0]*50)
    else:
        print(f"{word} failed with status code {response.status_code}")
    return 0

print(len(vocab))
vocab=[word for word in vocab if word not in df["word"].values]
print(len(vocab))

for i,word in enumerate(vocab):
    make_ngram_lists(word)
    if i%100==0:
        #save progress and compress.
        df.to_csv("word_popularity_data.csv.zip",index=False,compression="zip")
    sleep(WORD_TIME_GAP)
#final save
df.to_csv("word_popularity_data.csv.zip",index=False,compression="zip")




