---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
<!-- http://www.iangoodfellow.com/blog/jekyll/markdown/tex/2016/11/07/latex-in-markdown.HTML -->

# Lab 7 / Part 3: Nesting Conditional Statements  

In this lab you'll:
- be interpreting a flowchart with multiple possible outcomes to questions, and  
- nesting conditional statements based on the direction of the arrows in the flowchart.  

#### C O N T E N T S  
<a href="#setup">Setup for Python3</a>  
1. <a href="#hard-flowchart">This flowchart is harder than it looks.</a>  
2. <a href="#nest-brackets">Nesting Brackets in a Text Editor (in JavaScript)</a>
3. <a href="#nest-states">Nesting conditional statements</a>
4. <a href="#version-py">The Python version</a>

* * *

<a id="setup"></a>
## Setup for Python3   

Let's be sure your Terminal session will run Python3 (instead of the prepackaged Python 2.7.x) when calling `python` on the command line. We can crete an "alias" for python3 by running the following command:  

  {% highlight terminal %}
  $ alias python=/usr/local/bin/python3 {% endhighlight %}

Alternatively, you can simply run `python3` in the Terminal instead of `python`, but this gets annoying after awhile.  

Once you've done this, you're all set.  

* * *  

<a id="hard-flowchart"></a>
## 1. This flowchart is harder than it looks.      

Our goal for this lab will be to turn the following flowchart into a Python or JavaScript program. It will be a program consisting of a series of _conditional statements:_  

