s=input("Enter an sequence of letters: ")
max=0
seq=s[0]
count=s[0]
for i in range(len(s)-1):
    if(s[i+1]>=s[i]):
        count+=s[i+1];
        if(len(count)>max):
            max=len(count)
            seq=count
    else:
        count=s[i+1]
print(seq)
