
from collections import Counter

dict={'a':67,'b':23,'c':45,'d':56,'e':12,'f':69}


n=Counter(dict)

high=n.most_common(3)

print(dict,"\n")
print("keys:values")

for i in high:
    print(i[0]," :",i[1])