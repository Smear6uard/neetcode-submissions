def concatenate(s1: str, s2: str) -> str:
    newStr=s1+s2
    if len(newStr)>10:
        return "Too long!"
    else:
        return newStr



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
