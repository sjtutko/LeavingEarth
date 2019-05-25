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
Edges are tuples of the form (cost, time, [hazards])"""

class gameboard():
  _baselineMap = {'Earth' : {'Sub-orbital Space' : (3,0,[]),
                             'Earth Orbit' : (8,0,[]),
                             'Earth' : (-1, 0, [])},
                  'Sub-orbital Space' : {'Earth' : (-1,0,[]),
                                         'Earth Orbit' : (5,0,[])},
                  'Earth Orbit' : {'Earth' : (0, 0, ['atmosphere']),
                                   'Lunar Fly-by' : (1, 0, []),
                                   'Lunar Orbit' : (3, 0, []),
                                   'Mars Fly-by' : (3, 3, ['radiation']),
                                   'Mars Orbit' : (5, 3, ['radiation']),
                                   'Inner Planetary Transfer' : (3, 1, []),
                                   'Outer Planetary Transfer' : (6, 1,['radiation']),
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
                  'Mars Orbit' : {'Earth Orbit' : (5, 3, ['radiation']),
                                  'Mars' : (0, 0, ['re-entry', 'landing']),
                                  'Phobos' : (1, 0, ['landing']),
                                  'Inner Planetary Transfer' : (4, 2, ['radiation']),
                                  'Outer Planetary Transfer' : (5, 1, ['radiation']),
                                  'Mars Orbit' : (-1, 0, [])},
                  'Mars' : {'Mars Orbit' : (3, 0, []),
                            'Mars' : (-1, 0, [])},
                  'Phobos' : {'Mars Orbit' : (1, 0, []),
                              'Phobos' : (-1, 0, [])},
                  'Ceres' : {'Inner Planetary Transfer' : (5, 2, ['radiation']),
                             'Outer Planetary Transfer' : (3, 1, ['radiation']),
                             'Ceres' : (-1, 0, [])},
                  'Venus Fly-by' : {'Venus Orbit' : (1, 0, []),
                                    'LOST' : (-1, 0, [])},
                  'Venus Orbit' : {'Venus' : (0, 0, ['re-entry']),
                                   'Inner Planetary Transfer' : (3, 1, ['radiation']),
                                   'Outer Planetary Transfer' : (9, 1, ['radiation']),
                                   'Venus Orbit' : (-1, 0, ['radiation'])},
                  'Venus' : {'Venus Orbit' : (6, 0, []),
                             'Venus' : (-1, 0, [])},
                  'Mercury Fly-by' : {'Mercury Orbit' : (2, 0, []),
                                      'Mercury' : (4, 0, ['landing']),
                                      'LOST' : (-1, 0, [])},
                  'Mercury Orbit' : {'Mercury' : (2, 0, ['landing']),
                                     'Inner Planetary Transfer' : (7, 1, ['radiation']),
                                     'Mercury Orbit' : (-1, 0, [])},
                  'Mercury' : {'Mercury Orbit' : (2, 0, []),
                                'Mercury' : (-1, 0, [])},
                  'Inner Planetary Transfer' : {'Earth Orbit' : (3, 1, []),
                                                'Mars Orbit' : (4, 2, ['radiation']),
                                                'Ceres' : (5, 1, ['radiation', 'landing']),
                                                'Venus Orbit' : (3, 1, ['radiation']),
                                                'Venus Fly-by' : (2, 1, ['radiation']),
                                                'Mercury Fly-by' : (5, 1, ['radiation']),
                                                'LOST' : (-1, 0, [])},
                  'LOST' : {'LOST' : (-1, 0, [])}}
  def __init__(self, expansion = 'Leaving Earth'):
    self.board = gameboard._baselineMap

  def getBoard(self):
    return self.board