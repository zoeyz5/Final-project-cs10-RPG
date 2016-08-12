# Final-project
We are buliding an RPG game 
In this game, you have mainly these functions for adventuring:
(However, there are some bugs caused by the delay of the turtle graphic so please don't press the buttom too frequently!!! Thank you~~

1)	Battle
We have already help you set the difficulty of this game to a good level, so don’t worry about the balance of the game.
There are almost 20 maps in this game. When you go to entrances and exits we will transfer you to the correlation map automatically. There are even some second level maps like some buildings waiting you to explore. 
You can set whether or not to meet an enemy by the setting. Make sure to switch this button off when your HP is too low.
The chance that you meet an enemy is 1/12 by step.
You can escape when you believe the chance to win is too low.
There are many skills you can master. With the upgrade of your level, your skill will be unlocked. Different skills may be suitable for different levels.
One interesting thing is that when both your and your enemies’ HP are negative, you and they still have chance to do the last fight. This skill is very powerful and will cause more damage. 
There are 5 bosses in the game. Their levels have negative relationship with the time that you might meet them. The final goal is to beat boss 5 in the tower and save the world!!!

2)	Shopping
You can buy 2 things in shop that is represented by a red icon. They are “Potion of Life” (Red) and “Crystal of Power” (Blue) which help recovers your HP and MP.
You need money to buy these two stuffs. The gold can be earned in two following ways:
1.	Pick up from the treasure in the maps.
2.	Be rewarded when winning a battle

3)	Walking
Yeah! You have the feeling of being a virtual world and have freedom to explore and appreciate the cute plants and architectures.

4)	P.S
When you don’t know which icon represents what, just use the helper in the game

5)	Loading
You can also load your progress in our game so you don’t need to start again next time.

1.	Various lists

We use various lists and dictionaries to store our variables and take the adventages of the dictionary to speed up the program.
We use list in the list to store more information, the items in the list of list will naturally form the index so they are very useful to represent the position and the items.
For example, we put all the positions a player can reach in a map in a list so we can directly predicate whether a player can go there or not(the place one can go is represented by "0", and the place one can't go is represented by "1"

2.	variables

The basic ones are playerx and playery, all of our map systems are based on these two variables. 
we have different variables for the enemies and player, and each of them has different variables like HP, MP, ATK, DEF...etc. Although we didn't learn class in lecture we try to use this in our program.
the player's variables are global ones because we need to use they all the time.
we end the script pf the enemies once their HP is lower or equals to 0, so we can continue our game.
we also have some variables that not directly affect the battle system but helping items like gold. Player can use gold to buy the portions.

3.  scripts

Initially, We have many scripts in the program because there are many options of actions. We separate each scene to avoid making a mess. 
Some of the scripts are used for settings and some of them are used for operation and some contains both. Some are more functional while some are more expressive force that helps the game to reach the aesthetics effect to accomplish an entire game.
With a main script that is running for most of the time and contact with other scripts by something that is very similar to the broadcasting in Snap!, all the sprites are linked together and interact well with each other. With the same idea we call another fuction when the other is operating so we don't need to boardcast.

