def integrate(func, xlow, xhigh, n):
    length = xhigh - xlow
    sect = length / n
    area = 0
    for j in range(n):
        x = xlow + sect * j
        y = eval(func.replace("x", str(x)))
        secarea = y * sect
        area = area + abs(secarea)
    return (area)

function = input("Enter function: ")
lowl = float(input("Low limit:" ))
highl = float(input("High limit:"))
N = int(input("No of points: "))
r = integrate(function, lowl, highl, N)
print("integral of %s between %5.2f and %5.2f = %6.2f" %(function,lowl,highl,r))
