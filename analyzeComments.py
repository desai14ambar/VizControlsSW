from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords  
from string import punctuation

stopwords = set(stopwords.words('english') + list(punctuation))

def reduceComments(row, colData, wsData):

    getComments = wsData.cell(row, colData+1).value
    if not getComments == None:
        commentTokens = (word_tokenize(getComments))
        # stopwords = set(stopwords.words('english') + list(punctuation))
        content = [w for w in commentTokens if w not in stopwords]
        commentFlt = ' '.join([''.join(sub) for sub in content])
        wsData.cell(row, colData+2).value = commentFlt
        return content