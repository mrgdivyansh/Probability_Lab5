ata = {0: 3,1: 8,2: 12,3: 15,4: 9,5: 3}
#Mean
mean = sum(x * freq for x, freq in data.items()) / sum(data.values())

#Variance
variance = sum((x - mean) ** 2 * freq for x, freq in data.items()) / sum(data.values())

print(f"Mean (Expected Value): {mean:.2f}")
print(f"Variance: {variance:.2f}")