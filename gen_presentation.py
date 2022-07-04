# python ./gen_presentation.py ./context/wiki_test.json 0 101 abc/json
import sys
import json
import time
import numpy as np
from pipelines import pipeline
from gensim.models import KeyedVectors
pages = []
start = None
end = None
if len(sys.argv) >= 3:
  fileSrc = sys.argv[1]
  start = int(sys.argv[2])
  end = int(sys.argv[3])
else:
  fileSrc = False
  print('missing parametter')
  sys.exit()
if (len(sys.argv) > 4):
  exportName = sys.argv[4]
else:
  exportName = None
if (not fileSrc) or (not end):
  print('missing: fileSource || start || end')
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

fileName = fileSrc.split('/')[-1].split('.')[0]
def generate_distractors(answer, count):
  answer = str.lower(answer)
  try:
    closestWords = model.most_similar(positive=[answer], topn=count)
  except:
    return []
  distractors = list(map(lambda x: x[0], closestWords))[0:count]
  return distractors

def writeToFile(fileName, presentations=[]):
  if (exportName):
    with open(exportName, "w", encoding='utf8') as outfile:
      outfile.write(json.dumps(presentations, indent = 2))
  else:  
    with open(f"{fileName}_{start}-{end-1}_presentations.json", "w", encoding='utf8') as outfile:
      outfile.write(json.dumps(presentations, indent = 2))
print("----------")
startProcess = time.time()
nlp_generate_question = pipeline('e2e-qg')
presentations = []
totalSlides = 0
for page in pages:
  id = int(page['id'])
  is_in_range = id in range(start, end)
  if (is_in_range):
    try:
      # Xu ly tao cau hoi
      presentation = {
        'name': page['title'],
        'index': page['index'],
        'slides': []
      }
      timeLocal = time.localtime()
      now = time.strftime("%H:%M:%S", timeLocal)
      print("id: ", page['id'], " name: ", presentation['name'], " at: ", now)
      paragraphs = page['paragraphs']
      for paragraph in paragraphs:
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
          slide = {
          }
          if answer:
            slide['title'] = ctx['question']
            slide['titleLowercase'] = ctx['question'].lower()
            options = generate_distractors(answer, 3)
            if options: # Has option => create slide/slideOptions to push to presentation.slides
              slide['slideOptions'] = []
              slide['type'] = 'pickAnswer'
              for option in options:
                slide['slideOptions'].append({
                  'title': option.capitalize(),
                  'correct': 'false'
                })
              slide['slideOptions'].append({
                'title': answer.capitalize(),
                'correct': 'true'
              })
              np.random.shuffle(slide['slideOptions'])
              presentation['slides'].append(slide)
            else: # No option => push to type ans to generate matchpair
              pass
            
      if(len(presentation['slides']) > 0):
        presentations.append(presentation)
        totalSlides += int(len(presentation['slides']))
      else:
        print('fail: no slides generated')
    except:
      # theo doi ngoai le xay ra
      print('Error at id: ', id, ' index: ', page['index'])
      writeToFile(fileName, presentations)
      break
  else:
    pass
writeToFile(fileName, presentations)
endProcess = time.time()
print(f'Process done: {round((endProcess - startProcess) / 60, 2)} minutes')
print(f'totalSlides: {totalSlides}')
# 22 slides, 205.03 sec 1 presentation