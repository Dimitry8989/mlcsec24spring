'''
Assignment #1: Print Your Name: 
Objective: Write a program that prints your name to the console. 
'''
print('**** Assignment 1 ******')
print('Dimitry Tsomashvili \n')

'''
Assignment #2: Simple Math Operations: 
Objective: Create a program that performs simple math operations on two numbers. 
Requirements: The program should add, subtract, multiply, and divide two numbers and print the results. Use 
variables to store the numbers and results. 
'''

print('**** Assignment 2 ******')
a=10
b=2

print('a+b=' + str(a+b))
print('a-b=' + str(a-b))
print('a*b=' + str(a*b))
print('a/b=' + str(a/b) + '\n')

'''
Assignment #3: Area of a Circle: 
Objective: Write a program that calculates the area of a circle. 
Requirements: The program should ask the user to input the radius of the circle and then calculate and display 
the area. Use the formula area = math.pi * radius ** 2. 
'''

print('**** Assignment 3 ******')
import math

x=input('Please Enter The Radoius of The Circle ')

print('The Area of The Circle According to The Radius is ' + str(math.pi * float(int(x) ** 2)) + '\n')


'''
Assignment #4: Convert Minutes to Seconds: 
Objective: Develop a program that converts minutes into seconds. 
Requirements: The program should take a number of minutes as input and output the equivalent number of 
seconds. 
'''

print('**** Assignment 4 ******')

t=input('Please Eneter Minutes ')
print('Minutes You Enetered in Seconds Will Be ' + str(int(t) * 60) + '\n')



'''
Assignment #5: Print IP addresses: 
Objective: given the network with the following pattern: 192.168.0.3/24. 
Pring all the IP addresses within this network.
'''
print('**** Assignment 5 ******')

# Define the network
network_prefix = '192.168.0.'
subnet_mask = 24

# Calculate the number of IP addresses
num_addresses = 2 ** (32 - subnet_mask)

# Print all IP addresses in the network
for i in range(num_addresses):
    # Calculate the IP address
    ip_address = network_prefix + str(i)
    print(ip_address)
