# 100daysofcode
Just a repository for my #100DaysofCode

I'm new to programming. I studied basic Java for a semester at school. Then recently,
learnt the basics of Python, in about a week. Most of my programs will be basic, and
probably full of mistakes. I'd appreciate any feedback on the programs, I'm new and
looking to improve my skills, not flaunt them.

-joystickTest.py-
	This is the first completed program from my challenge. It works at the moment, I 
	will provide a short run through each command and how it works.
	
	To initiate the class, you must declare a background. This can be done like the way
	it is done in the program test, at the bottom. It looks like this:
	
	O = (0, 49, 83)									As you can see, the background is drawn in the program.
	X = (70, 130, 180)							It must be drawn in a 64 pixel grid, otherwise it wont
	waves_background = [						execute. If you know the syntax for the Sense HAT this
    	O, X, O, O, O, O, O, O,			will be familiar.
    	O, X, O, O, X, O, O, X,
    	O, O, X, O, X, O, O, X,
    	O, O, X, O, O, X, O, O,
    	O, O, X, O, O, X, O, O,
    	O, X, O, O, O, X, O, O,
    	O, X, O, O, X, O, O, X,
    	O, O, O, O, X, O, O, X
    	]
	
After creating the joystick class in the program, you must invoke the move function.
And thats it, there is nothing else to do. After invoking the move function, the LEDs
will light up in your background with the selected highlight colour. The colours are
in RGB and must be declared in a tuple, as above.

The code looks like:
example = JoystickLed((highlight_col), waves_background)
example.move()
