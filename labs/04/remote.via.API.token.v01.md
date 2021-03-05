---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Creating Your Remote Repository Using a _GitHub_ API Access Token
_This brief tutorial proposes an alternative to the original method of linking your remote repository. You are here because you've been redirected from [Lab 4 / Part 2.](/Goldford-MTEC1003-OL78/labs/04/lab-04-git-part-02a.html){:target="_blank"}_  

In this tutorial, we'll be:  
1. <a href="#mktoken">Creating a <i>GitHub</i> API access <b>token</b> to use on the command line, and</a>    
2. <a href="#remote">Using this token to run a CURL command that will create your new REMOTE repository with the same name you gave to your LOCAL.</a>   

* * *

<a id="mktoken"></a>
### 1. Create a _GitHub_ API Access Token  

From the top-right corner of your _GitHub_ page, click on your avatar and select **Settings** from the dropdown list:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.token/01.png" width="200px">  

On the next page, there is a left sidebar. Scroll down and click on the **Developer Settings** button:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.token/02.png" width="454px">  

On the next page, do the following:  

  1. Click on **Personal access tokens** from the left sidebar, and  
  2. Click the **Generate new token** button on the right:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.token/03.png" width="2000px">

The next page is called "New personal access token." We're going to create a _token,_ or a number that will allow us to access the GitHub API from the command line. We'll use this instead of our _GitHub_ password to authorize ourselves when we link our remote repository, as we'll see later. On this page, do the following:

  1. Click the **repo** checkbox, which will automatically check all the related checkboxes below it. We're going to use this access token for creating repositories, so we want to be sure this category has been enabled.  
  2. Type a **note** that you'll recognize. You'll only get to see the token once, and after that you'll only have this note to recognize your token by!  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.token/04.png" width="2000px">

Now, scroll down to the bottom of this page and click the green **Generate token** button:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.token/05.png" width="436px">

On the next page, you'll see your new API token value — a long string of characters — appear in a green frame. Notice the warning that reads, _"Make sure to copy your personal access token now. You won't be able to see it again!"_  Notice that there is also a clipboard icon next to your token value. **Click the token icon** to copy your token to the clipboard:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.token/06.png" width="2000px">

Finally, **paste** this token value somewhere for safe keeping. For example, you can create a text file and save the token inside it. Keep the token (and the token **note** that you created above) wherever you can easily access it.

This is your personal API token; don't share it with anybody! We'll use it instead of your _GitHub_ password in the steps that follow, so <span style="color:red"><i>don't lose your token!</i></span>  

* * *

<a id="remote"></a>
### 2. Create Your New _**REMOTE**_ Repo  

Copy your token value to the clipboard (if you haven't just done it in the previous steps). Now, we are ready to link our local and remote repositories using the access token we've just created.  

In Terminal, resuming just where we'd paused our work in [Lab 4 / Part 2.](/Goldford-MTEC1003-OL78/labs/04/lab-04-git-part-02a.html){:target="_blank"}, type the following long command:  

{% highlight terminal %}
$ curl -i -H "Authorization: token 38597e1f2g1az2h5870fs6i465rty5w234c97qqq" -d '{ "name": "lab-04-version-control" }' https://api.github.com/user/repos  
{% endhighlight %}

Or, if you get an error running this command, you may need to alter it slightly with **escape characters** to be sure your quotation marks are parsed properly in your Terminal (this may be helpful for Git for Windows users) like so:  

{% highlight terminal %}
$ curl -i -H "Authorization: token 38597e1f2g1az2h5870fs6i465rty5w234c97qqq" -d "{ \"name\": \"lab-04-version-control\" }" https://api.github.com/user/repos
{% endhighlight %}

Whichever one you use, be sure to make one essential change to your command above:  

Replace the fake API token (<span style="color:red">38597e1f2g1az2h5870fs6i465rty5w234c97qqq</span>) with the token you created, copied, and saved on your own _GitHub_ page. This is the equivalent of using your _GitHub_ password to "log in" to the GitHub API from the command line.  

When you're ready, press `<ENTER>` to run the command.  

You'll see A LOT of text printed to the console...  

{% highlight terminal %}
HTTP/2 201
server: GitHub.com
date: Sun, 28 Feb 2021 23:37:08 GMT
content-type: application/json; charset=utf-8
content-length: 6301
cache-control: private, max-age=60, s-maxage=60
vary: Accept, Authorization, Cookie, X-GitHub-OTP
etag: "38597e1f2g1az2h5870fs6i465rty5w234c97qqq38597e1f2g1az2h5870fs6i465rty5w234c97qqq"
x-oauth-scopes: repo
x-accepted-oauth-scopes: public_repo, repo
location: https://api.github.com/repos/yourUserName/lab-04-version-control
...many...
...more...
...lines...
...of...
...text!...
"allow_squash_merge": true,
"allow_merge_commit": true,
"allow_rebase_merge": true,
"delete_branch_on_merge": false,
"network_count": 0,
"subscribers_count": 1
}
$
{% endhighlight %}

Follow the link printed towards the top under "location:" to verify that your new remote repository is working on _GitHub._ It should follow the general pattern of https://api.github.com/repos/yourUserName/lab-04-version-control. When you see the name of the repository online, you know it worked:  

<img src="/Goldford-MTEC1003-OL78/labs/04/img.token/07.png" width="2000px">

_Congratulations!_ You've successfully created your new **remote** repository (on _GitHub_) and you're now ready to link it to your **local** repository, and finally you'll be able to `git commit` and `git push` from the command line!  

Once you've completed the steps in this tutorial, return to [Lab 4 / Part 2.](/Goldford-MTEC1003-OL78/labs/04/lab-04-git-part-02a.html){:target="_blank"} exactly where the link to this tutorial appears, and resume work on the lab.    

* * *  
