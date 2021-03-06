Overall the flow of your diagram is looking really good. The first thing I 
noticed was that you drew the ‘creates’ line from the UserInterface to the 
NumberSet class. If you’re doing it a bit different than the starter code, I’m 
sure there’s a totally some way to do it this way, though the given setup in 
the starter code has NumberSet as part of the Card class rather than 
UserInterface. I believe that class is set up for generating the numbers on the
 cards as Card is the only class that imports NumberSet in the starter code. 
Though once again, you might be intending to do it differently. I think that 
for UserInterface, you can remove the box containing “None” for having no 
variables, but I’m not completely sure. For the rest of your variables and 
methods I can tell you’ve thought about a lot of the solution, I’m not seeing 
anything that is obviously missing that is needed to get it to work. I like the 
inclusion of the words on the arrows showing directions because it shows the 
meaning of the lines before we’ve been taught which lines to use in more 
specific situations. Each of the methods with arguments are well documented to 
include names and variables types, great job on that. One last thing is a total 
nitpick and it probably doesn’t affect anything, but you could maybe shift your 
class boxes in a way to not include a large white space in the corner. Though 
even without that, it is great and readable how it is now. Great work!


The first thing that I noticed that I would suggest is to use a frame that 
outlines your entire UML diagram, this not only would clearly show that every 
class is contained in what you're labeling "bingo" but It also helps the layout 
of your UML diagram. Just with the formatting adding a frame also adds a border 
around your class boxes so they aren't pushed right up against the walls of 
your UML diagram. The next thing I noticed is that there is no connection 
between Card and NumberSet, I think that needs to be in there since cards 
contain NumberSets. So adding a relation that each Card has a NumberSet within 
in it would be important. I really like how you connected NumberSet to 
UserInterface though, I can see the logic behind that and can understand where 
you are coming from and I might even go add that to my UML now. All of your 
individual class diagrams look properly set up and correctly show the 
information inside. One thing I would suggest is that instead of labeling 
m_cards as an array in your Deck class, to label it as Card[] to show that it 
is an array containing Card objects. Otherwise upon looking at it I can't 
really see anything else that I would change, I really also like your use of 
the arrows like Erik talked about in the lecture today, adding that sense of 
direction to the diagram is super helpful and makes it a lot easier to read. 
Great job!


I think your UML is off to a great start! I can see that you've documented 
the starter code effectively and added some new methods of your own to fill 
in the gaps that were present. Your UML is also legible, each of your classes 
are named correctly, and you included association and dependency arrows to 
match your code. Nice work! This leads me to believe that you have a good 
understanding of how the starter code works, and you have some sort of plan 
on how to implement this program! 
However, there are a few small things I am noticing that could be improved on. 
First of all, there are some typos in your UML. In the UserInterface class, 
-getNumberInput has "iteget" instead of "integer", and -getStringInput has 
is spelled "INput" on accident, but those are pretty easy things to fix. 
Secondly, whenever you specify an array, if I understand UML correctly, I 
believe it needs to be typed like so: type[]. This can be an int, string, 
bool, or even an object of another class as the type of array. Take a closer 
look at the options array and m_cards array, as those are likely to be 
comprised of objects of a different class (if you are following the starter 
code closely...if you aren't doing that, then please disregard what I said!). 
Third of all, if you have no data fields in your UserInterface class, instead 
of typing "None", if I understand UML correctly, I think you can simply leave 
it blank.
It also might be beneficial to denote how many objects are creating / being 
created by other objecst using multiplicity constraints.
Again, you may be solving this program differently than me, but if you are 
mostly going off of the starter code, I do not think UserInterface and 
NumberSet are supposed to connect directly. The starter code uses a different 
class as a sort of middle-man between the UserInterface class and the NumberSet, 
so try to take a closer look at that!
One final thing: in your card class, I think you forgot to specify what parameters 
print() can take. You did it correctly in the Deck class, so try to replicate that! 
Alright, I'm sorry if I got a bit nitpicky, but I do think you are off to a great 
start! Good job so far!


It looks like you did a very thorough job on your UML diagram.
The Navigability specifications by your association and dependency arrows make 
your daigram easy to read and understand.
The first thing that jumps to my attention about your UML diagram is that the 
UserInterface class creates a NumberSet object.
Although the source code didn't seem to to do this, you may have other plans. 
It was to my understanding that the Deck and Card classes created and used the 
NumberSet class but again, if that's your plan there's nothing wrong with that.
Including + and - before data members and operations provides a layout for your
UML diagram that makes it easier to read. Gret job including those.
I noticed that in many of your classes you have the initializer included in the 
operations, although the in-class examples didn't include this and I think Erik 
said something about it.
Including it clarifies members that are defined in the initializer and variables 
that are dependent upon the input of the function.
On the other side of the spectrum is including them when they are redundant such 
as when each input term is used as a data member also.
I think you hit the perfect balance between including them and ommiting them, 
well done!
This may be a little unrelated and or unessesary in your UML diagram but from my 
beginers perspective on UML diagrams it seems like setting up the diagram starting 
at the top center makes the most sense. Then all the classes that it uses are 
underneath or the the sides. This directs the eye and makes the diagram easy to 
read. I'll need to take a bit of my own advice in this case!
Great job, I hope you do well on your final program!
