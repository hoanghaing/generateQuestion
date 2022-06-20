import time
from pipelines import pipeline
import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
print('Import package and loading model...')
startLoadingModel = time.time()
tmp_file = './data/embeddings/word2vec-glove.6B.300d.txt'
model = KeyedVectors.load_word2vec_format(tmp_file)
endLoadingModel = time.time()
print(f'Loading model: {endLoadingModel-startLoadingModel}')

def generate_distractors(answer, count):
    answer = str.lower(answer)
    try:
        closestWords = model.most_similar(positive=[answer], topn=count)
    except:
        return []
    distractors = list(map(lambda x: x[0], closestWords))[0:count]
    return distractors

print('Program is running...')

startProcess = time.time()
nlp_generate_question = pipeline('e2e-qg')
quesAndContexts = []
results = []
# context = 'When the American League declared itself a major league in 1901, the new league moved the previous minor league circuit Western League\'s Kansas City Blues franchise to Washington, a city that had been abandoned by the older National League a year earlier. The new Washington club, like the old one, was called the "Senators" (the second of three franchises to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team.'
context = 'Python is a programming language. Created by Guido van Rossum and first released in 1991.'
questions = nlp_generate_question(context)
for question in questions:
  quesAndContexts.append({
    "question": question,
    "context": context
  })

nlp_find_answer = pipeline("multitask-qa-qg")
for ctx in quesAndContexts:
  print(ctx['question'])
  answer = nlp_find_answer(ctx)
  result = {
    'question': ctx['question']
  }

  if answer: 
    print(answer)
    options = generate_distractors(answer, 3)
    if options:
      print(options)
      options.append(answer)
      result['options'] = options
      result['answer'] = answer
      results.append(result)
    else:
      print('No option')
      break
  else:
    print('No answer')
    break

endProcess = time.time()
print("----------")
print("result: ", results)
print(f'Process time: {endProcess-startProcess}')
print(f'Total time: {endProcess-startLoadingModel}')