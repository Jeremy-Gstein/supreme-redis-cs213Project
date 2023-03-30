import redis
import time

# Connect to Redis (Input later, leave in code for now.)
r = redis.Redis(host='localhost', port=6379, db=0)

# Get all set keys starting with 'sets_'
# Redis Data is stored as arbirarty len sentences of text.
# Need to get ALL sets (set_N) / set_1, set_2..etc.
set_keys = r.keys('set_*') # Currently takes ~40 seconds to enummerate all existing set keys.

# Combine all sets into a single union set (with scores)
union_set = r.sunion(set_keys)
print('[+] Connected to Redis, Generating Set List...')
# Get Numbers, concat to single string and add to list below.
removeNumbers = ''
for num in range(10):
    removeNumbers += str(num)
# Sort the union set by splitting each value into individual words
charsToRemove = ['.', ',', '!', '?','"','_','$','#','@','%','^','&','*','(',')','[',']',';', ':',"'",'-','/','>','<','`',removeNumbers, ]
print(charsToRemove)
removeChars = "".join(charsToRemove).encode('utf-8') 
# Concat list of chars to remove and save to str var. Store as a bytes object in utf-8 format.
# Create a List to store individual unique words.
# Normilize all chars to lowercase and remove unwanted chars before appending to list.
print("[+] Creating Sorted Set")
sorted_set = []
for value in union_set:
    words = value.split()
    for word in words:
        trimedWord = word.translate(None, removeChars) #Arg needs to be bytes value
        sorted_set.append(trimedWord.lower())
sorted_set.sort()

print('[+] Creating Frequency Dict.')
# Create a Dict to store Word: Freq. 
freq_dict = {}
for word in sorted_set:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

# Create 2 itterators. Word will be key and freq is value. (Member and Score for sorted_set)
for word, freq in freq_dict.items():
    r.zadd('word_freq', {word: freq})

# word_freq = r.zrange('word_freq', 0, -1, withscores=True)

# Temp work around for None type value.
r.zrem('word_freq', b'')

# <---Testing--->
'''
for word, freq in word_freq:
    print(f'{word}: {freq}')
'''


# todo: REMOVE OR FIX 
'''
timer_total = 0.0
# init timer (end rest)
start_time = time.time()


# Function for a timer for testing.
# Global var is 'timer_total' this keeps track of time. (start_timer = time.time() is needed outside scope)
# Get the current time and subtract start (0.0) and total ()
def end_t():
global timer_total
endTime = time.time()
timer_total = endTime - start_time - timer_total
print(f"Elapsed Time Since Last Call: { round(timer_total, 5) } ")
'''

