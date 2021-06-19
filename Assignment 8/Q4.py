str1 = "Select the paragraphs that you want to convert to list items. On the Home tab, in the Paragraph group, do either of the following: Click the Bullets button to convert the selection to a bulleted list. Click the Numbering button to convert the selection to a numbered list"
import re
str1 = re.sub("[^\w]", " ",  str1).split()
c=0
for i in str1:
    c=c+1

print("No of Words in the given String is", c)