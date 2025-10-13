#Given two large datasets representing different product inventories from two warehouses, write a function to find the products available in both inventories.
#Author - Vedika Udgir

set1 = {"laptop", "mouse", "keyboard", "monitor"}
set2 = {"tablet", "mouse", "keyboard", "smartphone"}

common = set1 & set2
print(common)