modes = ("+", "-", "*", "/")
option = select("Choose one:", options = modes)

click(Pattern("1578682167285.png").exact().targetOffset(1,-2))
wait("1578682243776.png")
click(Pattern("1579120702699.png").targetOffset(-50,-13))
if option == modes[0]:
    click(Pattern("1579120702699.png").targetOffset(55,48))
elif option == modes[1]:
    click(Pattern("1579120702699.png").targetOffset(55,18))
elif option == modes[2]:
    click(Pattern("1579120702699.png").targetOffset(54,-15))
else:
    click(Pattern("1579120702699.png").targetOffset(55,-46))
click(Pattern("1579120702699.png").targetOffset(-50,-13))
click(Pattern("1579120702699.png").targetOffset(108,50))

