import redis

# Connect to Redis
r = redis.Redis(host='10.0.0.40', port=6379, db=0)

# Get all set keys starting with 'sets_'
set_keys = r.keys('set_*')

# Combine all sets into a single union set
union_set = r.sunion(set_keys)

# Sort the union set by splitting each value into individual words
charsToRemove = ['.', ',', '!', '?' ]
sorted_set = []
for value in union_set:
    words = value.split()
    for word in words:
        trimedWord = word.translate(None, b".,!?")
        sorted_set.append(trimedWord.lower())
sorted_set.sort()

freq_dict = {}
for word in sorted_set:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

for word, freq in freq_dict.items():
    r.zadd('word_freq', {word: freq})

word_freq = r.zrange('word_freq', 0, -1, withscores=True)
for word, freq in word_freq:
    print(f'{word}: {freq}')

