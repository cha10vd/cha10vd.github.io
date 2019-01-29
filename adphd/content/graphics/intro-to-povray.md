Title:      Graphics with POV-Ray
Author:     victor
Date:       January 29, 2019
Slug:       pov-intro
Tags:       Graphics
Category:   Graphics

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

### Observer vs. Observed

In generating an image based on positions of objects (be these atoms, bonds or isosurfaces), we are
required to fully specify two objects:

1. That which we are observing,
2. The camera through which we observe our object.

#### Specifying the camera

Specifying the camera is a relatively easy task, as it is an abstract object in space. it needs not 
have a shape or any such geometric parameters, neither must it be given color, as it won't be seen.

We must therefore specify 3 parameters, each comprised of a vector in space.

### The Basic Language Syntax

The POV-Ray language consists of the following building blocks:
* identifiers, 
+ reserved keywords, 
+ floating point expressions, 
+ strings, 
+ special symbols and 
+ comments.

POV-Ray allows you to define **identifiers**. Indentifiers are analogous to variables in languages like
Python. An identifier may be 1 to 40 characters long. It may consist of upper and lower case letters, 
the digits 0 through 9 or an underscore character ("_"). the first character must be an alphabetic 
character.

**Comments** have their syntax borrowed from the **C** language and are made using the **//** syntax for
single-line comments and **/\* ... \*/** for multi-line comments. 

##### Declaring identifiers

We can set variables by use of the *#declare* keyword. We would thus set the value of pi as follows:

```pov
#declare PI = 3.1415;
```

Identifiers created by the **#declare** directive are permanent in duration and global in scope.
Once created, they are available throughout the scene and they are not released until all parsing
is complete or until they are specifically released using #undef. See "Destroying Identifiers". 
Those created by the #local directive are temporary in duration and local in scope.
