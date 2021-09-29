---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
<!-- http://www.iangoodfellow.com/blog/jekyll/markdown/tex/2016/11/07/latex-in-markdown.html -->

# Lab 10 / Part 1: While Loops in Python + JavaScript  

#### C O N T E N T S  
<a href="#setup">Setup for Python3</a>  
<a href="#repo">Setting Up Your Lab 10 Repository</a>
1. <a href="#gimmy">Gimmy My Number</a>
2. <a href="#stories">Which Floor Do You Work On?</a>
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

_ProTip:_ **Bookmark the following page so that you can easily repeat these steps in your future labs!**  
* [Cloning a Remote Repo Using Your _GitHub_ API Access Token](https://einbahnstrasse.github.io/Goldford-MTEC1003-OL78/labs/04/cloning.with.token.v01.html){:target="_blank"}   
* On _GitHub_, create and name your new repository **lab-10-more-loops** and **clone** it inside your **/mtec1003** folder.  
* Once you've completed the steps at the link above, you're ready to begin.  
* Open up your text editor (e.g. Atom, Sublime Text, etc.)...  
* Note: **ALL FILES YOU CREATE BELOW MUST BE SUBMITTED IN YOUR NEW REPOSITORY THIS WEEK.**  

* * *  

<a id="gimmy"></a>
## 1. Gimmy My Number    

1. Using your text editor, create a new file called **gimmymynumber.html** in your **lab-10-more-loops** repository.  
2. Set up an HTML file, and add <span style="color: tomato;">`<script>`</span> tags… start writing your JavaScript between the tags.  
3. Ask the user for a number greater than 100 (_"Gimmy a number greater than 100 plz..."_).  
4. If the user enters a number _greater than_ 100, congratulate them! (_“_<span style="color: tomato;">`<number>`</span> _is greater than 100! Good work."_).  
5. But if they enter a number **less** than 100, ask again (_“This number is less than 100, dummy. Try again... I've got all day…”_).  
6. Use a <span style="color: tomato;">_**while loop**_</span> to accomplish this. Your loop should keep asking the user to enter a satisfactory number, and it should do so for as many times as necessary; until finally the user returns a number greater than 100.  

Example JavaScript Console output should resemble the following:  

<img src="/Goldford-MTEC1003-OL78/assets/gimmymynumber.example.png" alt="Gimmy Example Output" width="600">  

<!-- <iframe src="{{ site.baseurl }}/labs/10/gimmymynumber.example.png" width="600px" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> -->

<!-- <img src="/Goldford-MTEC1003-OL04/labs/02/img/submit.lab2.v2.png"> -->

* **Save** your HMTL/JavaScript file, and make sure to **test** it using Google Chrome's JavaScript Console.  
* Once you know it works, recreate a version of this in Python:  
  - In your text editor, create a new file called **gimmymynumber.py** in your **lab-10-more-loops** repository.  
  - Don't bother setting up HTML tags; no need for this in Python!  
  - Repeat steps 3-6 above, carefully recalling how Python syntax differs from JavaScript (_e.g. how will you ask the user for input in Python?_).  
  - **Save** your Python script, and make sure to **test** it by running Python on your Terminal's command line.  
* Use git **status**, **add**, **commit**, and **push** to version your two files and submit them.  

* * *

<a id="stories"></a>
## 2. Which Floor Do You Work On?  
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

<img src="/Goldford-MTEC1003-OL78/assets/stories.example.png" alt="Stories Example Output" width="600">  

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
