# If statements

In the previous two sets of exercises, you have learned about variables and functions.  Broadly speaking variables are used to refer to spaces in memory.  These spaces can then hold a value.  Functions are then used to change the values of the variables that are stored in memory.  Towards the end of the exercise on functions, we saw that this distinction was not as clear cut as this.  The sets of instruction within a function are themselves stored in memory.  As we saw when we learned to use sympy, we can, therefore, write a function that takes another function as one of the input variables.

In this exercise, the last piece of the programming puzzle will be introduced.  Once you have completed this series of exercises you will thus know everything that you need to know to program anything.   To be clear, there will still be more to learn as you will always want to use functions written by others to reduce the length of the programs you write.  With an understanding of logic and the material that we have studied thus far, however, you can (in theory) write all the code you will use yourself.

You need to use logic if the set of commands the programs executes depends on the value of a variable.  To see what I mean consider the code shown in `main.py`.  The line:

````
data = np.loadtxt("mydata.dat")
````

loads the data from the file `mydata.dat` into a NumPy array called `data`.  You can look at this file by clicking the `mydata.dat` tab.  As you can see this file contains 1000 1-digit integers.  The array `data`, therefore, has one thousand elements.  We do not need to know this, however, as we can get the number of elements in the array by using the command `len(data)`.

If you run the code on the left a graph with 1000 points is generated.  The x coordinates of these points are the integers starting at 0 and finishing at 999.  The y coordinates, meanwhile, are all either 0 or 1.  The y-coordinate of a point is equal to one when the corresponding element of the data array is equal to 5.  If, by contrast, the corresponding element is not equal to five then the y-coordinate of that point is zero.  

We are able to make a plot like this one because we use an if statement in this line:

````
if data[i] == 5 : filter[i] = 1
````

This statement tells python that the ith element of the array called `filter` should only be set equal to 1 if the ith element of data is equal to 5.  When the filter array is initialised two lines above this one all the elements within it are set equal to zero.  Consequently, if the ith element of data is not equal to five then the ith element of filter, which is not changed by the line containing the if statement above, will be zero.

To pass this exercise, and to demonstrate that you have understood the basics of if statements, modify the code.  Change the variable called `filter` into a single integer that is initialised to zero. Replace the code that plots the graph with code to print the final value of `filter`.  Lastly, modify the code that is executed when `data[i]==5` so as to ensure that when filter is output by your print statement it is equal to the total number of fives in the array called `data`.    
