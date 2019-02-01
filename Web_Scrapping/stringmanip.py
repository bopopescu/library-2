

def manipstring(a):
    p = a.split('.')
    print(len(p))
    st = ''
    x = 0
    while x < len(p):
        print(p[x])
        if x == 0:
            st = p[x].strip() + '.'
        else:
            st = st + p[x].strip()

        x += 1

    print(st)


a ='$42\n.\n97'
manipstring(a)

