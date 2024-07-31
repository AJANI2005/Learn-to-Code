
A = "hello world"
B = "world"

def fls(stringa, stringb,idxa = 0,idxb = 0):
   
    #Base case
    if idxa == len(stringa) or idxb == len(stringb): return 0
    
    options = []
    if(stringa[idxa] == stringb[idxb]):
        options.append(fls(stringa, stringb, idxa+1, idxb+1) + 1)
   
    options.append(fls(stringa, stringb, idxa+1, idxb))
    options.append(fls(stringa, stringb, idxa, idxb+1))

    

    return max(options)


print(fls(A,B,0,0))

