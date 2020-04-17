#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)- its one loop. for each iteration it changes the value of a and stops when it is less then n*n*n. there is only one operation on the call stack


b) O(n^2) - its a nested loop. runtime increases as the value of n increases


c) O(n) - runs n times until it reaches zero

## Exercise II
    using a binary search...

    -set the high and low indexes
    -divide the floors in half by adding high and low and dividing by 2 and set it to the current floor
    -check to see if the egg breaks by comparing to the current floor
    -if it doesnt break set to the current floor
    -otherwise switch to other half
    -split the current floors in half
    -continue splitting and comparing until you find f

    runtime is O(log n) because it divides n each iteration


