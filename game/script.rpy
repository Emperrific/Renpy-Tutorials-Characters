# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image ctc_gear:
    Animation("cog1.png", 0.2, "cog2.png", 0.2, "cog3.png", 0.2)
    xpos 0.9
    ypos 0.8

image empish icon1 = "butterfly.png"
image empish icon2 = "CoderGirl-WhiteBackground.jpg"
image side empish icon1 = "butterfly.png"
image side empish icon2:
    "CoderGirl-WhiteBackground.jpg"
    size (150,150)

define e = Character("Eileen", who_color="#c8ffc8", what_color="#aaaaaa")
define emp = Character("Emp", image="empish", ctc="ctc_gear", ctc_position="fixed", window_background="new_window_bg.png")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hello, world."

    emp icon1 "You've created a new Ren'Py game."

    emp icon2 "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
