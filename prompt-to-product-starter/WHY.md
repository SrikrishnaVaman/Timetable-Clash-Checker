# Why this workshop


## The argument in brief

For seventy years, programmers dreamed of writing software in plain
English. COBOL tried, fourth-generation languages tried, and decades of
research on program synthesis tried. Around 2020 the boundary finally
moved: a large language model can now turn a paragraph into a working
function in seconds.

Software is the discipline best placed to absorb this change, because of
its material. Code is text, and language models produce text. A program
can be checked in seconds by running it, changed in seconds by rewriting
it, and restored for free with `git revert`. None of this is true of a
bridge, a chemical plant or an aircraft wing.

## What changes, and what doesn’t

In 1986 Fred Brooks split the difficulty of software into two kinds
(Brooks 1987). Accidental complexity is the work of expressing a
solution: syntax, boilerplate, remembering library calls. Essential
complexity is the work of understanding the problem: what the software
must do, its edge cases, its trade-offs. Generative AI is the largest
reducer of accidental complexity we have ever had. It does very little
for essential complexity.

Peter Naur made a related point a year earlier (Naur 1985). Programming,
he argued, is building a theory of the problem in the programmer’s mind;
the program text is only a shadow of that theory. An AI tool can produce
the shadow. It cannot put the theory in your head, and without it,
nobody can safely change, debug or defend the code.

## Six skills and one rule

What is left for you, then, is a set of six skills. **Specification**:
turning a fuzzy requirement into a testable statement of what “done”
means. **Verification**: designing the test that would catch an answer
that looks right but is not. **Review**: reading code faster and more
critically than you write it. **Understanding** (what Naur called
theory-building): keeping the understanding of a system alive, in your
head and in words your team can share. **Orchestration**: running the
loop of prompt, run, verify and commit as a habit. **Ownership**: being
able to explain and defend every line you submit, whoever or whatever
drafted it.

## The ownership rule

One rule ties the six skills together: *if you cannot explain a piece of
code you submitted, you are not done with it.* It applies whoever or
whatever drafted the code. An AI assistant can take on much of the
typing; it cannot take on the responsibility.

## References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-brooks1987nosilver" class="csl-entry">

Brooks, Jr., Frederick P. 1987. “No Silver Bullet: Essence and Accidents
of Software Engineering.” *Computer* 20 (4): 10–19.

</div>

<div id="ref-naur1985theory" class="csl-entry">

Naur, Peter. 1985. “Programming as Theory Building.” *Microprocessing
and Microprogramming* 15 (5): 253–61.

</div>

</div>
