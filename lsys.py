from ezdraw import * 

def lsys(s, rules):
    keys = rules.keys()
    keys.sort() # sort keys by length to have precedence
    out = []
    stk = list(s)
    while stk:
        for sym in keys:
            if stk[:len(sym)] == list(sym):
                out.append(rules[sym])
                stk = stk[len(sym):]
                break;
        if stk:
            out.append(stk[0])
            stk.pop(0)
    return "".join(out)

i = "A"
iterations = 16
for x in xrange(iterations):
    print x,'th iteration start'
    #i = lsys(i, {"A": "F[B+[-B+A]]", "B": "-A+F[+A][-F]"})
    i = lsys(i, {"A": "A+BF+", "B": "-FA-B"})

print i
ez = EZDraw()
#ez.pos = (ez.w-50,ez.h - 50)
nth = 0
stk = []
for sym in i:
    if sym == 'F':
        ez.forward(1.5)
    elif sym == '-':
        ez.left(pi/2)
    elif sym == '+':
        ez.right(pi/2)
    elif sym == '[':
        stk.append((ez.pos, ez.angle))
    elif sym == ']':
        ez.pos, ez.angle = stk.pop()
    nth += 1
    if nth % 256 == 0:
        ez.update(0)

print "done"

while True:
    ez.update(0)
