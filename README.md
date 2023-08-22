# oferhlyp_python

## Overview
**Oferhlýp** is a free libre open source abstract strategy game played between two players on 7x7 grid. On the surface, gameplay is similar to checkers (draughts). However, there are several differences:

- Tokens may move in any direction rather than just forwards diagonally.
- A player’s own pieces may be jumped to create a more dynamic game.
- Tokens must be jumped twice before they are removed from the board.
- Each player has a "king" token that must be captured to end the  game.


## History
**Oferhlýp** was conceived in 2013 while I was working on another game. _Claim the Crown_ incorporated the concept of tokens with two hit points but featured various types of Middle Ages themed units like spearmen and archers and replaced jump attacks with dice rolling combat. **Oferhlýp** is a purer abstract interpretation of that with a focus on strategy over luck.

The first iteration of **Oferhlýp** was fun to play and had good early and middle play development, but the endgame stalled and produced a lot of stalemate situations. Beginning with the version 2 fork, the board has been revised to a standard grid (*a la* certain Hnefetafl variants) and kings have been introduced.

**Oferhlýp** is developed on Codeberg and living rules can be found in [this repository](https://codeberg.org/jaerrib/oferhlyp).

## Project goals
My goal with **Oferhlýp** *the board game* is to build an engaging abstract strategy experience that is simple to learn while offering a level of complexity in mastering it. My goal for *the Python version* is to build a companion game to be hosted with the [**Mǽrstánas** web app](https://codeberg.org/jaerrib/maerstanas-webapp).