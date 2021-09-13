n=3
for i in range(n):
    print("*"*(i+1))

for i in range(n):
    print("*"*(n-i))

# def removerandsplit(string, word):
#     new = string.replace(word, "")
#     return new.strip()

# string = "raghav isgood football player"
# r = removerandsplit(string, "player")
# print(r)

def rmvsplt(str, word):
    new = str.replace(word, "")
    return new.strip()

str = "raghav isgood football player"     
k = rmvsplt(str, "raghav")
print(k)

