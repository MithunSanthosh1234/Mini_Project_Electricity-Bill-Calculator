def domestic(units):
     if(units<=100):
        pay=0
        print("no need to pay")
     elif (units>100 and units<201):
        units=units-100
        pay=units*2.50
        print("You have to pay:Rs.",pay,)
     elif(units>201 and units<501):
         units=units-100
         pay=units*4
         print("You have to pay:Rs.",pay)
     else:
        pay=units*6
        print("You have to pay:Rs.",pay)
    
def commercial(units):
    if(units<=100):
        print("no need to pay")
    elif (units>101 and units<=201):
        units=units-100
        pay=units*4.50
        print("You have to pay:Rs.",pay)
    elif(units>201 and units<=500):
        units=units-100
        pay=units*6
        print("You have to pay:Rs.",pay)
    else:
        units=units-100
        pay=units*7
        print("You have to pay:Rs.",pay)
        
        
def industry(units):
    if(units<=100):
        print("no need to pay")
    elif(units>101 and units<=200):
        units=units-100
        pay=units*6.50
        print("You have to pay:",pay)
    elif(units>201 ana units<=500):
        units=units-100
        pay=units*8
    else:
        units=units-100
        pay=units*8.50
        print("You have to pay:",pay)

print ("Select your Locality")
print("1.Domestic")
print("2.Commerical ")
print("3.Industry")

choice=int(input("Enter your choice"))

if (choice==1):
    print("Domestic")
    units=int(input("Enter your units"))
    domestic(units)
elif (choice==2):
    print("Commercial")
    units=int(input("Enter your units"))
    commercial(units)

elif (choice==3):
    print("Industry")
    units=int(input("Enter your units"))
    industry(units)

