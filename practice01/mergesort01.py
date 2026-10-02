print("Hello, world!, 29 September, evening session")
list_for_mergesort=[12, 13, 43,62, 24, 51, 87, 69, 91, 3, 46, 53, 38, 99, 23, 72, 41, 85,21, 73, 68, 52, 33, 28, 16,19, 2, 94, 39]

def mergesort(list_for_sorting):
    list1=[]
    list2=[]
    combined_list =[]
    n=(len(list_for_sorting))
    m=0
    
    
    if len(list_for_sorting)%2==0:
        list1 = list_for_sorting[:int((n/2))]
        list2 = list_for_sorting[int(n/2):]
        list1.sort()
        list2.sort()
    else:
        m=int(n+1)
        list1 = list_for_sorting[:int((m/2))]
        list2 = list_for_sorting[int(m/2):]
        list1.sort()
        list2.sort()    
        i=0
    for i in range(1, len(list_for_sorting)):
        if len(list1)>0 and len(list2)>0:        
            if list1[0]<list2[0]:
                combined_list.append(list1[0])
                list1.pop(0)
            else:
                combined_list.append(list2[0])
                list2.pop(0)          
    return combined_list, len(list1), len(list2)
    
sorted_list = mergesort(list_for_mergesort) 
print(sorted_list)

        