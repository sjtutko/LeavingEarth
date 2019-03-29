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

--------------------------technologies.py----------------------------
This module represents the technologies and vehicles of Leaving Earth 
(by the Lumenaris Group) and the expansion packs: Outer Planets 
and Stations.

This module is not intended as a stand-alone module and has no main()
This module contains several classes, which record the attributes of
each technology or vehicle in the game.
"""
from abc import ABC, abstractmethod
from random import choice, sample

class researchedTech(ABC):
  """parent class for all technology"""

  """risk outcome deck has:
      60 success cards, $10 to remove
      15 minor failure cards, $5 to remove
      15 major failure cards, $5 to remove"""
  _riskDeck = ['success']*60+['minor failure']*15+['major failure']*15

  def __init__(self):
    self._cost = 10
    self.initializeRisk
    super().__init__()

  def initializeRisk(self):
    self.riskCards = sample(researchedTech._riskDeck,3)
  
  def getRisk(self):
    return choice(self.riskCards)

  @staticmethod
  @abstractmethod
  def getOutcome(riskOutcome):
    pass