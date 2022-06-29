import json
def addPresentTitleToSlide(presentations):
  for presentation in presentations:
    name = presentation['name'].lower()
    for slide in presentation['slides']:
      title = slide['title'].lower()
      if(name not in title):
        slide['title'] = f"[{presentation['name']}] {slide['title']}"

def getPresentation(exportName):
  # support you apppend data instead of override new, if the target exportName .json file has data inside
  if(exportName):
    f = open(exportName)
    data = json.load(f)
    return data
  return []