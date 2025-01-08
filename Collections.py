# List is a collection which is  ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable and unindexed.No duplicate members.
# Dictionary is a collection which is ordered and changeable. No duplicate members.

# 1. List [] =>
# Allows Duplicate, 
# Any type of data can be stored,
# We can modify the list item. We can add or remove 
# insert(), append(), extend(), pop()

# a = [1,2,3,4,5]
# print(a)
# a.append(True)
# a.append("test")
# a.append(6)
# a.append(50)
# a.append(3)
# print(a)
# ---------------------

# a = [1,2,3,4,5]
# print(a[0])
# a.insert(0,10)
# print(a)

# --------------------

# a = [1,2,3,4,5]
# a[0]=20
# print(a)

# --------------------

# a = [1,2,3,4,5]
# a.pop(4)
# print(a)

# --------------------

# a = [1,2,3,4,5]
# a.pop()
# a.pop()
# print(a)

# ---------------------
# a = [1,2,3,4,5]
# b = [10,20,30,40]
# a.extend(b)
# print(a)

# -------------
# Tuple
# Allows Duplicate, 
# Any type of data can be stored,
# We cannot modify the list item. We cannot add or remove 

# a = (1,2,3,4)
# print(type(a))
# print(a)

# -------------------

# a = (1,2,3,4)
# b = list(a)
# print(type(a))
# print(type(b))
# b.pop()
# print(a)
# print(b)

# -------------------
# Set
# Do not Allow Duplicate, Duplicate values will be removed.
# Any type of data can be stored,
# We cannot modify the list item. We can add or remove 
# Sets are unordered
# add(), update(), remove(), pop()

# a = {1,2,3,4,2,1,5}
# print(type(a))
# a.add(90)
# print(a)
# a.remove(5)
# print(a)

#---------------------
# a = {1,2,3,2,3,5,4,90}
# print(a)
# a.pop()
# print(a)

#---------------------
# Dictionary
# Do not Allow Duplicate, Duplicate values will overwrite existing value.
# Any type of data can be stored,
# key:value pair {"name":"test"}
# get() - keys(),values(),items()
# update{{"age":2}}
# del => a.pop("age")
# del => del a["age"]
# clear => a.clear()




# a = {
#     "name":"emc",
#     "age":1,
#     "location":"chennai",
#     "students":["bala","alex","siva"]
#     }
# print(type(a))
# print(a)
# print(a["name"])
# print(a["students"])
# print(a.keys())
# print(a.values())

#-------------
# a = {
#     "name":"emc",
#     "age":1,
#     "location":"chennai",
#     "students":["bala","alex","siva"]
#     }
# a["age"]=3
# a["color"]="red"
# a.update({"location":"madurai"})
# print(a)

#-------------
# a = {
#     "name":"emc",
#     "age":1,
#     "location":"chennai",
#     "students":["bala","alex","siva"]
#     }
# a.pop("age")
# print(a)


#-------------
# a = {
#     "name":"emc",
#     "age":1,
#     "location":"chennai",
#     "students":["bala","alex","siva"]
#     }
# del a["age"]
# print(a)

#-------------
# a = {
#     "name":"emc",
#     "age":1,
#     "location":"chennai",
#     "students":["bala","alex","siva"]
#     }
# del a # complete dictioinary delete
# print(a)]

# -------------------

a = {
    "name":"emc",
    "age":1,
    "location":"chennai",
    "students":["bala","alex","siva"]
    }

a.clear()
print(a)