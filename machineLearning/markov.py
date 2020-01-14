import numpy as np

def getProbs(probDict):
    probs = []
    the_sum = 0
    for word in probDict.keys():
        the_sum += probDict[word]
    for word in probDict.keys():
        probs.append(probDict[word]/the_sum)
    return probs

def main():
    file_name = str(input('Type in the name of the file you want to train on: '))
    try:
        #open and clean data
        file = open(file_name, 'r')
        file = file.read()
        file = file.split(' ')
        for i in range(0, len(file)):
            file[i] = file[i].strip(',')
            file[i] = file[i].strip('?')
            file[i] = file[i].strip(')')
            file[i] = file[i].strip('(')
            file[i] = file[i].strip('.')
            file[i] = file[i].strip('!')
            file[i] = file[i].strip(']')
            file[i] = file[i].strip('[')
        ###get two dicts ready for counts and individual vocab words
        vocab = {}
        vocab_counts = {}
        index = 0
        #####initiates the vocab dict to unique valued words
        for i in range(0, len(file)):
            if file[i] not in vocab.keys():
                vocab[file[i]] = index
                vocab_counts[file[i]] = 1
                index += 1
            else:
                vocab_counts[file[i]] += 1
        ## for all words create two new dicts for rows and columns
        for key in vocab.keys():
            vocab[key] = {}
            for small_key in vocab.keys():
                vocab[key][small_key] = 0
        #####get the number of instances for each bigram for each word
        for i in range(1, len(file)):
            prev = file[i-1]
            curr = file[i]
            vocab[prev][curr] += 1
        current = str(input('Type in the word you want to start the song with: '))
        song_length = int(input('Enter the number of words for the song: '))
        song = current
        for i in range(0, song_length):
            probs = getProbs(vocab[current])
            listofwords = list(vocab[current].keys())
            word_to_add = np.random.choice(listofwords, size=1, p=probs)
            current = str(word_to_add[0])
            song = song + " " + current
        print(song)
    except Exception as e:
        print('An Error has unfortunately occured:')
        print(e)
if __name__ == '__main__':
    main()


        
        
            
        
    
