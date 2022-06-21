# python ./gen_mce.py ./context/sample.json
import sys
import json
import time
from pipelines import pipeline
import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
paragraphs = []

if len(sys.argv) > 1:
  fileSrc = sys.argv[1]
else:
  fileSrc = False
  print('missing parametter')
  sys.exit()
if not fileSrc:
  print('missing parametter')
  sys.exit()
else:
  f = open(fileSrc)
  paragraphs = json.load(f)['data']

print('Import package and loading model (Estimated 50 seconds)...')
startLoadingModel = time.time()
tmp_file = './data/embeddings/word2vec-glove.6B.300d.txt'
model = KeyedVectors.load_word2vec_format(tmp_file)
endLoadingModel = time.time()
print(f'Loaded model: {round(endLoadingModel-startLoadingModel, 2)} seconds') #about 50 second

def generate_distractors(answer, count):
    answer = str.lower(answer)
    try:
        closestWords = model.most_similar(positive=[answer], topn=count)
    except:
        return []
    distractors = list(map(lambda x: x[0], closestWords))[0:count]
    return distractors

print("----------")
print(f'Processing paragraph (Estimated: {round(len(paragraphs) * 25 / 60, 2)} mins)..')

startProcess = time.time()
nlp_generate_question = pipeline('e2e-qg')
mces = []
typeans = []
ques = []
for context in paragraphs:
  quesAndContexts = []
  questions = nlp_generate_question(context)
  for question in questions:
    quesAndContexts.append({
      "question": question,
      "context": context
    })


  nlp_find_answer = pipeline("multitask-qa-qg")
  for ctx in quesAndContexts:
    answer = nlp_find_answer(ctx)
    result = {
      'question': ctx['question']
    }
    if answer:
      options = generate_distractors(answer, 3)
      if options: # Has option => push to *_mce
        options.append(answer)
        result['options'] = options
        result['answer'] = answer
        mces.append(result)
      else: # No option => push to *_type
        result['answer'] = answer
        typeans.append(result)
    else: # No answer => push to *_question
      ques.append(result)

# Serializing json 
json_mces = {
  'length': len(mces),
  'data': mces
}

json_typeans = {
  'length': len(typeans),
  'data': typeans
}
json_ques = {
  'length': len(ques),
  'data': ques
}

# fileName extraction
fileName = fileSrc.split('/')[-1].split('.')[0]
totalQuestion = len(mces) + len(typeans) + len(ques)
# Writing to json
with open(f"{fileName}_mces.json", "w") as outfile:
  outfile.write(json.dumps(json_mces, indent = 2))
with open(f"{fileName}_typeans.json", "w") as outfile:
  outfile.write(json.dumps(json_typeans, indent = 2))
with open(f"{fileName}_ques.json", "w") as outfile:
  outfile.write(json.dumps(json_ques, indent = 2))
endProcess = time.time()
print(f'Process done: {round(endProcess - startProcess, 2)} seconds') #about 20s 1 paragraph
print("----------")
print(f'Total Question: {totalQuestion}')
print(f'MCEs: {len(mces)}')
print(f'Type answer: {len(typeans)}')
print(f'Question: {len(ques)}')