<img src="/Goldford-MTEC1003-OL04/labs/07/engineering-flow-chart.png" alt="engineering flow chart" width="600">  
[view source](https://cacoo.com/blog/12-funny-flowcharts-help-navigate-lifes-toughest-decisions/){:target="_blank"}

But... do you notice anything different? Do you see the "branching" effect of this flowchart? How you answer the 1st question determines the "path" taken along the chart, and how you answer the 2nd question will determine 1 of 4 possible "final" outcomes.  

To accomplish this, we'll need to talk about writing _multiple_ conditional statements and, most importantly, _nesting_ our conditions within one another...  

* * *

<a id="nest-brackets"></a>
## 2. Nesting Brackets in a Text Editor (in JavaScript)  

In your text editor (Atom, Sublime Text, etc.), make a new file and save it with the name **nesting.js** inside your **/lab-07-conditionals** folder, so that it immediately gives us the proper highlighting syntax.  

On line 1, type a **left curly bracket** &#8594; `{`  

Notice what happens:

{% highlight js %}{}{% endhighlight %}

Amazing! You typed one open bracket, and it kindly autofills the closing bracket that you'll need later.  

Now, press `return` and see what happens:

{% highlight js %}{

}{% endhighlight %}

Even better! Instead of dropping one line, it drops two, and it properly places your cursor indented on the middle line, so that you're ready to type code inside your brackets. It also properly indented the closing bracket for you on the third line.  

So now, with your cursor positioned on that middle line, type _another_ **left curly bracket** &#8594; `{`  

{% highlight js %}{
  {}
}{% endhighlight %}

As expected, it properly autofills the closing bracket. Now press `return` one more time:

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

* * *

<a id="nest-states"></a>
## 3. Nesting conditional statements  

Let's use this technique to nest different "layers" of conditions.  

Close the file you were working with (you can delete it, honestly. We won't need **nesting.js** for the lab.)  

Set up a _new_ HTML file as you usually do, and open up `<script></script>` tags. Call this one **flowchart.HTML**.  

Now, make your first (i.e. "outer") conditional statement by typing the following:  

{% highlight js linenos %}var move = prompt("Does it move? (yes/no)");
if (move == "yes") {
  [our 1st "then" clause here];
} else if (move == "no") {
  [our 2nd "then" clause here];
} else {
  console.log("Answer my question! You didn't type yes or no.");
}{% endhighlight %}

Notice that we defined the variable `move`, which will store the string `"yes"` or `"no"` and serve as our _boolean value._  

So, what will our “then” clauses look like inside these brackets, i.e. on lines 3 and 5?  

Check the original flowchart and notice that _another if/then/else conditional_ will be needed to serve as the "then" clause in _each_ of our "if" and "else if" statements. The "if" and "else if" portions are the yes/no responses to our first question, "Does it move?" Notice there's one other possibility: that the user neither types "yes" or "no" but some unacceptable response. This scenario becomes our final "else" statement.  

So this means we need to "nest" or "embed" another set of conditions _inside_ our first (i.e. "outer") condition. The outcome of the question "Does it move?" will determine what question comes next, as the flowchart shows us.  

Repeat these steps to create the _same format_ for the code above:  

{% highlight js linenos %}var move = prompt("Does it move? (yes/no)");
if (move == "yes") {
  var should = prompt("Should it? (yes/no)");
  if (should == "yes") {
    [another 1st "then" clause];
  } else if (should == "no") {
    [another 2nd "then" clause];
  } else {
    console.log("Answer my question! You didn't type yes or no.");
  }
} else if (move == "no") {
  [our 2nd "then" clause here];
} else {
  console.log("Answer my question! You didn't type yes or no.");
}{% endhighlight %}

Now we've got our first "inside" condition planted firmly inside the outer "if" statement, i.e. lines 3-10 above. Look again at the flowchart to see what the "then"/consequent statements should be on lines 5 and 7. One should print "no problem" and the other should tell us something about duct tape, according to the picture.  

Fill in these missing “then” clauses like so:  

{% highlight js linenos %}var move = prompt("Does it move? (yes/no)");
if (move == "yes") {
  var should = prompt("Should it? (yes/no)");
  if (should == "yes") {
    console.log("No problem");
  } else if (should == "no") {
    console.log("Then use duct tape!!!");
  } else {
    console.log("Answer my question! You didn't type yes or no.");
  }
} else if (move == "no") {
  [our 2nd "then" clause here]
} else {
  console.log("Answer my question! You didn't type yes or no.");
}{% endhighlight %}

Notice on line 3 above that we defined a new variable `should` to store the _boolean value_ for the question "Should it?", followed by another _if/then/else conditional statement._  

We're almost done. We just need to repeat these steps and fill in the last of our "inner" conditions, i.e. to expand line 12 above. By this we mean coding up the _right_ side of our flowchart; i.e. what happens if the user answers "no" to our first question, "Does it move?"  

Can you finish the flowchart by _nesting_ one last series of conditions? Give it a try, test it in Chrome, save your code, make sure your **flowchart.HTML** file is included in your **/lab-07-conditionals** folder, and don't forget to **add**, **commit**, and **push** your changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.HTML){:target="_blank"} if you need it!  

* * *

<a id="version-py"></a>
## 4. The Python version

Doing it in JavaScript first make it totally clear what the boundaries of our conditions are — thanks to the brackets JavaScript requires. We can easily make the same program in Python, but it's slightly more confusing without the brackets. You probably already know that instead of brackets and semicolons, Python uses indentation and the colon.  

Recall the basic formula for a conditional statement in Python:  

{% highlight py linenos %}myVar = input("What is your answer? yes/no")  
if myVar == "yes":
  [our 1st "then" clause here]
elif myVar == "no":
  [our 2nd "then" clause here]
else:
  print("Answer my question! You didn't type yes or no."){% endhighlight %}

With this in mind, make a new file and call it **flowchart.py**. Rewrite the code above to recreate the first ("outer") question of our flowchart, "Does it move?" but using Python syntax.  

Then, create the first "nested" condition in Python, beginning on line 3 above, being careful about the indentation:  

{% highlight py linenos %}myVar = input("What is your answer to my 1st question? (yes/no) ")  
if myVar == "yes":
  myNextVar = input("What is your answer to my 2nd question? (yes/no) ")
  if myNextVar == "yes":
    [another 1st "then" clause]
  elif myNextVar == "no":
    [another 2nd "then" clause]
  else:
    print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
  [our 2nd "then" clause here]
else:
  print("Answer my question! You didn't type yes or no."){% endhighlight %}

See how the precise level of indentation in Python mimics the exact placement of brackets in JavaScript?  

In particular, notice how the indent of line 8 ("else:") compares to line 10 ("elif myVar == 'no'"). Line 8 is indented by one `tab` farther than line 10, which means line 10 is part of the _outer condition._  

Can you finish the flowchart by filling in the right variable names and consequences, then _nesting_ your last conditions using Python syntax? Give it a try, test it in the Termianl, save your code, make sure your **flowchart.py** file is included in your **/lab-07-conditionals** folder, and don't forget to **add**, **commit**, and **push** your changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.HTML){:target="_blank"} if you need it!

Your final **/lab-07-conditionals** folder by the submission deadline should include the following files:  
  * cake.html  
  * cake.py  
  * spanish.html  
  * spanish.py  
  * oddcalc.html  
  * oddcalc.py  
  * reminders.v01.py  
  * reminders.v02.py  
  * flowchart.html    
  * flowchart.py  

* * *
