
#group the anagrams
def group(s):
    dict={}
    for item in s:
        key="".join(sorted(item))
        if key not in dict:
            dict[key]=[]
        dict[key].append(item)
    return list(dict.values())


str=["eat","bat","tea","atb",'ate','ten']
print(group(str))










