import random
import csv
import eightpuzzle
def generateStates():
   numbers = list(range(9))
   states = []

   states.clear

   random.seed(5)

   while len(states) < 71:
       random_permutation = tuple(random.sample(numbers, len(numbers)))
       states.append(random_permutation)
  
   with open("scenarios.csv", 'w', newline='') as csvfile:
       writer = csv.writer(csvfile)
       for state in states:
           writer.writerow(state)

def compareHeuristics():
   h1Depth = 0
   h1Nodes = 0
   h1Fringe = 0
   h2Depth = 0
   h2Nodes = 0
   h2Fringe = 0
   h3Depth = 0
   h3Nodes = 0
   h3Fringe = 0
   h4Depth = 0
   h4Nodes = 0
   h4Fringe = 0
   states = []
  
      
   with open('scenarios.csv', mode='r') as file:
       reader = csv.reader(file)
       for row in reader:
           states.append([int(value) for value in row])

   with open("results.csv", 'w', newline='') as csvfile:       
       writer = csv.writer(csvfile)
       writer.writerow(['H1 Depth', ' H1 Nodes', ' H1 Fringe', ' H2 Depth', ' H2 Nodes', ' H2 Fringe', ' H3 Depth', ' H3 Nodes', ' H3 Fringe', ' H4 Depth', ' H4 Nodes', ' H4 Fringe'])

       for state in states:
          
           print(state)
           puzzle = eightpuzzle.EightPuzzleState(state)
           problem = eightpuzzle.EightPuzzleSearchProblem(puzzle=puzzle)
           h1Path, h1Explored, h1Frontier= search.aStarSearch(problem, search.misplacedTilesHeuristic)
           print("h1 done")
           h1Depth += len(h1Path)
           h1Nodes += len(h1Explored)
           h1Fringe += len(h1Frontier.heap)
           print("Depth: "+str(len(h1Path))+", Expanded Node: "+str(len(h1Explored))+", Fringe Size: "+str(len(h1Frontier.heap))+".")
           h2Path, h2Explored, h2Frontier= search.aStarSearch(problem, search.euclideanHeuristic)
           print("h2 done")
           h2Depth += len(h2Path)
           h2Nodes += len(h2Explored)
           h2Fringe += len(h2Frontier.heap)
           print("Depth: "+str(len(h2Path))+", Expanded Node: "+str(len(h2Explored))+", Fringe Size: "+str(len(h2Frontier.heap))+".")
           h3Path, h3Explored, h3Frontier= search.aStarSearch(problem, search.manhattanHeuristic)
           print("h3 done")
           h3Depth += len(h3Path)
           h3Nodes += len(h3Explored)
           h3Fringe += len(h3Frontier.heap)
           print("Depth: "+str(len(h3Path))+", Expanded Node: "+str(len(h3Explored))+", Fringe Size: "+str(len(h3Frontier.heap))+".")
           h4Path, h4Explored, h4Frontier= search.aStarSearch(problem, search.outofplaceHeuristic)
           print("h4 done")
           h4Depth += len(h4Path)
           h4Nodes += len(h4Explored)
           h4Fringe += len(h4Frontier.heap)
           print("Depth: "+str(len(h4Path))+", Expanded Node: "+str(len(h4Explored))+", Fringe Size: "+str(len(h4Frontier.heap))+".")

           writer.writerow([len(h1Path), len(h1Explored), len(h1Frontier.heap),
               len(h2Path), len(h2Explored), len(h2Frontier.heap),
               len(h3Path), len(h3Explored), len(h3Frontier.heap),
               len(h4Path), len(h4Explored), len(h4Frontier.heap)])

          
          
       writer.writerow([])
       writer.writerow(['Averages'])
       writer.writerow([h1Depth/71, h1Nodes/71, h1Fringe/71, h2Depth/71, h2Nodes/71, h2Fringe/71, h3Depth/71, h3Nodes/71, h3Fringe/71, h4Depth/71, h4Nodes/71, h4Fringe/71])


if __name__ == "__main__":
   generateStates()
   compareHeuristics()
