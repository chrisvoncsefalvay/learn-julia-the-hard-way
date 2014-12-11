{% import "macros/ork.jinja" as ork with context %}
Exercise 0: The Setup
*********************

First things first – we'll have to setup your computer to work with Julia. Fortunately, this is quite easy regardless of the OS you use! 

Binaries
========

If you use Windows, Mac OS X, Ubuntu, Fedora/RHEL/CentOS or a generic Linux distribution that does packages, the download page for the Julia language (http://julialang.org/downloads/) is the easiest way to obtain an installer or package version of Julia. For the purposes of this book, we will assume you're using version v0.3.3. Julia is a young language, and it is developing quite a lot. There is, currently, no guarantee that the final version –&nbsp;or, indeed, the next version! – will look anything like it currently does.


Package managers
================



IJulia
======


There is an implementation of the vastly successful IPython notebook environment for Julia. The IPython system, now known as the Jupyter project, is a great way to interactively use Julia in a notebook environment that users of Mathematica or similar software might be used to. It also allows literate coding, mixing Markdown notes and formatting with executable code. To install IJulia, you will need an existing IPython installation, either a distribution like Anaconda or by installing Python and the IPython notebook environment by downloading the Python distribution for your operating system. Once that is in place, install Julia using the instructions above. Then launch Julia and install IJulia using the ``Pkg.add("IJulia")`` command. Congratulations, you now have your very own notebook environment for Julia! 

To launch your environment, either use the `profile` IPython parameter::

	$ ipython notebook --profile julia


Alternatively, you can fire up the Julia REPL and launch IJulia by::

	using IJulia
	notebook()

