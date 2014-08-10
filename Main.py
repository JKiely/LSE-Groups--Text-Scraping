import csv
import string

NewsFolder = '/home/john/Documents/Grive/Groups Project/News texts'
ListFolder = '/home/john/Documents/Grive/Groups Project/Lists'
ResultsFolder = '/home/john/Documents/Grive/Groups Project/Results'


def normal(value, factor, Ignore = False, c = 100000):
    '''
    Takes in a value, the factor you wish to normalise it by, and a constant by which to multiply it.
    For example the term count (value) and the total length of the text document (value) with a constant
    of 100,000 returns a value of 1 for each time in 100,000 the word is used.
    '''
    if Ignore == False:
        return round(((float(value)/factor)*c), 2)
    else: 
        return value

def textChecker(words, news):
    '''
    textChecker takes a list of keywords (words) and a collection of news articles in a single .txt file (news)
    and returns a list of normalised values corresponding to the number of times the word appeared.
    '''
    results = []
    for term in words:
        termcount = 0
        if type(term) == list: #Lists within lists are collections of words that we feel should be treated as the same word
            results.append(normal(sum(textChecker(term, news)), len(news)))
        else:
            for word in news:
                if term == word:
                    termcount += 1
            if termcount == 0:
                results.append(0)
            else:
                results.append(normal(termcount, len(news)))
    return results 

def newsItor(words, d1, d2):
    '''
    Takes in a list of words you wish to search and the range of years you wish to search (ending on the final one),
    it returns one list of values per year, sorted into a metalist.
    '''
    metaResults = []
    for n in range(d1,d2+1):
        newsFile = open((str(NewsFolder) + '/news_' + str(n) + '.TXT'), 'r').read() #Iterates though appropreatly named files
        newsFile = [word.strip(string.punctuation) for word in newsFile.lower().split()]
        metaResults.append(textChecker(words, newsFile))
    return metaResults
                    
def listMaker(listname):
    '''
    Takes the name of a txt document in the project folder with keywords, each on a new line, and returns a list of said keywords.
    Groups of words that are to be treated as one word should be put on the same line separated by commas, comments may be added to the document
    using the # key.
    '''
    listDoc = open((str(ListFolder) + '/'+ listname +'.txt'), 'r') 
    listDoc = listDoc.readlines()
    newList = []
    for i, line in enumerate(listDoc):
        if line == '\n':
            None
        elif line[0] == '#':
            None
        elif len(line.split(',')) > 1: #Creates sublist out of comma seperated keywords
            templist = [j.lower().rstrip() for j in line.split(',')]
            newList.append(templist)
        else:
            newList.append(line.lower().rstrip())
    return newList

def writer(results, destination):
    '''
    Takes a list of results and writes them to a text file (destination) in the results folder, also returns the results to the terminal
    '''
    resultsDoc = open((str(ResultsFolder) + '/'+ destination +'.txt'), 'w')
    writer = csv.writer(resultsDoc)
    for item in results:
        writer.writerow(item)
    resultsDoc.close()
    return results

def scraper(words, start, end, Transpose=False):
    '''
    Brings together all of the previous functions.
    Takes the word list and the start and end dates and the textchecker you wish to use, 
    returns the results list from checker and creates a results document using writer.
    '''
    if Transpose == False:
        return writer(newsItor((listMaker(words)), start, end), ('Results for '+ words + ' ' + str(start) + '-' + str(end)))
    else:
        from numpy import transpose
        return writer(transpose(newsItor((listMaker(words)), start, end)), ('Results for '+ words + ' ' + str(start) + '-' + str(end)))

