#Arnav Vasa
#CS175L
#Average From Input File v2

#The program reads and displays the contents of the numbers.txt file.
def main():

    # call the function
    avgerrorcheck()

def avgerrorcheck():
    # Initializing total and index
    total = 0
    index = 0

    # Open a file named numbers.txt file.
    infile = open('numbers.txt', 'r')

    # Reading each input
    for num in infile:
        number = num.split()
        integer = number[0]
        check = False

        # Check input's data type
        for i in range(len(integer)):
            if ord(integer[i]) >= 48 and ord(integer[i]) <= 57 or ord(integer[i]) == 45:
                check = True

        # Sum executes
        if check == True:
            index += 1
            total += float(integer)
            print('I read in', index, 'number(s) Current number is:', float(integer), 'Total is:', float(total))

        # Skip executes
        else:
            print(f'Bad data: {integer} skipping')

    # Calculate Average
    print(f'Average: {total/index}')

    # Close the file.
    infile.close()

# Call the main function.
if __name__ == '__main__':
    main()
