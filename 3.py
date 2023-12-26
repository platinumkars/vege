print("Welcome to smart fridge")

# This loop will go on until the budget is integer or float
while True: 
	try:
		num = float(input("Enter the number of vegetables you have : "))
		# if budget is integer or float it will be stored 
		# temporarily in variable 's'
		s = num 
	except ValueError:
		print("ENTER ONLY NUMBERS")
		continue
	else:
		break

# dictionary to store product("name"), quantity("quant"), 
# price("price") with empty list as their values
a ={"name":[], "days":[]}
c ={"name":[], "days":[]}

# converting dictionary to list for further updation
b = list(a.values())

# variable na value of "name" from dictionary 'a'
na = b[0]

# variable qu value of "quant" from dictionary 'a'
da = b[1]

# converting dictionary to list for further updation
d = list(c.values())

# variable na value of "name" from dictionary 'a'
na = d[0]

# variable qu value of "quant" from dictionary 'a'
da = d[1]

# This loop terminates when user select 2.EXIT option when asked
# in try it will ask user for an option as an integer (1 or 2) 
# if correct then proceed else continue asking options
while True:
	try:
		ch = int(input("1.ADD\n2.EXIT\nEnter your choice : "))
	except ValueError:
		print("\nERROR: Choose only digits from the given option")
		continue
	else:
		# check the budget is greater than zero and option selected
		# by user is 1 i.e. to add an item
		if ch == 1 and s>0:	 

			# input products name			 
			pn = input("Enter vegetable name : ") 
			# input quantity of product
			q = input("Enter quantity : ")

			# checks if product name already in list
			if pn in na: 
				# find the index of that product
				ind = na.index(pn) 

				# remove quantity from "quant" index of the product
				da.remove(da[ind])  

				# insert new value given by user earlier
				da.insert(ind, q)  
			else:
				# append value of in "name", "quantity", "price"
				na.append(pn) 

				# as na = b[0] it will append all the value in the
				# list eg: "name":["rice"]
				da.append(q)

l = 0
m = 0
date = 0

# print final grocery list
for i in range(s): 
  try:
    date += 1

    s_n = s[l][0]
    g_n = g[m][0]
    
    print( f"|Day {date} | side_dish {s_n} | soup {g_n} |")
    m += 1
    l += 1

  except IndexError:
    g.append(["null"])
    date -= 1