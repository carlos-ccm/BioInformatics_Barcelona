import re

def verificaCodi(codi):
    patro = r"^[0-9]{5}"
    return bool(re.match(patro,codi))
 
def verificaCorreu(correu):
    patro =  r"^[a-z0-9]{5,20}@[a-z0-9]{1,}\.[a-z]{2,}$"
    if re.match(patro,correu):
        return True
    else:
        return False

def canviaNom(nom1,nom2,text):
    mod_text = re.sub(r"\b" +nom1 + r"\b",nom2,text)
    return mod_text