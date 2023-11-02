def str(x):
    return float(x)
try:
    print(float("1"))
except ValueError:
    print("Could not convert the string to a float")
    
