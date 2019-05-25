"""Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

--------------------------missionPlanner.py--------------------------
This module contains methods for basic mission planning algorithms
for the game Leaving Earth (by the Lumenaris Group) and the expansion 
packs: Outer Planets and Stations.
This module can be run on its own for basic mission planning or as
called by leavingEarth.py for higher level simulation.  
"""
import math

def main():
  """assumes module is called in isolation
  this function can serve as a scratchpad"""
  import gameboards
  theRules = gameboards.gameboard()
  myboard = theRules.getBoard()
  earthPaths = shortestPaths(myboard,'Earth')
  mercuryPaths = shortestPaths(myboard, 'Mercury')
  outbound = getMissionSegment('Earth','Mercury',myboard,earthPaths)
  inbound = getMissionSegment('Mercury','Earth',myboard,mercuryPaths)
  fullMission = outbound+inbound
  print(fullMission)

def shortestPaths(gameboard, origin):
  """implementation of dijsktra's algorithm for shortest path from origin"""
  #initialize solution structure
  #solution == key: (distance from origin, predecessor node)
  pathSolution = {}
  for node in gameboard:
    pathSolution[node] = [math.inf,'']
  pathSolution[origin] = [0,origin]
  
  unvisitedNodes = set(gameboard.keys())
  
  while unvisitedNodes:
    #visit unvisited node with smallest known distance from origin
    current_node = next(iter(unvisitedNodes))
    for node in unvisitedNodes:
      if pathSolution[node][0]<pathSolution[current_node][0]:
        current_node = node
    #for each unvisited neighbor of current node, calculate distance
    #replace known value if smaller
    for neighbor in set(gameboard[current_node].keys()):
      if neighbor in unvisitedNodes:
        #ignore automatic maneuvers (-1 cost maneuvers)
        if gameboard[current_node][neighbor][0]>-1:
          tempDistance = pathSolution[current_node][0]+gameboard[current_node][neighbor][0]
          if tempDistance < pathSolution[neighbor][0]:
            pathSolution[neighbor][0] = tempDistance
            pathSolution[neighbor][1] = current_node
    #remove current node from unvisited nodes
    unvisitedNodes.remove(current_node)
  
  return pathSolution

def getMissionSegment(origin, destination, gameboard, pathSolution):
  """collect path, collect costs, zip path and costs together
  for tuple pair (node, cost), cost to reach paired location
  returned cost pairs will not include the origin, so mission segments
  can be threaded together"""
  
  path = [origin]
  cost_pairs = []
  current_node = destination
  while pathSolution[current_node][1] != current_node:
    path.insert(1,current_node)
    current_node = pathSolution[current_node][1]
  for previous_node, current_node in zip(path, path[1:]):
    cost_pairs.append((current_node,gameboard[previous_node][current_node]))
  return cost_pairs

def planMission():
  pass

def printMission():
  pass

def manageRisk():
  pass

def planProgram():
  pass

def printProgram():
  pass

if __name__ == "__main__":
    main()