# Aggregation of Text documents from the United States Goverment.
### [Govinfo Bulk Data Public Repository](https://www.govinfo.gov/bulkdata)

## Supreme Court 1937 - 1975
- This is provided by Govinfo as a .zip containing all in a single file.
- 26538264 Words.

## United States Satutes (Congress from 2003 - 2016)
- Uses Govinfo xml format for each year. 
- $Year:$WordCount

## main.rs takes a .txt file and segments it into 'sets' in redis
- expects a sinlge textfile that has been formatted using append-slash-n.sh script to provide new lines.
- text file will be placed into a sets segmented every 1000 chars.

## sort-db.py takes set_N where N is the index and the set contains arbitrary text data.
- sort data into words and return values WORD:FREQ to a sorted set.
- ignore chars, numbers, and odd cases of 'non' english words.


