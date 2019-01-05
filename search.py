import glob
import re

for i in glob.glob("*/*/*.gt.txt"):
     with open(i, 'r') as f:
         for line in f:
             x = re.findall(r'[\u000A\u001A]', line)
             #x = re.findall(r'[a]', line)
             if not x == []:
                  print(i+":")
                  print(x)


