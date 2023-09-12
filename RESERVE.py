
## The Project's Code (احجز) ##


#Part_1


def Create_New_Email ():
    print ("""
Sign In
           """)
    First_Name = input ("First Name: ")
    input ("Last Name: ")
    input ("E-mail: ")
    Password = input ("Password: ")
    Confirmation = input ("Confirm Password: ")

    Attempts = 0
    Max_Attempts = 3

    if Confirmation == Password:
        print (f"""
Welcome {First_Name}""")
    while Confirmation != Password and Attempts < Max_Attempts:
        if Confirmation != Password:
            print ("Incorrect Password")
            Confirmation = input ("Confirm Password: ")
            Attempts += 1
        if Confirmation != Password and Attempts == Max_Attempts:
            print ("""
ERROR 408
""")
            exit ()
        if Confirmation == Password:
            print (f"""
Welcome {First_Name}""")
        

Create_New_Email ()


#Part_2


def Destination_Cost (Country):
    if Country == "Kuwait":
        return 50
    elif Country == "KSA":
        return 80
    elif Country == "UAE":
        return 75
    elif Country == "Bahrain":
        return 60
    elif Country == "Qatar":
        return 60.5
    elif Country == "Oman":
        return 55.25
    elif Country == "Yemen":
        return 40


#Part_3


def Airways_Cost (Airways):
    if Airways == "Kuwait Airways":
        return 25
    if Airways == "Fly Emirates":
        return 35
    if Airways == "Jazeera":
        return 20
    if Airways == "Saudi Arabian Airways":
        return 30.5
    if Airways == "Qatar Airways":
        return 25.5
    if Airways == "fly Dubai":
        return 30


#Part_4


def Duration_Cost (Time):
    return int (Time * 5)


#Part_5


def Ticket_Cost ():
    Country = input ("Where do you want to travel? ")
    Airways = input ("By which airways do you want to travel? ")
    Time = int (input ("How long do you want to stay? "))
    
    Total_cost = Destination_Cost (Country) + Airways_Cost (Airways) + Duration_Cost (Time)
    
    print (f"""
           Destination: {Country}
           Airways: {Airways}
           Duration: {Time}
           """)
    return Total_cost

Total_price = Ticket_Cost ()

print (f"Your total price is: {Total_price} KD.")


#Part_6


def Knet_Pay ():
    Cancel = input ("Do you want to cancel? ")
    if Cancel == "Yes":
        print (Ticket_Cost ())
    if Cancel == "No": 
        Bank = input ("Bank's Name: ")
        Card_Number = input ("ATM Card's Number: ")
        Expire = input ("Card's Expire: ")
        Password = input ("Card's Password: ")
        print (f"""
Bank: {Bank}
ATM Card's Number: {Card_Number}
Card's Expire: {Expire}
Password: {Password} """)
        print ("""
HAVE A NICE JOURNEY!
          """) 
  
Knet_Pay ()