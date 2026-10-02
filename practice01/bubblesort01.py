print("Hello, world!, 29 September morning session")
list_to_be_sorted = [16,51,19,2,94,38,9,8,53,51,26,44,51,11,41,48,2,71,65,74,85,52,65,9,69,65,40,85,92,18,4,24,87,38,13,5,72,16,27,35,14,10,31,6,21,71,73,7,14,62,66,31,54,51,10,74,42,88,24,11,23,70,3,53,60,81,73,59,82,21,12,28,43,16,62,24,51,87,69,91,3,46,53,12,38,99,23,72,94,69,41,85,62,85,21,73,68,52,33,21,28,19]
def sort1 (list_of_numbers):
    for n in range(0, len(list_of_numbers)):
        for i in range(0, (len(list_of_numbers)-1)):
            if list_of_numbers[i] >list_of_numbers[i+1]:
                continue 
            else:
                temp =list_of_numbers[i]
                list_of_numbers[i] = list_of_numbers[i+1]
                list_of_numbers[i+1] = temp
                temp=0
    print("sorting completed")
    print(list_of_numbers)
sort1(list_to_be_sorted)
        
            