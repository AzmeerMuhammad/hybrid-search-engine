from nltk.stem import PorterStemmer
ps=PorterStemmer()
def stem(tokens:list[str])->list[str]:
    arr=[]
    for token in tokens:
        arr.append(ps.stem(token))
    return arr

# tokens=['reserve', 'bank', 'australia', 'rba', 'came', 'january', 'running', 'banks', 'studies']
# print(stem(tokens))
