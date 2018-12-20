
def perm_gen_lex(a):
    permlist = []
    if a == '':
        return []
    if len(a) == 1:
        return [a]
    for i in range(len(a)):
        # print(char + '+')
        simpler = a[:i] + a[i+1:]
        list = perm_gen_lex(simpler)

        # print("s:", simpler)
        # permlist = perm_gen_lex(simpler)
        # print(permlist)
        for char in list:
            permlist.append(a[i:i+1] + char)


    return permlist
