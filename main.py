"""
if...elif...else
| - Python uses indentation to define blocks of code
| - If blocks sometimes referred to as control blocks allow your programs to handle different scenarios -- essentially giving your programs the ability to make decisions. 
"""
# to run any example remove the hashtags
#if True:
#    print("Do this")
#print("Do this even if false")

#customer = input("What kind of customer are you? ")
#if customer == "new":
#    print ("Here is a coupon")
#print("Show this to all customers")

#is_true = input("Is it true? ")
#if is_true == "yes":
#    print("I am going to do this")
#else:
#    print("I am going to do that")    

choice = input("What is your choice? ")
if choice == "rock":
    print("you chose rock")
elif choice == "paper":
    print("you chose paper")
elif choice == "scissors":
    print("you chose scissors")
else:
    print("That choice is invalid")

# test conditions <, > <=, >=, !=                
    