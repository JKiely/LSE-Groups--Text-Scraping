'''
Program that can scrape though a series of text documents for keywords drawn from
an aditional document, returning the normalised tallys of each keyword in a csv file
that can be used to make graphs.

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
'''
import csv
import numpy as np

def normal(value, factor):
    c = 100000
    n =0
    '''
    Takes in a value, the factor you wish to normalise it by, and a constant by which to multiply it.
    For example the term count (value) and the total lengh of the text document (value) with a constant
    of 100,000 returns a value of 1 for each time in 100,000 the word is used.
    '''
    if n == 1:
        return round(((float(value)/factor)*c), 2)
    elif n == 0: #Set the value of n as 0 to return unnormalised variables.
        return value
    else:
        return ValueError


def textChecker(words, news):
    '''
    textChecker takes a list of keywords (words) and a collection of news articles in a single .txt file (news)
    and returns a list of normalised values corrisponding to the number of times the word appeared.
    '''
    results = []
    for t in words:
        termcount = 0
        if type(t) == list: #Lists within lists are collections of words that we feel should be treated as the same word
            results.append(normal(sum(textChecker(t, news)), len(news)))
        else:
            for i, line in enumerate(news):
                if t in line.lower(): #All words treated as lowercase
                    termcount += 1
            if termcount == 0:
                results.append(0)
            else:
                results.append(normal(termcount, len(news)))
    return results 

def newsItor(words, d1, d2):
    '''
    Takes in a list of words you wish to serch and the range of years you wish to search (ending on the final one),
    it returns one list of values per year, sorted into a metalist.
    '''
    metaResults = []
    for n in range(d1,d2+1): #Adds one to the stop value so that we may imput the final year we want results from
        newsFile = open(('C:\Users\JKiely\Google Drive\Groups Project\News texts\\news_' + str(n) + '.TXT'), 'r') #Iterates though appropreatly named files
        newsFile = newsFile.readlines()
        metaResults.append(textChecker(words, newsFile)) #Adds each results list to the meta list
    return metaResults
                    
def listMaker(listname):
    '''
    Takes the name of a txt document in the project folder with keywords, each on a new line, and returns a list of said keywords.
    Groups of words that are to be treated as one word should be put on the same line seperated by commas, comments may be added to the document
    using the # key.
    '''
    listDoc = open(('C:\Users\JKiely\Google Drive\Groups Project\\'+ listname +'.TXT'), 'r') #Current location of lists
    listDoc = listDoc.readlines()
    newList = []
    for i, line in enumerate(listDoc):
        if line == '\n': #Ignores blank lines
            None
        elif line[0] == '#': #Ignores comments
            None
        elif len(line.split(',')) > 1: #Creates sublist out of comma seperated variables
            templist = []
            for j in line.split(','):
                templist.append(j.lower().rstrip()) #Converted to lowercase
            newList.append(templist)
        else:
            newList.append(line.lower().rstrip())
    return newList

def writer(results, destination):
    '''
    Takes a list of results and writes them to a text file (destination) in the results folder, also returns the results to the terminal
    '''
    resultsDoc = open(('C:\Users\JKiely\Google Drive\Groups Project\Results\\'+ destination +'.TXT'), 'w') #Can edit an existing document or create a new one
    writer = csv.writer(resultsDoc)
    for item in results:
        writer.writerow(item)
    resultsDoc.close()
    return results

def scraper(n, words, start, end):
    '''
    Brings together all of the prevous functions.
    Takes the word list and the start and end dates and the textchecker you wish to use, 
    returns the results list from checker and creats a results document using writer.
    '''
    if n == 0:
        return writer(newsItor((listMaker(words)), start, end), ('Results for '+ words + ' ' + str(start) + '-' + str(end)))
    elif n == 1:
        return writer(np.transpose(newsItor((listMaker(words)), start, end)), ('Results for '+ words + ' ' + str(start) + '-' + str(end)))
    else:
        return ValueError


print scraper(0, 'test', 1993, 2013)
