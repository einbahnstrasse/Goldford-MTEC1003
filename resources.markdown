---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Software + Resources
_A list of stuff we'll be using throughout the course._  
_Be sure you've installed + tested all 7 of these before you arrive in class:_  

* * *

### 1a. Windows Users: A Free Terminal Emulator
_If you're not on macOS, you'll most likely need a program that mimics the behavior of the Unix command line._  
_Mac users can ignore this step! But if you're on Windows, install one of these free apps:_  

* [Git BASH _(recommended!)_](https://gitforwindows.org/){:target="_blank"}  
* [Xshell](https://xshell.en.softonic.com/){:target="_blank"}  
* [Cmder](https://cmder.net/){:target="_blank"}  
* [PuTTY](https://www.puttygen.com/download-putty){:target="_blank"}  
* Or, check out some others: [15 Best Terminal Emulators for Windows in 2020](https://www.puttygen.com/windows-terminal-emulators){:target="_blank"}  

### 1b. Windows Users: Virtual Desktop (Optional)  
_Additionally, Windows users may request access to a Virtual Desktop to be able to work on macOS remotely._  

* [CityTech Virtual Computer Lab](https://www.citytech.cuny.edu/virtual-lab/){:target="_blank"}  

* * *

### 2. Text Editor
_Check your operating system for compatibility and install one of these:_  

* [Visual Studio Code (RECOMMENDED)](https://code.visualstudio.com/download){:target="_blank"}  
* [Atom](https://atom.io/){:target="_blank"}  
* [Sublime Text 3](https://www.sublimetext.com/3){:target="_blank"}  
* [Visual Studio Code](https://code.visualstudio.com/download){:target="_blank"}  

* * *

### 3. Homebrew _(macOS and Linux systems only!)_
_Package management system to ease installation of other tools and software._  

1. INSTALL:  
	* See the [Wiki](https://github.com/Homebrew/legacy-homebrew){:target="_blank"}, or scroll to the [end of the Homebrew homepage](https://brew.sh/){:target="_blank"}  
	* Or, open your Terminal and run:  
			`ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`  
	* You may then need to run the following to check installation and update:  
			`brew doctor`  
			`brew update`  
2. VERIFY:  
	* Open your Terminal and run:  
			`brew --version`  
	* Your console should return something that looks like this:  
			`Homebrew 2.4.9`  
			`Homebrew/homebrew-core (git revision 58437; last commit 2020-08-08)`

* * *

### 4. GIT  
_Version control system for tracking changes in development code or any set of files._  
<p class="redish"><i>You'll be using GIT (and GitHub.com) to submit your lab homework every week, so be sure to set this up!</i></p>  

* Windows Users: install GIT using [Git for Windows](https://gitforwindows.org/){:target="_blank"}  
* macOS users: Follow the instructions using Homebrew below...  

1. INSTALL:  
		`brew install git`  
2. VERIFY:  
	* Open your Terminal and run:  
			`git --version`  
	* Your console should return something that looks like this:  
			`git version 2.20.1 (Apple Git-117)`

* * *

### 5. Set up a Free Public Account on _GitHub.com_
<p class="redish"><i>You'll be using GIT (and GitHub.com) to submit your lab homework every week, so be sure to set this up!</i></p>  

1. SIGN UP:  
	* Go to [Github.com](http://github.com){:target="_blank"} to get started;  
	* or visit [this 'How-To' Page for extra support.](https://www.wikihow.com/Create-an-Account-on-GitHub){:target="_blank"}  
2. VERIFY:
	* Immediately <a href="mailto:LGoldford@citytech.cuny.edu">email the instructor with your Github user account name</a> to receive grades in this class!!  

* * *

### 6. Google Chrome  
_A web browser with great built-in device compatibility tools._  

1. INSTALL:  
	* [Direct from Chrome homepage](https://www.google.com/intl/en/chrome/){:target="_blank"}  
2. VERIFY:  
	* Chrome can be launched from your /Applications folder.  

* * *

### 7. Python 3 + pip
_**Python** is an object-oriented, interpreted, and interactive programming language that we'll be introducing alongside JavaScript. It's great for quick prototyping and even better for data visualization._  

_**pip** is the standard package manager for the Python language, allowing you to easily install code packages + modules from the extensive [standard library.](https://docs.python.org/3/py-modindex.html){:target="_blank"}_  

1. INSTALL using these tutorials:  
	* [macOS](https://evansdianga.com/install-pip-osx/){:target="_blank"}  
	* [Windows](https://phoenixnap.com/kb/install-pip-windows){:target="_blank"}  
2. VERIFY:  
	* Verify Python 3:  
		* Open your Terminal and run:  
			`python3 --version`  
		* Your console should return something that looks like this:  
			`Python 3.8.5`
	* Verify pip:  
		* Open your Terminal and run:  
			`pip --version`  
		* Your console should return something that looks like this:  
			`pip 20.2 from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip (python 3.8)`  
		* or:  
			`pip 18.1 from C:\Python37\lib\site-packages\pip (python 3.7)`  
3. Create an alias so that anytime you run `python` on the command line, you'll be using Python 3 instead of older versions.  
	* When using Python, run this command when you **begin** a Terminal session:  
			`alias python=/usr/local/bin/python3`  
