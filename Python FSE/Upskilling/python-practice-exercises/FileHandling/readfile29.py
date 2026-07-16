def read_File():
    try:
        with open("greeting.txt","r") as file:
            content = file.read()
            
        print(content)
    except FileNotFoundError:
        print("File not found")
    
read_File()