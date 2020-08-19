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
3. <a href="#mod-reminders">Modified Reminders</a>

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
## 1. This flowchart is harder than it looks      

Our goal for this lab will be to turn the following flowchart into a Python or JavaScript program. It will be a program consisting of a series of _conditional statements:_  

<img src="/Goldford-MTEC1003-OL04/labs/07/engineering-flow-chart.png" alt="engineering flow chart" width="500" height="400">
[view source](https://cacoo.com/blog/12-funny-flowcharts-help-navigate-lifes-toughest-decisions/){:target="_blank"}

But... do you notice anything different? Do you see the "branching" effect of this flowchart? How you answer the 1st question determines the "path" taken along the chart, and how you answer the 2nd question will determine 1 of 4 possible "final" outcomes.  

To accomplish this, we'll need to talk about writing _multiple_ conditional statements and, most importantly, _nesting_ our conditions within one another...

## 1. Nesting brackets in JS  

In your text editor (Atom, Sublime Text, etc.), make a new file and save it with the name **nesting.js** inside your **/lab-07-conditionals** folder, so that it immediately gives us the proper highlighting syntax.  

On line 1, type a **left curly bracket** &#8594; `{`  

Notice what happens:

{% highlight js %}{}{% endhighlight %}

Amazing! You typed one open bracket, and it kindly autofills the closing bracket that you'll need later.  

Now, type `return` and see what happens:

{% highlight js %}{

}{% endhighlight %}

Even better! Instead of dropping one line, it drops two, and it properly places your cursor indented on the middle line, so that you're ready to type code inside your brackets. It also properly indented the closing bracket for you on the third line.  

So now, with your cursor positioned on that middle line, type _another_ **left curly bracket** &#8594; `{`  

{% highlight js %}{
  {}
}{% endhighlight %}

As expected, it properly autofills the closing bracket. Now type `return` one more time:

{% highlight js %}{
  {

  }
}{% endhighlight %}

And voilà! It properly indented things again, which helps us visualize the placement of each pair of brackets.  

We can do this endlessly, embedding one pair of brackets in another like some kind of weird obsession...  

{% highlight js %}{
  {
    {
      {
        {
          console.log("Okay, this is ridiculous. Why are we doing this??");
        }
      }
    }
  }
}{% endhighlight %}

This is called _nesting._ We can _nest_ one pair of brackets inside another.  

This means we can also _nest_ blocks of code _inside_ other blocks of code. Which is great, because we need this to reproduce the flowchart above. This is what we want!  

Try placing your cursor next to one of your left opening brackets. It should <span style="background-color: #FFFF00; color: #000000;">highlight</span> (or in many cases <ins>underline</ins>) both your opening bracket AND the corresponding closing bracket, which further helps you keep track of your code; not only does it help draw your eyes to the right place, it also makes sure you haven't forgotten your closing bracket!  






Save your code, make sure your **reminders.v02.py** file is included in your **/lab-07-conditionals** folder, and don't forget to **add**, **commit**, and **push** your changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

Your final **/lab-07-conditionals** folder by the submission deadline should include the following files:  
  * cake.html  
  * cake.py  
  * spanish.html  
  * spanish.py  
  * oddcalc.html  
  * oddcalc.py  
  * reminders.v01.py  
  * reminders.v02.py  

* * *
