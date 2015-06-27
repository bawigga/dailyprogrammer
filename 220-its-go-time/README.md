# It's Go Time

---
[[2015-06-24] Challenge #220 [Intermediate] It's Go time!](https://www.reddit.com/r/dailyprogrammer/comments/3axjac/20150624_challenge_220_intermediate_its_go_time/)

## Requirements

### Input Description

You will be given the size of the grid as a width and a height. Next, you will be given the player's colour - either b or w. Finally, you will be given a grid of the appropriate dimensions, using the format I used in the Description: spaces for empty grid regions, and b and w for stones of either colour.

### Output Description

Output the co-ordinate of the location which, if you were to place a stone of your own colour there, would result in the greatest number of your opponent's stones being removed. The top-left corner is location (0, 0).


#### Example 1
```
7 5
b      
 bbbbb 
bbwwwwb
bww wb 
 bwwwwb
  bbbbb
```

```
(3, 2)
```

#### Example 2

```
9 11
w
    ww   
  wwbbbw 
  wbbbbw 
 wwbbbbw 
 wwwwwww 
 wbbbbww 
 wbwbbww 
 wbwbbww 
 wwwbbww 
    wbw  
    w    
```

```
(5, 10)
```

#### Example 3

```
7 7
w
w w w w
 bbbbb 
wbbbbbw
 bbbbb 
wbbbbbw
 bbbbb 
w w w w
```

```
No constructive move
```

#### Example 4

```
4 3
b
 bw 
bw w
 bw 
```

```
(2, 1)
```

#### Example 5

```
7 5
b
 bb bb 
bww wwb
 bbbbb 
bwwwb  
 bb    
```

```
(3, 1)
```