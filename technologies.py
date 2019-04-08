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

Class Hierarchy and Attributes:
|Item
|*cost
|+Payload
||*mass
||*capabilities
||*restrictions
||+Astronaut
|||*skill
|||*name
|||*status
||+RockSample
|||*origin
||+Supplies
||+Craft
|||*capacity
|||*status
|||*hazardousManeuvers
|||+Probe
|||+Eagle
|||+Vostok
|||+Apollo
|||+Aldrin
|+Advancement
||*riskCards
||*capability
||+Surveying
||+Rendezvous
||+LifeSupport
||+ReEntry
||+Landing
"""
from abc import ABC, abstractmethod
from random import choice, sample

class item(ABC):
  """parent class for all technology"""
  def __init__(self):
    super().__init__()
    self._cost = 0
  
  def getCost(self):
    return self._cost

class payload(item):
  """parent class for all payload components:
  samples, supplies, probes, capsules
  Capabilities represent the Advanced maneuvers the payload can participate in,
  by definition the payload cannot participate in maneuvers not listed.
  Restrictions represent pre-requisites for purchasing"""
  
  def __init__(self):
    super().__init__()
    self._mass = 0
    self._capabilities = []
    self._restrictions = []

  def getMass(self):
    return self._mass

  def getCapabilities(self):
    return self._capabilities
  
  def getRestrictions(self):
    return self._restrictions

class astronaut(payload):
  """defining class for all atronauts.
  astronaut skills: medic, pilot,
  all astronauts have zero mass (stated for clarity)
  status options: healthy, incapacitated, dead"""
  
  _names = {'medic' : ['Mike Collins','Valentina Tereshkova','Valery Bykovsky',
                       'Gherman Titov', 'Boris Yegorov'],
            'pilot' : ['Neil Armstrong','Joseph Walker','Alan Shepard',
                       'John Glenn','Yuri Gagarin'],
            'mechanic' : ['Jim Lovell','Vladimir Komarov','Gus Grissom',
                          'Buzz Aldrin','Konstantin Feoktistov']}

  def __init__(self, skill, name = ''):
    super().__init__()
    self._cost = 5
    self._skill = skill
    self._status = 'healthy'
    if name is not '':
      self._name = name
    else:
      self._name = choice(astronaut._names[skill])
  
  def getSkill(self):
    return self._skill
  
  def getName(self):
    return self._name

  def assignName(self, name = ''):
    if name is not '':
      self._name = name
    else:
      self._name = choice(astronaut._names[self._skill])
    return self._name
  
  def getStatus(self):
    return self._status

  def injure(self):
    self._status = 'incapacitated'

  def kill(self):
    self._status = 'dead'

  def heal(self, crewSkills = [], location = 'away'):
    if self._status == 'healthy':
      print(self._name + " is healthy")
    elif self._status == 'incapacitated':
      if 'medic' in crewSkills:
        self._status = 'healthy'
        print(self._name + " is now healthy")
      elif location == 'Earth':
        self._status = 'healthy'
        print(self._name + " is now healthy")
      else:
        print(self._name + " cannot be healed")
    else:
      print(self._name + " is dead and cannot be healed")

class advancement(item):
  """parent class for all advancements"""

  """risk outcome deck has:
      60 success cards, $10 to remove
      15 minor failure cards, $5 to remove
      15 major failure cards, $5 to remove"""
  _riskDeck = ['success']*60+['minor failure']*15+['major failure']*15

  def __init__(self):
    super().__init__()
    self._cost = 10
    self.initializeRisk()

  def initializeRisk(self):
    self.riskCards = sample(advancement._riskDeck,3)
  
  def getRisk(self):
    if len(self.riskCards):
      return choice(self.riskCards)
    else:
      return 'success'
  
  def buyDownRisk(self, riskOutcome):
    self.riskCards.remove(riskOutcome)

  @staticmethod
  @abstractmethod
  def getCapability():
    pass
  
  @staticmethod
  @abstractmethod
  def getOutcome(riskOutcome, crewSkills = []):
    pass

class surveying(advancement):
  @staticmethod
  def getCapability():
    return 'surveying'
  
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Surveying Success"
    else:
      return "Surveying Fails"

class rendezvous(advancement):
  @staticmethod
  def getCapability():
    return 'rendezvous'
  
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
      if riskOutcome == 'success':
        return "Docking/Separating Successful"
      elif riskOutcome == 'minor failure' and 'pilot' in crewSkills:
        return "Docking/Separating Successful"
      else:
        return "No Docking/Separating, damage chosen comp."

class lifeSupport(advancement):
  @staticmethod
  def getCapability():
    return 'life support'
  
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Occupants Survive"
    elif riskOutcome == 'minor failure' and 'mechanic' in crewSkills:
        return "Occupants survive"
    else:
      return "Occupants die"

class reEntry(advancement):
  @staticmethod
  def getCapability():
    return 're-entry'
  
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Atmospheric Re-Entry Successful"
    elif riskOutcome == 'minor failure':
      return "Capsule is damaged, occupants survive"
    elif riskOutcome == 'major failure':
      return "Capsule is destroyed, occupants die"

class landing(advancement):
  @staticmethod
  def getCapability():
    return 'landing'
  
  @staticmethod
  def getOutcome(riskOutcome, crewSkills = []):
    if riskOutcome == 'success':
      return "Landing Successful"
    elif riskOutcome == 'minor failure' and 'pilot' in crewSkills:
      return "Landing Successful"
    elif riskOutcome == 'minor failure':
      return "Rough landing, damage chosen comp."
    elif riskOutcome == 'major failure' and 'pilot' in crewSkills:
      return "Rough landing, damage chosen comp."
    elif riskOutcome == 'major failure':
      return "Impact with surface, spacecraft destroyed"

class rockSample(payload):
  def __init__(self, origin):
    super().__init__()
    self._origin = origin
    self._mass = 0
    self._restrictions = []

  def getOrigin(self):
    return self._origin

class supplies(payload):
  def __init__(self, quantity=1):
    super().__init__()
    self._cost = quantity
    self._mass = quantity
    self._restrictions = ['life support']

class craft(payload):
  """craft can be either operational, damaged, or destroyed
  craft can be repaired, by default if on earth
  hazardous maneuvers are maneuvers that can damage the craft"""

  def __init__(self):
    super().__init__()
    self._capacity = 0
    self._status = 'operational'
    self._capabilities = set([])
    self._restrictions = set([])
    self._hazardousManeuvers = set([])

  def getCapacity(self):
    return self._capacity

  def getHazMan(self):
    return self._hazardousManeuvers
  
  def getStatus(self):
    return self._status

  def damage(self):
    self._status = 'damaged'
    print("craft damaged")

  def destroy(self):
    self._status = 'destroyed'
    print("craft destroyed")

  def attemptManeuver(self, maneuver, advancements, crewSkills = []):
    """technologies is an dict of advancement instances where the advancement
    name is the key of the dict"""
    if maneuver in self._hazardousManeuvers:
      self.destroy()
    elif self._restrictions.union([maneuver]) <= set(advancements.keys()):
      if maneuver in self._capabilities:
        if self._status == 'operational':
          result =  advancements[maneuver].getRisk()
        else:
          print("spacecraft is not operational")
          result = 'major failure'
        outcome = advancements[maneuver].getOutcome(result, crewSkills)
        if 'damage' in outcome:
          self.damage()
        return outcome
      else:
        print("craft cannot perform that maneuver")
    else:
      print("the advancement for this maneuver has not been researched")

  def repair(self, crewSkills = [], location = 'away'):
    if self._status == 'operational':
      print("craft is operational")
    elif self._status == 'damaged':
      if 'mechanic' in crewSkills:
        self._status = 'operational'
        print("craft repaired")
      elif location == 'Earth':
        self._status = 'operational'
        print("craft repaired")
      else:
        print("craft cannot be repaired")
    else:
      print("craft cannot be repaired")

class probe(craft):
  def __init__(self):
    super().__init__()
    self._capacity = 0
    self._cost = 2
    self._mass = 1
    self._capabilities = set(['surveying','rendezvous','radiation'])
    self._restrictions = set([])
    self._hazardousManeuvers = set(['re-entry', 'landing'])

class eagle(craft):
  def __init__(self):
    super().__init__()
    self._capacity = 2
    self._mass = 1
    self._cost = 4
    self._capabilities = ['surveying','rendezvous','landing','life support']
    self._restrictions = ['landing']
    self._hazardousManeuvers = ['re-entry','radiation']

class vostok(craft):
  def __init__(self):
    super().__init__()
    self._capacity = 1
    self._mass = 2
    self._cost = 2
    self._capabilities = ['surveying','rendezvous','life support','re-entry']
    self._restrictions = ['re-entry']
    self._hazardousManeuvers = ['landing','radiation']

class apollo(craft):
  def __init__(self):
    super().__init__()
    self._capacity = 3
    self._mass = 3
    self._cost = 4
    self._capabilities = ['surveying','rendezvous','life support','re-entry']
    self._restrictions = ['re-entry']
    self._hazardousManeuvers = ['landing','radiation']

class aldrin(craft):
  def __init__(self):
    super().__init__()
    self._capacity = 8
    self._mass = 3
    self._cost = 4
    self._capabilities = ['surveying','rendezvous','life support','radiation']
    self._restrictions = ['life support']
    self._hazardousManeuvers = ['re-entry','landing']