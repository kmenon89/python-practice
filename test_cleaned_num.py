#test cleaning a number

number="9,22,20,333"
cleaned_number=""

for char in number:
    if char in '0123456789':
        cleaned_number=cleaned_number+char #checks if everytime if it is a number and appends to the number
        #appends since cleaned_number is character hence you get only the number
        print(cleaned_number+"this is char: "+ char)
new_numer=int(cleaned_number)
