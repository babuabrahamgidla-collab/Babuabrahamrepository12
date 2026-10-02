print("Hello, world!, 30 September afternoon session")
def palindrome_check(input_string):
    my_input_string = input_string
    my_input_string_as_list= list(my_input_string)
    reversed_string_list=[]
    for char in my_input_string_as_list[::-1]:
        reversed_string_list.append(char)
    if my_input_string_as_list == reversed_string_list:
        print("The input string is a palindrome")
    else:
        print("The input string is not a palindrome")
#palindrome_check("abcdefgfedcba")
def num_to_list_reverse(number):
    inputnumber = number
    counter=0
    present_number = 0
    reversed_list1=[]
    while not inputnumber//10<1:
        reminder = inputnumber%10
        reversed_list1.append(reminder)
        counter =counter+1
        inputnumber=inputnumber//10
    addme= inputnumber%(10**(counter))
    reversed_list1.append(addme)    
    return reversed_list1
def list_to_number(inputlist):
    list1=inputlist    
    
    i=1
    number = 0
    for digit in list1:
        number = number + digit*(10**(len(list1)-i))
        i=i+1
    return number  

def num_palindrome_check(given_number):
    reversed_number_list = num_to_list_reverse(given_number)
    reversed_number= list_to_number(reversed_number_list)
    print("The given number is ", given_number)
    print("The reversed number is ", reversed_number)
    if given_number == reversed_number:
        print("The given number is a palindrome")
    else:
        print("The given number is not a palindrome")    
num_palindrome_check(1234321)
    
    

