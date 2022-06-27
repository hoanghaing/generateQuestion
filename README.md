# Tạo các presentations
```
python ./gen_presentation.py "input json" start_id end_id "export fileName"
```
<br/> Ví dụ: 
```python ./gen_presentation.py ./context/wiki_test.json 0 101```
<br/>
Chạy xử lý với file wiki_test.json, từ id 0 -> id 101.
<br/>
"export fileName" xài cho trường hợp giả sử chạy đến id = 59 bị lỗi và hệ thống vẫn tạo file từ 0 -> 58 với tên abc.json, lúc này có thể chạy lại 59 -> 100 bằng cách như sau.
```
python ./gen_presentation.py ./context/wiki_test.json 59 101 "abc.json"
```
<br />Trả về 'filename'_presentation.json hoặc exportFileName đã cho vào
<br /> Format (wiki_test.json):
```
[
  {
    "name": "Bob Benmosche",
    "index": "wikipedia-23886872",
    "slides": [
      {
        "title": [
          "When did Rabbi Herman Ben Mosche move the family to the United States?"
        ],
        "titleLowercase": "when did rabbi herman ben mosche move the family to the united states?",
        "slideOptions": [
          {
            "title": "1892",
            "correct": "false"
          },
          {
            "title": "1891",
            "correct": "false"
          },
          {
            "title": "1895",
            "correct": "false"
          },
          {
            "title": "1894",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "When did he earn his Bachelor of Arts degree in Mathematics?"
        ],
        "titleLowercase": "when did he earn his bachelor of arts degree in mathematics?",
        "slideOptions": [
          {
            "title": "1965",
            "correct": "false"
          },
          {
            "title": "1963",
            "correct": "false"
          },
          {
            "title": "1969",
            "correct": "false"
          },
          {
            "title": "1966",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "When did Benmosche join Arthur D. Little and Information Science as a consultant?"
        ],
        "titleLowercase": "when did benmosche join arthur d. little and information science as a consultant?",
        "slideOptions": [
          {
            "title": "1971",
            "correct": "false"
          },
          {
            "title": "1978",
            "correct": "false"
          },
          {
            "title": "1976",
            "correct": "false"
          },
          {
            "title": "1975",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "In what year did Ben Mosche join the Chase Manhattan systems group?"
        ],
        "titleLowercase": "in what year did ben mosche join the chase manhattan systems group?",
        "slideOptions": [
          {
            "title": "1971",
            "correct": "false"
          },
          {
            "title": "1978",
            "correct": "false"
          },
          {
            "title": "1976",
            "correct": "false"
          },
          {
            "title": "1975",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "Who was the owner of Kidder Peabody?"
        ],
        "titleLowercase": "who was the owner of kidder peabody?",
        "slideOptions": [
          {
            "title": "fornaro",
            "correct": "false"
          },
          {
            "title": "nardelli",
            "correct": "false"
          },
          {
            "title": "essner",
            "correct": "false"
          },
          {
            "title": "Benmosche",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "What was Benmosche promoted to president and Chief Operating Officer?"
        ],
        "titleLowercase": "what was benmosche promoted to president and chief operating officer?",
        "slideOptions": [
          {
            "title": "cfo",
            "correct": "false"
          },
          {
            "title": "cto",
            "correct": "false"
          },
          {
            "title": "seel",
            "correct": "false"
          },
          {
            "title": "COO",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "In what year did Ben Mosche become COO?"
        ],
        "titleLowercase": "in what year did ben mosche become coo?",
        "slideOptions": [
          {
            "title": "1998",
            "correct": "false"
          },
          {
            "title": "1996",
            "correct": "false"
          },
          {
            "title": "1999",
            "correct": "false"
          },
          {
            "title": "1997",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "What year was he named Chairman of the Board and CEO of MetLIfe?"
        ],
        "titleLowercase": "what year was he named chairman of the board and ceo of metlife?",
        "slideOptions": [
          {
            "title": "1997",
            "correct": "false"
          },
          {
            "title": "1996",
            "correct": "false"
          },
          {
            "title": "1999",
            "correct": "false"
          },
          {
            "title": "1998",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "In what year was he appointed Chairman of the Board and CEO of MetLife?"
        ],
        "titleLowercase": "in what year was he appointed chairman of the board and ceo of metlife?",
        "slideOptions": [
          {
            "title": "1997",
            "correct": "false"
          },
          {
            "title": "1996",
            "correct": "false"
          },
          {
            "title": "1999",
            "correct": "false"
          },
          {
            "title": "1998",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "When did he retire?"
        ],
        "titleLowercase": "when did he retire?",
        "slideOptions": [
          {
            "title": "2007",
            "correct": "false"
          },
          {
            "title": "2005",
            "correct": "false"
          },
          {
            "title": "2008",
            "correct": "false"
          },
          {
            "title": "2006",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "In what year did Benmosche retire?"
        ],
        "titleLowercase": "in what year did benmosche retire?",
        "slideOptions": [
          {
            "title": "2012",
            "correct": "false"
          },
          {
            "title": "2011",
            "correct": "false"
          },
          {
            "title": "2010",
            "correct": "false"
          },
          {
            "title": "2013",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "What year was the one time discoth\u00e8que bought?"
        ],
        "titleLowercase": "what year was the one time discoth\u00e8que bought?",
        "slideOptions": [
          {
            "title": "2002",
            "correct": "false"
          },
          {
            "title": "2003",
            "correct": "false"
          },
          {
            "title": "1999",
            "correct": "false"
          },
          {
            "title": "2001",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "In what year did Benmosche produce 3,000 bottles of wine?"
        ],
        "titleLowercase": "in what year did benmosche produce 3,000 bottles of wine?",
        "slideOptions": [
          {
            "title": "2012",
            "correct": "false"
          },
          {
            "title": "2013",
            "correct": "false"
          },
          {
            "title": "2010",
            "correct": "false"
          },
          {
            "title": "2011",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "When did Benmosche testify to the Congressional Troubled Asset Relief Program (TARP) Oversight Panel?"
        ],
        "titleLowercase": "when did benmosche testify to the congressional troubled asset relief program (tarp) oversight panel?",
        "slideOptions": [
          {
            "title": "2011",
            "correct": "false"
          },
          {
            "title": "2009",
            "correct": "false"
          },
          {
            "title": "2012",
            "correct": "false"
          },
          {
            "title": "2010",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "What was the name of the person who later asked for a personal private jet?"
        ],
        "titleLowercase": "what was the name of the person who later asked for a personal private jet?",
        "slideOptions": [
          {
            "title": "fornaro",
            "correct": "false"
          },
          {
            "title": "nardelli",
            "correct": "false"
          },
          {
            "title": "essner",
            "correct": "false"
          },
          {
            "title": "Benmosche",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "Who was the President of the TARP oversight panel in 2010?"
        ],
        "titleLowercase": "who was the president of the tarp oversight panel in 2010?",
        "slideOptions": [
          {
            "title": "fornaro",
            "correct": "false"
          },
          {
            "title": "nardelli",
            "correct": "false"
          },
          {
            "title": "essner",
            "correct": "false"
          },
          {
            "title": "Benmosche",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "Who oversaw the sale of non-core assets in AIG\u2019s portfolio to pay down the $182 billion in government aid?"
        ],
        "titleLowercase": "who oversaw the sale of non-core assets in aig\u2019s portfolio to pay down the $182 billion in government aid?",
        "slideOptions": [
          {
            "title": "fornaro",
            "correct": "false"
          },
          {
            "title": "nardelli",
            "correct": "false"
          },
          {
            "title": "essner",
            "correct": "false"
          },
          {
            "title": "Benmosche",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "Benmosche's management has been credited with leading the company to what?"
        ],
        "titleLowercase": "benmosche's management has been credited with leading the company to what?",
        "slideOptions": [
          {
            "title": "profits",
            "correct": "false"
          },
          {
            "title": "earnings",
            "correct": "false"
          },
          {
            "title": "competitiveness",
            "correct": "false"
          },
          {
            "title": "profitability",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "What was Benmosche diagnosed with in 2010?"
        ],
        "titleLowercase": "what was benmosche diagnosed with in 2010?",
        "slideOptions": [
          {
            "title": "prostate",
            "correct": "false"
          },
          {
            "title": "breast",
            "correct": "false"
          },
          {
            "title": "cancers",
            "correct": "false"
          },
          {
            "title": "cancer",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "What did he continue to do while undergoing an aggressive oral chemotherapy regime?"
        ],
        "titleLowercase": "what did he continue to do while undergoing an aggressive oral chemotherapy regime?",
        "slideOptions": [
          {
            "title": "working",
            "correct": "false"
          },
          {
            "title": "works",
            "correct": "false"
          },
          {
            "title": "worked",
            "correct": "false"
          },
          {
            "title": "work",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "In what year did Charlie Rose interview him in December 2012?"
        ],
        "titleLowercase": "in what year did charlie rose interview him in december 2012?",
        "slideOptions": [
          {
            "title": "2011",
            "correct": "false"
          },
          {
            "title": "2009",
            "correct": "false"
          },
          {
            "title": "2012",
            "correct": "false"
          },
          {
            "title": "2010",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      },
      {
        "title": [
          "In what year did Benmosche give an interview to the Wall Street Journal?"
        ],
        "titleLowercase": "in what year did benmosche give an interview to the wall street journal?",
        "slideOptions": [
          {
            "title": "2012",
            "correct": "false"
          },
          {
            "title": "2011",
            "correct": "false"
          },
          {
            "title": "2010",
            "correct": "false"
          },
          {
            "title": "2013",
            "correct": "true"
          }
        ],
        "type": "pickAnswer"
      }
    ]
  }
]
```
# Cài đặt
Yêu cầu: Python 3.7.9, gensim, pytorch === 1.10.0, transformers==3.0.0, pipeline <br />
Tham khảo lệnh ở các repo sau để cài nếu cần: <br />
- https://github.com/patil-suraj/question_generation
- https://github.com/KristiyanVachev/Question-Generation <br />

