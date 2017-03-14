word = 'sangmyung university'
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1

print "키-키값",d
print "저장된 문자의 갯수 (중복 제외)", len(d)
print "키: ",d.keys()
print "키값: ", d.values()