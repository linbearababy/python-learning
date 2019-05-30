project 01 

# Assignment Overview

This assignment involves coding and testing of a program that uses Python arithmetic.

The basic design of your first program that in this class prompts for input, performs arithmetic on that information and then displays the results.

# Background

This programming project will use the input and print functions along with some simple mathematics for conversion. The important part of the project is to learn the skills needed to access the class web site to download a project description, create a new program in Python and finally to hand it in.

# Program Specifications
Conversions are useful both in science and daily life. Here we examine some obscure, but useful conversions as well as some silly ones.

If you canoe in the Boundary Waters Canoe Area (BWCA) you portage (carry) your canoe and gear between lakes as you wander deeper into the wilderness (top image is of Dr. Enbody canoeing; middle image is daughter portaging gear; left is Dr. Enbody portaging a canoe). BWCA maps label distances on portages in rods, an old unit of measurement that is 5.0292 meters, which is approximately the length of a canoe so it is a useful measurement in the wilderness.

Here is a piece of a BWCA map showing portages between lakes (black lines) with the length of the portage labeled in rods. (Red triangles are campsites.)

-----------------------
Your program will prompt the user for a floating-point value representing a distance in rods. You will reprint that value along with that value converted to the following values. The most important value for planning a trip is the time to walk the portage.

• meters

• feet

• miles

• furlongs

• the time in minutes to walk that distance


You can find these measures on the web, but so everyone is using the same conversions we require that you use these so testing will yield the same results:

• 1 rod = 5.0292 meters

• 1 furlong = 40 rods

• 1 mile = 1609.34 meters

• 1 foot = 0.3048 meters

• average walking speed is 3.1 miles per hour

# Assignment Notes:
1. To clarify the project specifications, sample output is appended to the end of this document.
  
2. To receive credit your program must take in input, do some simple arithmetic based on that input, and then print results.

3. Round all floating-point output to three places, i.e. use round( x, 3 ). Important: do not round intermediate results because rounding differences will compound resulting in a wrong result. Round values only when you print them.

4. Testing on Mimir does exact matching of output so we provide a file strings.txt of strings for you to copy to make it easier to get the matching correct.

5. Items 1-6 of the Coding Standard will be enforced for this project.

6. The input function is used to accept a response from the user. The function accepts a
string (a sequence of characters between quotes) as a prompt to display to the user. It then waits until the user types a response (terminated by the user touching the Enter key). Finally, the function returns the user’s response as a string.

If the user’s response is supposed to be processed as a numeric value, the returned string must be converted into a number. When working with floating point values, a string is converted into a floating point number using the float function. The function accepts a string as its argument and returns the floating point number which the string represents. A typical interaction would be something like:

     num_str = input( "Please enter a number: " )
     num_float = float( num_str )

7. The print function is used to display any combination of variables, values and strings in the output window. Each item to be displayed must be separated from another item by a comma. All the items will be displayed together, followed by a new line. For example:

        print( num_int, " times two is ", num_int*2 )
        
Three items will be displayed when the print function is called: the value of the variable
num_int, the string " times two is ", and the result of the calculation. Assuming that the value of the variable num_int is 26, then the output will be: 26 times two is 52

8. The file named number_input.py in the project directory contains a program which illustrates the use of some standard library functions.

# Sample Interaction

                         Test 1
      Input rods: 1
      You input 1.0 rods.
      Conversions
      Meters: 5.029
      Feet: 16.5
      Miles: 0.003
      Furlongs: 0.025
      Minutes to walk 1.0 rods: 0.06


                   Test 2
      Input rods: 10
      You input 10.0 rods.
      Conversions
      Meters: 50.292
      Feet: 165.0
      Miles: 0.031
      Furlongs: 0.25
      Minutes to walk 10.0 rods: 0.605
      
                    Test 3
      Input rods: 444.44
      You input 444.44 rods.
      Conversions
      Meters: 2235.178
      Feet: 7333.26
      Miles: 1.389
      Furlongs: 11.111
