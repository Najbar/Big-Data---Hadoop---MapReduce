import re

WORD_RE = re.compile(r'[\w]+' )

words = WORD_RE.findall('Big data, Hadoop and map reduce. (Hello world)')
print(words)