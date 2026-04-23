
# Find-S and Candidate elimination algorithm


# Attribute Names:
# 1. Sky
# 2. AirTemp
# 3. Humidity
# 4. Wind
# 5. Water
# 6. Forecast
# 7. EnjoySport (Target)

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Change', 'Yes']
]

S = ['0'] * (len(data[0]) - 1)   
G = ['?'] * (len(data[0]) - 1)   

print("Initial S:", S)
print("Initial G:", G)
print("-" * 50)

for ex in data:
    attributes = ex[:-1]
    target = ex[-1]

    if target == 'Yes':   
        for i in range(len(S)):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

    else:   
        for i in range(len(G)):
            if G[i] == '?':
                if S[i] != attributes[i]:
                    G[i] = S[i]
                else:
                    G[i] = '?'

    print("S:", S)
    print("G:", G)
    print("-" * 50)

print("Final Specific Hypothesis (S):", S)
print("Final General Hypothesis (G):", G)