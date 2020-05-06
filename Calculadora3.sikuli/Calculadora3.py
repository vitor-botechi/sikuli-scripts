Settings.MoveMouseDelay = 2

running = True

def isRunning(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.CTRL, isRunning)

click(Pattern("1578682167285.png").exact().targetOffset(1,-2))
wait("1578682243776.png")

Settings.MoveMouseDelay = 0.5
click(Pattern("1579120702699.png").targetOffset(-104,17))

while exists ("1578682243776.png") and running:
    click(Pattern("1579120702699.png").targetOffset(55,48))    
    click(Pattern("1579120702699.png").targetOffset(-104,17))

click(Pattern("1579120702699.png").targetOffset(108,50))

