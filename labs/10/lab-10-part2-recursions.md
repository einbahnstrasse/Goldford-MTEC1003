---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
<!-- http://www.iangoodfellow.com/blog/jekyll/markdown/tex/2016/11/07/latex-in-markdown.html -->

# Lab 10 / Part 2: Python + JavaScript Recursions     

#### C O N T E N T S  
<a href="#setup">Setup for Python3</a>  
<a href="#repo">Setting Up Your Lab 10 Repository</a>
1. <a href="#hny">Happy New Year! (in JavaScript)</a>
2. <a href="#timing">Add Timing + Interactivity</a>
3. <a href="#hanoi">The Tower of Hanoi (in Python)</a>
<!-- 4. <a href="#bmi">Calculating Body Mass Index  (BMI) in Python</a> -->

* * *

<a id="setup"></a>
## Setup for Python3   

Let's be sure your Terminal session will run Python3 (instead of the prepackaged Python 2.7.x) when calling `python` on the command line. We can crete an "alias" for python3 by running the following command:  

  {% highlight terminal %}
  $ alias python=/usr/local/bin/python3 {% endhighlight %}

Alternatively, you can simply run `python3` in the Terminal instead of `python`, but this gets annoying after awhile.  

* * *  

<a id="repo"></a>
## Setting Up Your Lab 10 Repository  

<span style="color: red;">_You should already have your repository set up after completing Lab 10 / Part 1._</span>   

* * *  

<a id="hny"></a>
## 1. Happy New Year! (in JavaScript)  

1. Using your text editor, create a new file called **happynewyear.html** in your **lab-10-more-loops** repository.  
2. Set up an HTML file, and add <span style="color: tomato;">`<script>`</span> tags… start writing your JavaScript between the tags.  
3. Start by <span style="color: tomato;">defining</span> a new _**recursive function**_. Name this function `countDown`. It should take one <span style="color: tomato;">argument</span>; name this argument `start`. Don't forget to **add braces** (_we'll write our function's **statements** inside this code block!_):  

{% highlight javascript %}
function countDown(start) {
  } {% endhighlight %}

{:start="4"}
4. Our function will take a `start` number, then count from that number down to 1, and finally will print "HAPPY NEW YEAR!". To do this, start by printing the current value of `start` on the console. Make this the first line inside your function's braces:  

{% highlight javascript %}
console.log(start); {% endhighlight %}

{:start="5"}
5. On the next line, let's create a <span style="color: tomato;">local variable</span> that cannot be accessed anywhere else in our program; only from inside our function. We'll name this variable `nextNumber` and use it to designate the _**"next"**_ number in our count down. Type the following on the next line:  

{% highlight javascript %}
let nextNumber = start - 1; {% endhighlight %}

We'll use this line of code to **decrement** our `start` variable, one-by-one, until we reach our **base case**...  

### A Side-Note About `let`  

By using `let`, we're telling JavaScript to create a <span style="color: tomato;">local variable</span> with a special property known as [block scope.](https://www.w3schools.com/js/js_let.asp){:target="_blank"} That means our variable `nextNumber` can only be accessed from within this block of code. You might find this feature really helpful in your future JavaScript adventures...  

### Setting Up the Base Case    

{:start="6"}
6. Next, we'll use a _**conditional statement**_ to make our base case. Create an <span style="color: tomato;">_**if** clause_</span> followed by an <span style="color: tomato;">_**else** clause_</span>. Use the <span style="color: tomato;">_**if** clause_</span> to control what happens in your function for all values of `nextNumber` that are _greater than_ 0. Within this code block, our function will <span style="color: tomato;">_**continually call itself**_</span>, implementing our **recursion**. Type this clause like so:  

{% highlight javascript %}
if (nextNumber > 0) {
    countDown(nextNumber);
} {% endhighlight %}

It's important to note that the condition specified by the <span style="color: tomato;">_**if** clause_</span>:  

{% highlight javascript %}
(nextNumber > 0){% endhighlight %}

designates our **base case**. As long as `nextNumber` continues to be _greater than 0_, the function will keep calling itself, reducing its local variable by 1. But once this condition is no longer `true`, the function will stop.  

{:start="7"}
7. Now, inside the <span style="color: tomato;">_**else** clause_</span>, imagine that you've counted down all the way to 1. What happens when the ball finally drops on New Year's Eve, after the counting...?

{% highlight javascript %}
} else {
  console.log("HAPPY NEW YEAR!");
}{% endhighlight %}

