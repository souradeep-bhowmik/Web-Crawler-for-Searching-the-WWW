# Web Crawler for Searching the WWW
__Date of Project:__ November 2019

This project was developed to help me understand searching algorithms in greater depth and also I've tried to relate it with the real-world by using this to navigate a live (Iowa State University Computer Science) website while using the default page as the start node and then navigating to a goal node (privacy policy webpage). For the Best First Search and Beam search algorithms the heuristic used is a concatenation of number of "PRIVACY" words times 5 and number of "POLICY" words times 5 in a webpage. The heuristic is simplistic, but can be refined further to incorporate very accurate and faster search results.

__BFS:__ Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

Wiki source and more information: https://en.wikipedia.org/wiki/Breadth-first_search

__DFS:__ Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

Wiki source and more information: https://en.wikipedia.org/wiki/Depth-first_search

__Best First Search:__ Best-first search is a search algorithm which explores a graph by expanding the most promising node chosen according to a specified rule.

Wiki source and more information: https://en.wikipedia.org/wiki/Depth-first_search

__Beam Search:__ In computer science, beam search is a heuristic search algorithm that explores a graph by expanding the most promising node in a limited set. Beam search is an optimization of best-first search that reduces its memory requirements.

Wiki source and more information: https://en.wikipedia.org/wiki/Beam_search

# Instructions for environment setup:
* Install __Python 3.x.x__ using [Python downloads page](https://www.python.org/downloads/) and selecting your operating system and latest stable release
* Install __BeautifulSoup4__ in Python using `[sudo] pip install beautifulsoup4`

# Execution instructions:
* `python Searching_In_WWW.py`
