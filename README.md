# ESM 244 - Lab 10
## SQL and Python in R Markdown

The goal of this lab is to demo some ways to work with other languages (SQL, Python) within the R Studio IDE we've grown to know and love. 

Together, we will:

- Explore and query a relational database with SQL in R Markdown using the `RSQLite` package
- Work with and update databases using SQL
- Talk through a Python-in-RMarkdown demo using `reticulate`

**You should**:

1. Install [`RSQLite`](https://www.r-project.org/nosvn/pandoc/RSQLite.html) package by Kirill Müller et al. in R: "`RSQLite` embeds the 'SQLite' database engine in R and provides an interface compliant with the 'DBI' package. The source for the 'SQLite' engine is included."

- `install.packages("RSQLite")`

-----------
**WARNING: potential unnecessary frustration below.**

(...but do this if you're interested in interfacing between R and Python.)

Allison will also **demo** how to run some Python code in R Markdown using [`reticulate`](https://rstudio.github.io/reticulate/).

**IF** you want to actually do the Python part now or later (not required - I'll just demo this part), you **can** follow along [here](https://rstudio.github.io/reticulate/) to get set-up. I installed Anaconda to get Python 3.7, & set my pathway to that version. This can be kind of a challenging set-up/installation/pathway battle, but once you get it running it's user-friendly through R Markdown.
