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
            stk = stk[1:]
    return "".join(out)

i = "A"
iterations = 9
for x in xrange(iterations):
    print x,'th iteration start'
    #i = lsys(i, {"A": "F[B+[-B+A]]", "B": "-A+F[+A][-F]"})

print i
ez = EZDraw()
#ez.pos = (ez.w/2,ez.h - 50)
nth = 0
stk = []
for sym in i:
    if sym == 'F':
        ez.forward(10.0)
    elif sym == '-':
        ez.left(pi/10)
    elif sym == '+':
        ez.right(pi/10)
    elif sym == '[':
        stk.append((ez.pos, ez.angle))
    elif sym == ']':
        ez.pos, ez.angle = stk.pop()
    nth += 1
    if nth % 16 == 0:
        ez.update(0)

print "done"

while True:
    ez.update(0)
