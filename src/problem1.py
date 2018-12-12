"""
Exam 1, problem 1.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Zhen Yang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg

# -----------------------------------------------------------------------------
# DONE: 2. Right-click on the  src  folder and
#              Mark Directory as ... Sources Root,
#          if you have not already done so.
# -----------------------------------------------------------------------------


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


def run_test_problem1():
    """ Tests the   problem1  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem1  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of problem1: '
    title += 'red & blue, then cyan & magenta'
    window = rg.RoseWindow(400, 250, title)

    # Test 1:
    square = rg.Square(rg.Point(125, 50), 60)
    square.fill_color = 'red'
    square.outline_color = 'blue'
    square.outline_thickness = 3

    problem1(square, 6, window)
    window.continue_on_mouse_click()

    # Test 2:
    square = rg.Square(rg.Point(250, 100), 100)
    square.fill_color = 'cyan'
    square.outline_color = 'magenta'
    square.outline_thickness = 6

    problem1(square, 3, window)
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem1: yellow & black'
    window = rg.RoseWindow(300, 400, title)

    # Test 3:
    square = rg.Square(rg.Point(150, 125), 150)
    square.fill_color = 'yellow'

    problem1(square, 15, window)
    window.close_on_mouse_click()


def problem1(square, thickness, window):
    square.attach_to(window)
    side = square.length_of_each_side
    centerx = square.center.x
    centery = square.center.y
    circle = rg.Circle(rg.Point(centerx, centery + side), side * 0.5)
    circle.fill_color = square.fill_color
    circle.outline_thickness = thickness
    line = rg.Line(circle.center, rg.Point((centerx - side * 0.5), centery))
    line.thickness = thickness
    line.color = square.outline_color
    circle.attach_to(window)
    line.attach_to(window)
    window.render()
    """
    See   problem1_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Square.
      -- A positive integer
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      -- Draws, on the given rg.RoseWindow:
           -- The given rg.Square.
           -- An rg.Circle that:
                -- is directly below and touching the given rg.Square,
                -- has diameter the same as the length of each side
                     of the given rg.Square,
                -- has fill color the same as the fill color
                     of the given rg.Square, and
                -- has the given thickness as its outline thickness.
                     (SEE THE PICTURES.)
            -- An rg.Line that:
                -- has one endpoint is at the center of the above rg.Circle,
                -- has another endpoint that is at the midpoint of the
                     left side of the given rg.Square,
                -- has color the same as the outline color
                     of the given rg.Square, and
                -- has the given thickness.  (SEE THE PICTURES.)

      Note: Attach the rg.Line  AFTER  attaching the rg.Square and rg.Circle.
      Must render but   ** NOT close **   the window.

    Type hints:
      :type square:    rg.Square
      :type thickness: int
      :type window:    rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
