#!/usr/bin/python
import sys
import time

# define math functions
def fadd(a,b):
	return  a + b 
def fsub(a,b):
	return a - b
def fmul(a,b):
	return a * b
def fdiv(a,b):
	return a / b

# calculation

print ('Program Needs Cleanup')
print ('Options:')
print ('1:Addition')
print ('2:Subtraction')
print ('3:Multiplication')
print ('4:Division')
print ('5.Exit')

choice = input('select option:')

num1 = float(input('Enter 1st number')) 
num2 = float(input('Enter 2nd number')) 

# calculate functions and output to screen
if choice == 1:   
    answer = fadd(num1,num2) 
    print num1, "+", num2, "=", answer 

elif choice == 2:
	answer = fsub(num1,num2)
	print num1, "-", num2, "=", answer

elif choice == 3:
	answer = fmul(num1,num2)
	print num1, "*", num2, "=", answer

elif choice == 4:
	answer = fdiv(num1,num2)
	print num1, '/', num2, "=", answer

elif choice == 5:
    sys.exit(0)

else:
	print "invalid input!"

#-----------
#nr analyzer
#-----------

choice = raw_input('analyze nr yes/no')
if choice == 'yes':
    
    if  answer != round(answer):
        print ('the number is not a whole number, rounding to nearest whole number')
        answer = round(answer)
        print answer                #testing
        print int(answer)           #testing
    
    if answer%2==0:
        print ('the number is even')
    else:
		print ('the number is uneven') 

    if answer > 1:
        for i in range(2, int(answer)):
            if answer % i == 0:
                print ('this is a not prime number1')
                print answer, ('divided by'), i, ('='), answer/i 
                break
            else:
                print ('this is a prime number2')
                print answer, ('divided by'), int(i), ('='), answer/i
                            
                
    else:
        print ('this is not a prime number3')

    
 
elif choice == 'no':
	print 'no'
	print 'shieeet'

else:
	print 'wrong input, program will close in 2s'
	time.sleep(2)
	exit()
