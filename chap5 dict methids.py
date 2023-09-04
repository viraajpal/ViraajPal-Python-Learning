mydict = {

    "fast": "in a quick manner",
    "viraaj": "a coder",
    "marks": [1, 2, 3],
    1: 2,
    "anotherdict": {'viraaj': 'player'},
}
print(type(mydict.keys()))
print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())
print(mydict)
updatedict = {
    "lavish": "monu",
     "viraaj": "a dancer",
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("viraaj"))
