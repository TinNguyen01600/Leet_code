"""
You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. 
When your friend makes a guess, you provide a hint with the following info:
    - The number of "bulls", which are digits in the guess that are in the correct position.
    - The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong 
    position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.

Input: secret = "1807", guess = "7810"
Output: "1A3B"

Input: secret = "1123", guess = "0111"
Output: "1A1B"

Input: secret = "110", guess = "011"
Output: "1A2B"

Input: secret = "11", guess = "01"
Output: "1A0B"
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        i = 0
        while i < len(guess):
            if guess[i] == secret[i]:   
                bull += 1
                # secret = secret[:i] + '' + secret[i + 1:]
                # guess = guess[:i] + '' + guess[i + 1:]
                secret = secret.replace(secret[i], '', 1)
                guess = guess.replace(guess[i], '', 1)
                i -= 1
            i += 1
            
        for i in range(len(guess)):
            if guess[i] in secret:
                cow += 1
                secret = secret.replace(guess[i], 'a', 1)
        return str(bull) + 'A' + str(cow) + 'B'