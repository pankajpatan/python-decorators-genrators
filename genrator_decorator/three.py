
 
  
def readfile():
    with open('test.txt','r') as f:
        for line in f:
            for word in  line.split():
                yield word
for n in readfile():
    print(n)