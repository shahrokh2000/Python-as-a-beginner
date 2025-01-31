this_number = 2
max = int(input('number='))
while (this_number < max):
    is_prime_number = True
    counter = 2
    while (counter < this_number):
        if ((this_number %  counter)== 0):
            is_prime_number = False
            break
        counter = counter + 1
        
    if (is_prime_number == True):
        print (this_number)

    this_number =this_number + 1
