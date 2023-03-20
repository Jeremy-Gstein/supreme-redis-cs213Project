import redis
import time

start_time = 0.0

def get_t():
    global start_time
    start_time = time.time()
def end_t():
    endTime = time.time()
    total = endTime - start_time
    print(f"Elapsed time: {total}")
get_t()
# Connect to Redis (Input later, leave in code for now.)
r = redis.Redis(host='10.0.0.22', port=6379, db=0)

# Get all set keys starting with 'sets_'
# Redis Data is stored as arbirarty len sentences of text.
# Need to get ALL sets (set_N) / set_1, set_2..etc.
set_keys = r.keys('set_*') # Currently takes ~40 seconds to enummerate all existing set keys.
end_t()
get_t()
# Combine all sets into a single union set (with scores)
union_set = r.sunion(set_keys)
end_t()
get_t()
# Get Numbers, concat to single string and add to list below.
removeNumbers = ''
for num in range(10):
    removeNumbers += str(num)
# Sort the union set by splitting each value into individual words
charsToRemove = ['.', ',', '!', '?','"','_','$','#','@','%','^','&','*','(',')','[',']',';', ':',"'",'-','/','>','<','`',removeNumbers, ]
removeChars = "".join(charsToRemove).encode('utf-8') 
end_t()
get_t()
# Concat list of chars to remove and save to str var. Store as a bytes object in utf-8 format.
# Create a List to store individual unique words.
# Normilize all chars to lowercase and remove unwanted chars before appending to list.
sorted_set = []
for value in union_set:
    words = value.split()
    for word in words:
        trimedWord = word.translate(None, removeChars) #Arg needs to be bytes value
        sorted_set.append(trimedWord.lower())
sorted_set.sort()
end_t()
get_t()
# Create a Dict to store Word: Freq. 
freq_dict = {}
for word in sorted_set:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1
end_t()
get_t()
# Create 2 itterators. Word will be key and freq is value. (Member and Score for sorted_set)
for word, freq in freq_dict.items():
    r.zadd('word_freq', {word: freq})
end_t()
get_t()
word_freq = r.zrange('word_freq', 0, -1, withscores=True)
end_t()
get_t()
# Temp work around for None type value.
r.rem('word_freq', b'')
end_t()
# <---Testing--->
'''
for word, freq in word_freq:
    print(f'{word}: {freq}')
'''




















