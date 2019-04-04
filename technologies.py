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

class item(ABC):
  """parent class for all technology"""
  def __init__(self):
    self._cost = 0
    super().__init__()
  
  def getCost(self):
    return self._cost

class astronaut(item):
  """defining class for all atronauts.
  astronaut skills: medic, pilot,
  all astronauts have zero mass (stated for clarity)"""
  
  _names = {'medic' : ['Mike Collins','Valentina Tereshkova','Valery Bykovsky',
                       'Gherman Titov', 'Boris Yegorov'],
            'pilot' : ['Neil Armstrong','Joseph Walker','Alan Shepard',
                       'John Glenn','Yuri Gagarin'],
            'mechanic' : ['Jim Lovell','Vladimir Komarov','Gus Grissom',
                          'Buzz Aldrin','Konstantin Feoktistov']}

  def __init__(self, skill, name = ''):
    self._cost = 5
    self._skill = skill
    if name is not '':
      self._name = name
    else:
      self._name = choice(astronaut._names[skill])
    super().__init__()
  
  def getSkill(self):
    return self._skill
  
  def getName(self):
    return self._name
  
  def getMass(self):
    return 0

class advancement(item):
  """parent class for all advancements"""

  """risk outcome deck has:
      60 success cards, $10 to remove
      15 minor failure cards, $5 to remove
      15 major failure cards, $5 to remove"""
  _riskDeck = ['success']*60+['minor failure']*15+['major failure']*15

  def __init__(self):
    self._cost = 10
    self.initializeRisk()
    super().__init__()

  def initializeRisk(self):
    self.riskCards = sample(advancement._riskDeck,3)
  
  def getRisk(self):
    return choice(self.riskCards)

  @staticmethod
  @abstractmethod
  def getOutcome(riskOutcome, crewSkills = []):
    pass

class surveying(advancement):
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Surveying Success"
    else:
      return "Surveying Fails"

class rendezvous(advancement):
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
      if riskOutcome == 'success':
        return "Docking/Separating Successful"
      elif riskOutcome == 'minor failure' and 'pilot' in crewSkills:
        return "Docking/Separating Successful"
      else:
        return "No Docking/Separating, Damage Chosen Comp."

class lifeSupport(advancement):
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Occupants Survive"
    elif riskOutcome == 'minor failure' and 'mechanic' in crewSkills:
        return "Occupants Survive"
    else:
      return "Occupants Die"

class reEntry(advancement):
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Atmospheric Re-Entry Successful"
    elif riskOutcome == 'minor failure':
      return "Capsule is damaged, Occupants Survive"
    elif riskOutcome == 'major failure':
      return "Capsule is destroyed, Occupants Die"

class landing(advancement):
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Landing Successful"
    elif riskOutcome == 'minor failure' and 'pilot' in crewSkills:
      return "Landing Successful"
    elif riskOutcome == 'minor failure':
      return "Rough Landing, Damage Chosen Comp."
    elif riskOutcome == 'major failure' and 'pilot' in crewSkills:
      return "Rough Landing, Damage Chosen Comp."
    elif riskOutcome == 'major failure':
      return "Impact with Surface, Spacecraft Destroyed"

class component(item):
  pass