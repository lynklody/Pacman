# Pacman
An Automated Search Project for CS 205 AI

Code Template Source:
http://ai.berkeley.edu/project_overview.html

Zhenyu Yang: 862187998
Hui Su 862187726


Finding a Fixed Food Dot using Depth First Search

Does Pacman actually go to all the explored squares on his way to the goal?
No, according to the method DFS, we can find the Pacman will choose the left path first. And if it gets the goal in the search process of the left part, then it will stop the process. Therefore, it won’t explore the squares which only show in the right part of search path. 

