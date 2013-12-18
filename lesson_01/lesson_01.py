'''
We're going to write a short program to compute square roots using Newton's
method.

Newton's method is this: for some x you wish to find the square root of, make a
guess.

If the guess is good enough, you're done.

If the guess is not good enough, adjust it. This adjustment is made by
averaging the guess with x/guess.

***
* Exercise 0: Why does that work?
***

The code below defines a function, sqrt(), which will use this method. It also
defines some helper functions. It's good practice to separate concerns out into
reusable components like this

sqrt() demonstrates several important features of Python syntax:

    - How to define a function
    - while-loops
    - If-statements
    - Basic arithmetic: +, *, /, -, abs()
    - Boolean values (True and False)
    - Setting and changing variables

But it's not complete! There are some pieces missing. This is a
fill-in-the-blank assignment but I want to you to get this working and then
play with what you can learn here.

***
* Exercise 1: Finish the program
***

***
* Exercise 2: In your terminal, run the python interpreter with no input files.
* At the >>> prompt, type
*
*    import this
*
* It's good shit.
***
'''

def sqrt(x):
    guess = 0.1
    finished = False
    while not finished:
        if good_enough(guess,x):
            # !!!!!
            # Something needs to be done here ...
            return guess
        assert(finished == False)
        guess = adjust(guess,x)
    return guess

def good_enough(guess,x):
    return (abs(guess**2 - x) < 0.001)

def adjust(guess,x):
    '''
    You can put documentation strings anywhere. Many people find this helpful.
    '''
    return average(guess,x/guess)

def average(x,y):

    # Fill in the appropriate code above this line.
    # Also, remove pass when you're done.
    # Also, this is the other type of comment. Anywhere you see a
    # pound sign, the rest of the line is a comment.
    pass

'''
Some afterthoughts
===

You're probably familiar with the concept of a *function* in algebra. Example:

    f(x) = x*x

Functions map values from a domain to values of a codomain. In Python, I'd
write my example this way:

    def f(x):
        return x*x

`def` means "I wish to define a function."

`return` is how you give back the answer you worked so hard to compute.

To call a function, you'd write something like this:

    f_x = f(2)

Now f_x is bound to the result of calling `f(2)`.

Now, in algebra, f(2) will *always* be 4. Always always always. In fact, part
of the mathematical definition of a function is that for any given input x
yielding output y, x ALWAYS yields y.

This is called referential transparency. In programming, people for some reason
call things functions which are not, strictly speaking, functions. For example,
many languages have a function which gives the time (as milliseconds since 1
January 1970). Let's call it `time()`.

Every time I call time(), the answer will be different. Therefore time() is not
a math function. Properly it is a *procedure* or *subroutine*.

I don't expect you to care that much but do keep this in mind. Code which
behaves non-deterministically is where bugs come from (unless of course your
core algorithm is incorrect).

I won't rant this much in the future but from the beginning I'd like to urge
you to write code which is referentially transparent as much as possible. It's
so much easier to test and debug code with computable, deterministic results
than otherwise.

At some point all code must interface with the horrifying and terrible real
world. However, the more you can quarantine that, the better.
'''

##########################################
### ABANDON ALL HOPE YE WHO ENTER HERE ###
### But seriously, like at any good    ###
### zoo, don't touch - just look.      ###
##########################################

if __name__=="__main__":
    assert (abs(sqrt(4.0) - 2.00001092578) - 2.0) < 0.0001
    print "Beautiful! You've finished."
    print "Now, type the following: git commit -a -m 'finished lesson 1'"

