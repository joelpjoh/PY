a = input("Enter the string:")

if len(a) >= 3:
    if a.endswith("ing"):
        a = a[:-3] + "ly"
    else:
            a = a+ "ing"
print(a)
