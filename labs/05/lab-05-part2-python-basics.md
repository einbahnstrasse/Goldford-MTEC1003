---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Lab 5 Part 2: _Greetings_ and _Madlibs_ in Python  

Once you've made these simple programs in JavaScript, doing them in Python will be a piece of cake!  The two languages share a lot in common. We'll do the first of these, "greetings", together below, and then you'll have no problem doing the other one, on your own.  

We won't be running Python inside of an HTML script on a website, so in your text editor (e.g. Atom, Sublime Text, etc.) simply create a new file and give it the .py extension. This signals your text editor to invoke the proper syntax highlighting up front. Name this first file **greetings.py**.

## Setup for Python3   

Let's be sure your Terminal session will run Python3 (instead of the prepackaged Python 2.7.x) when calling `python` on the command line. We can crete an "alias" for python3 by running the following command:  

  {% highlight terminal %}
  $ alias python=/usr/local/bin/python3 {% endhighlight %}

Once you've done this, you're all set. Onto making "greetings.py" ...  

* * *  

## Recreating _Greetings.html_ but in Python  

In JavaScript, a variable is _declared_ by typing `var` like so:

  {% highlight js %}
  var myVariable = someValue; {% endhighlight %}

Notice that in addition to our _declaration_, we also assigned a value (someValue).

In Python, we don't need to _declare_ a variable... Instead, a variable is automatically "declared" when we assign a value to it. So, we just write:  

  {% highlight py %}
  myVariable = someValue {% endhighlight %}

(Also, notice that we don't use the semicolon at the end of a line in Python, as we do in JavaScript.)  

To prompt the user for input, we don't type `prompt()` as we do in JavaScript. In Python (i.e. Python3) we use the `input()` method.  
So, our first line of code in **greetings.py** will look something like this:  

  {% highlight py %}
  username = input("So, like, what's your name? ") {% endhighlight %}

We've successfully (1) prompted the user for input, and (2) stored that user input in a new variable called "username".  
The last step is to print it back out in a string back in the console. Our print function in Python is pretty simple:

  {% highlight py %}
  print("Look Mom, no semicolon!") {% endhighlight %}

Now, we just have to _concatenate_ a string that includes the input stored in the `username` variable.  
So, this means our 2nd and last line of code in **greetings.py** will look a little something like this:  

  {% highlight py %}
  print("Hi, " + username + "!") {% endhighlight %}

Here, we've (1) concatenated a string, stored inside our `username` variable, into a longer string to form a greeting, and (2) we returned this final string to the console with a `print()` function.  

Now we just have to **test** our python script by running it on the command line.

Back in Terminal, simply type `python`, then a space, and then drag-and-drop your **greetings.py** file onto the Terminal window (**remember:** this will quickly create a `full path` to your file on the command line!). Run the command by hitting `enter`, of course.

The output will look like this:  

  {% highlight terminal %}
  $ python /Users/louisgoldford/Desktop/greetings.py  
  So, like, what's your name? dumpsterFyreFestival  
  Hi, dumpsterFyreFestival!  
  $ {% endhighlight %}

Make sure your file is included in your **/lab-05-js-py** folder, and don't forget to **add**, **commit**, and **push** your changes!  
Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html) if you need it!  

* * *   

## Recreating _Madlibs.html_ but in Python  

Now that you've seen how easily we can translate our JavaScript code into Python, write new versions of the _Madlibs_ programs you made in [Lab 5 / Part 1.](/Goldford-MTEC1003-OL04/labs/05/lab-05-part1-js-basics.html)

If you're feeling comfortable, you can skip the 1st version of madlibs (i.e. the one with hardcoded values), and move quickly onto making the final version (i.e. the one with variables prompted with user input using Python's `input()` method, described above). You can call it **madlibs.py**. Don't forget to **test** your programs on the command line too.  

Make sure your file is included in your **/lab-05-js-py** folder, and don't forget to **add**, **commit**, and **push** your changes!  
Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html) if you need it!  

Your final **/lab-05-js-py** folder by the submission deadline should include the following:  
* greetings.html  
* greetings.py   
* madlibs.html  
* madlibs.py  

* * *  
