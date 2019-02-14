Title: Vim Scripting Part 1
Author: victor
Date: February 09, 2019
slug: vim_script_1
Tags: Vim
Category: Vim Scripting

**Source:** [IBM: Scripting the Vim editor, Part 1](https://www.ibm.com/developerworks/library/l-vim-script-1/index.html)

> **The joke goes:**
>
> *"Emacs would be a great operating system if only it had a decent text editor, vi would be a great
>  text editor if only it had a decent operating system."*

Vim has a powerful scripting language which allows for the automation of repetitive tasks and extensive
customization to the needs of its enduser.

The basic building blocks of Vim scripting mimic those of more traditional scripting languages such
as Python: 

* Variables, 
+ Values, 
+ Expressions, 
+ Simple flow control, 
+ Vim-specific utility functions.

### Running Vim scripts
---

Running Vim scripts is straightforward. These can be saved to files or input by the user at runtime.
A script file is executed using the following syntax:

```vim
:source /full/path/to/the/scriptfile.vim
```

We may also directly type commands in command-line mode using the `:call` prefix. 

The most common way to invoke Vim scripts is by creating new keyboard mappings. These are stored in
the .vimrc initialization file in the home directory:

```vim
:nmap ;s :source /full/path/to/the/scriptfile.vim<CR>
:nmap \b :call MyBackupFunc(expand('%'), { 'all': 1 })<CR>
```

With the above examples, when in Normal mode the key sequence `;s` will execute the specified script
file, and a `\b` sequence will call `MyBackupFunc()`.

### The modes of Vim
---

| Name         | Description                                                                                  |
|--------------|----------------------------------------------------------------------------------------------|
| Normal       | Mode Vim starts in. Everything the user types in normal mode is interpreted as commands.     |
| Insert       | Once in insert mode, typing inserts characters just like a regular text editor.              |
| Visual       | Used to make selections of text, similar to how clicking and dragging with a mouse behaves.  |
| Command Line | Entered by typing the `:` character when in Normal mode. Where Vim functios are called       

Given the variety of modes to Vim, when we come to map certain functions to keystrokes, it is important
to define not only the key to be assigned, but also the mode in which to operate.
In light of this, Vim makes available the following functions:

| Function   | Description                           |
|------------|---------------------------------------|
| `:nmap`    | Normal mode mapping                   |
| `:imap`    | Insert mode mapping                   |
| `:vmap`    | Visual and select mode mapping        |
| `:smap`    | Select mode mapping                   |
| `:xmap`    | Visual mode mapping                   |
| `:cmap`    | Command-line mode mapping             |


### Representing unprintable commands
---

When scripting in Vim, we may wish to represent "invisible" commands; That is, the non-alphanumeric
keys on our keyboard and actions carried out with the mouse. These keys are given special representation
in vim, and are typically encloseb between angle brackets.

We've compied below some of the most useful commands and provide links to fuller tables for reference.


#### Unprintable key mappings

**Source: ** [Vim wiki](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_2))

| Symbol        | Meaning             |
|---------------|---------------------|
| <CR\>         | Carriage Return     |
| <BS\>         | Backspace           |
| <C-x\>        | Ctrl key modifier   |
| <S-x\>        | Shift key modifier  |
| <A-x\>        | Alt key modifier    |
| <C-S-x\>      | Combined Ctrl Shift |
| <Tab\>        | Tab                 |
| <F1\>-<F12\>  | Function keys F1-12 |
| <Space\>      | Space bar           |

#### Mouse mappings

**Source: ** [Vim wiki](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_1))

| Symbol          | Meaning              |
|-----------------|----------------------|  
| <LeftMouse\>    | Left button press    |
| <LeftRelease\>  | Left button release  |
| <2-LeftMouse>   | Left double-click    |
| <RightMouse\>   | Right button press   |
| <RightRelease\> | Right button release |
| <3-RightMouse>  | Right triple-click   |


## The anatomy of a Vim script
---

