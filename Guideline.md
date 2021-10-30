# Guideline for the Roguelike game

This Rougelike game is developed by **Steve Yan (P1908326)** for the intention of Assignment 1 in COMP 311 Multimedia Application Development. This instruction contains the Guideline for playing the game.

## Characters

The game is themed on dungeon adventure. Player (act as the King![king](/Users/ex10si0n/Desktop/Roguelike/assets/king.png)) can break the wooden wall, beat the enimies (![elf](/Users/ex10si0n/Desktop/Roguelike/assets/elf.png), ![goblin](/Users/ex10si0n/Desktop/Roguelike/assets/ghost.png), ![goblin](/Users/ex10si0n/Desktop/Roguelike/assets/goblin.png)) and the boss![boss](/Users/ex10si0n/Desktop/Roguelike/assets/boss.png) as well as gain some enhancement from the chests ![chest](/Users/ex10si0n/Desktop/Roguelike/assets/chest.png)or the merchants![merchant](/Users/ex10si0n/Desktop/Roguelike/assets/merchant.png).

## Player Properties

There are three dimension of player properties. Respectively, **HP**, **ATK**, **AXE**.

### HP (Health Point)

Player's initial **HP** is 20, during the battle (When you pass through the enemies) Player's HP will deduct by the **ATK** of that enemy. In addition, the **HP** of that enemy will also deduct by Player's **ATK**.

### ATK (Attack)

Player's initial **ATK** is 4, calculation method has been explained in **HP Section**.

### AXE (Number of axe for breaking wooden walls)

Player's initial **AXE** is 5, the **AXE** will deduct by 1 when Player walk through the wooden wall. If the **AXE** is 0, the Player cannot access the wooden wall.

## Merchant

In this game, Merchant is a key NPC that is game changing. The Player should have a wisely decision in store interface in order to be alive for more levels.

## Difficulty

The difficulty of level is gradually increase, which means that the **ATK** and **HP** of enemies will be increase (quantatively by plus (2, 2)). The price of each components in the store is fixed. But the coins that enemy given will not be increase.

