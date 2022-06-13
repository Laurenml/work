import os

for f in os.listdir() :
  for a in open("one.txt", "r"):
      words = a.split(" ")
      word_dict = dict.fromkeys(words, 0)
      for word in words:
          word_dict[word]+=1
print(word_dict)
    
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

tfdoc = computeTF(word_dict, words)


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log(N/float(val))
        
    return idfDict

idfs = computeIDF([word_dict])

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidf_doc = computeTFIDF(tfdoc, idfs)


import pandas as pd
pd.DataFrame([word_dict])