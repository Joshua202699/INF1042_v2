mots = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}
for m in mots:
    freq[m] = freq.get(m, 0) + 1
print(freq)  # {'apple': 3, 'banana': 2, 'orange': 1}

# Trouver le mot le plus fréquent
plus_freq = max(freq, key=freq.get)
print("Plus fréquent:", plus_freq)
