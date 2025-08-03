# phones ={
#     "john": 7890,
#     "jane": 3210,
#     "doe": 5555
# }
# print(phones)

# print(type(phones))
# print(len(phones))
# print(phones["john"])
# print(phones.get("jane"))
# print(phones.keys())

# phones["jane"] = 3333
# print(phones)

# phones["alice"] = 4444
# print(phones)

# more_phones = {
#     "bob": 8888,
#     "charlie": 7777
# }
# phones.update(more_phones)
# print(phones)

# phones.pop("john")
# print(phones)

# phones.popitem()
# print(phones)

# phones.clear()
# print(phones)

# for x,y in phones.items():
#     print(x,y)

phones = {
    "area1": {
        "x": 1,
        "y": 2,
        "z": 3
    },
    "area2": {
        "a": 4,
        "b": 5,
        "c": 6
    }
}
print(phones["area1"]["x"])
print(phones["area2"]["a"])