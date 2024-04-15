import matplotlib.pyplot as plt

def main():
    #Try 
    try:
        #Opens the file
        infile = open('expenses.txt','r')

        #Created two lists
        label = []
        value = []

        #Using a loop to add the label and value to the lists
        for line in infile:
            line = line.rstrip()
            isAlpha = line.split('\t')[1][:-1].isalpha()
            if not isAlpha:
                label.append(line.split('\t')[0])
                value.append(line.split('\t')[1])
            else:
                print('ERROR: expense value must be a float or an integer')

        #Creating a pie chart
        plt.pie(value, labels=label, colors=('r', 'y', 'g', 'c', 'b', 'm'))

        #Defining the Title of the pie graph
        plt.title('Monthly Expenses')

        #Showing the pie graph
        plt.show()

    #Except IOError
    except IOError:
        print('An error occurred trying to read\nthe file expenses.txt')

    #Except ValueError
    except ValueError:
        print('ERROR: expense value must be a float or an integer')

    #Except error
    except:
        print('An error occured')
    
if __name__ == '__main__':
    main()
