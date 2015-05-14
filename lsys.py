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

def render(commands, ruleset={'forward_dist':10.0, 'angle':pi/2}):
    ez = EZDraw()
    #ez.pos = (ez.w-50,ez.h - 50)
    nth = 0
    stk = []
    for sym in commands:
        if sym == 'F':
            ez.forward(ruleset['forward_dist'])
        elif sym == '-':
            ez.left(ruleset['angle'])
        elif sym == '+':
            ez.right(ruleset['angle'])
        elif sym == '[':
            stk.append((ez.pos, ez.angle))
        elif sym == ']':
            ez.pos, ez.angle = stk.pop()
        nth += 1
        if nth % 256 == 0:
            ez.update(0)
    return ez

i = "A"
iterations = 10
for x in xrange(iterations):
    print x,'th iteration start'
    #i = lsys(i, {"A": "F[B+[-B+A]]", "B": "-A+F[+A][-F]"})
    #i = lsys(i, {"A": "A+BF+", "B": "-FA-B"}) # dragon curve
    i = lsys(i, {"A": "B[-FA]", "B": "FA[+B]"})


print "done"

ruleset = {
            'forward_dist': 5.0,
            'angle': pi/5
        }

print i
ez = render(i, ruleset)
while True:
    ez.update(0)
