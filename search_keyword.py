# https://github.com/barrust/mediawiki
from mediawiki import MediaWiki
wikipedia = MediaWiki()
x = wikipedia.search('washington')
y = wikipedia.opensearch('washington')
# print(x)
print(y)
