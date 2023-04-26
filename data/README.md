# Aggregation of Text documents from the United States Goverment.
# $GOV-ARCHIVE-WEBSITE

# Supreme Court 1937 - 1975
    - $WordCount
# United States Satutes (Congress from 2003 - 2016)
    - $Total:$WordCount
    - $Year:$WordCount

# main.rs takes a .txt file and segments it into 'sets' in redis
# sort-db.py takes set_N where N is the index and the set contains arbitrary text data.
    - sort data into words
    - ignore chars, numbers, and odd cases of 'non' english words.


