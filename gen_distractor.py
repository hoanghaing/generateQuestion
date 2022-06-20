import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
glove_file = './data/embeddings/glove.6B.300d.txt'
tmp_file = './data/embeddings/word2vec-glove.6B.300d.txt'
import os
    
if not os.path.isfile(glove_file):
    print("Glove embeddings not found. Please download and place them in the following path: " + glove_file)
# from gensim.scripts.glove2word2vec import glove2word2vec
# glove2word2vec(glove_file, tmp_file)
model = KeyedVectors.load_word2vec_format(tmp_file)
print(model)
def generate_distractors(answer, count):
    answer = str.lower(answer)
    
    ##Extracting closest words for the answer. 
    try:
        closestWords = model.most_similar(positive=[answer], topn=count)
    except:
        #In case the word is not in the vocabulary, or other problem not loading embeddings
        return []

    #Return count many distractors
    distractors = list(map(lambda x: x[0], closestWords))[0:count]
    
    return distractors

options = generate_distractors('messi', 4)
# options = generate_distractors('YouTube', 3)
# options = generate_distractors('Tailwind', 3)
# options = generate_distractors('1945', 3)
# options = generate_distractors('Final Fantasy Tactics: The War of the Lions', 3)
# options = generate_distractors('stephencurry', 3)
# options = generate_distractors('28th International Eucharistic Congress', 3)
print(options)
options.append('213')
print(options)