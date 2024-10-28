from winsound import Beep
from time import sleep
from datetime import datetime

## these lists are the duration of the beep and sleep
## dot = 1 unit; dash = 3 units; space between = 1 unit
## between letters = 3 units; between words = 7 units
dot  = [100, .100] # 100 ms on, 100 ms off .
dash = [300, .100] # 300 ms on, 100 ms off -
lspace = (0, .200) # 0 ms on, 300 ms off ''  200ms to account for pause after dots and dashes
wspace = [0, .400] # 0 ms on, 700 ms off '/' 400ms to account for lspace and pause after dots and dashes

## blank strings that will be populated with the user input
message = ""

## a dictionary of letters (keys) and dot/dash combo list (values)
charset = {
    'a': [dot, dash],                    # .-
    'b': [dash, dot, dot, dot],          # -...
    'c': [dash, dot, dash, dot],         # -.-.
    'd': [dash, dot, dot],               # -..
    'e': [dot],                          # .
    'f': [dot, dot, dash, dot],          # ..-.
    'g': [dash, dash, dot],              # --.
    'h': [dot, dot, dot, dot],           # ....
    'i': [dot, dot],                     # ..
    'j': [dot, dash, dash, dash],        # .---
    'k': [dash, dot, dash],              # -.-
    'l': [dot, dash, dot, dot],          # .-..
    'm': [dash, dash],                   # --
    'n': [dash, dot],                    # -.
    'o': [dash, dash, dash],             # ---
    'p': [dot, dash, dash, dot],         # .--.
    'q': [dash, dash, dot, dash],        # --.-
    'r': [dot, dash, dot],               # .-.
    's': [dot, dot, dot],                # ...
    't': [dash],                         # -
    'u': [dot, dot, dash],               # ..-
    'v': [dot, dot, dot, dash],          # ...-
    'w': [dot, dash, dash],              # .--
    'x': [dash, dot, dot, dash],         # -..-
    'y': [dash, dot, dash, dash],        # -.--
    'z': [dash, dash, dot, dot],         # --..
    '1': [dot, dash, dash, dash, dash],  # .----
    '2': [dot, dot, dash, dash, dash],   # ..---
    '3': [dot, dot, dot, dash, dash],    # ...--
    '4': [dot, dot, dot, dot, dash],     # ....-
    '5': [dot, dot, dot, dot, dot],      # .....
    '6': [dash, dot, dot, dot, dot],     # -....
    '7': [dash, dash, dot, dot, dot],    # --...
    '8': [dash, dash, dash, dot, dot],   # ---..
    '9': [dash, dash, dash, dash, dot],  # ----.
    '0': [dash, dash, dash, dash, dash], # -----
    ' ': [wspace]                        # /
}



## define a function that will produce a beep
def play_sound(int, float):
    frequency = 550      # Set frequency to 1kHz
    Beep(frequency, int) # Beep is 550kHz for a duration
    sleep(float)         # Sleep for a duration


    
## define a function that will play the message using beeps    
def play_message(message):
    morseText = ""
    for character in message:            # for each character in the message
        print(character)                 # print the character
        for unit in charset[character]:  # for the character's place in the charset dictionary
            play_sound(unit[0], unit[1]) # beep or pause for the dot, dash, or space
            if unit == dot:              # if the letter unit is a dot
                morseText += '.' 	 # add a . to the morseText string
            if unit == dash:		 # if the letter unit is a dash
                morseText += '-'	 # add a - to the morseText string
            if unit == wspace:		 # if the character is a whitespace
                morseText += '/'	 # add a / to the morseText string
        morseText += ' '                 # add a whitespace to the output for character spaces
        sleep(lspace[1])                    # pause between letters for 200ms
    return morseText                     # return the morseText string which will be saved to file


## define a function that will act as main function, taking user input, and calling other functions
def main():
    while True:                                                     # while True loop to continue program
        print("Enter '!done' to exit program.")                     # give exit option        
        ## ask for user input, clarify user can only enter numbers, letters, and spaces
        message = input("Please enter your message below. Numbers, letters, and spaces only.\n").lower()        
        ## check for special entry by user
        if message.lower() == "!done": # if user enters "!done"
            break		       # break while True loop, ending the function
        ## check for regular user input
        else:                                                                # user input is not !done or !read
            if message.replace(' ', '').isalnum():                           # check that message is alphanumeric
                print("\nMessage will print below while broadcasting\n")     # inform user of initialization
                morseText = play_message(message)                            # store converted message to variable
                continue                                                     # continue while True loop
        ## if user input is invalid
            else:                                            # user input is not !done or !read, not alphanumeric
                print("Error: Alphanumeric messages only\n") # inform user that their input is invalid
                for _ in range(4):                           # repeat the following beep 4 times
                    play_sound(75, .075)                     # beep for 75ms with 75ms rests between
                continue                                     # continue while True loop

## run main function
main()
