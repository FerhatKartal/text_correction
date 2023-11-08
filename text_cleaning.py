#metni noktalama işaretlerinden ve özel karakterlerden arındırmak. 

import string
from text import text

print(text.translate(str.maketrans(" "," ",string.punctuation)))