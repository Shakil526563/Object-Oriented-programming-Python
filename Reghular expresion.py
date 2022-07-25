"""re means regular expression"""
import re
pa=r"shakil"
if re.search(pa,"shakil is a good boy"):
    print("match")
else:
    print("not match")

pa=r"shakil"
if re.match(pa,"shakil is a good boy"):
    print("match")
else:
    print("not match")


pattern=r"5"
print(re.findall(pattern,"9,8,6,5,4,5,7"))

paa=r"9"
list="5,9,8,7,4,6,9"
ma=re.findall(paa,list)
print(ma)

"""import re modules ar vitore search match ,findall function ghula kaj kore"""
str=r"shkil"
text="shkil is a good boy"
te=re.sub(str,"shakil",text,count=1)
print(te)
"""sub function value replace ar jonno use kore,and count=1 means shkil str ta akbar paile akbar just replace 
hobe ,2 ba 3 dile shakil 2 ba 3 bar thakle ei change hobe.
"""