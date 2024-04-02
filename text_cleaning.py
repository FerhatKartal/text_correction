#metni noktalama işaretlerinden ve özel karakterlerden arındırmak. 

import string
# from text import text
def cleaning(text):

    return text.translate(str.maketrans(" "," ",string.punctuation))