All Vim statements end with a newline, just like BASH and Python (and unlike C). Like these languages,
long statements can be broken across multiple lines using the `\` character.

Unlike these languages, however, multiple statements cannot be separated within a single line by the 
`;` charater, with Vim replacing this with `|`.


### Variables
---

#### 1. Assignment

Vim variables fall into three categoreis and are set using the `let` keyword.

Vim supports the following variable types:

* Scalars      - *Strings* or *numbers*.
+ Lists        - Square bracket-delimited ordered sequences, indexed from 0.
+ Dictionaries - Unordered sets of values delimited by braces, accessed by string keys.

Lists and dictionaries obey the same synatx as python.
Let us define a variable of each type:

```vim
let name = "Victor"
let height = 171
let interests = [ 'Programming', 'Maths', 'Music', 100 ]
let phone     = { 'cell':07894071719, 'work':'?' }
```
Note that variable types, once assigned, are permanent and strictly enforced at runtime.

#### 2. Scope

A variable declared outside any function will default to a global scope, while declaring
a variable inside a functoin scopes it locally to that function.

We can manually set the scope of a variable by prefixing it with a letter followed by a
colon.


| Prefix    | Scoping meaning                      |
|-----------|--------------------------------------| 
| g:varname | Global                               |
| s:varname | Local to the current script file     |
| w:varname | Local to the current editor window   |
| t:varname | Local to the current editor tab      |
| b:varname | Local to the current editor buffer   |
| l:varname | Local to the current function        |
| a:varname | A parameter of the current function  |
| v:varname | One that Vim predefines              |      


#### 3. Expressions

##### Variable manipulation and comparison

| Type                  | List               |
|-----------------------|--------------------|
| Logicals              | `&& || !`          |
| Numericals            | `+ - / % *`        |
|                       | `==  > >= < <= !=` |
| String concatenation  | `.`                |


### Defining functions
---

#### 1. Declaring functions

Functions in Vimscript are defined using the `function` keyword, followed by the name of the function,
then the list of parameters. The body of the function then starts on the next line, and continues until
a matching `endfunction` keyword is encountered.

We take an example from the [IBM guide to vimscripting](https://www.ibm.com/developerworks/linux/library/l-vim-script-2/index.html?ca=drs-)
website, where we censor profanities from a given text:

```vim 
function ExpurgateText (text)
    let expurgated_text = a:text
 
    for expletive in [ 'cagal', 'frak', 'gorram',
    \                  'mebs', 'zarking']
        let expurgated_text
        \   = substitute(expurgated_text, 
        \                expletive, '[DELETED]', 'g')
    endfor
 
    return expurgated_text
endfunction

```
Function names in Vimscript must start with an uppercase letter, unless they are explicitly scoped. 
When functions are declared with an explicit scope prefix, these must always be called with their 
scoping prefixes.

##### Function redeclaration

Redeclaring a function is treated as a fatal error in Vim as a mechanism of preventing *collisions*.
The need to create functions in scripts that are designed to be loaded repeatedly means we must be
able to circumvent this where necessary.

The Vimscripting language therefore provides a keyword modifier allowing reloading of a given function,
given by the `!` symbol.

Therefore, by declaring our ExpurgateText as `function! ExpurgateText`, would circumvent any reloading
issues.

#### 2. Calling functions

Calling a function follows the standard syntax adopted in languages like C and Python. We name the
function and provide a parameter list in parentheses.

```vim
let success = setline('.', ExpurgateText(getline('.'))) 
```

Where Vimscripting differs from the languages we mention above is that Vimscript does not allow you
to implicitly throw away the return value of a function without using it.

Where we we wihs to use the function as a procedure or subroutine and ignore its return value, we 
must therefore prefix its call with the `call` prefix.

Ommiting the `call` lads Vimscript to assume that the function call is actually a built-in Vim command,
and we may draw parallels to the need to explicitly use the `./` prefix in bash when calling local 
scripts.


#### 3. Providing functions with parameters

Functions can take up to 20 parameters. These are then scoped to the current function and can therefore
be accessed within it via the `a:` prefix.

For example:
```vim
function PrintDetails(name, title, email)
  echo 'Name: ' a:title a:name 
  echo 'Contact:' a:emailendfunction
endfunction
```

**variadic parameter lists** are also permitted instead of named parameters when the number of arguments
to be passed remains unknown.

To do so, we use an elipsis `(...)` instead of our parameter list. When this is done, all passed arguments,
whose max. number is now unlimited, are not grouped into an array of name `000`.

Note that while arrays are 0-indexed in vim, this is an "exception" in that `a:0` stores the number
of arguments passed to the function, such that the arguments start at `a:1`.

```vim
function Average(...) 
  let sum = 0.0 
  for nextval in a:000    
    let sum += nextval 
  
  endfor return sum / a:0 
endfunction
```

Named and variadic parameters may be combined by placing the elpsis after the named parameters, *e.g.*

```vim
function ScoreTable(student, ...)

```
