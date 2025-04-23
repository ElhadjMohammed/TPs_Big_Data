import pandas as pd
import time

star_time = time.time()

chunk_size = 100000 

for chunk in pd.read_csv("2019-Nov.csv", chunksize=chunk_size):
    chunk.dropna(inplace = True)
    chunk.drop_duplicates(inplace = True)
    chunk.to_csv("clean_data.csv", mode='a', index=False)

end_time = time.time()

execution_time = end_time - star_time

print(f"execution time with method compression is : {execution_time}")