import json

d = '{ "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5 } '

json1 = json.loads(d)
print (json1)
print (type(json1))

d2={
    "channel": "sony ten",
    "sports":['cricket', 'football','basketball'],
    "top_players":('ronaldo', 7 ,'messi', 10 ),
    "isgood":False
}
jscomp = json.dumps(d2)
print(jscomp)
print(type(jscomp))

