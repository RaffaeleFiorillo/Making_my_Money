# Making_my_Money
This Repository contains the very first game I created, which I thought I had lost.

![Cover](https://github.com/RaffaeleFiorillo/Making_my_Money/assets/75253335/10dc7679-0291-46ca-adba-1868dfb08d69)

# Important Notes
For sentimental value, I decided to mantain the code as was when I originally made it. Therefore, this repository contains the original project structure without changing a thing. Not a single comma, dot, line of code... 
This means that this repository will remain as is with an additional "Making my Money(Beta).exe". The README could be an exception, meaning that it could be updated.

As my first game, it helped me learn the basics of pygame and Game Development, allowing me to later build more complex stuff (like [Fast and Curious](https://github.com/RaffaeleFiorillo/Fast_and_Curious), [Scopa Game](https://github.com/RaffaeleFiorillo/Scopa_Game), etc.).

I began making this game in August 5, 2019 but only had a playable version in September 7, 2019 (at my birth day). The project structure is bad, the code is basic, the language used is inconsistent (English, Portuguese, Italian, CV-Kriol), ... it is a mess! But what can I say? When I played it again 5 YEARS LATER I liked it a lot. The nostalgia was strong with this one. It made me laugh, it made me excited,... and I want to share this feeling with others.

I will make a "Making_my_Money_Remastered" repository (you can find it [here](https://github.com/RaffaeleFiorillo/Making_my_Money_Remastered)), where I will work on improving this game in terms of structure, code, game-feeling, polishing, etc.

# Description of the Game
In this section I will talk about how the game works, the agents and entities involved,... and all that stuff 

## Goal
You must collect the most amount of money possible, while staying alive by avoiding touching the enemies.

## Main Character
![io vivo](https://github.com/RaffaeleFiorillo/Making_my_Money/assets/75253335/cc209fcc-7da0-4572-9ced-1096b48230bc)

This is the Character you control. His name is "Io"(It)/ "Me"(Eng)/ "Eu"(Pt). He can move Up, Down, Left and Right and also in any (logically possible) diagonal combination of this directions.

## Enemies
![enemy](https://github.com/RaffaeleFiorillo/Making_my_Money/assets/75253335/fd402cfe-fd7f-4de3-a254-b963f729dfc2)

There is a total of 5 Enemies. All look and move in the same way. They can move horizontally and vertically, but only in one of them at the time. Their movement is random, hence unpredictable.

## Points
Collectable that pop out randomly and at random places during the game. You must touch them to gain points. There are 3 different kind of collectables, each one with it's own value (Coin < Golden Ingot < Diamond).

Notes: 
- I think the idea was to have more points the faster you collect a collectable, but it was not implemented;
- The only collectable that currently works is the Coin;

### Coin
![moneta](https://github.com/RaffaeleFiorillo/Making_my_Money/assets/75253335/b6e11901-5ebe-45cf-9827-aa1da55bab2c)

The most common collectable, but also the least valuable. It holds a value of 5 points.

### Golden Ingot
![pepita](https://github.com/RaffaeleFiorillo/Making_my_Money/assets/75253335/21091f22-cb81-4c93-8164-ab867f8950ce)

Exists only as a concept and as assets (image and sound). It's value was not specified.

### Diamond
![diamante](https://github.com/RaffaeleFiorillo/Making_my_Money/assets/75253335/97365169-c34e-4bcb-83f2-847f0028a2cf)

Exists only as a concept and as assets (image and sound). It's value was not specified.

## Life
![hp](https://github.com/RaffaeleFiorillo/Making_my_Money/assets/75253335/70a76585-0425-4868-b834-069a13ca62f0)

Another type of Collectable. The Main Character gains a Life when touching it. Exists only as a concept and as assets (image and sound).

# Fun Facts:

- As was already said, this was the very first game I created;
- I wanted to recreate the game "Snake" (from the Nokia phone). Which can be noted if you pay attention to the window's caption, since I completely forgot to change it after switching to creating an original game. I decided to mantain snakes in the game, but as the enemies;
- The ideia for the game was due to a high influence I had from my Tunisian (at the time) brother-in-law: Hani Bahba. Which was (and I think still is) searching for ways to get rich;
