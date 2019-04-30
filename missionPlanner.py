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
  pass

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
    for neighbor in gameboard[current_node]:
      if neighbor[0] in unvisitedNodes:
        #ignore automatic maneuvers (-1 cost maneuvers)
        if neighbor[1]>-1:
          tempDistance = pathSolution[current_node][0]+neighbor[1]
          if tempDistance < pathSolution[neighbor[0]][0]:
            pathSolution[neighbor[0]][0] = tempDistance
            pathSolution[neighbor[0]][1] = current_node
    #remove current node from unvisited nodes
    unvisitedNodes.remove(current_node)
  
  return pathSolution

def getPath(origin, destination, pathSolution):
  path = [origin]
  current_node = destination
  while pathSolution[current_node][1] != current_node:
    path.insert(1,current_node)
    current_node = pathSolution[current_node][1]
  return path

def planMission():
  pass

def manageRisk():
  pass

def planProgram():
  pass

if __name__ == "__main__":
    main()