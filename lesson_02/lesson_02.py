'''

    To understand recursion, you must first understand recursion.

    David Hunter, Essentials of Discrete Mathematics

This lesson is designed to get you thinking about recursion, iteration, and the
call stack.

Recursion is, simply put, when a function calls itself. The classic motivating
example is the mathematical factorial function and I won't disappoint, viz:

    5! = 5 * 4 * 3 * 2 * 1

How might we define this function in Python? Let's look at it another way:

    5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3 * 2 * 1

Ah-hah! `factorial(5)` is `5 * factorial(4)`! So something like this, perhaps?

    def factorial_1(n):
        n * factorial_1(n-1)

Don't run this. Beware! Here be dragons. Specifically, this function has no way
of knowing when it is finished: you can always subtract 1 from whatever value
of `n` given (there are [a lot of numbers][1]).

[1]: http://vimeo.com/13497928

***
* Exercise 1
*
* Modify factorial_2 below to terminate at the correct time.
***
'''

def factorial_2(n):
    '''
    Modify this code!
    '''
    return "Delete this line"
    n * factorial_2(n-1)

'''
But there's another problem. So perhaps you've solved the issue of making the
function eventually terminate, but you may not get a chance to if you run out
of memory.

Every time you call a function in Python, you add a *stack frame* to the
function call stack. The call stack is simply some memory allocated for your
program to keep track of the state of a function. If function `a` calls `b`,
which then calls `c`, you want to keep track of what's going on in `a` so that
when you're done with `b` and `c` you can resume your computation.

Fair enough. But the amount of memory `factorial_2` uses is directly
proportional to the size of the input number. Can we do better than this?

One strategy would be to write an *iterative* version of factorial; that is,
one which uses loops instead of recursion. It is [provable][2] that all
recursive algorithms can be expressed with loops - and vice versa.

[2]: http://stackoverflow.com/questions/2093618/can-all-iterative-algorithms-be-expressed-recursively

***
* Exercise 2: Write an iterative version of factorial below.
*
* Here is how you use while loops in Python:
*
*     while <boolean condition>:
*         <body of while loop>
*
* The body of the loop can (and should!) modify the state of the program around
* it to make the boolean condition False.
***
'''

stupid_number = 5
while stupid_number > 0:
    print factorial_2(stupid_number)
    stupid_number = stupid_number - 1

def factorial_iterative(n):
    '''
    Fill in this function and remove the line below :)
    '''
    assert True

'''
In some languages - eg Scheme, Common Lisp, Racket, or [Perl if you download
the right module and feel you must atone for some sin][3] - recursion doesn't
*always* have to be a death knell to memory usage.

[3]: https://metacpan.org/pod/Sub::Call::Tail

These languages provide what is known as *tail recursion*: if the last thing a
function does is call itself - and I mean the *very* last thing - the compiler
will forego pushing another frame on the call stack and simply reuse the
existing stack frame.

I'll elucidate this in Scheme:

    (define (factorial n accumulator)
      (if (= n 1)
          accumulator
          (fac (- n 1) (* n accumulator))))

    (factorial 5 1)

In Scheme, it's easy to see what the tail call is. By order of operations, if
`n` is to equal to 1 then the only statement in the function is another call to
`factorial`.

This is similar to the Python version with loops:

    def factorial_iterative(n):
        accumulator = 1
        while n != 1:
            accumulator = n * accumulator
            n = n -1
        return accumulator

What follows is an example of how to simulate tail recursion optimization in
Python. No exercises, just something to meditate on.
'''

def tail_rec(fun):
    '''
    Receive a function `fun` as an argument;
    Return a function which accepts `fun` and runs it in a loop.
    '''
    def tail(fun):
       a = fun
       while callable(a):
          a = a()
       return a
    return (lambda x: tail(fun(x,fun)))

def tail_fac(args,f):
    '''
    Instead of normal function arguments, we take two:

    - a dictionary of actual function arguments
    - a function to call when finished

    The function to call, incidentally, is itself.
    '''
    if args['n'] == 1:
        return args['acc']
    else:
        args['acc'] = args['n'] * args['acc']
        args['n'] = args['n'] - 1
        return (lambda: f(args,f))

fac = tail_rec(tail_fac)
fac({'n':10000,'acc':1})

##########################################
### ABANDON ALL HOPE YE WHO ENTER HERE ###
### But seriously, like at any good    ###
### zoo, don't touch - just look.      ###
##########################################

if __name__ == "__main__":
    assert factorial_1(5) == 120
    assert factorial_2(5) == 120
    assert factorial_iterative(5) == 120
    assert fa
    print "Prima! You're done."
    print "Now, type the following: git commit -a -m 'finished lesson 2'"
