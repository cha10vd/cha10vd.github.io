Title: Fast GUI programming with Tk and Python
Author: victor
Date: February 04, 2019 
Slug: gui-tkint
Tags: GUI, Tkinter, interactivity
Category: GUI Programming

## Intro

Much of a theoretician's work involves running calculations. we feed in data and parameters and get
data and paraemeters back. From these numbers alone, it's often very difficult to draw much meaningful
insight.

To overcome our limitations in extracting info directly fom numbers we make recourse to graphs and 
figures. In Python, my programming languages of choice, Matplotlib makes drawing a graph, arbitrarily
straight forward.

The native support for interactivity is, however, very lacking. There's no way to vary parameters in
a graph on the fly. 

This is where Tkinter comes in. the ***Tk*** ***inter***face provides a method for rapid graphical 
interface development and using Tkinter we can effortlessly add interactivity to a matplotlib plot
and much else.

## Hello World!

No introduction to programming is complete without Hell world!. we therefore start by making a simple
window with a "Hello World!" button:

```python
from tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()
```

<figure>
  <img src="\..\assets\images\gui\tkHello.png" alt="Tk's Hello World! window" style="width:75%; margin-left: auto; margin-right: auto;"/>
  <figcaption> Our rather unimpressive Hello World! window </figcaption>
</figure>

While this exammple is arguably not particularly exciting, it allows us to discuss the basic anatomy
of a tkInter program.

the implementation of Tcl/Tk in Python takes advantage of Python's capacity for object-orientation
and windows are objects to which we may bind fither objects.

after importing tkinter via the **import** directive, the first thing we do is create the **root**
widget. This is an ordinary window, with a title bar and other decoration provided by your window
manager. It serves as the foundation for everything we may subsequently add to our program.


We should only have root widget for each program, and it must be created before any other widgets. 

We then add other widgets by instantiating these and *packing* them in our root. Here we make a 
Label widget:

```python
  w = Label(root, text="Hello, world!")
  w.pack()
```

Once we havd added all the widgets we may wish to use in our program, we create the main execution
loop. This is the loop that keeps the window on the user's screen, listening to inputs and cues for
further execution. It exits the loop until we close the window..

## Calculator

With the basic tk anatomy under our belt, we may proceed to analyse slightly more interesting examples,
The classic being a simple calculator.

We start off by creating functions to automate the creation of the basic components of our calculator.
Calculators need buttons and a display. We start with these.

#### Buttons

The layout of a typical calculator arranges buttons in rows of 3. We can mimic this organization in our
code by assigning buttons to **frame** widgets, each representing a row.

```python 
def button(root, side, text, command=None):
  w = Button(root, text=text, command=command)
  w.pack(side=side, expand=YES, fill=BOTH)
  return w

def frame(root, side):
  w = Frame(root)
  w.pack(side=side, expand=YES, fill=BOTH)
  return w
```

#### Display

```python
def screen(root, text, side):
  w = Entry(root, relief=SUNKEN,
        textvariable=text)
  w.pack(side=side, expand=YES,
         fill=BOTH)
  return w
```

### The Calculautor object

```python
class Calculator(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.pack(expand=YES, fill=BOTH)
    self.master.title('Simple Calculator')
    self.master.iconname('calc1')

    display = StringVar()
    screen(self, text=display, side=TOP)

    # Create number buttons. Allow for negative
    # and decimal numbers with - and . buttons:
    for key in ("123", "456", "789", "-0."):
      keyF = frame(self, TOP)
      for char in key:
        button(keyF, LEFT, char,
               lambda w=display; s=' %s '%char:
                 w.set(w.get()+s))

    # Create buttons for arithmetic operations:
    opsF = frame(self, TOP)
    for char in "+-*/=":
      if char == '=':
        btn = button(opsF, LEFT, char)
        btn.bind('<ButtonRelease-1>',
                 lambda e, s=self, w=display:
                   s.calc(w), '+')
    else:
        btn = button(opsF, LEFT, char,
                     lambda w=display, c=char:
                       w.set(w.get()+' '+c+' '))

    # Finally, we create the clear button to 
    # reset our calculator:
    clearF = frame(self, BOTTOM)
    button(clearF, LEFT, 'Clr', 
           lambda w=display: w.set(''))
```
