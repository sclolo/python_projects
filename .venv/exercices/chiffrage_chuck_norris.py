import re

def chiffre(ch):
    print (f"Codage de {ch}")
    
    p1 = "(1+|0+)"
    reg = re.compile(p1)
    ch2 = ""
    for m in reg.finditer(ch):
        print(m.start(), m.group()[0])
        match m.group()[0]:
            case "0":
                ch2+="00 "
            case "1":
                ch2+="0 " 
        ch2 += "0" * len(m.group()) + " "
    return ch2

def dechiffre(ch):
    print (f"Décodage de {ch}")
    ch2=""
    tc = ch.split(" ")
    for i in range(0,len(tc),2):
        match tc[i]:
            case "0":
                ch2+="1"* len(tc[i+1])
            case "00":
                ch2+= tc[i+1]
    return ch2
    
if __name__ == "__main__":
    # result -> 0 0 00 0000 0 000
    ch = "10000111"
    
    str_code = chiffre(ch)
    str_decode = dechiffre(str_code)
    
    print(f"{ch} : codée => {str_code}, décodée => {str_decode}")