### A Side-Note About Checking Your Braces  

Make sure your code is written properly in all the correct braces & code blocks. Use your text editor to make sure you've gotten this correct: Put your cursor on any open brace and notice how it <span style="color: tomato;">highlights</span> for you the corresponding closing brace. Use this to be sure you've enclosed all statements properly in their correct braces!  

### Calling Your Function  

{:start="8"}
8. So far you've <span style="color: tomato;">definined</span> your function. You just need to <span style="color: tomato;">call</span> it. Let's run a countDown from 10 seconds. _Below & outside of your function definition,_ i.e. on the next line, call it with an argument of 10:  

{% highlight javascript %}
countDown(10);{% endhighlight %}

Example JavaScript Console output should resemble the following:

<img src="/Goldford-MTEC1003/assets/hny.jsconsole.output.png" alt="HNY Example Output" width="200px">  

* **Save** your HMTL/JavaScript file, and make sure to **test** it using Google Chrome's JavaScript Console.  
* For this exercise, you DON'T need to create a Python version!!  
* Use git **status**, **add**, **commit**, and **push** to version your file and submit it.  
* Since we'll be making changes and adding to this file, **commit** your file with a **message** resembling this:  

{% highlight terminal %}
$ git commit -m "first version of happynewyear.html"{% endhighlight %}

Now, let's make some changes that will make our count down a much cooler experience...

* * *

<a id="timing"></a>
## 2. Add Timing + Interactivity  

When you imagine a proper New Year's Eve count down, though, isn't it true that we count down _one second at a time_ until all the seconds have passed, and it's time for the ball to drop? Let's add this timing feature, so that we don't get our entire count down in the console at once, but instead: one number at a time, with a 1-second delay between each number, all the way down to our final _"Happy New Year!"_ message at the end.

First, let's make sure we're all on the same page. Your 1st version of the file should look like this:  

{% highlight html linenos %}
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <script>
      function countDown(start) {
          console.log(start);

          let nextNumber = start - 1;

          if (nextNumber > 0) {
              countDown(nextNumber);
          } else {
            console.log("HAPPY NEW YEAR!");
          }
      }
      countDown(10);
    </script>
  </body>
</html>{% endhighlight %}

If your code doesn't yet look like this, make the necessary changes & corrections to be sure it's working before moving on. <span style="color: tomato;">_Your line numbers do not have to match mine,_</span> but for ease of communication, I'll be referring to the line numbers above for the rest of this exercise...  

### Asking the User  

By now, you should remember how to ask the user for input. We want to ask the user how many seconds there are until New Year's Eve. Then, we'll **pass** this as an **argument** to our function, which will count down from a user-supplied number. _Where do you think we should ask for user input?_ If you guessed between the function definition and call, then you're right!

{:start="9"}
9. Insert a new line 20, between the function **definition** and its **call**, and ask the user for input:
  - **Declare** a new variable for this user input. You can call it `count`.
  - Set it equal to a prompt. Ask them _"How many seconds there are until New Year's Eve?"_ or something like that.
  - Don't forget to **convert** the user response to an integer.
  - You can do _all of this_ in 1 line of code. Can you think of how to do it?
