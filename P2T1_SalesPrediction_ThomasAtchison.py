# P2T1_SalesPrediction_ThomasAtchison.py
# 11 Sep 2018
# CTI-110 P2T1 - Sales Prediction
# Tom Atchison

# get projected total sales.
total_sales = float (input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit.
print ('the profit is $', format(profit, ',.2f'))
