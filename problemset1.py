# #1 . print twinkal twinkal little star
print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.""")


# # 2 . REp ma 
# #  terminal ma che

# # 3 . external modulo
import pyttsx3
engine = pyttsx3.init()
engine.say("hii how are you")
engine.runAndWait()

# #  4 . os modulo
import os

# Specify the path of the directory
directory_path = "D:/Series/"

# Get the list of files and directories in the specified directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
import pyjokes

print(pyjokes.get_joke())