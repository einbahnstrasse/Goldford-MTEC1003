---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
<!-- http://www.iangoodfellow.com/blog/jekyll/markdown/tex/2016/11/07/latex-in-markdown.html -->

# Lab 7 / Part 2: Python Conditionals   

#### C O N T E N T S  
<a href="#setup">Setup for Python3</a>  
1. <a href="#js-stuff">Recreating JavaScript Conditional Exercises in Python</a>  
2. <a href="#reminders-user">Reminders (User Input)</a>
3. <a href="#bmi">Calculating Body Mass Index (BMI) in Python</a>

* * *

<a id="setup"></a>
## Setup for Python3   

Let's be sure your Terminal session will run Python3 (instead of the prepackaged Python 2.7.x) when calling `python` on the command line. We can crete an "alias" for python3 by running the following command:  

  {% highlight terminal %}
  $ alias python=/usr/local/bin/python3 {% endhighlight %}

Alternatively, you can simply run `python3` in the Terminal instead of `python`, but this gets annoying after awhile.  

Once you've done this, you're all set.  

* * *  

<a id="js-stuff"></a>
## 1. Recreating JavaScript Conditional Exercises in Python    

_**NOTE:** This section starts with the same 3 exercises from Lab 7 / Part 1. If you feel more comfortable with Python rather than JavaScript, you can start with this section in Python and then complete the JavaScript exercises last. Either way, click on the link below for Lab 7 / Part 1 to see the details for each program._  

In [Lab 7 / Part 1](/Goldford-MTEC1003-OL04/labs/07/lab-07-part1-javascript-conditionals.html){:target="_blank"}, you made 3 programs that returned different results depending on user input:  

  1. cake.html  
  2. spanish.html  
  3. oddcalc.html  

Using your own knowledge of Python, aided in part by this week's ["Booleans + Conditionals" slides](https://einbahnstrasse.github.io/MTEC1003-OL04-slides/slides/python.conditionals.tutorial.v01/#/){:target="_blank"}, translate your 3 HTML/JavaScript programs into Python, and save them as: cake.py, spanish,py, and oddcalc.py.

Make sure they're in your **/lab-07-conditionals** repository!

Now we just have to **test** our python scripts by running them on the command line.

Back in Terminal, simply type `python`, then a space, and then drag-and-drop one of your new files, e.g. **cake.py**, onto the Terminal window (**remember:** this will quickly create a `full path` to your file on the command line!). Run the command by hitting `enter`, of course.

Make sure your file is included in your **/lab-07-conditionals** repo, and don't forget to **add**, **commit**, and **push** your changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

* * *   

<a id="reminders-user"></a>
## 2. Reminders (User Input)  

Write a Python program that:
* asks the user for the current hour (but in military time: 0-23), then  
* converts the number from a string to a float,  
* sets up a series of conditions based on the current time, and  
* prints one of the following **reminders:**  

<div class="schedulingtable">
<table>
<colgroup>
<col width="15%" />
<col width="85%" />
</colgroup>
<thead>
<tr class="header">
<th>Hour</th>
<th>Reminder</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">0 to 5</td>
<td markdown="span">"It's early. You should be sleeping!"</td>
</tr>
<tr>
<td markdown="span">5 to 7</td>
<td markdown="span">"Wake up, brew that coffee, get that mile run in, and get that breakfast..."</td>
</tr>
<tr>
<td markdown="span">7 to 9</td>
<td markdown="span">"Time to go to work."</td>
</tr>
<tr>
<td markdown="span">9 to 12</td>
<td markdown="span">"You should be working!"</td>
</tr>
<tr>
<td markdown="span">12 to 13</td>
<td markdown="span">"Take your lunch break!"</td>
</tr>
<tr>
<td markdown="span">13 to 17</td>
<td markdown="span">"Do you feel that afternoon lull?"</td>
</tr>
<tr>
<td markdown="span">17 to 19</td>
<td markdown="span">"Time to hit the gym..."</td>
</tr>
<tr>
<td markdown="span">19 to 21</td>
<td markdown="span">"Gotta eat that dinner."</td>
</tr>
<tr>
<td markdown="span">21 to 23</td>
<td markdown="span">"Get that SLEEP. And rePEAT!"</td>
</tr>
<tr>
<td markdown="span">any other hour</td>
<td markdown="span">"You didn't type an acceptable value! (0-23)"</td>
</tr>
</tbody>
</table>
</div>

Save your code, calling it **reminders.v01.py**.

Save your code, make sure your **reminders.v01.py** file is included in your **/lab-06-review** folder, and don't forget to **add**, **commit**, and **push** your changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

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

  {% highlight py %} import sys {% endhighlight %}

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
