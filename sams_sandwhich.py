#sams sandwhich task
import datetime
#creating a function that forces a users name
def force_name(message,lower,upper):
    while True: #this is an infinite loop    
        name=str(input(message)).title() #asking the user for name and adding capital letter
        if len(name)>=lower and len(name)<=upper and name.isalpha():# Checking for range and invalids
            break   # breaks the loop
        else:   # if the name doesnt fit the requirments it will not work
                print("Invalid name")
    return name #outputs a valid name

#This function will ensure the user can only enter in a valid number within a range

def force_number(message,lower,upper):
    while True:  # Forces the user to enter a valid number
        try:
            num=int(input(message))  # Convert input to an integer
            if num>=lower and num<=upper:  # Check if number is within the valid range
                break  # Valid number, exit loop
            else:
                print('Please enter a valid number, thanks.')
        except ValueError:  # This will pick up any errors if an integer was not entered
            print('Error - only type in numbers please.')
    return num


def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list):
        print(count+1," ", bread_list[count])
        count += 1
    bread_selected=int(input("which bread did you want? Enter a number: "))
    return bread_list[bread_selected-1]

def meat_selection():
    meat_list = ["Chicken", "Pork", "Beef", "Meatballs", "Duck"]
    count=0
    print("We have the following meats:")
    while count < len(meat_list):
        print(count+1," ", meat_list[count])
        count += 1
    meat_selected=int(input("which meat did you want? Enter a number: "))
    return meat_list[meat_selected-1]

def cheese_selection():
    cheese_list = ["Cheddar", "Mozzerella", "Swiss", "American", "Blue"]
    count=0
    print("We have the following cheeses:")
    while count < len(cheese_list):
        print(count+1," ", cheese_list[count])
        count += 1
    cheese_selected=int(input("which cheese did you want? Enter a number: "))
    return cheese_list[cheese_selected-1]

def dressing_selection():
    dressing_list = ["Mayonaise", "Ranch", "Mustard", "Butter", "Pesto"]
    count=0
    print("We have the following dressings:")
    while count < len(dressing_list):
        print(count+1," ", dressing_list[count])
        count += 1
    dressing_selected=int(input("which dressing did you want? Enter a number: "))
    return dressing_list[dressing_selected-1]

def salads_selection():
    salad_list = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    count=0
    print("We have the following salds, you can have as many as you want")
    while count <len(salad_list):
        print(count," ",salad_list[count])
        count +=1
    print("Press ENTER when you have finished choosing your salads")
    salads_added = "" #will hold a string of more than one item
    selected_salad= " " #prompts the user to enter a number in to select a salad

    while selected_salad != "":#if enter is not pressed it will keep prompting the user to select a salad
        selected_salad= input(f"What number salad do you want?\nYou have selected: {salads_added}")
        if selected_salad != "": #if you press enter this if statement won't run
            selected_salad= int(selected_salad)
            #this variable keeps adding on each selected item from salad list
            salads_added = salads_added + " " + salad_list[selected_salad-1]
    return salads_added.strip() #removes empty space at start of the string

def output_textfile(first_name,phone_number,sandwhich_order):
    date_time=datetime.datetime.now()
    outFile=open("sams_sandwhich.txt","a") #opening up a new text file
    print(f"\n***Order for {first_name} - {phone_number}:***")
    outFile.write(f"\nDate of booking: {date_time}")
    for item in sandwhich_order:
        print (item)
        outFile.write(f"\n End of order: {date_time}")
    print(f"***End of order : {date_time} ***")
    outFile.write("\n")
    outFile.write("\n")
    outFile.close()#closes of the text file
    #once the file prints, it goes back to the menu 




#main program
today=datetime.datetime.now()
print("Welcome to Sam's Sandwhich Shop")
first_name=force_name("Please enter in your first name: ",2,15)
phone_number=force_number("Please enter your phone number: ",0,999999999999999)
bread_choice=bread_selection() #creating a variable that calls up  the bread function and returns their choice
meat_choice=meat_selection() #creating a variable that calls up  the meat function and returns their choice
cheese_choice=cheese_selection() #creating a variable that calls up  the cheese function and returns their choice
dressing_choice=dressing_selection() #creating a variable that calls up  the cheese function and returns their choice
salad_choice=salads_selection()
sandwhich_order=[]
#adding selected items to a list
sandwhich_order.append(first_name)
sandwhich_order.append(phone_number)
sandwhich_order.append(f'''Your selected bread: {bread_choice}''')
sandwhich_order.append(f'''Your selected meat: {meat_choice}''')
sandwhich_order.append(f'''Your selected cheese: {cheese_choice}''')
sandwhich_order.append(f'''Your selected dressing: {dressing_choice}''')
sandwhich_order.append(f'''Your selected salads: {salad_choice}''')
output_textfile(first_name,phone_number,sandwhich_order)