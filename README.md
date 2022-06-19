# Question Generation using 🤗transformers
This repository was a clone of: https://github.com/patil-suraj/question_generation (See instruction here)
Bonus 2 file:
1. **search_keyword.py**:
- input: keyword.
- output: wikipedia relevant keyword with link
```
Sample: 'washington'
Output: [
	('Washington', '', 'https://en.wikipedia.org/wiki/Washington'),
	('Washington, D.C.', '', 'https://en.wikipedia.org/wiki/Washington,_D.C.'),
	('Washington (state)', '', 'https://en.wikipedia.org/wiki/Washington_(state)'),
	('Washington Commanders', '', 'https://en.wikipedia.org/wiki/Washington_Commanders'), ('Washington University in St. Louis', '', 'https://en.wikipedia.org/wiki/Washington_University_in_St._Louis'),
	('Washington Capitals', '', 'https://en.wikipedia.org/wiki/Washington_Capitals'), ('Washington Nationals', '', 'https://en.wikipedia.org/wiki/Washington_Nationals'), ('Washington Wizards', '', 'https://en.wikipedia.org/wiki/Washington_Wizards'), ('Washington State University', '', 'https://en.wikipedia.org/wiki/Washington_State_University'),
	('Washington Senators (1901–1960)', '', 'https://en.wikipedia.org/wiki/Washington_Senators_(1901%E2%80%931960)')
]
```
2. **playground.py**:
- input: sentence  or paragraph
- output: question
```
Sample: 'When the American League declared itself a major league in 1901, the new league moved the previous minor league circuit Western League\'s Kansas City Blues franchise to Washington, a city that had been abandoned by the older National League a year earlier. The new Washington club, like the old one, was called the "Senators" (the second of three franchises to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team.'
Output:
 [
	 'When did the American League declare itself a major league?', 
 	'Who moved the Kansas City Blues franchise to Washington?',
 	'What was the name of the new Washington club?', 
	 'How many Senators teams did Jim Manning manage?'
 ]
```
