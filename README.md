# Learn Julia the Hard Way

Because quite frankly, that's the only way to learn any technical programming language.

Julia has recently emerged as the young, dynamic newcomer in the scientific computing/data science computing market – for all the right reasons. Julia is fast, agile, fast, easy to use and... did I mention it's actually pretty fast?


## Content roadmap

LJtHW is a work in progress, and will see times of intense development punctuated by times of not much happening. This is largely owing to the author's rather busy schedule, in addition to the fact that the language is constantly changing and there is occasionally a need to go back and revisit older parts. I will try to adhere to the following content roadmap:


| Exercise | Subject                                         | Status         |
|:--------:|-------------------------------------------------|:--------------:|
|		   | **PART 1: Understanding Julia **				 | |
| 0        | [The Setup](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/03-ex0.md)                                   | FIRST DR        |
| 1        | [Printing](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/04-ex1.md)                                    | FIRST DR         |
| 2		   | [Variables](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/05-ex2.md)								         | FIRST DR			  |
| 3		   | [Types](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/06-ex3.md)											 | FIRST DR			  |
| 4		   | [Collections](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/07-ex4.md)			 | FIRST DR	          |				
| 5 	   | [Strings](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/08-ex5.md)										 | TODO			  |
| 6 	   | Control flow									 | TODO			  |
| 7 	   | Sequential iteration							 | TODO			  |
| 8	   | Functions										 | TODO			  |
| 9	   | Scope											 | TODO			  |
| 10	   | Methods & multiple dispatch								 | TODO			  |
| 11	   | Handling errors								 | TODO			  |
| 12	   | Heaps and queues								 | TODO			  |
| 13	   | I/O											 | TODO			  |
| 14	   | Dates and times							     | TODO			  |
| 15	   | Streams									     | TODO			  |
| 16	   | Parallel computing								 | TODO			  |
| 17	   | Unit testing									 | TODO			  |
| 18	   | Looking under the hood							 | TODO			  |
| 19	   | Executing C code								 | TODO			  |
| | **PART 2: Applied Julia** | |
| | (This part to be planned out) | |

NB. The order of modules may change depending on how the interdependence of the various chapters changes. The roadmap is not final. I am very happy to listen to suggestions from the community, since it's difficult to gauge at the moment what is going to be a core feature in Julia and how the demographic of those learning Julia will evolve.

## Slant

The Julia base package is pretty big, although at the same time, there are lots of other packages around to expand it with. The result is that on the whole, it is impossible to give a thorough overview of all that Julia can do in just a few brief exercises. Therefore, I had to adopt a little 'bias', or 'slant' if you please, in deciding what to focus on and what to ignore. 

Julia is a technical computing language, although it does have the capabilities of any general purpose language and you'd be hard-pressed to find tasks it's completely unsuitable for (although that does not mean it's the best or easiest choice for any of them). Julia was developed with the occasional reference to R, and with an avowed intent to improve upon R's clunkiness. R is a great language, but relatively slow, to the point that most people use it to rapid prototype, then implement the algorithm for production in Python or Java. Julia seeks to be as approachable as R but without the speed penalty. 

Owing to this, and partly to my own background as a data scientist, LJTHW is going to be somewhat biased towards the needs of statisticians. As such, there will be relatively little talk about fast Fourier transforms, integration and other mathemagical concepts that are beyond the immediate need, while some other components, such as the plotting package Gadfly, which would normally not be of general interest, will be explored. I have tried to strike a fair balance, and I hope I have succeeded there.

## Audience

Unlike most of Zed Shaw's _Learn X the hard way_ books, LJTHW is not intended for complete novices to programming – Julia is simply not ready yet for people wishing to learn programming by using it, although I see great potential in teaching people a functional programming language ahead of clobbering them with object-oriented concepts. On the other hand, one of the best things about Julia is that it was written by hackers, not language nerds. Yes, it's got all sorts of [metaprogramming goodness](http://docs.julialang.org/en/release-0.3/manual/metaprogramming/), it's [homoiconic](http://c2.com/cgi/wiki?HomoiconicLanguages) and it's got all sorts of other amazing things about it that may be of interest to a few, but they are not relevant to being good, or even pretty good, at Julia. Therefore, I am treating the audience as one of people who need to get a job done, not computer scientists. The latter probably already have taught themselves Julia!

## How to compile

There were some compilation instructions here. For now, these have been removed because I have found the Dexy system used by Zed Shaw a pain to deal with, and I will instead use a Pandoc-based conversion to a fully fledged eBook. I will provide compilation instructions in a bit, but until then, you could do worse than reading the chapters in sequence on Github!

## Author

I'm a data scientist, hacker and recovering lawyer living in Oxford, England. In my day job, I'm a software architect, and my parents still don't know what that means. When not working, I am coding for fun and spending time with my wife and our adorable Tortie kitten, River. My website is [here](http://www.chrisvoncsefalvay.com). You can e-mail me [here](mailto:chris[AT]chrisvoncsefalvay[DOT]com).