Download file pretrain model + asset (830MB): https://drive.google.com/file/d/15GcFtPUKzT1LsLq0lC2jzvvdklG9efjG/view?usp=sharing <br />
Giải nén:
- vứt **file glove.6B.300d** vào trong thư mục ./data/embeddings/
- vứt 2 file **train-v1.1.json**, **dev-v1.1.json** vào thư mục ./data/squad-v1/

Tiến hành tạo ra vector tử glove.6b.300d, chạy (Mất khoảng 2 phút): <br />
```
python gen_vector.py
```
Sẽ nhận được file word2vec-glove.6B.300d.txt trong cùng thư mục <br />

Đưa data cần xử lý vào json, đặt trong thư mục ./context <br />
Ví dụ: data là file sample.json. <br />
Tạo quiz bằng cách chạy lệnh: <br />
```
python ./gen_mce.py [path-to-your-json-file]
Eg: python ./gen_mce.py ./context/sample.json
```
Quá trình chạy xong sẽ tạo ra 3 file .json: <br />
- File sample_mces.json: File có multiple choice hoàn chỉnh <br />
- File sample_typeans.json: File bị fail trong quá trình tạo đáp án sai, coi như type answer <br />
- File sample_ques.json: File bị fail: không tìm được đáp án cho câu hỏi được tạo, chỉ chứa mình câu hỏi <br />

