#Dictionary Code Challenge {}
#Places to visit
#convert 2 separate lists to dictionary

test_keys = ["Costa Rica", "Hawaii", "India", "Europe", "Bali"]
test_values = [1, 2, 3, 4, 5]
  
# Printing original keys-value lists
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))
  
# using naive method
# to convert lists to dictionary
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break  
  
# Favorite places to visit 
print ("Favorite places to visit : " +  str(res))
