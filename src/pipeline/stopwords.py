import nltk
from nltk.corpus import stopwords
sw = set(stopwords.words("english"))
def remove_stopwords(tokens:list[str])->list[str]:
    arr=[]
    for token in tokens:
        if token not in sw:
            arr.append(token)
    return arr

# tokens = ['the', 'reserve', 'bank', 'of', 'australia', 'rba', 'came', 'into', 'being', 'on', 'january']
# print(remove_stopwords(tokens))

#using list comp
# return [token for token in tokens if token not in sw]

