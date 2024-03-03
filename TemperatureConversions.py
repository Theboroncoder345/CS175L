# Arnav Vasa
# CS175L
# Temperature Conversions
def main():
    controlLoop()

def convertToKelvin(temp):
    kelcon = convertToCentigrade(temp) + 273.15
    return kelcon

def convertToCentigrade(temp):
    celcon = (5/9)*(temp-32)
    return celcon

def doConversion(temp):
    print(f'Fahrenheit: {temp:.2f} Kelvin: {convertToKelvin(temp):.2f} Centigrade: {convertToCentigrade(temp):.2f}')

def repeat():
    repeater = int(input('How many conversions would you like to do this time? '))
    for x in range (repeater):
        doConversion(getFahrenheit())

def controlLoop():
    loopdec = input('Do you want to do some conversions(Yes or No)? ')
    if loopdec == 'yes':
        repeat()

def getFahrenheit():
    temp = float(input('Enter Fahrenheit temperature: '))
    while temp < -50 or temp > 130:
        print('Invalid Input! Please try again!')
        temp = float(input('Enter Fahrenheit temperature: '))
    return temp

if __name__ == '__main__':
    main()
