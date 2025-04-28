import pandas as pd
import time

star_time = time.time()

df = pd.read_csv('2019-Nov.csv.zip', compression='zip')

end_time = time.time()

execution_time = end_time - star_time

print(f"execution time with method compression is : {execution_time}")

print(df.head(5))


# ########################################################### DASK


import dask.dataframe as dd

star_time = time.time()

df = dd.read_csv("2019-Nov.csv")

end_time = time.time()

execution_time = end_time - star_time

print(f"execution time with method Dask is : {execution_time}")

column_count = df.shape[1]
print(f"Number Column : {column_count}")

row_count = df.shape[0].compute()
print(f"Number Rows : {row_count}")

print(df.head(10)) 

# Filtered Column price Wihtin price < 1

filtered_df = df[df["price"] < 1]
print(filtered_df.head())

filtered_df.to_csv("filtered_data_dask.csv", single_file=True)





# ################################# chunk_size

import pandas as pd

star_time = time.time()

 
chunk_size = 100000 

for chunk in pd.read_csv("2019-Nov.csv", chunksize=chunk_size):
    pass
    # print(chunk.shape) 
    # print(chunk.head())

end_time = time.time()

execution_time = end_time - star_time

print(f"execution time with method chunksize is : {execution_time}")


# SUM TOTAME PRICES 

total_prices = 0 

for chunk in pd.read_csv("2019-Nov.csv", chunksize=chunk_size):
    total_prices += chunk["price"].sum() 

print(f"Total prices: {total_prices}") 


# Filtered Column price Wihtin price < 1


for chunk in pd.read_csv("2019-Nov.csv", chunksize=chunk_size):
    filtered_chunk = chunk[chunk["price"] < 1] 
    filtered_chunk.to_csv("filtered_data.csv", mode='a', index=True)




################################# CLEAN DATA with chunk_size



# import pandas as pd
# import time

# star_time = time.time()

 
# chunk_size = 100000 

# for chunk in pd.read_csv("2019-Nov.csv", chunksize=chunk_size):
#     chunk.dropna(inplace = True)
#     chunk.drop_duplicates(inplace = True)
#     chunk.to_csv("clean_data.csv", mode='a', index=False)

# end_time = time.time()

# execution_time = end_time - star_time

# print(f"execution time with method compression is : {execution_time}")