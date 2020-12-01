---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Lab 14 / Part 2: Advanced Web Design Concepts  

#### C O N T E N T S  
1. <a href="#overview">Overview of This Lab</a>  
2. <a href="#diving">Creating a Page With `<div>` Containers</a>    
  - <a href="#hero">Make a Container for a "Hero Image"</a>    
  - <a href="#naving">Make a Container for a Navbar</a>  
  - <a href="#textelems">Make Containers for Body Text Elements</a>  
  - <a href="#extcss">Link to an External CSS Style Sheet</a>  
3. <a href="#heroimg">Adding + Styling a Hero Image</a>  

* * *  

<a id="overview"></a>
## 1. Overview of This Lab  

In this lab, we'll make a simple website in HTML and stylize it with CSS.  

But this time, we'll employ some more advanced web design concepts by building a site that includes:  
* some interrelated pages (e.g. a main page, "About Me", "Contact", etc.)  
* a navigation menu, or "navbar" to link these pages together (with so-called "sticky" positioning)
* a "hero image" at the top of each page  
* using `<div>` (i.e. HTML _"dividers"_) to separate and position your content on a page  
* custom font integration using Google Fonts  
* building a custom color scheme for your site using Adobe Color  

In order to do this, start by creating a new repository on _GitHub_. Call it **lab-14-part2-site** and then **CLONE** it onto your local machine inside your **/mtec1003** folder. (As always, use your knowledge of git and all of your previous references in order to do this.)   

* * *   

<a id="diving"></a>
## 2. Creating a Page With `<div>` Containers  

In your new **/lab-14-part2-site** repository, start by creating a new HTML file and immediately save it as **index.html.  

This will be the front page of your site; i.e. your "home page."  

Type "HTML" + the `TAB` key to generate a boilerplate HTML document.  

Inside your `<head>` tag, and in between the `<title></title>`, type the name of your page: call it "My Home Page".  

<a id="hero"></a>
### Make a Container for a "Hero Image"

Now, inside your page's `<body>` tag, type "div" and then press the `TAB` key to format the proper tags. So far, your page should look like this:  

