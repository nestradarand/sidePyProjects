import numpy as np

file = open('tyler.txt','r')
file = file.read()
file = file.split(' ')

all_count = 6000



vocab = {}
vocab_counts = {}


index = 0
#####initiates the vocab dict
for i in range(0,len(file)):
    if file[i] not in vocab.keys():
        vocab[file[i]] = index
        vocab_counts[file[i]] = 1
        index +=1
    else:
        vocab_counts[file[i]] += 1
for key in vocab.keys():
    vocab[key] = {}
    for small_key in vocab.keys():
        vocab[key][small_key] = 0
        
for i in range(1,len(file)):
    prev = file[i-1]
    curr = file[i]
    vocab[prev][curr] += 1        
current = "for"
song = current
for i in range(0,300):
    max_prob = 0
    word_to_add = ''
    probs = getProbs(vocab[current])
    listofwords = list(vocab[current].keys())
    word_to_add = np.random.choice(listofwords,size = 1,p = probs)
    current = str(word_to_add[0])
    song = song + " " + current
print(song)


def getProbs(probDict):
    probs = []
    the_sum = 0
    for word in probDict.keys():
        the_sum += probDict[word]
    for word in probDict.keys():
        probs.append(probDict[word]/the_sum)
    return probs
        
        
            
        
    
