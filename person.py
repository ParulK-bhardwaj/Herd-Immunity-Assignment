import random
from virus import Virus

class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        # random.random() generates a random number between 0.0 to 1.0
            random_infection_rate = random.random()
            if self.infection != None:
                if random_infection_rate < self.infection.mortality_rate:
                    self.is_alive = False
                else:
                    self.is_alive = True
                    self.is_vaccinated = True
                    self.infection = None
                return self.is_alive

if __name__ == "__main__":
    # Person class test
    #if condition returns False, AssertionError is raised, else it will not raise any issues.
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Unvaccinated person attributes test
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Infected person attrubtes test
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus
   

    # Check the survival of an infected person. Since the chance
    # of survival is random we need to check a group of people. 
    # Create a list to hold 100 people.
    people = []
    for i in range(1, 101):
        virus_infected_person = Person(i, False, virus)
        people.append(virus_infected_person)
    #  Resolve whether the Person survives the infection or not by looping over the people list. 
    for person in people:
        survived = person.did_survive_infection()

    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people should succumb. 
    did_survive = 0
    did_not_survive = 0
    for person in people:
        if person.is_alive:
            did_survive += 1
        else:
            did_not_survive += 1
    print(f"No. of people survived: {did_survive}")
    print(f"No. of people that did not survive: {did_not_survive}")
    print(f"Mortality Rate: {virus.mortality_rate}; % Of People Succumbed: {did_not_survive/100 * 100}%")
  

    # Stretch challenge! 
    uninfected_people = []
    for i in range(1, 101):
        person = Person(i, False)
        uninfected_people.append(person)
    
    uninfected_people_number = 100
    infected_people_number = 0
    for person in uninfected_people:
        random_infection_rate = random.random()
        if random_infection_rate < virus.repro_rate:
            person.infection = virus
            infected_people_number += 1
    print(f"Infected People that were uninfected initially: {infected_people_number}")
    print(f"Uninfected People now: {uninfected_people_number - infected_people_number}")
            

    """ Check the infection rate of the virus by making a group of 
    unifected people. Loop over all of your people. 
    Generate a random number. If that number is less than the 
    infection rate of the virus that person is now infected. 
    Assign the virus to that person's infection attribute. 

    Now count the infected and uninfect people from this group of people. 
    The number of infectedf people should be roughly the same as the 
    infection rate of the virus.
    """