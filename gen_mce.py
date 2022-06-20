# python .\gen_mce.py .\context\sample.json
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
  print(paragraphs)
  print(type(paragraphs))
  for item in paragraphs:
    print(item)

print('Import package and loading model...')
startLoadingModel = time.time()
tmp_file = './data/embeddings/word2vec-glove.6B.300d.txt'
model = KeyedVectors.load_word2vec_format(tmp_file)
endLoadingModel = time.time()
print(f'Loading model: {endLoadingModel-startLoadingModel}') #about 50 second

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
context = 'Python is a programming language. Created by Guido van Rossum and first released in 1991.' #2 quiz
# context = 'When the American League declared itself a major league in 1901, the new league moved the previous minor league circuit Western League\'s Kansas City Blues franchise to Washington, a city that had been abandoned by the older National League a year earlier. The new Washington club, like the old one, was called the "Senators" (the second of three franchises to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team.' #3 quiz
# context = 'Ronaldo began his career with Portugal at age 18. He scored his first goal at UEFA Euro 2004 and helped Portugal reach the final, although they lost to Greece 1-0. The first World Cup he played at was the 2006 FIFA World Cup. He scored a goal and helped Portugal earn fourth place. Two years later, he became Portugal\'s full captain' #1 quiz
# context = 'SM Entertainment is a record label and talent agency in South Korea. It is one of the main entertainment businesses in Korea. It was founded by Lee Su-man, a former singer. It was originally focused solely on entertainment management. Since then, however, they have expanded their business interests to establishing subsidiary companies and incorporating affiliates. They have foreign subsidiaries, such as SM Japan, Asia, and USA.' #0 quiz
# context = 'Joseph Robinette Biden Jr. born November 20, 1942) is an American politician and the 46th and current president of the United States since 2021. Biden was also the 47th vice president from 2009 through 2017 during the Barack Obama presidency. He is a member of the Democratic Party and is from Wilmington, Delaware. Before becoming vice president, Biden was a U.S. Senator from Delaware from 1973 to 2009. He had served in the Senate longer than any other President or Vice President.' #1quiz
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
  # print(result['question'])
  if answer: 
    # print(answer)
    options = generate_distractors(answer, 3)
    if options:
      # print(options)
      options.append(answer)
      result['options'] = options
      result['answer'] = answer
      results.append(result)
    # else:
      # print('No option')
  # else:
    # print('No answer')

endProcess = time.time()
print("----------")
print("result: ", results)
print(f'Process time: {endProcess-startProcess}') #about 20s 1 paragraph
print(f'Total time: {endProcess-startLoadingModel}') #about 70s total