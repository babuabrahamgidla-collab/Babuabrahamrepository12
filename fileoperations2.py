print("Hello, world!, 26 September")

try:
    
    with open("C:\\Users\\babua\\PycharmProjects\\pythonproject02\\books.txt", "r") as f:
        line_is_not_blank=True 
        while line_is_not_blank:
            line_as_read = f.readline()
            if not line_as_read: 
                line_is_not_blank = False  
            else:
                print(line_as_read.strip())
                
except Exception as e:
    print(f"File is not found: {e}")
print("___________________________________________________________________________________")
    
try:
    with open("C:\\Users\\babua\\PycharmProjects\\pythonproject02\\books.txt", "r") as f:
        for line in f:
            print(line.strip())
        
             
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
    
    



