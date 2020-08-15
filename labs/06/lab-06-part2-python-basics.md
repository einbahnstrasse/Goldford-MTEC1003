---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
<!-- http://www.iangoodfellow.com/blog/jekyll/markdown/tex/2016/11/07/latex-in-markdown.html -->

# Lab 6 Part 2: Some Simple, Stupid Python Programs   

#### C O N T E N T S  
<a href="#setup">Setup for Python3</a>  
1. <a href="#saytwice">Recreating <i>SayTwice.html</i> but in Python</a>  
2. <a href="#temperature">Recreating (and Debugging) <i>Temperature.html</i> but in Python</a>
3. <a href="#bmi">Calculating Body Mass Index (BMI) in Python</a>

* * *

<a id="setup"></a>
## Setup for Python3   

Let's be sure your Terminal session will run Python3 (instead of the prepackaged Python 2.7.x) when calling `python` on the command line. We can crete an "alias" for python3 by running the following command:  

  {% highlight terminal %}
  $ alias python=/usr/local/bin/python3 {% endhighlight %}

Once you've done this, you're all set. Onto making "greetings.py" ...  

* * *  

<a id="saytwice"></a>
## 1. Recreating _SayTwice.html_ but in Python  

In [Lab 6 / Part 1](/Goldford-MTEC1003-OL04/labs/06/lab-06-part1-js-basics.html){:target="_blank"}, you made a program that asked for user input and echoed it back twice to the console. How would we do that in Python?  

What if I told you... that you already know the two things in Python you'll need: `input()` and `print()`? Remember those?!  

I bet you can do the rest...  

Save your new code to a file called **saytwice.py**. Make sure it's in your **lab-06-review** repository!

Now we just have to **test** our python script by running it on the command line.

Back in Terminal, simply type `python`, then a space, and then drag-and-drop your **saytwice.py** file onto the Terminal window (**remember:** this will quickly create a `full path` to your file on the command line!). Run the command by hitting `enter`, of course.

The output will look like this:  

  {% highlight terminal %}
  $ python /Users/louisgoldford/mtec1003/lab-06-review/saytwice.py  
  Give me a word to say twice: michaelCaine
  michaelCaine! michaelCaine!
  $ {% endhighlight %}

Make sure your file is included in your **/lab-06-review** folder, and don't forget to **add**, **commit**, and **push** your changes!  
Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

* * *   

<a id="temperature"></a>
## 2. Recreating (and Debugging) _Temperature.html_ but in Python  

