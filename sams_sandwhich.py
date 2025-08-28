#sams sandwhich task
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
        selected_salad= input(F"What number salad do you want?\nYou have selected: {salads_added}")
        if selected_salad != "": #if you press enter this if statement won't run
            selected_salad= int(selected_salad)
            #this variable keeps adding on each selected item from salad list
            salads_added =salads_added + " " + salad_list[selected_salad]
    return salads_added.strip() #removes empty space at start of the string



#main program
print("Welcome to Sam's Sandwhich Shop")
bread_choice=bread_selection() #creating a variable that calls up  the bread function and returns their choice
meat_choice=meat_selection() #creating a variable that calls up  the meat function and returns their choice
cheese_choice=cheese_selection() #creating a variable that calls up  the cheese function and returns their choice
dressing_choice=dressing_selection() #creating a variable that calls up  the cheese function and returns their choice
salad_choice=salads_selection()
print(f'''
Your selected bread: {bread_choice}
Your selected meat: {meat_choice}
Your selected cheese: {cheese_choice}
Your selected dressing: {dressing_choice}
Your selected salads: {salad_choice}''')