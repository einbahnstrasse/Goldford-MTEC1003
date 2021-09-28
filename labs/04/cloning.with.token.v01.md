---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Cloning a Remote Repo Using Your _GitHub_ API Access Token  
_This brief tutorial proposes a quick & easy way of setting up your weekly repositories. Use this tutorial beginning in Week 5. **BOOKMARK** this page to easily retrieve it in the future._  

In this tutorial, we'll be:  
1. <a href="#remote">Creating a remote repository on <i>GitHub</i>.</a>    
2. <a href="#clone">Using your <i>GitHub</i> API access <b>token</b>, previously created in Week 3, to <span style="color:red">CLONE</span> your <em>remote</em> repository onto your <em>local</em> computer</a>   
3. <a href="#push">Making changes to the contents of your local repository, then running the normal sequence of git commands to version your files and push them up to your remote repository on <i>GitHub</i> (<i>Review</i>).</a>   

* * *

<a id="remote"></a>
### 1. Create Your _**REMOTE**_ Repository on _GitHub_    

Set up a remote repository on _GitHub_ as you normally would. From your home page on _GitHub_, click the green "New" button and on the next page, name your repository and be sure to select all of the correct options, just as we've done in previous weeks. For example, your repository for Week 5 should resemble this:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.clone/img.clone.01.create.repo.png" width="600px">   

After you create your repository, you're ready to [_**CLONE**_](https://git-scm.com/docs/git-clone){:target="_blank"} it onto your local computer.  

* * *

<a id="clone"></a>
### 2. _**CLONE**_ the Repo Using Your _GitHub_ API Access Token  

Retrieve your _GitHub_ API Access Token [created in Week 3](https://einbahnstrasse.github.io/Goldford-MTEC1003-OL78/labs/04/remote.via.API.token.v01.html){:target="_blank"}, and copy your token value to the clipboard.

In Terminal, navigate to your **mtec1003 folder**, where you keep repositories for this class. It should be something like:  

{% highlight terminal %}$ cd Desktop/myClasses/mtec1003/  
{% endhighlight %}  

Now, `copy` the following command (careful, it's long!) and `paste` it into your text editor (Atom, SublimeText, etc.):

{% highlight terminal %}
$ git clone https://38597e1f2g1az2h5870fs6i465rty5w234c97qqq@github.com/yourGitHubUserName/lab-05-js-py.git  
{% endhighlight %}

Before running this in Terminal, in your text editor replace the fake API token (<span style="color:red">38597e1f2g1az2h5870fs6i465rty5w234c97qqq</span>) with the token you created, and replace <span style="color:red">yourGitHubUserName</span> with your actual _GitHub_ username. This is the equivalent of using your _GitHub_ password to "log in" to the GitHub API from the command line.  

Also, be sure to <span style="color:red">change the name of the repository in this command</span> _(beyond week 5)_ to connect it to the remote repository you created for the current week. So, instead of `lab-05-js-py.git` you will need to be sure this name accurately matches the name you gave your repo on _GitHub_.  

Does everything look good? Any errors? <font size="2">_**Check your spelling!**_</font>    

When you're ready, `copy` your revised command, `paste` it on the command line, and press `<ENTER>` to run the command.  

In your Terminal, the command and its output should resemble this:

<img src="/Goldford-MTEC1003-OL78/labs/04/img.clone/img.clone.02.clone.repo.png" width="2000px">  

_Congratulations!_ You've successfully **CLONED** your **remote** repository onto your local computer and you're now ready to run the normal sequence of `git` commands, such as `git status`, `git commit`, and `git push`, from your command line.  

At this point, if you're feeling confident about your git command skills, **return to your lab to continue working.** Or, read the last section for a quick review of the sequence of `git` commands necessary to version your work.

* * *  

<a id="push"></a>
### 3. Make Changes to your File(s) and Version Them (_Review_)   

From here on, you can add new files and revise old ones, then track their changes under git. As a quick example, make a change to the README.markdown file you created on _GitHub_, which has now been cloned onto your computer. `open` this file in your text editor and type something new, for example on line 3, and be sure to `save` your changes (_locally_):  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.clone/img.clone.03.edit.a.change.png" width="600px">

Now, run the normal sequence of git commands in your Terminal to version these changes:

{% highlight terminal %}$ git status  
$ git add .   
$ git commit -m "made a change to the readme file"  
$ git push origin master  
{% endhighlight %}  

Your commit message should **be placed between double quotation marks** and should be **a summary of the changes made to the files in your commit**. For example, "made a change to the readme file" accurately reflects what has been accomplished during this commit.  

In your Terminal, these commands and their output should resemble the following:

<img src="/Goldford-MTEC1003-OL78/labs/04/img.clone/img.clone.04a.status.add.commit.push.png" width="600px">  

As always, your final step should be sure to **check your _GitHub_ repository** after running your `git push` command, to **VERIFY** that your most current work is reflected on _GitHub_, i.e. to be sure you've properly submitted your labs!  

You can **VERIFY** this from the front page of your _GitHub_ repo in 3 easy ways:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.clone/img.clone.v05.validate.png" width="2000px">  

_**Return to your lab and continue your work.**_

* * *  
