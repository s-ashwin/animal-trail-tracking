def formatLabels(labels):
  for index,label in enumerate(labels):
     labels[index]=label[2:-1]
  return labels

def readLabels():
  with open("./labels.txt") as f:
    contents = f.readlines()
    return contents

def getLabels():
    labels = readLabels()
    formattedLabels = formatLabels(labels)
    return formattedLabels

def getPredictionResult(array):
    labels=getLabels()
    index= array.index(max(array))
    return labels[index]