Format file paragraph (sample.json):
```
{
  "data": [
    "Python is a programming language. Created by Guido van Rossum and first released in 1991.",
    "Ronaldo began his career with Portugal at age 18. He scored his first goal at UEFA Euro 2004 and helped Portugal reach the final, although they lost to Greece 1-0. The first World Cup he played at was the 2006 FIFA World Cup. He scored a goal and helped Portugal earn fourth place. Two years later, he became Portugal's full captain",
    "SM Entertainment is a record label and talent agency in South Korea. It is one of the main entertainment businesses in Korea. It was founded by Lee Su-man, a former singer. It was originally focused solely on entertainment management. Since then, however, they have expanded their business interests to establishing subsidiary companies and incorporating affiliates. They have foreign subsidiaries, such as SM Japan, Asia, and USA.",
    "Joseph Robinette Biden Jr. born November 20, 1942) is an American politician and the 46th and current president of the United States since 2021. Biden was also the 47th vice president from 2009 through 2017 during the Barack Obama presidency. He is a member of the Democratic Party and is from Wilmington, Delaware. Before becoming vice president, Biden was a U.S. Senator from Delaware from 1973 to 2009. He had served in the Senate longer than any other President or Vice President.",
    "When the American League declared itself a major league in 1901, the new league moved the previous minor league circuit Western League's Kansas City Blues franchise to Washington, a city that had been abandoned by the older National League a year earlier. The new Washington club, like the old one, was called the 'Senators' (the second of three franchises to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team."
  ]
}
```
Format file output: (sample_mce.json):
```
{
  "length": 7,
  "data": [
    {
      "question": "What is a programming language?",
      "options": [
        "monty",
        "perl",
        "cleese",
        "Python"
      ],
      "answer": "Python"
    },
    {
      "question": "When was Python first released?",
      "options": [
        "1990",
        "1992",
        "1993",
        "1991"
      ],
      "answer": "1991"
    },
    {
      "question": "When did Portugal lose to Greece?",
      "options": [
        "2-1",
        "2-0",
        "3-1",
        "1-0"
      ],
      "answer": "1-0"
    },
    {
      "question": "Before becoming vice president, Biden was a U.S. Senator from what state?",
      "options": [
        "wilmington",
        "pennsylvania",
        "connecticut",
        "Delaware"
      ],
      "answer": "Delaware"
    },
    {
      "question": "When did the American League declare itself a major league?",
      "options": [
        "1903",
        "1902",
        "1899",
        "1901"
      ],
      "answer": "1901"
    },
    {
      "question": "What was the name of the new Washington club?",
      "options": [
        "senate",
        "congressmen",
        "senator",
        "Senators"
      ],
      "answer": "Senators"
    },
    {
      "question": "How many Senators teams did Jim Manning manage?",
      "options": [
        "second",
        "third",
        "fourth",
        "first"
      ],
      "answer": "first"
    }
  ]
}
```
# Reference:
This repository was a clone of: https://github.com/patil-suraj/question_generation (See instruction here)
Generate distractor part, referenced: https://github.com/KristiyanVachev/Question-Generation
Added 3 file below:
1. **search_keyword.py**:
- input: keyword.
- output: wikipedia relevant keyword with link
```
Sample: 'washington'
```
```
Output: [
	('Washington', '', 'https://en.wikipedia.org/wiki/Washington'),
	('Washington, D.C.', '', 'https://en.wikipedia.org/wiki/Washington,_D.C.'),
	('Washington (state)', '', 'https://en.wikipedia.org/wiki/Washington_(state)'),
	('Washington Commanders', '', 'https://en.wikipedia.org/wiki/Washington_Commanders'), ('Washington University in St. Louis', '', 'https://en.wikipedia.org/wiki/Washington_University_in_St._Louis'),
	('Washington Capitals', '', 'https://en.wikipedia.org/wiki/Washington_Capitals'), ('Washington Nationals', '', 'https://en.wikipedia.org/wiki/Washington_Nationals'), ('Washington Wizards', '', 'https://en.wikipedia.org/wiki/Washington_Wizards'), ('Washington State University', '', 'https://en.wikipedia.org/wiki/Washington_State_University'),
	('Washington Senators (1901–1960)', '', 'https://en.wikipedia.org/wiki/Washington_Senators_(1901%E2%80%931960)')
]
```
2. **gen_question.py**:
- input: sentence  or paragraph
- output: question
```
Sample: 'When the American League declared itself a major league in 1901, the new league moved the previous minor league 
circuit Western League\'s Kansas City Blues franchise to Washington, a city that had been abandoned by the older National
League a year earlier.The new Washington club, like the old one, was called the "Senators"\ (the second of three franchises
to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team.'
```
```
Output:
 [
'When did the American League declare itself a major league?', 'Who moved the Kansas City Blues franchise to Washington?',
'What was the name of the new Washington club?', 'How many Senators teams did Jim Manning manage?'
 ]
```
```
Sample: Python is a programming language. Created by Guido van Rossum and first released in 1991.
```
```
Output: ['What is a programming language?', 'Who created Python?', 'When was Python first released?']
```
```
Sample: 'Ronaldo began his career with Portugal at age 18. He scored his first goal at UEFA Euro 2004 and helped
Portugal reach the final, although they lost to Greece 1-0. The first World Cup he played at was the 2006 FIFA World Cup.
He scored a goal and helped Portugal earn fourth place. Two years later, he became Portugal\'s full captain'
```
```
Output: [
'When did Ronaldo start his career with Portugal?', "What was Ronaldo's first goal at UEFA Euro 2004?",
'When did Portugal lose to Greece?', 'Who was the first World Cup Ronaldo played at?'
]
```
```
Sample: 'Joseph Robinette Biden Jr. born November 20, 1942) is an American politician and the 46th and current president of
the United States since 2021. Biden was also the 47th vice president from 2009 through 2017 during the Barack Obama presidency.
He is a member of the Democratic Party and is from Wilmington, Delaware. Before becoming vice president, Biden was a U.S. Senator
from Delaware from 1973 to 2009. He had served in the Senate longer than any other President or Vice President.'
```
```
Output: [
'When was Joseph Robinette Biden Jr. born?','Who is the 46th and current president of the United States since 2021?',
'From 2009 to 2017 who is Biden a member of?', 'Before becoming vice president, Biden was a U.S. Senator from what state?'
]
```
3. **multitaskQA.py**:
- input: object with context and question
- output: the answer
```
Sample:
answer = nlp({
    "question": "When did the American League declare itself a major league?",
    "context": "When the American League declared itself a major league in 1901, the new league moved the previous minor league circuit Western League\'s Kansas City Blues franchise to Washington, a city that had been abandoned by the older National League a year earlier.The new Washington club, like the old one, was called the 'Senators' (the second of three franchises to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team."})
print("answer: ", answer)
```
```
Output: 1901
```
4. **Generate Distractor**
- input: answer
- output: n wrong answer that similar to true answer
```
Sample:
options = generate_distractors('messi', 4)
print(options) => ["eto'o", 'ronaldinho', 'iniesta', 'ronaldo']
options = generate_distractors('SM entertainment', 4)
=> []: complex and many word answer make it hard to generate similar
options = generate_distractors('Youtube', 4)
=> ['facebook', 'myspace', 'twitter']
options = generate_distractors('Tailwind', 3)
=> ['headwind', 'crosswinds', 'oef']
options = generate_distractors('1945', 3)
=> ['1944', '1942', '1943']
options = generate_distractors('Final Fantasy Tactics: The War of the Lions', 3)
=> []
options = generate_distractors('stephencurry', 3)
=> []
options = generate_distractors('28th International Eucharistic Congress', 3)
=> []
```
**Summary**
- (1) Context finding: user input something, get the link, process the link to get paragraph, use paragraph as **context**
- (2) Question Generation: context in (1) is input of (2), with each context, get **questions**
- (3) Answer Generation: context in (1) and questions in (2) is input of (3), return **answer**
- (4) Adding another (wrong) options (Distractor) by Cosine Similarity-> MCE question
