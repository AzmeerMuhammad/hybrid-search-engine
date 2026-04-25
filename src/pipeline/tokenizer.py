from normalizer import normalize

def tokenize(text: str) -> list[str]:
    arr=[]
    for token in text.split():
        if len(token)>=2:
            arr.append(token)
    return arr


# raw = "The Reserve Bank of Australia (RBA) came into being on 14 January 1960"
# normalized=normalize(raw)
# tokens=tokenize(normalized)
# print(normalized)
# print(tokens)