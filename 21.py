data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]


hy = None

for ex in data:
    if ex[-1] == 'Yes':   
        if hy is None:
            hy = ex[:-1]
        else:
            for i in range(len(hy)):
                if hy[i] != ex[i]:
                    hy[i] = '?'   

print("Final Hypothesis:")
print(hy)