
#   square pattern
n = 4

for i in range(1,n+1):
    stars= ""
    for j in range(1,n+1):
        stars +="* "
    print(stars)

#   rectangle pattern
n = 3
m = 6

for i in range(1,n+1):
    stars = ""
    for j in range(1,m+1):
        stars+="* "
    print(stars)

# left angle triangle using both varibale 
n = 6


for i in range(1,n+1):
    stars = ""
    for j in range(1,n*2+1):
        stars+="* "
    print(stars)

# left angle triangle using one varibale 

n = 6 

for i in range(1,n+1):
    stars = ""
    for j in range(1,i+1):
        stars +="* "
    print(stars)













