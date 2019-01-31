Title:      Graphics with POV-Ray
Author:     victor
Date:       January 29, 2019
Slug:       pov-intro
Tags:       Graphics
Category:   Graphics
CSS:        tbox.css

<style>
code { 
  font-family: monospace;
}
</style>

Much of the time, following a calculation of physical propperties of a chemical system, it is of 
interest to be able to quickly visualize the results with minimal effort.

While there are many readily-downloadable programs out there capable of such feat, we wish to develop
four ourselves a toolkit which may provide us withe the skill to generate graphics from raw data as
if from scratch in a programmatic fashion.

We have several options available to ourselves, for example:

* Matplotlib
+ OpenGL
+ POV-Ray

Matplotlib offers ease of use at the cost of limited configurability and poor image quality. OpenGL, 
on the other hand, offers professional graphics at the expense of a high level of programming 
complexity.

As such, POV-Ray serves as a good intermediate. It allows for a discussion of important concepts in
graphical programming without the need for concern over hardware resource allocation.

## The Basic Language Syntax

The POV-Ray language consists of the following building blocks:

* Identifiers, 
+ Reserved keywords, 
+ Floating point expressions, 
+ Strings, 
+ Special symbols and 
+ Comments.

**Indentifiers** are analogous to variables in languages like Python. An identifier may be 1 to 40 
characters long. It may consist of upper and lower case letters, the digits 0 through 9 or an 
underscore character ("_"). the first character must be an alphabetic character.

**Comments** have their syntax borrowed from the **C** language and are made using the **//** syntax for
single-line comments and **/\* ... \*/** for multi-line comments. 

### Declaring identifiers

We can set variables via the *#declare* and *#local* keywords, depending on the required scope of the
variable, or as it is known in POV-Ray, *identifier*.

We would thus set the value of pi as follows:

```pov
#declare PI = 3.1415;
```

This would make PI permanent in duration and global in scope. It could, however, be destroyed by the
use of the *#undef* directive.

We may also use conditional directives such as *#ifdef* and *#ifndef*, in much the same way as in the
C preprocessor. 

### Setting up conditionals

POV-Ray supports **#if**, **#while** and **#case** statements. All must be appropriately followed by
the **#end** statement. 

```pov
#declare Which=1;
#if (Which)
  box { 0, 1 }
#else
  sphere { 0, 1 }
#end
```

These are complemented by a series of debug directives, outputting to 3 distinct text streams.

```pov
// TEXT_STREAM_DIRECTIVE:
  #debug STRING | #error STRING | #warning STRING
```

We could thus complement our conditional expression above as follows:

```pov
#declare Which=1;
#if (Which)
  box { 0, 1 }
  #debug "We have a box!\n"
#else
  sphere { 0, 1}
  #debug "We have a sphere!\n"
#end
```

### Defining macros

<div class="tBox"  markdown>
  <h4>Macro definition</h4>
  
  Thinking back to pure C, we can define a macro  in the preprocessor as follows:
  <br>    <code>#define circleArea(r) (3.1415\*(r)\*(r))</code><br>
  The defined macro is then treated as a name and a string. When that name is encountered in the 
  body of the code, the name is replaced with the string.
</div>

This *token substitution* feature of macros is largely true of how POV-Ray's functions work. They
do, however, steer away from one largely-abused feature of pure macros.

Taken from the POV-Ray documentation, consider the pure C macro:

```c
#def Typical_Cmac(Param)
```
and you invoke it as:
```c
Typical_Cmac(else A=B)
```

The **else**, **A**, **=**, **B** would substituted into the program code in place of **Param** 
using a cut-and-paste operation. No type checking is performed because anything is legal if all
you're doing is copying and pasting.

Function parameters in traditional programming languages do not use token substitution to pass values.
They create temporary, local variables to store parameters that are either constant values or 
identifier references which are in effect a pointer to a variable. POV-Ray macros use this 
function-like system for passing parameters to its macros.

With all this in mind, we could then define a macro in POV-Ray as follows:

```pov
// Define the macro. Parameters are:
//   T:  Middle value of time
//   T1, T2: Initial and final time
//   P1, P2: Initial and final position 
//           (may be float, vec or color)
#macro Interpolate(T,T1,T2,P1,P2)
   (P1+(T1+T/(T2-T1))*(P2-P1))
#end
```
We could then call upon this function as follows:

```pov
  #declare Value = Interpolate(I,0,15,3.0,5.5)*15;
```

Finally, an important point about the macro/function duality. Note the outer parenthesese in the
returned value of our macro. Our call to Iterpolate is treated by the program as if we had written:

```pov
  #declare Value = (P1+(T1+T/(T2-T1))*(P2-P1)) * 15;
```

There is no temporary variable acting as intermediary in the **Value** calculation to which the
result of ouri nterpolate fuction is returned prior to the subsequent multiplication. This results
in the need to carefully consider the order in which operations are carried out. Omitting the outer
parentheses would result in our calculation of the following:

```pov
  #declare Value = P1+(T1+T/(T2-T1))*(P2-P1) * 15;
```

By BODMAS, the P1 is not multiplied by 15 and we get the wrong answer.

<!--(### Observer vs. Observed
In generating an image based on positions of objects (be these atoms, bonds or isosurfaces), we are
required to fully specify two objects:
1. That which we are observing,
2. The camera through which we observe our object.
#### Specifying the camera
Specifying the camera is a relatively easy task, as it is an abstract object in space. it needs not 
have a shape or any such geometric parameters, neither must it be given color, as it won't be seen.
We must therefore specify 3 parameters, each comprised of a vector in space.)-->
