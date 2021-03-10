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
