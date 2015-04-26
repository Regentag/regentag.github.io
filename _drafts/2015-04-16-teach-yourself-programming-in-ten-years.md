---
layout: post
title:  "(번역) Teach Yourself Programming in Ten Years"
date:   2015-04-16 21:00:00
categories: etc
---

# 시작하기 전에.
 *[Peter Norvig](http://norvig.com/index.html)*님이 쓴 *[Teach Yourself Programming in Ten Years](http://norvig.com/21-days.html)*를 번역한 글입니다.

 *황요한(John Hwang)*님의 [2006년 번역](http://tavon.org/teach-yourself-programming-in-ten-years-korean.html)과 *Magicboy*님의 [2008년 번역](http://blog.magicboy.net/entry/프로그래밍-10년-완성)을 참고하였습니다. (두 분이 번역할 당시의 원문은 2015년 현재의 글과 달리 훨씬 짧았고 원 저자는 2014년까지 지속적으로 글을 갱신한 것으로 보입니다.) 그리고 [구글 번역기](https://translate.google.com)와 [네이버 사전](http://dic.naver.com)의 도움을 받았습니다.

"Teach yourself XXX"는 국내에서 비슷한 종류의 책들이 흔히 사용하는 제목인 "XXX 완성" 으로 번역하였습니다. 원문에서 제시된 링크들 중 한국어 페이지가 존재하는 곳은 원문의 링크와 한국어 페이지의 링크를 모두 포함시켰습니다.

번역에 대하여 수정해야 할 사항을 발견하셨다면 [GitHub 리파지토리](https://github.com/Regentag/regentag.github.io/issues)에 이슈를 남겨 주시기 바랍니다.

 - 2015. 4. 16.

* * *

## **프로그래밍 10년 완성**
**Peter Norvig**


# 다들 왜 그렇게 급한가?

Walk into any bookstore, and you'll see how to Teach Yourself Java in 24 Hours alongside endless variations offering to teach C, SQL, Ruby, 알고리즘, and so on in a few days or hours. The Amazon advanced search for [[title: teach, yourself, hours, since: 2000](http://www.amazon.com/gp/search/ref=sr_adv_b/?search-alias=stripbooks&unfiltered=1&field-keywords=&field-author=&field-title=teach+yourself+hours&field-isbn=&field-publisher=&node=&field-p_n_condition-type=&field-feature_browse-bin=&field-subject=&field-language=&field-dateop=After&field-datemod=&field-dateyear=2000&sort=relevanceexprank&Adv-Srch-Books-Submit.x=16&Adv-Srch-Books-Submit.y=5)] and found 512 such books. Of the top ten, nine are programming books (the other is about bookkeeping). Similar results come from replacing "teach yourself" with "learn" or "hours" with "days."
The conclusion is that either people are in a big rush to learn about programming, or that programming is somehow fabulously easier to learn than anything else. Felleisen et al. give a nod to this trend in their book [How to Design Programs](http://www.ccs.neu.edu/home/matthias/HtDP2e/index.html), when they say "나쁜 프로그래밍은 쉽다. 바보들은 그들이 아무리 멍청하더라도 21일만에 그것을 배울 수 있다." The Abtruse Goose comic also had [their take](http://abstrusegoose.com/249).

『C++ 언어 24시간 완성 (*[Teach Yourself C++ in 24 Hours](http://www.amazon.com/Sams-Teach-Yourself-Hours-5th/dp/0672333317/ref=sr_1_6?s=books&ie=UTF8&qid=1412708443&sr=1-6&keywords=learn+c%2B%2B+days)*)』이라는 제목이 무슨 의미인지 분석해 보자.

 * **완성:** In 24 hours you won't have time to write several significant programs, and learn from your successes and failures with them. You won't have time to work with an experienced programmer and understand what it is like to live in a C++ environment. In short, you won't have time to learn much. So the book can only be talking about a superficial familiarity, not a deep understanding. As Alexander Pope said, a little learning is a dangerous thing.

 * **C++:** 24시간 동안 (만약 이미 알고있는 다른 언어가 있다면) C++ 언어의 일부 문법을 배울 수 있을 것이다. 그러나 C++ 언어를 어떻게 사용해야 하는지에 대해 많은것을 배울 수는 없다. 예를 들어 당신이 베이직 개발자라면 C++ 언어의 문법을 베이직처럼 사용게 될 수는 있겠지만 C++ 언어가 실제로 무엇을 하는것에 좋은지, 그리고 나쁜지 알 수 없다. 요점은 무엇인가? [Alan Perlis](http://www-pu.informatik.uni-tuebingen.de/users/klaeren/epigrams.html)는 다음과 같이 말했다. "프로그래밍에 대한 당신의 생각에 영향을 주지 못하는 언어는 배울 가치가 없다". 한가지 가능한 점은 특정 과제를 수행하기 위한 기존 도구(*역주: 프로그램 또는 라이브러리)를 다루기 위하여 C++(또는 대부분 자바스크립트나 프로세싱 같은) 언어의 매우 작은 부분만을 배우는 것이다. 하지만 그것은 프로그래밍을 어떻게 하는 것인가에 대하여 배우는 것이 아니라, 단지 과제를 수행하기 위한 것 뿐이다.

 * **24시간:** 불행히도, 24시간은 충분치 못하다. 이에 대하여 뒤에서 설명할 것이다.

# 프로그래밍 10년 완성

Researchers ([Bloom (1985)](http://www.amazon.com/exec/obidos/ASIN/034531509X/), [Bryan & Harter (1899)](http://norvig.com/21-days.html#bh), [Hayes (1989)](http://www.amazon.com/exec/obidos/ASIN/0805803092), [Simmon & Chase (1973)](http://norvig.com/21-days.html#sc)) have shown it takes about ten years to develop expertise in any of a wide variety of areas, including chess playing, music composition, telegraph operation, painting, piano playing, swimming, tennis, and research in neuropsychology and topology. The key is deliberative practice: not just doing it again and again, but challenging yourself with a task that is just beyond your current ability, trying it, analyzing your performance while and after doing it, and correcting any mistakes. Then repeat. And repeat again. There appear to be no real shortcuts: even Mozart, who was a musical prodigy at age 4, took 13 more years before he began to produce world-class music. In another genre, the Beatles seemed to burst onto the scene with a string of #1 hits and an appearance on the Ed Sullivan show in 1964. But they had been playing small clubs in Liverpool and Hamburg since 1957, and while they had mass appeal early on, their first great critical success, Sgt. Peppers, was released in 1967. [Malcolm Gladwell](http://www.amazon.com/Outliers-Story-Success-Malcolm-Gladwell/dp/0316017922) has popularized the idea, although he concentrates on 10,000 hours rather than 10 years.

It may be that 10,000 hours, not 10 years, is the magic number. Or it might be some other metric; Henri Cartier-Bresson (1908-2004) said "Your first 10,000 photographs are your worst." True expertise may take a lifetime: Samuel Johnson (1709-1784) said "Excellence in any department can be attained only by the labor of a lifetime; it is not to be purchased at a lesser price." And Chaucer (1340-1400) complained "the lyf so short, the craft so long to lerne." Hippocrates (c. 400BC) is known for the excerpt "ars longa, vita brevis", which is part of the longer quotation "Ars longa, vita brevis, occasio praeceps, experimentum periculosum, iudicium difficile", which in English renders as "Life is short, [the] craft long, opportunity fleeting, experiment treacherous, judgment difficult." Of course, no single number can be the final answer: it doesn't seem reasonable to assume that each of programming, chess playing, checkers playing, and music playing could all require exactly the same amount of time to master, nor that all people will take exactly the same amount of time.

# 프로그래머가 되고 싶다면

여기 프로그래밍을 정복하기 위한 나의 방안들이 있다.

 * 프로그래밍에 **흥미**를 가지고, 재미가 있기 때문에 이것을 하는 것이어야 한다. Make sure that it keeps being enough fun so that you will be willing to put in your ten years/10,000 hours.

 * **Program.** 가장 좋은 학습 방법은 [직접 해 보면서(learning by doing)](http://www.engines4ed.org/hyperbook/nodes/NODE-120-pg.html) 배우는 것이다. To put it more technically, "the maximal level of performance for individuals in a given domain is not attained automatically as a function of extended experience, but the level of performance can be increased even by highly experienced individuals as a result of deliberate efforts to improve." [(p. 366)](http://www2.umassd.edu/swpi/DesignInCS/expertise.html) and "the most effective learning requires a well-defined task with an appropriate difficulty level for the particular individual, informative feedback, and opportunities for repetition and corrections of errors." (p. 20-21) The book *[Cognition in Practice: Mind, Mathematics, and Culture in Everyday Life](http://www.amazon.com/exec/obidos/ASIN/0521357349)* is an interesting reference for this viewpoint.

 * 다른 프로그래머들과 **함께 대화**하고, 다른 프로그램(코드)을 읽어야 한다. 이것은 어떠한 책이나 교육 과정보다도 중요하다.

 * If you want, put in four years at a **college** (or more at a graduate school). This will give you access to some jobs that require credentials, and it will give you a deeper understanding of the field, but if you don't enjoy school, you can (with some dedication) get similar experience on your own or on the job. In any case, book learning alone won't be enough. "Computer science education cannot make anybody an expert programmer any more than studying brushes and pigment can make somebody an expert painter" says Eric Raymond, author of The New Hacker's Dictionary. One of the best programmers I ever hired had only a High School degree; he's produced a lot of [great](http://www.xemacs.org/) [software](http://www.mozilla.org/), has his own [news group](http://groups.google.com/groups?q=alt.fan.jwz&meta=site%3Dgroups), and made enough in stock options to buy his own [nightclub](http://en.wikipedia.org/wiki/DNA_Lounge).

 * Work on **projects with** other programmers. Be the best programmer on some projects; be the worst on some others. When you're the best, you get to test your abilities to lead a project, and to inspire others with your vision. When you're the worst, you learn what the masters do, and you learn what they don't like to do (because they make you do it for them).

 * Work on **projects _after_** other programmers. Understand a program written by someone else. See what it takes to understand and fix it when the original programmers are not around. Think about how to design your programs to make it easier for those who will maintain them after you.

 * Learn at least a half dozen **programming languages**. Include one language that emphasizes class abstractions (like Java or C++), one that emphasizes functional abstraction (like Lisp or ML or Haskell), one that supports syntactic abstraction (like Lisp), one that supports declarative specifications (like Prolog or C++ templates), and one that emphasizes parallelism (like Clojure or Go).

 * Remember that there is a "**computer**" in "computer science". Know how long it takes your computer to execute an instruction, fetch a word from memory (with and without a cache miss), read consecutive words from disk, and seek to a new location on disk. (Answers here.)

 * Get involved in a language **standardization** effort. It could be the ANSI C++ committee, or it could be deciding if your local coding style will have 2 or 4 space indentation levels. Either way, you learn about what other people like in a language, how deeply they feel so, and perhaps even a little about why they feel so.

 * Have the good sense to **get off** the language standardization effort as quickly as possible.

With all that in mind, its questionable how far you can get just by book learning. Before my first child was born, I read all the How To books, and still felt like a clueless novice. 30 Months later, when my second child was due, did I go back to the books for a refresher? No. Instead, I relied on my personal experience, which turned out to be far more useful and reassuring to me than the thousands of pages written by experts.

Fred Brooks, in his essay *[No Silver Bullet](http://en.wikipedia.org/wiki/No_Silver_Bullet)* identified a three-part plan for finding great software designers:

 1. Systematically identify top designers as early as possible.

 2. Assign a career mentor to be responsible for the development of the prospect and carefully keep a career file.

 3. Provide opportunities for growing designers to interact and stimulate each other.

This assumes that some people already have the qualities necessary for being a great designer; the job is to properly coax them along. [Alan Perlis](http://www-pu.informatik.uni-tuebingen.de/users/klaeren/epigrams.html) put it more succinctly: "Everyone can be taught to sculpt: Michelangelo would have had to be taught how not to. So it is with the great programmers". Perlis is saying that the greats have some internal quality that transcends their training. But where does the quality come from? Is it innate? Or do they develop it through diligence? As Auguste Gusteau (the fictional chef in Ratatouille) puts it, "anyone can cook, but only the fearless can be great." I think of it more as willingness to devote a large portion of one's life to deliberative practice. But maybe fearless is a way to summarize that. Or, as Gusteau's critic, Anton Ego, says: "Not everyone can become a great artist, but a great artist can come from anywhere."

So go ahead and buy that Java/Ruby/Javascript/PHP book; you'll probably get some use out of it. But you won't change your life, or your real overall expertise as a programmer in 24 hours or 21 days. How about working hard to continually improve over 24 months? Well, now you're starting to get somewhere...

* * *

# References

Bloom, Benjamin (ed.) *[Developing Talent in Young People](http://www.amazon.com/exec/obidos/ASIN/034531509X)*, Ballantine, 1985.

Brooks, Fred, *[No Silver Bullets](http://citeseer.nj.nec.com/context/7718/0)*, IEEE Computer, vol. 20, no. 4, 1987, p. 10-19.

Bryan, W.L. & Harter, N. "Studies on the telegraphic language: The acquisition of a hierarchy of habits. *Psychology Review*, 1899, 8, 345-375

Hayes, John R., *[Complete Problem Solver](http://www.amazon.com/exec/obidos/ASIN/0805803092)* Lawrence Erlbaum, 1989.

Chase, William G. & Simon, Herbert A. ["Perception in Chess"](http://books.google.com/books?id=dYPSHAAACAAJ&dq=%22perception+in+chess%22+simon&ei=z4PyR5iIAZnmtQPbyLyuDQ) *Cognitive Psychology*, 1973, 4, 55-81.

Lave, Jean, *[Cognition in Practice: Mind, Mathematics, and Culture in Everyday Life](http://www.amazon.com/exec/obidos/ASIN/0521357349)*, Cambridge University Press, 1988.

* * *

# Answers

Approximate timing for various operations on a typical PC:

|                                     |                                        |
|-------------------------------------|---------------------------------------:|
| execute typical instruction         |        1/1,000,000,000 sec = 1 nanosec |
| fetch from L1 cache memory          |                            0.5 nanosec |
| branch misprediction                |                              5 nanosec |
| fetch from L2 cache memory          |                              7 nanosec |
| Mutex lock/unlock                   |                             25 nanosec |
| fetch from main memory              |                            100 nanosec |
| send 2K bytes over 1Gbps network    |                         20,000 nanosec |
| read 1MB sequentially from memory   |                        250,000 nanosec |
| fetch from new disk location (seek) |                      8,000,000 nanosec |
| read 1MB sequentially from disk     |                     20,000,000 nanosec |
| send packet US to Europe and back   | 150 milliseconds = 150,000,000 nanosec |

* * *

# 부록: 언어 선택하기

Several people have asked what programming language they should learn first. There is no one answer, but consider these points:

 * *Use your friends.* When asked "what operating system should I use, Windows, Unix, or Mac?", my answer is usually: "use whatever your friends use." The advantage you get from learning from your friends will offset any intrinsic difference between OS, or between programming languages. Also consider your future friends: the community of programmers that you will be a part of if you continue. Does your chosen language have a large growing community or a small dying one? Are there books, web sites, and online forums to get answers from? Do you like the people in those forums?
 * *Keep it simple.* Programming languages such as C++ and Java are designed for professional development by large teams of experienced programmers who are concerned about the run-time efficiency of their code. As a result, these languages have complicated parts designed for these circumstances. You're concerned with learning to program. You don't need that complication. You want a language that was designed to be easy to learn and remember by a single new programmer.
 * *Play.* Which way would you rather learn to play the piano: the normal, interactive way, in which you hear each note as soon as you hit a key, or "batch" mode, in which you only hear the notes after you finish a whole song? Clearly, interactive mode makes learning easier for the piano, and also for programming. Insist on a language with an interactive mode and use it.

Given these criteria, my recommendations for a first programming language would be **[Python](http://python.org/)** or **[Scheme](http://www.schemers.org/)**. Another choice is Javascript, not because it is perfectly well-designed for beginners, but because there are so many online tutorials for it, such as [Khan Academy's tutorial](https://www.khanacademy.org/computing/cs/programming). But your circumstances may vary, and there are other good choices. If your age is a single-digit, you might prefer [Alice](http://alice.org/) or [Squeak](http://www.squeak.org/) or [Blockly](https://blockly-demo.appspot.com/static/apps/index.html) (older learners might also enjoy these). The important thing is that you choose and get started.

* * *

# Appendix: Books and Other Resources

Several people have asked what books and web pages they should learn from. I repeat that "book learning alone won't be enough" but I can recommend the following:

 * **Scheme**: [Structure and Interpretation of Computer Programs (Abelson & Sussman)](http://www.amazon.com/gp/product/0262011530) is probably the best introduction to computer science, and it does teach programming as a way of understanding the computer science. You can see [online videos of lectures](http://www.swiss.ai.mit.edu/classes/6.001/abelson-sussman-lectures/) on this book, as well as the [complete text online](http://mitpress.mit.edu/sicp/full-text/book/book.html). The book is challenging and will weed out some people who perhaps could be successful with another approach.
 * **Scheme**: [How to Design Programs (Felleisen et al.)](http://www.amazon.com/gp/product/0262062186) is one of the best books on how to actually design programs in an elegant and functional way.
 * **Python**: [Python Programming: An Intro to CS (Zelle)](http://www.amazon.com/gp/product/1887902996) is a good introduction using Python.
 * **Python**: Several online [tutorials](http://wiki.python.org/moin/BeginnersGuide) are available at [Python.org](http://python.org/).
 * **Oz**: [Concepts, Techniques, and Models of Computer Programming (Van Roy & Haridi)](http://www.amazon.com/gp/product/0262220695) is seen by some as the modern-day successor to Abelson & Sussman. It is a tour through the big ideas of programming, covering a wider range than Abelson & Sussman while being perhaps easier to read and follow. It uses a language, Oz, that is not widely known but serves as a basis for learning other languages. <

* * *

# Notes

T. Capey points out that the [Complete Problem Solver](http://www.amazon.com/exec/obidos/ASIN/0805803092) page on Amazon now has the "Teach Yourself Bengali in 21 days" and "Teach Yourself Grammar and Style" books under the "Customers who shopped for this item also shopped for these items" section. I guess that a large portion of the people who look at that book are coming from this page. Thanks to Ross Cohen for help with Hippocrates.

* * *

[이 문서의 저작권은 *Peter Norvig*에게 있습니다. (2001-2014)](http://norvig.com/index.html)


끝.