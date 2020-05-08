def my_gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a < b:
        (a, b) = (b, a) #(큰수, 작은수) 형태로
        print("(a, b):", (a, b))
    while b != 0:
        print("(a, b) = (b, a%b) : ", (a, b), "=", (b, a%b))
        (a, b) = (b, a%b)
    return a

print(my_gcd(12, 16))