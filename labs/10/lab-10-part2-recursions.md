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
1. <a href="#hny">Happy New Year!</a>
2. <a href="#timing">Adding Timing and Interactivty</a>
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

<span style="color: red;">_You should already have your repository set up after completing Lab 10 / Part 1.<br>Instructions reappear below as a reminder:_</span>   

_Note that_ **ALL FILES MUST BE CREATED IN A NEW LAB 10 REPOSITORY!**  
* On GitHub, create and name your new repository <span style="color: tomato;">**lab-10-more-loops**</span> and <span style="color: tomato;">**clone**</span> it inside your <span style="color: tomato;">**/mtec1003**</span> folder.  
* Use your _**git cheatsheets**_ and the walkthrough(s) from previous lab(s) as references for how to do this!  
* You may find it particularly time-saving to set up your repositories using the method described in [Lab 5 / Part 1.](https://einbahnstrasse.github.io/Goldford-MTEC1003-OL04/labs/05/lab-05-part1-js-basics.html){:target="_blank"}  

Once you've done this, you're all set.  

* * *  

<a id="hny"></a>
## 1. Happy New Year!  

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

#### A Side-Note About `let`  

By using `let`, we're telling JavaScript to create a <span style="color: tomato;">local variable</span> with a special property known as [block scope.](https://www.w3schools.com/js/js_let.asp){:target="_blank"} That means our variable `nextNumber` can only be accessed from within this block of code. You might find this feature really helpful in your future JavaScript adventures...  

#### Setting Up the Base Case    

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
else {
  console.log("HAPPY NEW YEAR!");
}{% endhighlight %}

#### A Side-Note About Checking Your Braces  

Make sure your code is written properly in all the correct braces & code blocks. Use your text editor to make sure you've gotten this correct: Put your cursor on any open brace and notice how it <span style="color: tomato;">highlights</span> for you the corresponding closing brace. Use this to be sure you've enclosed all statements properly in their correct braces!  

#### Calling Your Function  

{:start="8"}
8. So far you've <span style="color: tomato;">definined</span> your function. You just need to <span style="color: tomato;">call</span> it. Let's run a countDown from 10 seconds. _Below & outside of your function definition,_ i.e. on the next line, call it with an argument of 10:  

{% highlight javascript %}
countDown(10);{% endhighlight %}

Example JavaScript Console output should resemble the following:

<img src="/Goldford-MTEC1003-OL04/assets/hny.jsconsole.output.png" alt="HNY Example Output">  

* **Save** your HMTL/JavaScript file, and make sure to **test** it using Google Chrome's JavaScript Console.  
* Once you know it works, recreate a version of this in Python:  
  - In your text editor, create a new file called **happynewyear.py** in your **lab-10-more-loops** repository.  
  - Don't bother setting up HTML tags; no need for this in Python!  
  - Repeat steps 3-8 above, carefully recalling how Python syntax differs from JavaScript (_e.g. how will you ask the user for input in Python?_).  
  - **Save** your Python script, and make sure to **test** it by running Python on your Terminal's command line.  
* Use git **status**, **add**, **commit**, and **push** to version your two files and submit them.  

* * *

<a id="timing"></a>
## 2. Adding Timing and Interactivity?

1. Using your text editor, create a new file called **whichfloor.html** in your **lab-10-more-loops** repository.  
2. Set up an HTML file, and add <span style="color: tomato;">`<script>`</span> tags… start writing your JavaScript between the tags.  
3. **Declare** a variable called <span style="color: tomato;">`maximum_stories`</span> and **initialize** it with a **value** of your choice. In other words: Decide how many floors your building should have.  
3. Ask the user which floor they work on (_"On what floor of the building is your office?"_).  
4. If the user enters a number _greater than_ <span style="color: tomato;">`maximum_stories`</span>, format + print an <span style="color: tomato;">**error message**</span> telling the user:  
  - what number they entered,  
  - how many floors are in the building, and  
  - ask them to enter a valid number.  
5. Print this same message to the JavaScript Console; so that we we can keep a record of what the user entered.  
6. If the user enters a valid number, format + print some kind of _"Congratulations!"_ message.  
7. Use a <span style="color: tomato;">_**while loop**_</span> to accomplish this. Your loop should keep asking the user to enter a satisfactory number and should do so for as many times as necessary; until finally the user returns a number within the bounds of your <span style="color: tomato;">`maximum_stories`</span> variable.  
8. **Save** your HMTL/JavaScript file, and make sure to **test** it using the JavaScript Console.
9. Try **initializing** your program with different values for your <span style="color: tomato;">`maximum_stories`</span> variable. For example, if you original set `maximum_stories` to a value of 10, increase it to 20 or some other value of your choice. Change this number at the start of your JavaScript program, **save** your HTML file in the text editor and **refresh** your program in Chrome. **Test** to make sure that your new values are reflected in the error messages thrown by your **while loop** program.  

Example JavaScript Console output should resemble the following:  

<img src="/Goldford-MTEC1003-OL04/assets/stories.example.png" alt="Stories Example Output" width="600">  

* Once you know it works, recreate a version of this in Python:  
  - In your text editor, create a new file called **whichfloor.py** in your **lab-10-more-loops** repository.  
  - Don't bother setting up HTML tags; no need for this in Python!  
  - Repeat steps 3-9 above, carefully recalling how Python syntax differs from JavaScript (_e.g. how will you ask the user for input in Python?_).  
  - **Save** your Python script, and make sure to **test** it by running Python on your Terminal's command line.  
* Use git **status**, **add**, **commit**, and **push** to version your two files and submit them.  

Make sure all your files are included in your **lab-10-more-loops** repo folder, and don't forget to **add**, **commit**, and **push** any additional changes! Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

At the end of Lab 10 / Part 1, your **lab-10-more-loops** folder should include the following files:  
  * gimmymynumber.html  
  * gimmymynumber.py  
  * whichfloor.html  
  * whichfloor.py  

When finished, move on to [Lab 10 / Part 2: Python + JavaScript Recursions](/Goldford-MTEC1003-OL04/labs/10/lab-10-part2-recursios.html){:target="_blank"}

* * *
