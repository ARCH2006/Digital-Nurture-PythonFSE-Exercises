def write_file():
    with open("greeting.txt","w") as file:
        file.write("Hello World")
        
    print("message written successfully")
    
write_file() 