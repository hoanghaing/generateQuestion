import time
from pipelines import pipeline
start = time.time()
nlp = pipeline('e2e-qg')
# result = nlp('Python is a programming language. Created by Guido van Rossum and first released in 1991.')
# result = nlp('Ronaldo began his career with Portugal at age 18. He scored his first goal at UEFA Euro 2004 and helped Portugal reach the final, although they lost to Greece 1-0. The first World Cup he played at was the 2006 FIFA World Cup. He scored a goal and helped Portugal earn fourth place. Two years later, he became Portugal\'s full captain')
# result = nlp('SM Entertainment is a record label and talent agency in South Korea. It is one of the main entertainment businesses in Korea. It was founded by Lee Su-man, a former singer. It was originally focused solely on entertainment management. Since then, however, they have expanded their business interests to establishing subsidiary companies and incorporating affiliates. They have foreign subsidiaries, such as SM Japan, Asia, and USA.')
# result = nlp('Joseph Robinette Biden Jr. born November 20, 1942) is an American politician and the 46th and current president of the United States since 2021. Biden was also the 47th vice president from 2009 through 2017 during the Barack Obama presidency. He is a member of the Democratic Party and is from Wilmington, Delaware. Before becoming vice president, Biden was a U.S. Senator from Delaware from 1973 to 2009. He had served in the Senate longer than any other President or Vice President.')
result = nlp('When the American League declared itself a major league in 1901, the new league moved the previous minor league circuit Western League\'s Kansas City Blues franchise to Washington, a city that had been abandoned by the older National League a year earlier. The new Washington club, like the old one, was called the "Senators" (the second of three franchises to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team.')
end = time.time()
print(result)
print(f'Run time: {end-start}')