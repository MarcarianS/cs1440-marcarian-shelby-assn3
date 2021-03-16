The first thing I saw when I opened your diagram was your
MenuOption Class. Your attribute types are defined as "any". 
For attributes, usually you want a specific type for your 
attributes. For your 'command' and 'description', I believe 
those types would be Strings. 
The next thing I saw was that your all of your attributes and
functions are public in your UML (denoted by the "+" in front of them 
instead of "-"). Once I looked closer, I saw that you showed them with 
double underscores, but in UML you would want to use the "-" instead of 
double underscores.
I also notice that all of the relationships between your classes are dashed
lines instead of solid. From what I remember about UML, that indicates a
dependency, but not an association. While it is true that each of the
classes are dependent on each other as you have shown, I think the 
relationship is supposed to be stronger. solid lines represent classes that
you can traverse between. In other words, from a Card object, you can get
back to the Deck object that it belongs to. I think your UML would be fine
if you just changes the appropriate lines from dashed to solid.
Next, it looks like you haven't identified the types for the arguments in
methods. Those, from what I know about UML, are inportant to understanding
the diagram. 
It also looks like your constructors are called init. That is what they're
called in the actual code, but typically they're named by the class which 
they construct for. So, the menu constructor would look like 
"Menu(header : String)" instead of "__init__(header)". 
It looks like you've got the starter code thoroughly diagramed, but there
are a few other methods used in the starter code that aren't already defined
that I think are pretty useful for the rest of the code. Of course, if
you're branching off from the starter code you can ignroe this part!
Finally, from what I understand about the UI Class, it has no attributes.
Since the commands come from the user, and are given to the UI after it 
has been created, I don't know that it could be an attrubute to the UI class
Good work on your UML, and good luck with the rest of your project!
