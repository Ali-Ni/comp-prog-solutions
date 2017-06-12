zero = str(int(False))
one = int(True)
two = one << one
three = two + one
four = two << one
six = str(four + two)
seven = str(four + three)
eight = str(four << one)
one = str(one)
two = str(two)
three = str(three)
four = str(four)


H = chr(int(seven+two))
e = chr(int(one+zero+one))
l = chr(int(one+zero+eight))
o = chr(int(one+one+one))
space = chr(int(three+two))
comma = chr(int(four+four))
W = chr(int(eight+seven))
r = chr(int(one+one+four))
d = chr(int(one+zero+zero))
period = chr(int(three+three))
print(H+e+l+l+o+comma+space+W+o+r+l+d+period)