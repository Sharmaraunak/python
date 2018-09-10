s=input("Enter an alphabet: ")
count=0
place=0
for letter in s:
    place+=1
    if letter =='b':
        if place <len(s):
            if s[place]== 'o':
                if place+1 < len(s):
                    if s[place+1]=='b':
                        count+=1
                    else:
                        continue

            else:
                continue
    else:
        continue


print("No. of bob: ",count)