This one's slightly more involved, so we'll do it together. Firstly, we need [a formula for our conversion](https://www.pleacher.com/mp/mlessons/algebra/funform.pdf){:target="_blank"} from degrees in Celcius (°C) to degrees in Fahrenheit (°F):

$$ {F} = {\frac{9}{5}}C + 32 $$

where:
  * F will be our result; i.e. degrees in Fahrenheit (°F), and  
  * C is our "user input"; i.e. degrees in Celcius (°C)  

Maybe you found this formula, or one like it, when you made your JavaScript version in [Lab 6 / Part 1](/Goldford-MTEC1003-OL04/labs/06/lab-06-part1-js-basics.html){:target="_blank"}. But how should we reconstruct it in Python?   

### Initial "Translation" of our JavaScript Code  

Consider your file **temperature.html** from Lab 6 / Part 1, and start your translation into Python by doing the obvious:  

  {% highlight py linenos %}  
  tempincelsius = input("Please enter a temperature in celsius: ")  
  tempinfahrenheit = (tempincelsius * (9 / 5)) + 32.0  
  print("The temperature is " + tempinfahrenheit + "°F") {% endhighlight %}  

...Our Python code is looking pretty good.... I mean, right?.........  
......Yeah, life's been pretty good to ya.... right?......  
.........We are **aWeSoMe cOdErZ** aren't we... RIGHT?!!!!...  

So, we save our code and go to our console to run it, and we are **SO SURE** it's gonna work... right?!  
Well, let's see what happens...  

  {% highlight terminal %}
  $ python /Users/louisgoldford/mtec1003/lab-06-review/temperature.py  
  Traceback (most recent call last):
    File "/Users/louisgoldford/mtec1003/lab-06-review/temperature.py", line 2, in <module>
      tempinfahrenheit = (tempincelsius * (9 / 5)) + 32.0  
  TypeError: can't multiply sequence by non-int of type 'float'
  $ {% endhighlight %}

WHAT JUST HAPPENED? First, breathe... Okay, now let's start to work the problem.    

### We Need a Floating-Point Number!  

The error we got mentions two crucial things: (1) it mentions that line 2 is a specific problem, and (2) it also mentions something about a `float` (non-int of type 'float'). What does this mean?

It means that something on line 2 (which is reprinted in our error message, and that helps! _tempinfahrenheit = tempincelsius * 1.8 + 32.0_) is not the expected **floating-point number** (i.e. a number with a decimal, in computer science terms). Without a floating-point number, the equation we wrote on line 2 can't be computed. We see that 1.8 and 32.0 are both numbers with decimals, so the only thing that might _not_ be a floating-point number in line 2 _must be_ our variable: **'tempincelsius'**.

So what **is** 'tempincelsius' then, anyway?  
And how can we **make** it a floating-point number?  

### Debugging with the `type()` Function  

Fortunately, in Python we can use a nifty function called `type()` to find out what **'tempincelsius'** really is. Start by going back to your **temperature.py** file and **commenting out** lines 2 and 3 (since that's where the error is occurring.)  

Just after line 1, insert a line and type the following:  

  {% highlight py linenos %}  
  tempincelsius = input("Please enter a temperature in celsius: ")  
  print(type(tempincelsius))
  # tempinfahrenheit = (tempincelsius * (9 / 5)) + 32.0  
  # print("The temperature is " + tempinfahrenheit + "°F") {% endhighlight %}

Now, on line 2 we're printing out (`print()`) the _result_ of the `type()` function.  
Save your file, and re-run it in Terminal:  

  {% highlight terminal %}
  $ python /Users/louisgoldford/mtec1003/lab-06-review/temperature.py  
  Please enter a temperature in celsius: 45
  <class 'str'>
  $ {% endhighlight %}

AHA! The result of our {% highlight py %} print(type(tempincelsius)) {% endhighlight %} command tells us that the variable we're testing, **'tempincelsius'**, is a STRING, NOT A DECIMAL (i.e. 'str' according to the result in our console). So, now we know we just need to _convert_ the **'tempincelsius'** variable into a `float`. For converting between strings and floats, python has two very handy functions: `float()` and `str()`. How nice!  

### Updating Our Code With the Right Conversions  

Go back to your code, **comment out** the print function, and **comment in** lines 3 + 4. Revise them so that it reads:  

  {% highlight py linenos %}  
  tempincelsius = input("Please enter a temperature in celsius: ")  
  # print(type(tempincelsius))
  tempinfahrenheit = (float(tempincelsius) * (9 / 5)) + 32.0   
  print("The temperature is " + str(tempinfahrenheit) + "°F") {% endhighlight %}

Here, we've updated our code so that we're converting variable **'tempincelsius'** into a `float` in order to compute the temperature. Then on line 4, we need to _concatenate_ the result into a larger string and print it out to the console, so we have to convert the **'tempinfahrenheit'** variable _back into a string, because it's a float._ If we forget to convert it back into a string, we'll get an error in the console similar to the one we got before we did our first conversion above.  

Try it out in the Terminal... Now it should work!  

  {% highlight terminal %}
  $ python /Users/louisgoldford/mtec1003/lab-06-review/temperature.py  
  Please enter a temperature in celsius: 32  
  The temperature is 89.6°F  
  $ {% endhighlight %}

Save your code, make sure your **temperature.py** file is included in your **/lab-06-review** folder, and don't forget to **add**, **commit**, and **push** your changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

* * *

<a id="bmi"></a>
## 3. Calculating Body Mass Index (BMI) in Python

Let's do something we haven't already done in JavaScript...  
Dunno about you, but the pandemic has led to me gaining some weight......... :$  

### How would you calculate the percentage of fat on a person's body?  

To do this we use [a formula for Body Mass Index (BMI)](https://www.pleacher.com/mp/mlessons/algebra/funform.pdf){:target="_blank"}:  

$$ {BMI} = \frac{703 \times W}{H^2} $$

where:
  * W is a person's weight (in pounds), and  
  * H is their height (in inches).  

With just these two inputs to the equation, we can describe a person's BMI; the percentage of their body weight that is fat.  

### How would we accomplish this with Python?  

As you can imagine, you'll need to start by asking the user for some input.  
In this case, you'll need to:  
1. ask the user for two things, and  
2. create separate variables and prompts for each. Then,  
3. you'll convert the strings into floats (just like we did in _temperature_ above),
4. make your equation (using the formula for BMI above),    
5. convert the result back into a string, and finally  
6. print the final result to the console.

So, in your text editor, create a new file and call it **bmi.py**, and get started!

### import sys

At the top of your new file on line 1, type the following:  

  {% highlight py %}  
  import sys {% endhighlight %}

`import` is a statement in Python that allows you to "import" a "module." In this case, `sys` is the module we're importing. A Python module is basically a file containing more Python code; more functions, variables, classes, methods, etc. We're using `sys` here to be sure you won't get any errors resulting from weird characters you may type, or those that might throw errors on the command line. You might try safeguarding yourself with this particular module in some of your other Python files too!

Write your code below your `import sys` line, so that your output in the console resembles this:

  {% highlight terminal %}
  $ python /Users/louisgoldford/mtec1003/lab-06-review/bmi.py  
  Enter your weight (in pounds): 153
  Okay, also enter your height (in inches): 68
  Your body mass index (BMI) is 23.2610294118%
  $ {% endhighlight %}

Although you won't need it, feel free to try out Python's [pow() method](https://www.w3schools.com/python/ref_func_pow.asp){:target="_blank"} to aid in your calculation.  

Save your code, make sure your **bmi.py** file is included in your **/lab-06-review** folder, and don't forget to **add**, **commit**, and **push** your changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!

* * *
