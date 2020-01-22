import urllib, urllib.request
from bs4 import BeautifulSoup
from collections import deque
from queue import PriorityQueue

startNode = "https://www.cs.iastate.edu/"
goalNode = "https://www.policy.iastate.edu/electronicprivacy"
nodesVisited = 0
openQueue = deque()
closedQueue = []        # To keep track of visited nodes
targetPath = {}         
openQueue.append(startNode)
targetPath[startNode] = startNode

print("########*******Results for BFS*******########")
while 1:
    activeNode = openQueue.popleft()
    try:
        if activeNode not in closedQueue:
            nodesVisited += 1
            if activeNode == goalNode:
                print("Number of nodes visited = " + str(nodesVisited))
                print("Length of solution path is: " + str(targetPath[activeNode].count("->")))
                print(targetPath[activeNode])
                break
            else:
                with urllib.request.urlopen(activeNode) as url:
                    linkContents = url.read().decode()
                soup = BeautifulSoup(linkContents, "html.parser")
                for anchor in soup.find_all("a"):
                    currentLink = anchor.get("href")
                    try:
                        if not currentLink.find("https") == -1 and not currentLink.find("iastate.edu") == -1:
                            openQueue.append(currentLink)
                        if not currentLink in targetPath.keys():
                            targetPath[currentLink] = targetPath[activeNode] + " -> " + currentLink
                    except:
                        pass
        closedQueue.append(activeNode)
    except:
        pass

print("########*******Results for DFS*******########")
while 1:
    activeNode = openQueue.popleft()
    try:
        if activeNode not in closedQueue:
            nodesVisited += 1
            if activeNode == goalNode:
                print("Number of nodes visited = " + str(nodesVisited))
                print("Length of solution path is: " + str(targetPath[activeNode].count("->")))
                print(targetPath[activeNode])
                break
            else:
                with urllib.request.urlopen(activeNode) as url:
                    linkContents = url.read().decode()
                soup = BeautifulSoup(linkContents, "html.parser")
                for anchor in reversed(soup.find_all("a")):
                    currentLink = anchor.get("href")
                    try:
                        if not currentLink.find("https") == -1 and not currentLink.find("iastate.edu") == -1:
                            openQueue.appendleft(currentLink)
                        if not currentLink in targetPath.keys():
                            targetPath[currentLink] = targetPath[activeNode] + " -> " + currentLink
                    except:
                        pass
        closedQueue.append(activeNode)
    except:
        pass

print("########*******Results for BEST*******########")
pq = PriorityQueue()
while 1:
    activeNode = openQueue.popleft()
    try:
        if activeNode not in closedQueue:
            nodesVisited += 1
            if activeNode == goalNode:
                print("Number of nodes visited = " + str(nodesVisited))
                print("Length of solution path is: " + str(targetPath[activeNode].count("->")))
                print(targetPath[activeNode])
                break
            else:
                with urllib.request.urlopen(activeNode) as url:
                    linkContents = url.read().decode()
                soup = BeautifulSoup(linkContents, "html.parser")
                for anchor in soup.find_all("a"):
                    childLink = anchor.get("href")
                    if not childLink in targetPath.keys():
                        targetPath[childLink] = targetPath[activeNode] + " -> " + childLink
                    with urllib.request.urlopen(childLink):
                        childContents = url.read().decode()
                    heuristicOne = childContents.lower().count("PRIVACY")
                    heuristicTwo = childContents.lower().count("POLICY")
                    heuristic = heuristicOne * 5 + heuristicTwo * 5
                    pq.put([heuristic, childLink])
                while not pq.empty():
                    elem = pq.get()[1]
                    if elem not in closedQueue and elem not in openQueue:
                        openQueue.appendleft(elem)
        closedQueue.append(activeNode)
    except:
        pass

print("########*******Results for BEAM with width 10*******########")
pq = PriorityQueue()
while 1:
    activeNode = openQueue.popleft()
    try:
        if activeNode not in closedQueue:
            nodesVisited += 1
            if activeNode == goalNode:
                print("Number of nodes visited = " + str(nodesVisited))
                print("Length of solution path is: " + str(targetPath[activeNode].count("->")))
                print(targetPath[activeNode])
                break
            else:
                with urllib.request.urlopen(activeNode) as url:
                    linkContents = url.read().decode()
                soup = BeautifulSoup(linkContents, "html.parser")
                for anchor in soup.find_all("a"):
                    childLink = anchor.get("href")
                    if not childLink in targetPath.keys():
                        targetPath[childLink] = targetPath[activeNode] + " -> " + childLink
                    with urllib.request.urlopen(childLink):
                        childContents = url.read().decode()
                    heuristicOne = childContents.lower().count("PRIVACY")
                    heuristicTwo = childContents.lower().count("POLICY")
                    heuristic = heuristicOne * 5 + heuristicTwo * 5
                    pq.put([heuristic, childLink])
                while not pq.empty() and len(openQueue) < 10:
                    elem = pq.get()[1]
                    if elem not in closedQueue and elem not in openQueue:
                        openQueue.appendleft(elem)
        closedQueue.append(activeNode)
    except:
        pass