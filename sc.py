f = lambda h : ((1 + (h / 2))/(1 - (h / 2)))**(1/h)
print("h = 1, 0.1, 0.01, 0.001, 0.0001")

for i in range(0, 6):

    print(f"h = {10**-i}, f(h) = {f(10**-i)}")