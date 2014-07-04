SRCS =$(wildcard *.tex)
PDFS = $(SRCS:.tex=.pdf)

.PHONY: all pdf handout clean

# The pdf target is for the LaTeX-Suite compilation shortcut
all: $(PDFS)

pdf: $(PDFS)

handout:
	$(MAKE) handout=1

%.pdf: %.tex
ifneq ($(handout),1)
	pdflatex -shell-escape $<
else
	pdflatex -shell-escape '\PassOptionsToClass{handout}{beamer} \input{$<}'
	pdflatex -shell-escape '\PassOptionsToClass{handout}{beamer} \input{$<}'
endif

clean:
	rm  *.aux *.log *.out *.snm *.nav *.toc

allclean:
	rm *.pdf *.aux *.log *.out *.snm *.nav *.toc
