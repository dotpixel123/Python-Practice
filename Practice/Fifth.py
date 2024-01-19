d = {"Shourya": "Me",
"My marks" : [12,3,31,23],
"His marks" : [12,32,32,2],
 "Shubham" : "Friend"}
print (type(d["My marks"]))
print (d.values())

print (d.keys())
print (list(d.keys()))

a = {} # not an empty set
print (type(a))
a = set() # an empty set
print (type(a))
a.add(323232323232344)
print (a)

# b = {[1,23,32,1,21,3]} # set can't contain list or dictionaries as they are unhashable
# print (b)

b = {(12,32,34,32,1)} # set can contain tupple as they are hashable
print (b)

a= {12,3,2,1,12,21,2321,2,1}
b= {121,31,3,43,1,31,2,2,1,3,43,1,3,}
print (a.intersection(b))
print (a.union(b))
