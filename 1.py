# Dataset
# Central tendency of 6 types of data 
data = {
    "Nominal": ["Male", "Female", "Male"],
    "Ordinal": ["A", "B", "A"],
    "Discrete": [2, 4, 6],
    "Continuous": [160.5, 165.2, 170.1],
    "Interval": [36.5, 37.0, 38.2],
    "Ratio": [18, 19, 20]
}
# Functions
def mean(d): return sum(d)/len(d)

def median(d):
    d = sorted(d); n = len(d); m = n//2
    return d[m] if n%2 else (d[m-1]+d[m])/2 

def mode(d): return max(set(d), key=d.count)

def var(d):
    m = mean(d)
    return sum((x-m)**2 for x in d)/(len(d)-1)

def sd(d): return var(d)**0.5

# Applying formulas
for k, v in data.items():
    print("\n", k, "Data")

    if k == "Nominal":
        print("Mode:", mode(v))

    elif k == "Ordinal":
        print("Median:", median(v))
        print("Mode:", mode(v))

    else:
        print("Mean:", mean(v))
        print("Median:", median(v))
        print("Mode:", mode(v))
        print("Variance:", var(v))
        print("SD:", sd(v))