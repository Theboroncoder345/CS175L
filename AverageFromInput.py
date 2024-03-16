#Arnav Vasa
#CS175L
#Average From Input File

#The program reads and displays the contents of the numbers.txt file.
def main():
    # Initializing total and index
    total = 0
    index = 0
    
    # Open a file named numbers.txt file.
    infile = open('numbers.txt', 'r')

    # Read the amount of integers from the file
    for num in infile:
        number = num.split()
        total += float(number[0])
        index += 1
        print('I read in', index, 'number(s) Current number is:', float(number[0]), 'Total is:', float(total))

    #Display the average
    print(f'Average: {total/index}')
    
    #Close the file.
    infile.close()

# Call the main function.
if __name__ == '__main__':
    main()
