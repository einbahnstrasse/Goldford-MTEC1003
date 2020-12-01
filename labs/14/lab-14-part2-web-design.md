---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Lab 14 / Part 2: Advanced Web Design Concepts  

#### C O N T E N T S  
1. <a href="#overview">Overview of This Lab</a>  
2. <a href="#diving">Creating a Page With `<div>` Containers</a>  
3. <a href="#cont">Brainstorming Content for your Website</a>  

* * *  

<a id="overview"></a>
## 1. Overview of This Lab  

In this lab, we'll make a simple website in HTML and stylize it with CSS.  

But this time, we'll employ some more advanced web design concepts by building a site that includes:  
* some interrelated pages (e.g. a main page, "About Me", "Contact", etc.)  
* a navigation menu, or "navbar" to link these pages together (with so-called "sticky" positioning)
* a "hero image" at the top of each page  
* using `<div>` (i.e. HTML _"dividers"_) to separate and place content on a page  
* custom font integration using Google Fonts  
* building a custom color scheme for your site using Adobe Color  

In order to do this, start by creating a new repository on _GitHub_. Call it **lab-14-part2-site** and then **CLONE** it onto your local machine inside your **/mtec1003** folder. (As always, use your knowledge of git and all of your previous references in order to do this.)   

* * *   

<a id="diving"></a>
## 2. Creating a Page With `<div>` Containers  

In your new **/lab-14-part2-site** repository, start by creating a new HTML file and immediately save it as **index.html.  

This will be the front page of your site; i.e. your "home page."  

Type "HTML" + the `TAB` key to generate a boilerplate HTML document.  

Inside your `<head>` tag, and in between the `<title></title>`, type the title of your page: "My Home Page".  

Now, inside your page's `<body>` tag, make 4 identical `<div>` elements. These will simply act as "containers" for different parts of your page: in this case, we'll be posting text elements inside each `<div>` and positining them later with CSS.  

So far your HTML source should look like this:  

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Home Page</title>
  </head>
  <body>
    <div>Divider1</div>
    <div>Divider2</div>
    <div>Divider3</div>
    <div>Divider4</div>
  </body>
</html>
{% endhighlight %}


* * *   

<a id="cont"></a>
## 3. Brainstorming Content for your Website  

For each of the pages **Home**, **About Me**, and at least 1 **Portfolio page**, start **brainstorming** ideas for **content** that will appear on your site.

Think of what you want the viewer to see when they first see your **Home** page, how you want to present yourself in your **About Me**, and what among your own projects, or professional interests, you'd want to present on any of your **Portfolio page**. Write out some initial ideas...  

In your Terminal, navigate to your **/lab-12-html** repository, and create a new folder inside of it. _(Remember: What command will you use to create a new folder?)_ Call this folder **/final-project-brainstorming**. Change your directory so that your Terminal is inside this folder. Verify you're in the correct location by running **pwd**. Your path should look something like this:

`/Users/[yourUserName]/myClasses-Fall2020/mtec1003//lab-12-html/final-project-brainstorming`

In your text editor (e.g. SublimeText, Atom, VS Code, etc.), create 3 new text documents (.txt) and save them in your **/final-project-brainstorming** folder, which is within your **/lab-12-html** repository, using the following names:
* **brainstorming-01-home-page.txt**  
* **brainstorming-02-about-me.txt**  
* **brainstorming-03-portfolio-v01.txt**  

In each of these files, type out your ideas for the content on each of the pages of your site. For example, in **brainstorming-02-about-me.txt**, type out a 1-2 paragraph **biography** with information about your education, work experience, your professional expertise or goals. Think about how you want to present yourself to a future employer, a future scholarship committee, an art gallery, on a graduate school application, etc. _Put your best foot forward!_  

Do the same for the **brainstorming-01-home-page.txt** and **brainstorming-03-portfolio-v01.txt**. What is the first thing you want them to see when they load your site in the browser? What pieces of your work would you want to present?

Each of these text files should contain _at least 1-2 paragraphs of text explaining your initial ideas_ and/or draft of body text to be published on your website.

Keep in mind: _You can change the contents of your site later!_ You don't need to turn in 100% complete ideas yet! Right now, the idea is to brainstorm and have at least a first draft of the site — that way, when we begin coding it later, you'll already have content to drop in! You can always revise this content later, add, or change things as we move forward...

* * *   

Make sure your files is included in your **/lab-12-html** folder, and don't forget to **add**, **commit**, and **push** your changes!  
Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

Your final **/lab-12-html** folder by the submission deadline should include the files from parts 1 + 2 of the Week 12 Labs, plus the new folder **/final-project-brainstorming** containing the **3 text files** described above.  

* * *  