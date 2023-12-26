#a ={"name":[], "days":[], "type":[]}

#b = list(a.values())

#a_na = b[0]

#a_da = b[1]

#a_tp = b[2]

#veg = {"name":["beans", "carrot", "potato", "drumstick", "birnjal"],
       #"days":[7, 14, 21, 3, 3],
       #"type":[1, 1, 1, 2, 2]}

#b = list(veg.values())

#na = b[0]

#da = b[1]

#tp = b[2]

#def helper():
  #print(f"vegetable in database {na}")
  #print(f"vegetable you have {a_na}")
  #print("if you don't have more vegetables enter (nothing)")

#while n < 5:
  #try:
    #c = input("Enter the vegetable you have: (h for help) ".lower())
      
    #if c in na: 
      #a["name"].append(c)
      #n += 1

    #elif c == "h":
      #helper()
  
    #elif c == "nothing":
      #n += 6
          
    #else:
      #print("Invalid Vegetable")
      #helper()
      #continue  

  #except:
    #continue

#for i in a:
  #for j in soup:
    #if i == j:

print("Welcome to smart fridge")

l = 0
m = 0
date = 0

soup = {3: ["drumstick"] , 3: ["birnjal"]}

side_dish = {7: ["beans"] , 14: ["carrot"] , 21: ["potato"]}

s_side_dish = dict(sorted(side_dish.items()))
s_soup = dict(sorted(soup.items()))

s = list(s_side_dish.values())
    
g = list(s_soup.values())

for i in range(5): 
  try:
    date += 1

    s_n = s[l]
    g_n = g[m]
    
    print( f"Day {date} side_dish {s_n} soup {g_n} ")
    m += 1
    l += 1

  except IndexError:
    g.append(["null"])
    date -= 1
    


