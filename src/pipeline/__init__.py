from normalizer import normalize
from tokenizer import tokenize
from stopwords import remove_stopwords
from stemmer import stem

class TextPipeline:
    def __init__(self):
        pass
    def process(self,text:str)->list[str]:
        text=normalize(text)
        tokens=tokenize(text)
        tokens=remove_stopwords(tokens)
        tokens=stem(tokens)
        return tokens


raw="The Reserve Bank of Australia (RBA) came into being on 14 January 1960!"
pipeline=TextPipeline()
print(pipeline.process(raw))

