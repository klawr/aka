# [aka.klawr.de](https://github.com/klawr/aka)

This repository is used to have prettier links in reports and other documents.  
Each project gets one **index.html** which is put into a respective directory,
e.g. the directory `srp` handles links from the Student Research Project and manages links such as:

https://aka.klawr.de/srp#1 which redirects to  
https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research.

Active projects include:
 - [Student research project](https://aka.klawr.de/srp)
 - [Student engineering project](https://aka.klawr.de/sep)

---

Create **index.html** automatically from an **.aka** file.
**.aka** files are created by LaTeX documents using the following snippet:

```latex
\usepackage{tocloft}

\newcommand{\akaAbb}{X} % Replace X with project abbreviation
\newcommand{\listlinkname}{Link Index - \url{https://aka.klawr.de/\akaAbb}} 
\newlistof{links}{aka}{\listlinkname}
\newcommand{\theaka}{\url{https://aka.klawr.de/\akaAbb\#\thelinks}}
\newcommand{\aka}[1]{\refstepcounter{links}\theaka%
\addcontentsline{aka}{links}{\url{\#\thelinks}: \tiny{\url{#1}}}}
```

The projectname **X** in the `\akaAbb` command has to be the name of the directory in this repository. <br>
Replace `aka.klawr.de` because I do not share. 🍰 <br>
The mappings are generated by calling links with e.g.
```latex
\aka{https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research}
```
And the respective list has to be inserted using:
```latex
\listoflinks
```
in the document.


The **index.html** in the respective project directory has to be updated of course.

Updates are done by feeding the generated **document.aka** into the provided **aka.py**.

The input is assumed to be a list of pairs of aka ids and the target links.
All links have to be marked by the \url styling of LaTeX.

The aka links are identified by `r'{\\url\s*{\\(#\d+)}:'`
(Should be cool automatically through the LaTeX snippet).

At the moment I see no way to create more than one index.html, so each
project has to have its own directory.
