from pipelines import pipeline
nlp = pipeline("multitask-qa-qg")

# for qa pass a dict with "question" and "context"
answer = nlp({
    "question": "When did the American League declare itself a major league?",
    "context": "When the American League declared itself a major league in 1901, the new league moved the previous minor league circuit Western League\'s Kansas City Blues franchise to Washington, a city that had been abandoned by the older National League a year earlier.The new Washington club, like the old one, was called the 'Senators' (the second of three franchises to hold the name). Jim Manning moved with the Kansas City club to manage the first Senators team."})
print("answer: ", answer)