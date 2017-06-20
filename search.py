# tf.idf Sequential Search in Python

import string, math, sys, os, time, glob, errno

startTime = time.process_time()
assert sys.version_info >= (3,0)

# TF IDF ALGORITHM:
# TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)
# IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
# Score = TF * IDF

# Return number of times term t appears in a document

termFrequencies = []
IDF = 0

def calculateTF(t):
  # TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)

  timesInDoc = 0
  counter = 0
  for doc in tokens:
    timesInDoc = 0
    for word in tokens[counter]:
      if word == t:
        timesInDoc += 1  

    #termFrequencies.append(timesInDoc)

    totalTerms = len(set(doc))
    termFrequencies.append(timesInDoc / totalTerms)
    counter += 1


  print("TF is ", timesInDoc, "\nTotal terms is ", totalTerms)
  print(termFrequencies)
  #return tf/totalTerms

def calculateIDF():
  # IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
  numDocs = len(allDocuments)
  numDocsWithT = 0
  for i in termFrequencies:
    if i > 0:
      numDocsWithT += 1
  if numDocsWithT != 0:
    return math.log(numDocs / numDocsWithT)
  else:
    return 0
 


def calculateScore():
  IDFScores = []
  print("IDF in ccalc is : ", IDF)
  for tf in termFrequencies:
    #print(tf)
    score = round(tf * IDF, 6)
    IDFScores.append(score)
  print(IDFScores)

# Returns the tokens of a document.

def createTokens(doc):
  return doc.lower().split(" ")

# Move this section of pre declarations to the top



#with open("./bigTextTest.txt", 'r') as file:
#    data = file.read().replace('\n', '')
#print(data)


#tokenisedData = [createTokens(data)]


#print(tokenisedData)

# Read documents from files

path = './corpus/*.txt'
files = glob.glob(path)
allDocuments = []
for name in files:
  with open(name) as f:
    allDocuments.append(f.read().replace('\n', ''))

tokens = [createTokens(d) for d in allDocuments]


print("Hey! What do you want to search?")
query = input().lower()

queryTokens = query.lower().split(" ")
#print(queryTokens)

print("---------------------------------------------")

calculateTF(query)
IDF = calculateIDF()
calculateScore()

#print(TF(query, tokens))

# for i in tokens:
#   for j in i:
#     print(j)

endTime = time.process_time()

print("Execution time: ", round((endTime-startTime), 4), "seconds")




