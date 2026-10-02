print("Hello, world!, 29 September, afternoon session")
list_for_quick_sort = [16,51,19,2,94,38,9,8,53,51,26,44,51,11,41,48,2,71,65,74,85,52,65,9,69,65,40,85,92,18,4,24,87,38,13,5,72,16,27,35,14,10,31,6,21,71,73,7,14,62,66,31,54,51,10,74,42,88,24,11,23,7,3,53,60,81,73,59,82,21,12,28,43,16,62,24,51,87,69,91,3,46,53,12,38,99,23,72,94,69,41,85,62,85,21,73,68,52,33,21,28,19]
mylist = [1,5,8,2,7,9,3,2,9]
def myquicksort(input_list): 
    if len(input_list)<2:
        return input_list
       
    pivot = input_list[0]
    smaller=[]
    larger = []
    for num in input_list[1:]:
        if num<pivot:
            smaller.append(num)
        else:    
            larger.append(num)            
                      
    return myquicksort(smaller) +  [pivot]+ myquicksort(larger) 
  
print("did the function code go well")
print(myquicksort(mylist))
    