10. User input will be stored inside your new variable. **Pass** this to your function **call** as its argument.
  - _(HINT: You don't need to make a new line of code for this step! You just need to change the function call, i.e. line 20.)_  
11. **Test** this by **reloading** your file in Chrome.  
  - First you should see the prompt. Enter a number.  
  - Then, your function should count down from this number. Check the Console to be sure.  
  - Reload the page and try different numbers to be sure it's working.  

* Use git **status**, **add**, **commit**, and **push** to update your file.  
* Your **commit message** can resemble this:  

{% highlight terminal %}
$ git commit -m "adding user input feature to happynewyear.html"{% endhighlight %}

### Add a Time Delay  

One last feature to add! We want the numbers to count down like we do in real life: 1 second at a time.  

{:start="12"}
12. Inside your <span style="color: tomato;">_**if** clause_</span> let's add a delay by making a change on line 15. On this line, we'll use the JavaScript function [setTimeout()](https://www.w3schools.com/jsref/met_win_settimeout.asp){:target="_blank"} to make sure our new `countDown()` function calls itself with a 1-second delay.

JavaScript's [setTimeout()](https://www.w3schools.com/jsref/met_win_settimeout.asp){:target="_blank"} function works like this:

{% highlight javascript %}
setTimeout(function, milliseconds, param1, param2, ...){% endhighlight %}

where `function` will be the name of a function to be called after a specific time delay (in our case, this will be our `countDown` function), and `milliseconds` is the time delay (for us, we're targeting 1 second, or 1000 milliseconds).

The optional parameters `param1` and `param2` are placeholders for any **arguments** we must **pass** to our named function (i.e. `countDown`).  What was that variable we passed to `countDown()` written in our original line 15? That variable will substitute `param1` in the formula above.

So, change line 15 so that it looks like this (i.e. inside your <span style="color: tomato;">_**if** clause_</span>):

{% highlight javascript %}
if (nextNumber > 0) {
    setTimeout(countDown, 1000, nextNumber);
}{% endhighlight %}

This ensures that your function calls itself _every 1 second_.  

Let's add the same delay to our final _"Happy New Year!"_ message. Inside your <span style="color: tomato;">_**else** clause_</span>, change line 17 to the following:  

{% highlight javascript %}
} else {
  setTimeout(function(){console.log("HAPPY NEW YEAR!");}, 1000, nextNumber);
}{% endhighlight %}

We've just **defined** a function inside the `setTimeout()` function: instead of naming a pre-existing function as the first argument to `setTimeout()`, now we've just included our original print message as its own function!  

Now, when you test your function, it should not only count down from a user-defined number of seconds; it should post each message to the console with a 1-second delay!  

* **Save** your HMTL/JavaScript file, and make sure to **test** it using Google Chrome's JavaScript Console.  
* For this exercise, you DON'T need to create a Python version!!  
* Use git **status**, **add**, **commit**, and **push** to version your file and submit it.  
* Your **commit message** can resemble this:  

{% highlight terminal %}
$ git commit -m "adding timing feature to happynewyear.html"{% endhighlight %}

* * *  

<a id="hanoi"></a>
## 3. The Tower of Hanoi (in Python)  

By now you should have watched a lovely video by Professor Thorsten Altenkirch, explaining the [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi){:target="_blank"} problem and how to implement it in Python:  

<iframe src="https://www.youtube.com/embed/8lhxIOAfDss" width="560" height="315" frameborder="0"></iframe>

Your task : <span style="color: tomato;">transcribe the Python code in this video into a working Python script.</span> Fortunately, the examples given in the video are very clear, so you should be able to watch the video again and simply type out the same code you see on your screen.

_(In the video, Prof. Altenkirch uses [Jupyter Notebook](https://jupyter.org/){:target="_blank"} to write Python in the browser, but <span style="color: tomato;">you don't need Jupyter to write your code!</span> Just like the other Python files you create for this class, make your transcription in your text editor, then debug in the Terminal.)_

So, create a new file in your text editor called **hanoi.py** and start typing the code you learn from the video. Be sure to include function **definitions** for `move()` and `hanoi()`, and don't forget a **base case** inside your `hanoi()` function!  

Your last line should **call** the `hanoi()` function exactly as he's done in the video (i.e. using the same arguments: 4, "A", "B", "C"), and should produce the following output when you run it in Terminal:  

{% highlight terminal %}
$ python3 /path/to/hanoi.py
Move disc from A to B!
Move disc from A to C!
Move disc from B to C!
Move disc from A to B!
Move disc from C to A!
Move disc from C to B!
Move disc from A to B!
Move disc from A to C!
Move disc from B to C!
Move disc from B to A!
Move disc from C to A!
Move disc from B to C!
Move disc from A to B!
Move disc from A to C!
Move disc from B to C!{% endhighlight %}

* **Save** your Python file, and make sure to **test** it on your Terminal's command line.  
* For this exercise, you DON'T need to create a JavaScript version!!  
* Use git **status**, **add**, **commit**, and **push** to version your file and submit it.  

* * *

Make sure all your files are included in your **lab-10-more-loops** repo folder, and don't forget to **add**, **commit**, and **push** any additional changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

At the end of Lab 10 / Part 2, your **lab-10-more-loops** folder should include the following files:  
  * gimmymynumber.html
  * gimmymynumber.py
  * whichfloor.html
  * whichfloor.py
  * happynewyear.v01.html
  * happynewyear.v02.html _(no Python versions of "Happy New Year!")_
  * hanoi.py _(no JavaScript version of the Tower of Hanoi example. Just transcribe the code from the video and test it in your Terminal.)_

* * *
