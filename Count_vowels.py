#number of vowels in given string
word=input("enter the word:")
vowels=("aeiou")
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print("{} occurred {}, many times".format(k,v))
       
        
