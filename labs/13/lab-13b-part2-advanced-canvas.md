---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Lab 13 / Part 2: Advanced Canvas     

#### C O N T E N T S  
1. <a href="#rowloop">Row Loop</a>  
2. <a href="#columnloop">Column Loop</a>  
3. <a href="#4by7">Four By Seven</a>  
4. <a href="#checkerboard">Checkerboard</a>  
5. <a href="#checkersgame">Checkers Game</a>  
6. <a href="#threecircles">Three Circles</a>  
7. <a href="#circlegrow">Circle Grow</a>  
8. <a href="#hemisphere">Hemisphere</a>  

* * *  

<a id="rowloop"></a>
## 1. Row Loop    

Name this file **rowloop.html**. Use a loop to make a row of 5 <span style="color: pink">pink</span> circles:  

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.rowloop.png" alt="row loop example output" width="300px">  

* * *   

<a id="columnloop"></a>
## 2. Column Loop  

Name this file **columnloop.html**. Use a loop to make a column of 5 <span style="color: LightBlue">light blue</span> circles:  

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.columnloop.png" alt="column loop example output" width="60px">  

* * *   

<a id="4by7"></a>
## 3. Four By Seven  

Name this file **4by7.html**. Use 2 loops to make a 4 x 7 grid of <span style="color: LightGreen">light green</span> circles:  

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.4x7.png" alt="4x7 example output" width="210px">  

* * *  

<a id="checkerboard"></a>
## 4. Checkerboard    

Name this file **checkerboard.html**. Make a checkerboard that has alternating <span style="color: black;background-color:white;">black</span> and white squares:  

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.checkerboard.png" alt="checkerboard example output" width="200px">  

* * *  

<a id="checkersgame"></a>
## 5. Checkers Game    

Name this file **checkersgame.html**. Using that same checkerboard you made before, place <span style="color: blue;background-color:DimGray;">blue</span> and <span style="color: green">green</span> pieces on the proper squares to start a game:  

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.checkersgame.png" alt="checkers game example output" width="200px">  

* * *  

<a id="threecircles"></a>
## 6. Three Circles      

Name this file **threecircles.html**. Make 3 concentric circles. The largest has a radius of 100 px and is <span style="color: red">red</span>. The medium circle has a radius of 75 px and is <span style="color: blue;background-color:DimGray;">blue</span>. The smallest circle has a radius of 50 px and is <span style="color: green">green</span>:  

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.threecircles.png" alt="3 circles example output" width="200px">  

* * *  

<a id="circlegrow"></a>
## 7. Circle Grow      

Name this file **circlegrow.html**. Use a loop to make a series of 9 or more circles that _grow_ in size with each iteration. The circles should move _diagonally_, starting in the upper left corner of the canvas and moving to the lower right, ending in the lower right corner, like this:  

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.circlegrow.png" alt="circle grow example output" width="200px">  

* * *  

<a id="hemisphere"></a>
## 8. Hemisphere      

Name this file **hemisphere.html**. Draw the two <span style="color: black;background-color:white;">black</span> and <span style="color: green">green</span> hemispheres pictured below. Experiment with the last 3 arguments of the `context.arc()` function. Recall that its standard form is:  

`context.arc(x, y, radius, 0, 2 * Math.PI, true)`  

* Argument 1 = x position  
* Argument 2 = y position  
* Argument 3 = radius  
* Argument 4 = starting angle of circle (0-360°)  
* Argument 5 = ending angle of circle (0-360°)  
* Argument 6 = fill side (which side of circle is colored)  

Your hemisphere should look something like this:

<img src="/Goldford-MTEC1003-OL78/labs/13/img/ex.hemisphere.png" alt="circle grow example output" width="200px">  

* * *  

_...And that's it! Now, time to move on to the next part of lab 13..._  
