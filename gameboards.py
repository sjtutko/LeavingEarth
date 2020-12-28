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

--------------------------gameboards.py------------------------------
This module represents the game boards and missions of Leaving Earth
(by the Lumenaris Group) and the two expansion packs: Outer Planets
and Stations.

This module is not intended as a stand-alone module and has no main()
This module contains the Gameboard class, which is initialized with
the maps of each game board.
"""

"""Gameboards are held in a dictionary object.
Keys are nodes, Values are Edges
Edges are tuples of the form (cost, time, [hazards], alternative cost WITHOUT aerobraking or slingshot hazard)
Hazards with '+' at the start of the character string represent "end of year" hazards"""

class gameboard():
  _baselineMap = {'Earth' : {'Sub-orbital Space' : (3,0,[]),
                             'Earth Orbit' : (8,0,[]),
                             'Earth' : (-1, 0, [])},
                  'Sub-orbital Space' : {'Earth' : (-1,0,[]),
                                         'Earth Orbit' : (5,0,[])},
                  'Earth Orbit' : {'Earth' : (0, 0, ['atmosphere']),
                                   'Lunar Fly-by' : (1, 0, []),
                                   'Lunar Orbit' : (3, 0, []),
                                   'Mars Fly-by' : (3, 3, ['solar radiaton']),
                                   'Mars Orbit' : (5, 3, ['solar radiaton']),
                                   'Inner Planetary Transfer' : (3, 1, []),
                                   'Outer Planetary Transfer' : (6, 1,['solar radiaton']),
                                   'Earth Orbit' : (-1, 0, [])},
                  'Lunar Fly-by' : {'Earth Orbit' : (1, 0, []),
                                    'Lunar Orbit' : (2, 0, []),
                                    'Moon' : (4, 0, ['landing']),
                                    'LOST' : (-1, 0, [])},
                  'Lunar Orbit' : {'Earth Orbit' : (3, 0, []),
                                   'Moon' : (2, 0, ['landing']),
                                   'Lunar Orbit' : (-1, 0, [])},
                  'Moon' : {'Lunar Orbit' : (2, 0, []),
                            'Moon' : (-1, 0, [])},
                  'Mars Fly-by' : {'Mars Orbit' : (3, 1, []),
                                   'Mars' : (3, 0, ['re-entry','landing']),
                                   'LOST' : (-1, 0, [])},
                  'Mars Orbit' : {'Earth Orbit' : (5, 3, ['solar radiaton']),
                                  'Mars' : (0, 0, ['re-entry', 'landing']),
                                  'Phobos' : (1, 0, ['landing']),
                                  'Inner Planetary Transfer' : (4, 2, ['solar radiaton']),
                                  'Outer Planetary Transfer' : (5, 1, ['solar radiaton']),
                                  'Mars Orbit' : (-1, 0, [])},
                  'Mars' : {'Mars Orbit' : (3, 0, []),
                            'Mars' : (-1, 0, [])},
                  'Phobos' : {'Mars Orbit' : (1, 0, []),
                              'Phobos' : (-1, 0, [])},
                  'Ceres' : {'Inner Planetary Transfer' : (5, 2, ['solar radiaton']),
                             'Outer Planetary Transfer' : (3, 1, ['solar radiaton']),
                             'Ceres' : (-1, 0, [])},
                  'Venus Fly-by' : {'Venus Orbit' : (1, 0, []),
                                    'Venus' : (1, 0, ['re-entry']),
                                    'LOST' : (-1, 0, [])},
                  'Venus Orbit' : {'Venus' : (0, 0, ['re-entry']),
                                   'Inner Planetary Transfer' : (3, 1, ['solar radiaton']),
                                   'Outer Planetary Transfer' : (9, 1, ['solar radiaton']),
                                   'Venus Orbit' : (-1, 0, ['solar radiaton'])},
                  'Venus' : {'Venus Orbit' : (6, 0, []),
                             'Venus' : (-1, 0, [])},
                  'Mercury Fly-by' : {'Mercury Orbit' : (2, 0, []),
                                      'Mercury' : (4, 0, ['landing']),
                                      'LOST' : (-1, 0, [])},
                  'Mercury Orbit' : {'Mercury' : (2, 0, ['landing']),
                                     'Inner Planetary Transfer' : (7, 1, ['solar radiaton']),
                                     'Mercury Orbit' : (-1, 0, [])},
                  'Mercury' : {'Mercury Orbit' : (2, 0, []),
                                'Mercury' : (-1, 0, [])},
                  'Inner Planetary Transfer' : {'Earth Orbit' : (3, 1, []),
                                                'Mars Orbit' : (4, 2, ['solar radiaton']),
                                                'Ceres' : (5, 1, ['solar radiaton', 'landing']),
                                                'Venus Orbit' : (3, 1, ['solar radiaton']),
                                                'Venus Fly-by' : (2, 1, ['solar radiaton']),
                                                'Mercury Fly-by' : (5, 1, ['solar radiaton']),
                                                'LOST' : (-1, 0, [])},
                  'LOST' : {'LOST' : (-1, 0, [])}}
  _outerPlanetsMap = {'Venus Fly-by' : {'Venus Orbit' : (0, 0, ['aerobraking'], 1),
                                        'Venus' : (1, 0, ['re-entry']),
                                        'Jupiter Fly-by' : (1, 1, ['solar radiaton','slingshot'], 10000),
                                        'LOST' : (-1, 0, [])},
                      'Mars Fly-by' : {'Mars Orbit' : (1, 1, ['aerobraking'], 3),
                                       'Mars' : (3, 0, ['re-entry','landing']),
                                       'Jupiter Fly-by' : (1, 3, ['solar radiaton','slingshot'], 10000),
                                       'LOST' : (-1, 0, [])},
                      'Outer Planetary Transfer' : {'Earth Orbit' : (1, 1, ['solar radiaton', 'aerobraking'], 6),
                                                    'Mars Orbit' : (2, 1, ['solar radiaton','aerobraking'], 5),
                                                    'Ceres' : (3, 1, ['solar radiaton','landing']),
                                                    'Jupiter Fly-by' : (4, 2, ['solar radiaton','slingshot'], 10000),
                                                    'Saturn Fly-by' : (3, 3, ['solar radiaton','slingshot'], 10000),
                                                    'Uranus Fly-by' : (4, 9, ['solar radiaton','slingshot'], 10000),
                                                    'LOST' : (-1, 0, [])},
                      'Jupiter Fly-by' : {'Jupiter Orbit' : (3, 0, ['jupiter','aerobraking'], 10),
                                          'Saturn Fly-by' : (0, 3, ['jupiter','solar radiaton','slingshot'], 10000),
                                          'Outer Planetary Transfer' : (4, 2, ['solar radiaton']),
                                          'LOST' : (-1, 0, ['jupiter'])},
                      'Jupiter Orbit' : {'Jupiter Fly-by' : (10, 1, ['jupiter','solar radiaton']),
                                         'Io' : (2, 0, ['jupiter','landing']),
                                         'Europa' : (2, 0, ['jupiter','landing']),
                                         'Callisto' : (5, 0, ['landing']),
                                         'Ganymede Orbit' : (3, 0, ['jupiter',]),
                                         'Jupiter Orbit' : (-1, 0, ['+jupiter'])},
                      'Ganymede Orbit' : {'Jupiter Orbit' : (3, 0, []),
                                          'Ganymede' : (2, 0, ['landing']),
                                          'Ganymede Orbit' : (-1, 0, [])},
                      'Ganymede' : {'Ganymede Orbit' : (2, 0, []),
                                    'Ganymede' : (-1, 0, [])},
                      'Io' : {'Jupiter Orbit' : (2, 0, []),
                              'Io' : (-1, 0, ['+jupiter'])},
                      'Europa' : {'Jupiter Orbit' : (2, 0, []),
                                  'Europa' : (-1, 0, ['+jupiter'])},
                      'Callisto' : {'Jupiter Orbit' : (5, 0, []),
                                    'Jupiter Fly-by' : (5, 0, ['jupiter']),
                                    'Callisto' : (-1, 0, [])},
                      'Saturn Fly-by' : {'Saturn Orbit' : (1, 0, ['saturn', 'aerobraking'], 7),
                                         'Uranus Fly-by' : (0, 5, ['solar radiation', 'slingshot'], 10000),
                                         'Outer Planetary Transfer' : (3, 3, ['solar radiation']),
                                         'LOST' : (-1, 0, ['saturn'])},
                      '' : {},
                      '' : {},
                      '' : {},
                      '' : {},
                      '' : {},
                      '' : {},
                      '' : {},
                      '' : {},
                      '' : {},}
  
  def __init__(self, expansion = "Leaving Earth"):
    self.board = gameboard._baselineMap
    if expansion == "Outer Planets":
      self.board.update(_outerPlanetsMap)

  def getBoard(self):
    return self.board