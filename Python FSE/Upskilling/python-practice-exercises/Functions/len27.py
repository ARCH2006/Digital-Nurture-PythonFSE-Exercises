def length(text):
    if text == "":
        print(" String cannot be empty")
        return 
    length = len(text)
    print(f"Length: {length}")
    
text = "Python"
length(text)