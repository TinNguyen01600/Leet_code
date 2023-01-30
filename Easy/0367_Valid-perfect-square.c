/*
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Input: num = 16
Output: true

Input: num = 14
Output: false

1 <= num <= 2^31 - 1
*/

#include <stdbool.h>

bool isPerfectSquare(int num){
    if (num == 1)   return true;
    for (int i = 1; i<46341; i++){
        if (i*i == num) return true;
        if (i*i > num)  return false;
    }
    return false;
}