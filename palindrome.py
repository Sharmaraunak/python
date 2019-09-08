def palindrome(s):
    result = True
    for i in range(len(s)):
        j = len(s)-i-1
        if(i<=j):
            if(s[i]!=s[j]):
                result =False
                break
            continue
    return result


print(palindrome("abba"))
print(palindrome("aba"))
print(palindrome("hello"))
