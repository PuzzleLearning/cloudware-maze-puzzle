cloudware-maze-puzzle
=====================

#### Introduction

Puzzle from the www.cloudware.pl company

#### What's the story?

I found a maze on the GoldenLine Cloudware profile. I am not sure if it's some old puzzle, or a hidden recruitation, but I'm sharing with you the solution written in Python (compatible with `2.7` as well as `3+`). It requires the `Pillow` graphics library, and you needed to convert the image first. I uploaded ready `.png` files.

![Maze which was solved](https://raw.githubusercontent.com/PuzzleLearning/cloudware-maze-puzzle/master/file_from_cloudware.jpg "Maze to be solved - free Cloudwarek!")

#### Solution

It's possbile to use the *Breadth-first search* algorithm to traverse the graph of possible paths.

![Result](https://raw.githubusercontent.com/PuzzleLearning/cloudware-maze-puzzle/master/result.png "Solution")

#### Usage

```
invoke: python make_me_free.py input.png result.png
```
