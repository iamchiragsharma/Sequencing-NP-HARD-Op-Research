# Sequencing-NP-HARD-Op-Research

## Abstract:

Job Sequencing problems are often tackled on the basis of 1 unit time as per job which is not possible in real life.__Here we present a improved method to optimize the Job Sequencing equivalent or better than Johnson's Method of Job Sequencing with variable job quantity as well as Non Binary Search Tree Conditions of Job Time while efficiently reducing total elapsed time of machines The effectiveness of the sequencing problem can be measured in terms of minimized costs, maximized profits, minimized elapsed time and meeting due dates etc.__

Explanation:


| Machines ↓  Jobs → | J1 | J2 | J3 | J4 | .. | .. | Jn-1 | Jn |
|-------------------|----|----|----|----|----|----|------|----|
| __M1__                | x<sub>11</sub> | x<sub>12</sub> | x<sub>13</sub> | x<sub>14</sub> | ..   | ..   |  x<sub>1n-1</sub>    | x<sub>1n</sub>   |
| __M2__                | x<sub>21</sub> | x<sub>22</sub> | x<sub>23</sub> | x<sub>24</sub> | ..   | ..   |  x<sub>2n-1</sub>    | x<sub>2n</sub>   |
| __M3__                | x<sub>31</sub> | x<sub>22</sub> | x<sub>32</sub> | x<sub>41</sub> | ..   | ..   |  x<sub>3n-1</sub>    | x<sub>2n</sub>   |
| __M4__                | x<sub>41</sub> | x<sub>22</sub> | x<sub>32</sub> | x<sub>41</sub> | ..   | ..   |  x<sub>4n-1</sub>    | x<sub>2n</sub>   |
| ..                |  ..  |    ..| ..   |   .. |   .. |..    |    ..  |  ..  |
| ..                |   .. |   .. |   .. |   .. |  ..  | ..   |  ..    |  ..  |
| __Mn-1__               | x<sub>61</sub> | x<sub>22</sub> | x<sub>32</sub> | x<sub>41</sub> | ..   | ..   |  x<sub>n-1n-1</sub>    | x<sub>2n</sub>   |
| __Mn__                | x<sub>21</sub> | x<sub>22</sub> | x<sub>32</sub> | x<sub>41</sub> | ..   | ..   |  x<sub>nn-1</sub>    | x<sub>nn</sub>   |

![Area](/assets/John_Formula.png)