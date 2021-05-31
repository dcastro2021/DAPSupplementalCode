#Create a string, a list, a dictionary
#1. Declare the data manually

print ("What countries do you want to visit?")
Countries = ["Hawaii", "Europe", "India", "Costa Rica"]
for x in Countries:
    print(x)

#2. Use a loop to declare the data

for x in "Hawaii":
    print(x)

#3Create a function that turns 3 strings into a list

def Convert(string):
    li = list(string.split (" "))
    return li

str1 = "Tacos are awesome"
print(Convert(str1))


#4Create a dictionary from 2 lists

lsta = [1, 5, 10, 20, 50, 100]
lstb = ["Washington", "Lincoln", "Hamilton", "Jackson", "Grant", "Franklin"]

dictb = {}

for x in range(3):
        dictb[lsta[x]] = lstb[x]
print(dictb)

  
#5 Printing original keys-value lists

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

#Create a dictionary using loops

Presidents = {'Washington' :1, 'Lincoln' :5, 'Hamilton' :10, 'Jackson' :20, 'Grant' :50, 'Franklin' :100}

Presidents_list = []

for Presidents, quantity in Presidents.items():
    Presidents_list.append([Presidents]*quantity)

    print(Presidents_list)   
    
#Import a .txt file. Iteratate through the data, creating a list of all strings that start with "S". Print the list.



#Use 3 inputs, send the strings to a function, have the function return a list of the inputs

#Create a code that has 2 functions. Have one call the other as part of the code.
