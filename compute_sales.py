"""Module to compute the total cost for all sales"""

import sys
import json
import time

start = time.time()

# READ DATA FROM BOTH JSON FILES
with open(sys.argv[1], "r", encoding="utf-8") as json1, open(
    sys.argv[2], "r", encoding="utf-8"
) as json2:
    product_list = json.load(json1)
    sales_list = json.load(json2)

# COMPUTE TOTAL COST (PRICE * QUANTITY)
res = []

for sale in sales_list:
    for product in product_list:
        if sale["Product"] == product["title"]:
            op = sale["Quantity"] * product["price"]
            res.append(op)

sum_sales = sum(res)
print("TOTAL: " + str(sum_sales))

# WRITE A TXT FILE
with open("sales_results.txt", "w", encoding="utf-8") as file1:
    file1.write("TOTAL: " + str(sum_sales) + "\n")
    end = time.time()
    file1.write("TIME ELAPSED: " + str(end - start))
    file1.close()

print("TIME ELAPSED: " + str(end - start))
