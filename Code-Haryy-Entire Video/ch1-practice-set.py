#TODO 1. Write a program to print Twinkle twinkle little star poem in python.
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
'''
)
#TODO 2. Use REPL and print the table of 5 using it.
# Done

# TODO 3. Install an external module and use it to perform an operation of your interest.

import pyttsx3
engine=pyttsx3.init()
# engine.say("Helo Mahnoor")
# engine.say("Helo Abubakar")
engine.runAndWait()

#TODO 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.


import os


def print_directory_contents(path):
    # Try if the entered directory is available in the path or not.
    try:
        # Use the os module to list the directory of content
        entries = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        
        # print names of directory one by one
        for entry in entries:
            print(entry)
            
    # display error in case of file not found
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
        
    # display error in case of permission not granted
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    # display error in case of any error
    except Exception as e:
        print(f"An error occurred: {e}")
# Enter your directory whose content you want to list
directory_path = "/Python- Code"
# print the list of all other stored directories in the given directory
print_directory_contents(directory_path)



#TODO 5. Label the program written in problem 4 with comments
# Done