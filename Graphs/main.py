from util import *
from queue import PriorityQueue


def main():
    """
    'all/admin' = 0, 'accounting/allaccounting' = 1, 'finance/allfinance' = 2, 'tech/alltech' = 3,
    'health/allhealth' = 4, 'marketing/allmarketing' = 5, 'retail/allretail' = 6, 'sales/allsales' = 7
    """
    categories = ('all/admin', 'accounting/allaccounting', 'finance/allfinance', 'tech/alltech','health/allhealth',
                  'marketing/allmarketing', 'retail/allretail', 'sales/allsales')

    for x in range(0, len(categories)):
        item = categories[x]
        if item == 'finance/allfinance':
            print (item)
    """  
    graphList = [[2],[4,5],[0,1,3,4],[2],[1,2],[1]]
    
    def DFSR(graph, u, goal, fringe, visited, path):
      fringe.append((u, visited, path))
      if u == goal:
          return path + [u]
      node = graph[u]
    
      for v in node:
          if v not in visited:
              if v == goal:
                  return path + [v]
    
              DFSR(graph, v, goal, fringe, visited + [v], path + [v])
    
      return path
    
    path = DFSR(graphList, 0, 5, [], [], [])
    
    for p in path:
      print (p)
    
    def DFSI(graph, state, goal):
    
      frontier = Stack()
      seen = []
      seen.append(state)
      visited = []
      node = (state, visited, seen)
      frontier.push(node)
    
      while not frontier.isEmpty():
    
          item = frontier.pop()
          node, visited, seen = item
          if node == goal:
              return path +[node]
    
          seen = seen + [node]
    
          choosenNode = graph[node]
          for n in choosenNode:
              if n not in seen:
                  if n == goal:
                      return path + [n]
    
                  frontier.push(n)
                  seen.append(n)
    
    
    def dfs(graph, start, goal):
      # initialise visited list, path list & fringe
      # Add starting node to the fringe
      visited = []
      path = []
      fringe = PriorityQueue()
      fringe.put((0, start, path, visited))
    
      # While there are still nodes in the fringe, keep exploring!
      while not fringe.empty():
          # 1. Remove the next most prioritised node from the fringe
          depth, current_node, path, visited = fringe.get()
    
          # 2. Check to see if it is the goal node
          if current_node == goal:
              return path + [current_node]
    
          # 3. Add to our list of explored nodes
          visited = visited + [current_node]
    
          # If not goal, get its child nodes
          child_nodes = graph[current_node]
          # 4. Add child nodes to the fringe if they haven't been visited yet
          for node in child_nodes:
              if node not in visited:
                  if node == goal:
                      return path + [node]
                  depth_of_node = len(path)
                  # The priority queue prioritises lower values over higher ones (i.e. 1 is prioritised higher than 10)
                  # Since we are using depth of node as our prioritisation measure we need to pass in negative priorities
                  # To ensure that nodes with greater depth get explored before shallower ones
                  fringe.put((-depth_of_node, node, path + [node], visited + [node]))
    
      return path
    
    
    #path = dfs(graphList, 0, 5)
    
    for p in path:
      print(p)
    
    """


if __name__ == "__main__": main()