# python ./gen_presentation.py ./context/wiki_test.json
import sys
import json
import time

from numpy import append
from pipelines import pipeline
from gensim.models import KeyedVectors
pages = []

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
  with open(fileSrc, encoding='utf-8') as f:
    pages = json.load(f)['data']
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
# print(f'Processing (Estimated: {round(len(pages) * 25 / 60, 2)} mins)..')

startProcess = time.time()
nlp_generate_question = pipeline('e2e-qg')
presentations = []
for page in pages:
  presentation = {
    'name': page['title'],
    'index': page['index'],
    'slides': []
  }
  print(presentation['name'])
  paragraphs = page['paragraphs']
  for paragraph in paragraphs:
    print("\t"+paragraph)
    questionAndContexts = []
    questions = nlp_generate_question(paragraph)
    for question in questions:
      questionAndContexts.append({
        "question": question,
        "context": paragraph
      })
    nlp_find_answer = pipeline("multitask-qa-qg")
    for ctx in questionAndContexts:
      answer = nlp_find_answer(ctx)
      slide = {}
      if answer:
        slide['title'] = ctx['question'],
        slide['titleLowercase'] = ctx['question'].lower()
        options = generate_distractors(answer, 3)
        if options: # Has option => create slide/slideOptions to push to presentation.slides
          slide['slideOptions'] = []
          slide['type'] = 'pickAnswer'
          for option in options:
            slide['slideOptions'].append({
              'title': option,
              'correct': 'false'
            })
          slide['slideOptions'].append({
            'title': answer,
            'correct': 'true'
          })
          presentation['slides'].append(slide)
        else: # No option => push to type ans to generate matchpair
          pass
          # result['answer'] = answer
          # typeans.append(result)
  presentations.append(presentation)
print(presentations)
print(len(presentations[0]['slides']))
# # fileName extraction
fileName = fileSrc.split('/')[-1].split('.')[0]

with open(f"{fileName}_presentations.json", "w") as outfile:
  outfile.write(json.dumps(presentations, indent = 2))
endProcess = time.time()
print(f'Process done: {round(endProcess - startProcess, 2)} seconds')
# 22 slides, 205.03 sec 1 presentation