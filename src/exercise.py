def main():
    #write your code below this line
    age = int(input('How old are you?'))
    
    if 0 <= age <= 120:
        print('Ok')
    else:
        print('Impossible!')

if __name__ == '__main__':
    main()
