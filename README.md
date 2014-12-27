# Learn Julia the Hard Way

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />


Because quite frankly, that's the only way to learn any technical programming language.

Julia has recently emerged as the young, dynamic newcomer in the scientific computing/data science computing market – for all the right reasons. Julia is fast, agile, fast, easy to use and... did I mention it's actually pretty fast?


## Content roadmap

LJtHW is a work in progress, and will see times of intense development punctuated by times of not much happening. This is largely owing to the author's rather busy schedule, in addition to the fact that the language is constantly changing and there is occasionally a need to go back and revisit older parts. I will try to adhere to the following content roadmap:


| Chapter | Subject                                         | Status         |
|:--------:|-------------------------------------------------|:--------------:|
|		    |**PART 1: Understanding Julia**				  |
| 0        | [The Setup](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/03-ex0.md)                                   | FIRST DR        |
| 1        | [Printing](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/04-ex1.md)                                    | FIRST DR         |
| 2		   | [Variables](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/05-ex2.md)								         | FIRST DR			  |
| 3		   | [Types](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/06-ex3.md)											 | FIRST DR			  |
| 4		   | [Collections](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/07-ex4.md)			 | FIRST DR	          |				
| 5 	   | [Strings](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/08-ex5.md)										 | FIRST DR	     |
| 6 	   | [Control flow](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/09-ex6.md)									 | FIRST DR			  |
| 7	   	   | [Functions](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/10-ex7.md)										 | FIRST DR			  |
| 8	   	   | [Handling errors](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/11-ex8.md)								 | FIRST DR			  |
| 9	   	   | I/O											 | TODO			  |
| 10	   | Streams									     | TODO			  |
| 11	   | Parallel computing								 | TODO			  |
| 12	   | Unit testing									 | TODO			  |
| 13	   | [Writing good Julia](https://github.com/chrisvoncsefalvay/learn-julia-the-hard-way/blob/master/_chapters/16-ex13.md)								 | TODO			  |
|  |**PART 2: Applied Julia**  |
| X01	   | Quadratic solver								 | TODO			  |
| X02	   | FizzBuzz										 | TODO			  |
| X03	   | Bob											 | TODO			  |
| X04	   | Levenshtein distance							 | TODO			  |
| X05	   | Dice											 | TODO			  | 
| X06	   | Great Circle distances							 | TODO			  | 
| X07	   | Data frames									 | TODO			  |
| X08	   | Plotting a time series							 | TODO			  |
| X09	   | Consuming a RESTful API						 | TODO			  |
| X10	   | Shell management from Julia					 | TODO			  |
| X11	   | Moving average in a DataFrame					 | TODO			  |
| X12	   | Naive Bayes classifier							 | TODO			  |
| X13	   | Fun with nucleotide sequences					 | TODO			  |
| X14	   | ? Save the Apollo astronauts ? (waiting for perm) | TODO		  |
| X15	   | Twulia! 										 | TODO			  |
| X16 	   | Longest Collatz sequence						 | TODO			  |


NB. The order of modules may change depending on how the interdependence of the various chapters changes. The roadmap is not final. I am very happy to listen to suggestions from the community, since it's difficult to gauge at the moment what is going to be a core feature in Julia and how the demographic of those learning Julia will evolve.

## Slant

The Julia base package is pretty big, although at the same time, there are lots of other packages around to expand it with. The result is that on the whole, it is impossible to give a thorough overview of all that Julia can do in just a few brief exercises. Therefore, I had to adopt a little 'bias', or 'slant' if you please, in deciding what to focus on and what to ignore. 

Julia is a technical computing language, although it does have the capabilities of any general purpose language and you'd be hard-pressed to find tasks it's completely unsuitable for (although that does not mean it's the best or easiest choice for any of them). Julia was developed with the occasional reference to R, and with an avowed intent to improve upon R's clunkiness. R is a great language, but relatively slow, to the point that most people use it to rapid prototype, then implement the algorithm for production in Python or Java. Julia seeks to be as approachable as R but without the speed penalty. 

Owing to this, and partly to my own background as a data scientist, LJTHW is going to be somewhat biased towards the needs of statisticians. As such, there will be relatively little talk about fast Fourier transforms, integration and other mathemagical concepts that are beyond the immediate need, while some other components, such as the plotting package Gadfly, which would normally not be of general interest, will be explored. I have tried to strike a fair balance, and I hope I have succeeded there.

## Audience

Unlike most of Zed Shaw's _Learn X the hard way_ books, LJTHW is not intended for complete novices to programming – Julia is simply not ready yet for people wishing to learn programming by using it, although I see great potential in teaching people a functional programming language ahead of clobbering them with object-oriented concepts. On the other hand, one of the best things about Julia is that it was written by hackers, not language nerds. Yes, it's got all sorts of [metaprogramming goodness](http://docs.julialang.org/en/release-0.3/manual/metaprogramming/), it's [homoiconic](http://c2.com/cgi/wiki?HomoiconicLanguages) and it's got all sorts of other amazing things about it that may be of interest to a few, but they are not relevant to being good, or even pretty good, at Julia. Therefore, I am treating the audience as one of people who need to get a job done, not computer scientists. The latter probably already have taught themselves Julia!

## How to compile

There were some compilation instructions here. For now, these have been removed because I have found the Dexy system used by Zed Shaw a pain to deal with, and I will instead use a Pandoc-based conversion to a fully fledged eBook. I will provide compilation instructions in a bit, but until then, you could do worse than reading the chapters in sequence on Github!

## How to contribute

<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Learn Julia the Hard Way</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.chrisvoncsefalvay.com" property="cc:attributionName" rel="cc:attributionURL">Chris von Csefalvay</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>. 

Pull requests are welcome! Please note that the contents of this book, including your contributions, may form the foundation of a future publication. By contributing, you waive any and all rights over the content you contribute, save the right to be credited as a contributor to the finished work. While I do intend to eventually market a full-length book version of this manuscript, the Github version will remain forever free and open-source (although it might not get updated). I will always acknowledge the community's contributions to this work, and anyone who has contributed to it and is acknowledged in the CONTRIBUTORS.md file will be expressly acknowledged unless they wish otherwise.

## Author

I'm a data scientist, hacker and recovering lawyer living in Oxford, England. In my day job, I'm a software architect, and my parents still don't know what that means. When not working, I am coding for fun and spending time with my wife and our adorable Tortie kitten, River. My website is [here](http://www.chrisvoncsefalvay.com). You can e-mail me [here](mailto:chris[AT]chrisvoncsefalvay[DOT]com).