{% highlight html linenos %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Home Page</title>
  </head>
  <body>
    <div class="">

    </div>
  </body>
</html>
{% endhighlight %}

Now, with your cursor already positioned between the `<div>` tags you just created (i.e. on line 9 above), make _another_ set of `<div>` tags; i.e. one `<div>` within another, like so:

{% highlight html linenos %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Home Page</title>
  </head>
  <body>
    <div class="">
      <div class="">

      </div>
    </div>
  </body>
</html>
{% endhighlight %}

On line 8, between the quotation marks, create a class identifier, and call it: "hero-image". On line 9, inside the "inner" `<div>` element, create another class label by typing "hero-text" between the quotation marks.  

These two nested `<div>` elements will contain the banner image (sometimes called "hero image") that will span the top of our web page.  

Now, inside the innermost `<div>`, add the following `<h1>` and `<p>` elements:  

{% highlight html %}
<h1>Hi, I'm Tony</h1>
<h5>I'm an Immunologist</h5>
{% endhighlight %}

This text will be placed on top of our "hero image". We'll format all of this using the class selectors we've just labeled in our CSS file later...  

So far, your page with the complete "hero image" container system should look like this:  

{% highlight html linenos %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Home Page</title>
  </head>
  <body>
    <div class="hero-image">
      <div class="hero-text">
        <h1>Hi, I'm Tony</h1>
        <h5>I'm an Immunologist</h5>
      </div>
    </div>
  </body>
</html>
{% endhighlight %}

<a id="naving"></a>
### Make a Container for a Navbar  

Next, let's make containers for a "navbar" — i.e. a navigation menu — so we can easily navigate our site.  

Between lines 13 and 14, create another `<div>` as you had done before...  

But this time, delete the class selector label from the opening tag, and replace it with an ID selector. Label this one "navbar". We'll use this ID selector to style our navbar uniquely in CSS.  

Inside these div tags, add some `<a>` link elements that we'll use for each page on our site:  

{% highlight html %}
<a href="index.html">Home</a>
<a href="aboutme.html">About Me</a>
<a href="myportfolio.html">My Portfolio</a>
<a href="contact.html">Contact</a>
{% endhighlight %}

_By the way: **make sure all links and divs are properly indented!**_  

<a id="textelems"></a>
### Make Containers for Body Text Elements    

Next, make 4 identical `<div>` elements, which we'll use to place content on our home page. In this example, we'll be placing news stories inside these divs.  

Inside each, provide placeholder text by labeling them "Divider1", "Divider2", and so on:  

{% highlight html %}
<div>Divider1</div>
<div>Divider2</div>
<div>Divider3</div>
<div>Divider4</div>
{% endhighlight %}

We're going to give each of these 4 div containers **BOTH** a class selector **AND** an ID selector. Why would we do this?? The reason is simple: We want all of these divs to have some of the same styling properties in common, and for that we typically use a class selector. But some of these divs will have unique properties that we don't want our other elements to have, and as you'll recall from Lab 13, we typically use ID selectors for unique properties.  

So, give these divs a generalized class selector, like "stuff", and then give them each a unique ID selector, for example "first," "second," "third," and "fourth." Add these selectors inline with each div's opening tag, like so:  

{% highlight html %}
<div class="stuff" id="first">Divider1</div>
<div class="stuff" id="second">Divider2</div>
<div class="stuff" id="third">Divider3</div>
<div class="stuff" id="fourth">Divider4</div>
{% endhighlight %}

Again, we'll use these selectors to add style and positioning in CSS.

<a id="extcss"></a>
### Link to an External CSS Style Sheet

Finally, let's add a relative link in our `<head>` (directly following our `<title></title>` tags) to an external style sheet. The file should be referenced as "style.css" and should be included inline with the link tag:  

{% highlight html %}
<link rel="stylesheet" href="style.css">
{% endhighlight %}

Now, create a new file, save it immediately as **style.css**, and be sure it's located in your local repository; i.e. the same directory that contains your index.html file. We'll add all of our styling rules here in the next part of the lab.

So far your HTML source should look like this:  

{% highlight html linenos %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Home Page</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div class="hero-image">
      <div class="hero-text">
        <h1>Hi, I'm Tony</h1>
        <h5>I'm an Immunologist</h5>
      </div>
    </div>
    <div id="navbar">
      <a href="index.html">Home</a>
      <a href="aboutme.html">About Me</a>
      <a href="myportfolio.html">My Portfolio</a>
      <a href="contact.html">Contact</a>
    </div>
    <div class="stuff" id="first">Divider1</div>
    <div class="stuff" id="second">Divider2</div>
    <div class="stuff" id="third">Divider3</div>
    <div class="stuff" id="fourth">Divider4</div>
  </body>
</html>
{% endhighlight %}

Make sure your 2 files are all included in your **/lab-14-part2-site** repo, and don't forget to **add**, **commit**, and **push** your changes!  

* * *   

<a id="heroimg"></a>
## 3. Adding + Styling a Hero Image     

First, let's define some universal properties in our CSS style sheet. On line copy the following the code into your **style.css** file:  

{% highlight css %}
/* universal properties */
body, html {
    height: 100%;
}
{% endhighlight %}

Right-click and save the following image file in your local repo (fauci.v01.jpg):  

<img src="fauci.v01.jpg" alt="Dr. Fauci" width="375px" />

We're going to use this as our "hero image".  

Next, let's reference this inside your **style.css** file.

Recall that your image container (`<div>`) has a class selector associated with it. We called this "hero-image".  

So, in our CSS, we need to only to identify this element by its class selector. Add some rules to this selector in your CSS like so:  

{% highlight css %}
.hero-image {
  background-image: url("fauci.v01.jpg");
  height: 30%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
{% endhighlight %}

Next, let's style the text we want to place over the image...   

Recall that your image text container also has a class selector associated with it. We called this "hero-text". This `<div>` contains an `<h1>` and an `<h5>` element.

In your external style sheet, add some rules for your hero text:  

{% highlight css %}
/* Center the text over the image. */
.hero-text {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
{% endhighlight %}

At this point, open your **index.html** file in Chrome to observe the current state of your home page. It should appear extremely plain, without almost no styling at all:  

<img src="resources/site.v01.png" alt="Dr. Fauci" width="700px" />

* * *   

Make sure your files is included in your **/lab-12-html** folder, and don't forget to **add**, **commit**, and **push** your changes!  
Use your [_git cheatsheet_ (from lab 3)](/Goldford-MTEC1003-OL04/labs/03/lab-03-git-intro.html){:target="_blank"} if you need it!  

Your final **/lab-12-html** folder by the submission deadline should include the files from parts 1 + 2 of the Week 12 Labs, plus the new folder **/final-project-brainstorming** containing the **3 text files** described above.  

* * *  
