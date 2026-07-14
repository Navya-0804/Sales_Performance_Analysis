# ============================================
# SALES PERFORMANCE ANALYSIS SYSTEM
# Think Champ Data Analytics Internship Project
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("        SALES PERFORMANCE ANALYSIS SYSTEM")
print("="*60)

# -------------------------------
# Create Sample Sales Dataset
# -------------------------------

np.random.seed(42)

products = ["Laptop","Mobile","Keyboard","Mouse","Monitor","Tablet","Headphones","Printer"]
categories = {
    "Laptop":"Electronics",
    "Mobile":"Electronics",
    "Keyboard":"Accessories",
    "Mouse":"Accessories",
    "Monitor":"Electronics",
    "Tablet":"Electronics",
    "Headphones":"Accessories",
    "Printer":"Electronics"
}

dates = pd.date_range("2026-01-01","2026-06-30")

data=[]

for i in range(500):
    product=np.random.choice(products)
    quantity=np.random.randint(1,8)

    if product=="Laptop":
        price=60000
    elif product=="Mobile":
        price=25000
    elif product=="Keyboard":
        price=1500
    elif product=="Mouse":
        price=500
    elif product=="Monitor":
        price=15000
    elif product=="Tablet":
        price=20000
    elif product=="Headphones":
        price=2000
    else:
        price=10000

    sales=quantity*price

    data.append([
        np.random.choice(dates),
        product,
        categories[product],
        quantity,
        sales
    ])

df=pd.DataFrame(data,
columns=["Date","Product","Category","Quantity","Sales"])

df.to_csv("sales_data.csv",index=False)

print("Dataset Created Successfully")
print()

# -------------------------------
# Load Dataset
# -------------------------------

df=pd.read_csv("sales_data.csv")

print("Dataset Shape :",df.shape)
print()

print(df.head())

print()

# -------------------------------
# Data Cleaning
# -------------------------------

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df["Date"]=pd.to_datetime(df["Date"])
df["Month"]=df["Date"].dt.strftime("%B")

print("\nData Cleaned Successfully")

# -------------------------------
# Sales Analysis
# -------------------------------

total_sales=df["Sales"].sum()
total_quantity=df["Quantity"].sum()

print("\nTotal Sales : ₹{:,.0f}".format(total_sales))
print("Total Quantity :",total_quantity)

# -------------------------------
# Top Products
# -------------------------------

top_products=df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\nTop Selling Products")
print(top_products)

# -------------------------------
# Category Sales
# -------------------------------

category_sales=df.groupby("Category")["Sales"].sum()

print("\nCategory Wise Sales")
print(category_sales)

# -------------------------------
# Monthly Sales
# -------------------------------

monthly_sales=df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales")
print(monthly_sales)

# -------------------------------
# Bar Chart
# -------------------------------

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# -------------------------------
# Line Chart
# -------------------------------

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# -------------------------------
# Pie Chart
# -------------------------------

plt.figure(figsize=(7,7))
category_sales.plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.title("Category Wise Sales")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

# -------------------------------
# Generate Report
# -------------------------------

report=f"""
SALES PERFORMANCE ANALYSIS REPORT

=====================================

Total Sales : ₹{total_sales:,.0f}

Total Quantity : {total_quantity}

Top Selling Products

{top_products}

Category Wise Sales

{category_sales}

Monthly Sales

{monthly_sales}

Analysis Completed Successfully.
"""

with open("report.txt","w") as f:
    f.write(report)

print("\nReport Generated Successfully")
print("sales_data.csv saved")
print("bar_chart.png saved")
print("line_chart.png saved")
print("pie_chart.png saved")
print("report.txt saved")

print("\nPROJECT COMPLETED SUCCESSFULLY")
