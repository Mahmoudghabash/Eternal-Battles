a = 'this is a test string for me to see that thing Bazingazest'

b = a.split()

b.sort(key = lambda x:len(x) , reverse = False)
print(b)
