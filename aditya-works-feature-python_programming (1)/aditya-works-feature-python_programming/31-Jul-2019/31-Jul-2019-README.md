## Automation
* Automation is the creation of technology and its application
in order to control and monitor the production and delivery
of various goods and services.
* It performs tasks that were previously performed by humans.
* Automation is being used in a number of areas such as manufacturing,
transport, utilities, defense,facilities, operations and lately,
information technology.
* Automation can be performed in many ways in various industries.
* For example, in the information technology domain, a software script can test
a software product and produce a report.
* There are also various software tools available in the market
which can generate code for an application.
* The users only need to configure the tool and define the process.
* In other industries, automation is greatly imporoving productivity,
saving time and cutting costs.
* Automation is evolving quickly and business intelligence in application 
is a new form of high-quality automation.
* In the technology domain, the impact of automation is increasing rapidly,
both in the software/hardware and machine layer.
* However, despite advances in automation, some manual intervention 
is always advised, even if the tool can perform most of the task.
### Uses of Automation : 
#### 1. To increase productivity :
* The automation of manufacturing operation usually increase 
production rate.
* This means greater output per hour of labour input.
* Thus, automation leads to increase in labour productivity.
#### 2. To reduce cost of production :
* The automation reduces the labour cost and increases the rate of production,
thereby reducing the cost of production.
#### 3. To improve product quality :
* The automation not only results in higher production rates than manual 
operations but also improves the product quality.
#### 4. To mitigate the effects of labour shortages : 
* In developed countries, where there is shortage of labour,
automated operations are used as a substitute for labour.
#### 5. To reduce production time :
* The automation reduces the time required for manufacturing the product.
#### 6. To avoid high cost of not automating :
* The automation exhibits overall benefits like : improved quality, high
better customer rate of production, higher salaries, better labour relations,satisfaction
and better company image.
#### 7. To have better control over manufacturing activities :
* Automation provides better control over entire manufacturing activity of a company.
#### 8. To improve worker safety : 
* The automation can completely replace the worker.
* The automation has changed the role of worker from active participation 
to a supervision.
#### 9. To reduce or eliminate routine manual and clerical tasks :
* Automation reduces/eliminates routine manual and clerical tasks which are
boring.
## Pattern Matching
* Pattern matching in computer science is the checking and locating of specific sequence of data 
of some pattern among raw dta or a sequence of tokens.
* Unlike pattern recognition, the match has to be exact in the case of pattern 
matching.
* Pattern matching is one of the most fundamental and important paradigms
in several programming languages.
* Many application makes uses of pattern matching as major part of their tasks.
* Pattern matching, in its classical form, involves the use of one-dimensional string
matching.
* Patterns are either tree structures or sequences.
* There are different classes of programming languages and machines which make use of 
pattern matching.
* In the case of machines, the major classification include deterministic finite state
automata, deterministic pushdown automata
* Regular programming languages make use of regular expressions for pattern matching.
* Tree patterns are also used in certain programming languages like 
Haskell as tool to process data based on the structure.
* There are many application for pattern matching in computer science.
* High-level language compilers make use of pattern matching in order to 
parse source files to determine if they are syntactically correct.
* In Programming languages and applications, pattern matching is used in identifying
the matching pattern or substituting the matching pattern with another token sequence.
## Regular Expression 
* A RegEx, or Regular Expression, is a sequence of character that forms a search pattern.
* RegEx can be used to check if a string contains the specified search pattern.
#### Regex Module
* Python has a built-in package called re, which can be used to work with
Regular Expressions.
* Import the re module:
```
import re
```
#### RegEx in Python
* When you have imported the re module, you can start using regular expressions:
Searching the string to see if it starts with "The" and ends with "Spain" :
```
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
```
#### RegEx Functions
The re module offers a set of functions that allow us to search a string for a match:
```
Function     Description
findall      Returns a list containing all matches
search       Returns a Match object if there is a match anywhere in the string
split        Returns a list where the string has been split at each match
sub          Replaces one or many matches with a string
```
#### Metacharacters
Metacharacters are characters with a special meaning :
```
Character    Description
 []          A set of character
 
  \          Signals a specials sequence(can also be used to escape special characters)
  
  .          Any character (except newline character)
  
  ^          Starts with 
  
  $          End with
  
  *          Zero or more occurrences
  
  +          One or more occurrences
  
  {}         Exactly the specified number of occurrences
  
  |          Either or 
  
  ()         Capture and group
```
#### Special Sequences
* A special sequence is a \ followed by one of the characters in the list below,
```
Character        Description
\A             Returns a match if the specified characters are at the beginning of the string

\b             Returns a match where the specified characters are at the beginning or at the end of a word

\B             Returns a match where the specified characters are present,
               but NOT at the beginning(or at the end)of a word

\d             Returns a match where the string DOES NOT contains digits

\s             Returns a match where the string contains a white space character

\S             Returns a match where the string DOES NOT contain a white space character

\w             Returns a match where the string contains any word characters

\W             Returns a match where the string DOES NOT contain any word characters

\Z             Returns a match if the specified characters are at the end of the string 

```
