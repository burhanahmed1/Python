# Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(int(18))
s.add(str('18'))
print(s)