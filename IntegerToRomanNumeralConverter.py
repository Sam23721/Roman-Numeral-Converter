Y = 1

while Y == 1: #This is the part of the code that keeps it looping until the user decides to stop
    
    num = int(input("Enter a number between 1 and 100000:")) #This allows the user to input their own number, and lets them know the boundries

    def int_to_roman(num):
        numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000,4000,5000,9000,10000,40000,50000,90000,100000] #These are all of the numbers required to make up all of the combinations between 1 and 100000
        roman = ["I" , "IV" , "V" , "IX" , "X" , "XL" , "L" , "XC" , "C" , "CD" , "D" , "CM" , "M" , "(IV)" , "(V)" , "(IX)" , "(X)" , "(XL)" , "(L)" , "(XC)" , "(C)"] #This is the roman numeral list, they are stored in the same numerical value order as the numbers list

        x = 20 #This is the total number of different integers that are in the list. There is 21 in total, but the count starts from 0 rather than 1
        roman_numeral = "" #THis is what makes sure the final output is a string

        while num != 0:    # This part of the code will loop round until the total of the inputed number reaches 0. It will start at the far right of the list of numbers (which is equal to x = 20) and will go through all of them until the value of the number reaches 0
            if numbers[x] <= num:
                roman_numeral += roman[x]
                num = num - numbers[x]
            else:
                x -= 1
        return roman_numeral

    print(int_to_roman(num)) #This is the print that will display the roman numeral version of the number after it has been converted

    cont = str(input("Do you want to enter another number? Y or N")) #This part asks the user if they want to input another number or stop the code. If the user types N, the code will break which will stop the program from continuing to run, where as if they type Y, the program will loop back round to the top.
    if cont == "N":
        break
        print("The program has now stopped.")
    else:
        continue
