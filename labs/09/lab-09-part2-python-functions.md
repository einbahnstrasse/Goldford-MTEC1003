---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
<!-- http://www.iangoodfellow.com/blog/jekyll/markdown/tex/2016/11/07/latex-in-markdown.html -->

# Lab 9 / Part 2: Python Functions   

<p>Note that <span style="color: red"><strong>ALL SOLUTIONS TO THESE PROBLEMS MUST BE SHOWN IN THE FORM OF A FUNCTION DEFINITION AND A CALL TO THAT FUNCTION.</strong></span></p>

#### C O N T E N T S  
<a href="#setup">Setup for Python3</a>  
1. <a href="#js-stuff">Recreating JavaScript Functions Exercises in Python</a>  

* * *

<a id="setup"></a>
## Setup for Python3   

Let's be sure your Terminal session will run Python3 (instead of the prepackaged Python 2.7.x) when calling `python` on the command line. We can create an "alias" for python3 by running the following command:  

  {% highlight terminal %}
  $ alias python=/usr/local/bin/python3 {% endhighlight %}

Alternatively, you can simply run `python3` in the Terminal instead of `python`, but this gets annoying after awhile.  

Once you've done this, you're all set.  

* * *  

<a id="js-stuff"></a>
## 1. Recreating JavaScript Functions Exercises in Python    

_**NOTE:** This section starts with the same exercises from Lab 9 / Part 1. If you feel more comfortable with Python rather than JavaScript, you can start with this section in Python and then complete the JavaScript exercises last. Either way, click on the link below for Lab 9 / Part 1 to see the details for each program._  

In [Lab 9 / Part 1](/Goldford-MTEC1003-OL04/labs/09/lab-09-part1-js-functions.html){:target="_blank"}, you made 4 programs:  

  1. greetings.html  
  2. pluralize.html  
  3. double.html  
  4. factorial.html

Using your knowledge of Python, aided in part by this week's [Python Function Definitions + Calls](https://einbahnstrasse.github.io/MTEC1003-OL04-slides/slides/functions.tutorial.v01/#/){:target="_blank"} slides, translate your HTML/JavaScript programs into Python and save them as: **greetings.py, pluralize,py, double.py,** and **factorial.py.**  

Make sure they're in your **/lab-09-functions** repository!

Now we just have to **test** our python scripts by running them on the command line.

Back in Terminal, simply type `python`, then a space, and then drag-and-drop one of your new files, e.g. **pluralize,py**, onto the Terminal window (**remember:** this will quickly create a `full path` to your file on the command line!). Run the command by hitting `enter`, of course.

Make sure your file is included in your **/lab-09-functions** repo, and don't forget to **add**, **commit**, and **push** your changes. Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it.  

* * *   

At the end of this lab, your **/lab-09-functions** folder should contain the following files:  
  * greetings.html  
  * greetings.py  
  * pluralize.html  
  * pluralize.py  
  * factorial.html  
  * factorial.py  

* * *
