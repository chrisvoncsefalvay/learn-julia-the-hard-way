{% import "macros/ork.jinja" as ork with context %} Exercise 0: The
Setup *****\****\****\**\*\*

First things first – we'll have to setup your computer to work with
Julia. Fortunately, this is quite easy regardless of the OS you use!

Binaries
========

If you use Windows, Mac OS X, Ubuntu, Fedora/RHEL/CentOS or a generic
Linux distribution that does packages, the download page for the Julia
language (<http://julialang.org/downloads/>) is the easiest way to
obtain an installer or package version of Julia. For the purposes of
this book, we will assume you're using version v0.3.3. Julia is a young
language, and it is developing quite a lot. There is, currently, no
guarantee that the final version –&nbsp;or, indeed, the next version! –
will look anything like it currently does.

Package managers
================

If you're using a \*NIX distribution, you might be able to use your
distro's package manager to get Julia.

Ubuntu
------

There is a PPA provided for Julia, so all you need to do is get a shell
and run the following commands:

    sudo add-apt-repository ppa:staticfloat/juliareleases
    sudo add-apt-repository ppa:staticfloat/julia-deps
    sudo apt-get update
    sudo apt-get install julia

:: Or, in Fedora:

    sudo dnf copr enable nalimilan/julia
    sudo yum install julia

:

Compiling from source
=====================

Julia changes rapidly, with often more than a dozen average changes per
day (!) to the source code. Therefore, some people tend to simply pull
the most recent nightly build from Git and recompile it every few days.
This is a great way to stay ahead of the curve, and also to come across
more bugs than one would want to when learning a new language. By all
means do use nightly builds when you are confident with Julia, but I do
not recommend doing so for the time you are trying to navigate your way
through it.

If you do want to use nightly builds, simply pull the master branch from
the [Julia GitHub repo](<https://github.com/JuliaLang/julia>) and
compile by typing make into the Terminal. To speed up the process, you
might wish to use a number of concurring processes (make -j n, where
\_n\_ is the number of concurrent processes you are going to use).

IJulia
======

There is an implementation of the vastly successful IPython notebook
environment for Julia. The IPython system, now known as the Jupyter
project, is a great way to interactively use Julia in a notebook
environment that users of Mathematica or similar software might be used
to. It also allows literate coding, mixing Markdown notes and formatting
with executable code. To install IJulia, you will need an existing
IPython installation, either a distribution like Anaconda or by
installing Python and the IPython notebook environment by downloading
the Python distribution for your operating system. Once that is in
place, install Julia using the instructions above. Then launch Julia and
install IJulia using the `Pkg.add("IJulia")` command. Congratulations,
you now have your very own notebook environment for Julia!

To launch your environment, either use the profile IPython parameter:

    $ ipython notebook --profile julia

:

Alternatively, you can fire up the Julia REPL and launch IJulia by:

    using IJulia
    notebook()

:

A word on IDEs
==============

As previously noted, this book diverges from Zed Shaw's framework a
little. As such, I will not take you through the intricacies of setting
up an IDE or a text editor. To cut a rather long story short – use what
works for you! Fortunately, most text editors do have some form of
support for Julia:

-   Vim: [julia-vim](<https://github.com/JuliaLang/julia-vim>)
-   Emacs: Julia highlighting is provided via [Emacs Speaks
    Statistics](<http://ess.r-project.org/>) (ESS) through
    [this](<https://github.com/emacs-ess/ESS/wiki/Julia>) package.
-   Textmate: a [Julia TextMate
    Bundle](<https://github.com/WestleyArgentum/Julia.tmbundle>) is
    available, which includes syntax support and somewhat rudimentary
    bundle features
-   Sublime Text:
    [Sublime-IJulia](<https://github.com/quinnj/Sublime-IJulia>)
    integrates IJulia into Sublime Text - installation is a little
    complex at this time, but worth it!
-   Notepad++: [Syntax
    highlighting](<https://gist.github.com/catawbasam/3858496>) is
    available for Notepad++.
-   Light Table: supports Julia out of the box and with more IDE-like
    features through [Juno](<http://junolab.org/docs/installing.html>).

There is an application similar to RStudio in the works, called [Julia
Studio](<http://forio.com/labs/julia-studio/>), aspiring to be more of a
fully-fledged IDE rather than a mere text editor. Unfortunately, at the
time of writing, it does not yet support Julia 0.3.

Ready teddy?
============

Open up Julia by launching IJulia, opening the Julia app provided with
the OS X version or calling Julia from the terminal (usually, julia).
You are greeted by the Julia REPL.:

    _

> \_ \_ \_(\_)\_ | A fresh approach to technical computing

> (\_) | (\_) (\_) | Documentation: <http://docs.julialang.org>
>
> :   \_ \_ \_| |\_ \_\_ \_ | Type "help()" for help.
>
> | | | | | |/ \_\` | |\
> | |\_| | | | (\_| | | Version 0.3.3 (2014-11-23 20:19 UTC)

> \_/ |\_\_'\_|\_|\_|\_\_'\_| | 'Official <http://julialang.org/>
> release'

> |\_\_/ | x86\_64-apple-darwin13.3.0
>
> julia\>

:: Your version may differ, as will the architecture (final line). If
you seek help on Julia forums, always be sure to mention what build you
have (the final three lines).

Congratulations. Your adventure begins here. {% import
"macros/ork.jinja" as ork with context %} Exercise 1: Let's get
printing! ***************\****************

In this exercise, we will familiarise ourselves with the Julia REPL and
print a few things.

Get to know and love the REPL
=============================

The great thing about REPLs is that they make learning a language a lot
easier - especially a language that is at least partly intended to allow
you to quickly prototype complex ideas in a few lines of code,
manipulate your code, iterate until you get the desired results, then
flesh it out or tidy it up.

Using the REPL isn't complicated, but it might be unusual at first if
you have not used much of a similarly constructed REPL (such as Prelude,
the Haskell REPL). It helps to remember a few commands and tricks for
the future.

Modes
-----

Julia's REPL has four 'modes', each indicated in the prompt.

### Julia

Prompt: julia\>

In this mode, you interact with the Julia engine directly. Pressing
Return/Enter executes the command in the current line and prints the
result. You can also access the result of the last operation in the ans
variable. If you don't wish for Julia to print the result, conclude your
line with a ; (semicolon).

### Help

Prompt: help\>

By typing ? at the beginning of a line, you can enter the help mode.
Entering anything searches the Julia documentation for that word.:

    help?> besselj
    INFO: Loading help data...
    Base.besselj(nu, x)
       Bessel function of the first kind of order "nu", J_\nu(x).

:: To leave help mode, use the Backspace key.

### Shell

Prompt: shell\>

To execute shell commands, enter \#. The REPL prompt will change to
shell\>, and anything you enter will be executed as a shell command.

### Search

Prompt: (reverse-i-search)'

By pressing \^R, you can initiate a reverse search of your history,
including from previous sessions. It will show you any commands that
match the pattern you have entered.

Key bindings
------------

The Julia REPL uses a few key bindings that might be very familiar to
those who have used \*nix based systems frequently in the past. Most
importantly, to exit the REPL, you can use \^D (Ctrl+D), which will also
close your shell, and you can abort a current operation using \^C.

There are many more key bindings that the Julia REPL recognises, but
these should be enough to get you off the ground.

Autocompletion and Unicode entry
--------------------------------

Using Tab triggers your new best friend, Julia's autocomplete feature.
Julia also knows Unicode math, so this is valid Julia:

    julia> 2*2.5* pi
    15.707963267948966

:: Pressing Tab autocompletes to Unicode symbols:

> julia\> sqrt [Tab] -1 julia\> sqrt{2} 1.4142135623730951

:: For all Unicode completions, check out [the Unicode conversion table
in the Julia
documentation](<https://github.com/JuliaLang/julia/blob/master/doc/manual/unicode-input-table.rst>).
Remember, you can also use Unicode symbols in saved code.

Let's say something!
====================

In the following, we'll be exploring a few ways to say hello to Julia.
Each of these has their place in the coder's arsenal, and while you will
eventually use the REPL a little less and your text editor a little
more, you will probably use the REPL quite a bit to test out new ideas.
Think of the REPL as your lab and the text editor as your drawing board
– scientists who spend all their time in the lab eventually go mad,
while those who are always at the drawing board rarely discover much!

Using the REPL
--------------

A REPL interface repeats everything you enter. This makes saying hello
to the world rather simple – simply declare a variable containing the
string literal "Hello, Julia!" or, even simpler, just declare the string
literal. Let's see both of these in action in the REPL.:

    julia> "Hello, Julia!"
    "Hello, Julia!"

    julia> v = "Hello, Julia!"
    "Hello, Julia!"

    julia> v
    "Hello, Julia!"

:

Using println()
---------------

Now for some actual coding. Time to invoke our first real function.
println prints the string representation of an object.:

    julia> println("Hello, Julia!")
    Hello, Julia!

:

You might notice that the "Hello, Julia!" string is not printed in bold
type. This is to indicate that rather than part of the REPL's print
cycle, it is a system output.

Using string concatenation
--------------------------

String concatenation is just a fancy name for putting strings together.
In this case, we create two variables that represent strings, then use
the string() function to put them together. The string() function
concatenates each of its positional arguments.:

    julia> what = "Hello"
    "Hello"

    julia> whom = "Julia"
    "Julia"

    julia> string(what, ", ", whom, "!")
    "Hello, Julia!"

:

Julia also allows for variables to be called within string literals. So
the above is equivalent to:

    julia> "$whom, $what!"
    "Hello, Julia!"

:

And this is true even for maths (or any function!):

    julia> "2 plus 2 is $(2+2)."
    "2 plus 2 is 4."

:

More about printing
===================

{% import "macros/ork.jinja" as ork with context %} Learn Julia The Hard
Way ********\********\****

Table Of Contents
=================

-   [Preface](preface.html)
-   [Introduction](introduction.html)
-   [Exercise 0](ex0.html)

Frequently Asked Questions
==========================

How long does this course take?

:   You should take as long as it takes to get through it, but focus on
    doing work every day. Some people take about 3 months, others 6
    months, and some only a week.

What kind of computer do I need?

:   You will need either a Windows, OSX or Linux computer to complete
    this book.

{% import "macros/ork.jinja" as ork with context %} Introduction: Need
for Speed ************\**************\**

> import "macros/ork.jinja" as ork with context %}

#### Learn Julia The Hard Way

Table Of Contents
=================

{% include "preface.rst" %} {% include "introduction.rst" %}

{% include "ex0.rst" %}

#### Next Steps

What should they do after reading your book to learn more on the
subject.

{% import "macros/ork.jinja" as ork with context %} Preface ***\****

