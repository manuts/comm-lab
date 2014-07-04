EE 703 Digital Message Transmission (Autumn 2013)
-------------------------------------------------

This repository contains the LaTeX files pertaining to the Autumn 2013 edition of the EE703 course at IIT Bombay. The pdf files corresponding to these source files can be found at [this link](http://www.ee.iitb.ac.in/~sarva/EE703/Autumn2013.html)

Compiling the source files
--------------------------

* For the assignments and exams, `pdflatex file.tex` will generate the pdf as long as you have the necessary LaTeX packages installed. For example, files containing figures require `tikz` to be installed.
* For the slides, there is a `Makefile` which helps generate both handout and non-handout versions of the pdf. In the handout version, all the `\pause` commands in `beamer` are disabled.

    + For the non-handout version, simply type `make` in the `slides` subdirectory
    + For the handout version, type `make handout` in the `slides` subdirectory

* Some slide decks contain plots which requires `gnuplot` to be installed on your machine.   
License
-------
This code is being released under the permissive [MIT License](http://choosealicense.com/licenses/mit/)
