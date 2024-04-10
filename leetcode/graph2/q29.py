wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]


ans=[]

vowels=["a","e","i","o","u","A","E","I","O","U"]
for w in queries:
    if w in wordlist:
        ans.append(w)
    else:
        mt=""
        for word in wordlist:
            if len(word)!=len(w):
                continue
            i=-1
            for ch in word:
                i+=1
                if i>=len(word) or i>=len(w):
                    mt=""
                    break
                if ch==w[i] or ch.capitalize()==w[i] or ch==w[i].capitalize() or ch.lower()==w[i] or ch==w[i].lower():
                    mt+=ch
                elif (ch in vowels) and (w[i] in vowels):
                    mt+=ch
                else:
                    mt=""
                    break
            if len(mt)==len(word) and len(mt)==len(w):
                ans.append(mt)
                break
        if mt=="":
            ans.append(mt)

print(ans)
                
                





