

# chiffrage Cesar
alp = "abcdefghijklmnopqrstuvwxyz"


def chiffrage(ch, decalage):
    # print(ch)
    ch2 = ""
    for l in ch.lower():
        c = alp.find(l)
        # ça
        # if (c != -1):
        #     g = (c + decalage) % len(alp)
        #     ch2 += alp[g]
        # else:
        #     ch2 += l
        # ou ça
        ch2 += alp[(c + decalage) % len(alp)] if c!=-1 else l 
        
    return ch2

if __name__ == "__main__":
    ch = "Je suis une chaine à coder"
    str_code =  chiffrage(ch, 3)
    str_decode =  chiffrage(str_code, -3)
    
    print(f"{ch} : codée => {str_code}, décodée => {str_decode}")
