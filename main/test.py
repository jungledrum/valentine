form = {
    'a': 1,
    'b': 2
}


def add_set(form):
    d = {}
    for k,v in form.iteritems():
        k = 'set__' + k
        d[k] = v
    return d

print add_set(form)
# form = map(add_set, form)

# print form