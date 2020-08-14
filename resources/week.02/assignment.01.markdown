---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
permalink: /resources/week.02/assignment.01.html/
---
# Assignment #1: 10 points
## Voice Allocation, poly~ And Usage Of _bach_

* Write your own `poly~` subpatcher — containing your own sound engine.
	* Consider tweaking our _ring modulator_, though you may not use a simple copy of the example patch.
	* Consider making your `poly~` handle AM, FM, a harmonizer, or any other "classic" synthesis method that you already know.
	* Or consult online forums for other ideas about your sound engine.
* Write a short musical sequence showing off your new poly~ instrument. 
	* Your sequence must be stored in a `bach.roll`.
	* Your synth engine must utilize at least 1 of `bach.roll`'s slots to control a synthesis parameter of your choice.
	* Consider using a slot to control each note's amplitude envelope, FM depth, or any other synthesis parameter you imagine.
	* Consider how your chosen sound and sketch of material might be used in our final project about memory.
	* _Some excerpts may be chosen for inclusion in, or for development towards, our final project._

### LENGTH
Between 1 and 2 minutes of material maximum.

### DOCUMENTATION
* Record a soundfile of your score playing back from your `poly~` using the Quickrecord patch, and export a text file (.txt) from your `bach.roll` to preserve your score.  
* Include your main patch, `poly~` subpatcher, score in text format, and short audio recording in a folder and make it into a .zip file.
* Audio recordings should be lossless .WAV or .AIFF files in 48kHz/24-bit (i.e. sampling rate / bit rate).
* Email me the .zip file _(or send me a link to it if the archive is too large)._

### DEADLINE
* <p class="redish">Due on Tuesday night, February 18th, at 11:59 PM.</p>
* As you will be presenting your work the following day (Wed. 2/19), **no late work will be accepted.**

### GRADING
Subject to the **GENERAL GRADING RUBRIC** located in our <a href="/index.html">Course Syllabus.</a>  
_Scores will be given out of 10 points. Your grade will be based on:_
* Elegance, simplicity, and readability of technical solutions in your Max patching; esp. communication between `bach.roll` and `poly~`, and the contents of your `poly~` subpatch.
* Inventiveness of the sound-producing engine inside your `poly~` subpatcher.
* Quality of the sound produced by your `poly~` and as captured in your sound file.
* Creativity and thoughtfulness of your musical ideas as recorded in your `bach.roll` MIDI composition.

### FEEDBACK
We will listen to and discuss your work as a group next Wednesday 2/19.

* * *