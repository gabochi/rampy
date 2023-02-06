# save code
# save render
# render (render

def render(ta='t', tb='t', tc='t', td='t', l=16):
    lenght = 1 << l
    out = []

    for T in range(lenght):
        t = T
        t = eval(ta)
        t = eval(tb)
        t = eval(tc)
        t = eval(td)
        out.append(t&255)

    with open('out.raw','wb') as file:
        file.write(bytes(out))
    print(f'{len(out)} bytes written')
