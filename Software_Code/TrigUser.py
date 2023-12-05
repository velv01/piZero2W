import math
angle = float(input("Enter angle in degrees: "))
trig = input("Sine (s), cosine (c), or tangent (t): ")
rad = math.radians(angle)

if trig == "s":
    print("Sine=%.5f" % math.sin(rad))
elif trig == "c":
    print("Cosine=%.5f" % math.cos(rad))
elif trig == "t":
    print("Tangent=%.5f" % math.tan(rad))
else:
    print("Error in input")