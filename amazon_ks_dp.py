import pandas as pd
import time
start_time = time.perf_counter()

dataframe = pd.read_excel('data.xlsx')
dataframe.Discount = dataframe.Discount.astype(int)
dataframe.Discounted_Price = dataframe.Discounted_Price.astype(int)

print('\nHere is the list of 30 items to select with $1000 budget and max discount:\n') 
print(dataframe)

discount = list(dataframe['Discount'])
price = list(dataframe['Discounted_Price'])
capital = 1000


col = capital + 1 # total columns in knapsack array including capital = 0
row = len (discount) # total no of rows in knapsack array for total items

amazon_ks_arr = [[0 for x in range (col)] for y in range (row)] #knapsack array
#print (amazon_ks_arr)


for item in range (row):
    for budget in range (col):

        if price[item] > budget:
            amazon_ks_arr[item][budget] = amazon_ks_arr[item-1][budget]
            continue

        previous_best_discount = amazon_ks_arr[item-1][budget]
        
        new_best_discount = discount[item] + amazon_ks_arr[item-1][budget- price[item]]
        
        amazon_ks_arr[item][budget] = max(previous_best_discount, new_best_discount)

amazon_knapsack_discount_solution = []
for row in amazon_ks_arr:
    for col in row:
        amazon_knapsack_discount_solution.append(col)
max_discount = max(amazon_knapsack_discount_solution)
print ('\nFrom knapsack-DP algorithm, maximum discount is: $',max_discount)

knapsack_table = pd.DataFrame(amazon_ks_arr)
print ('\nFollowing is the Knapsack table formed using DP:\n')
print (knapsack_table)

choosen_items = []
j = capital
for i in range (len(discount)-1,0,-1):
    if amazon_ks_arr[i][j] != amazon_ks_arr[i-1][j]:
        choosen_items.insert(0,i)
        j -= price[i]
total_items = len(choosen_items)
print ('\nTotal number of items to buy for max discount is:',total_items)
print ('\nAnd we need to buy items with following indices:',choosen_items)

dataframe_final = dataframe.iloc[choosen_items]

pricelist = list (dataframe_final['Discounted_Price'])
total_price = 0
for object in pricelist:
    total_price += object
print ('\nTotal money used from budget of $1000 in purchase is: $',total_price)

print('\n')
print('Following is the table of purchase decision:\n')
print(dataframe_final)

time_taken = (time.perf_counter() - start_time)
print ('\nTotal time taken on execution is %5.2f secs'%time_taken)
