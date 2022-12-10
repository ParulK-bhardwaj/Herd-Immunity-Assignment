import random, sys
# Cool reference to The Hitchhiker's Guide to the Galaxy. This made me read into this :)
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
# To use sys.argv(script name) and to be able to provide the input parameters from command line, we imported sys module.
import sys
 

class Simulation(object):
    """This class is used to run the Herd Immunity Simulation."""
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus #virus
        self.pop_size = int(pop_size) #number: Population size
        self.vacc_percentage = vacc_percentage #number: Percent of population that are vaccinated
        self.initial_infected = initial_infected #number: initial number of infected people
        self.population =  self._create_population() #list: using create population method
        # self.infected_population = [] #list
        self.vaccinated_population = [] #list
        # initially vaccinated population
        self.total_vaccinated = int( self.pop_size * self.vacc_percentage)
        self.vaccinated = 0 #number
        self.dead_population = [] #list
        self.fatalities = 0 #number

        # Set total infected to initial infected at the start before the virus
        self.infected = self.initial_infected #number 
        self.new_infected = [] #list
        self.interaction_number = 0 #number

        # number of times vaccination save someone from potentially becoming infected
        self.saved = 0

        # Created a Logger object and binded it to self.logger.
        self.file_name = f"{virus.name}_pop_{pop_size}_vp_{vacc_percentage}_infected_{initial_infected}.txt"
        self.logger = Logger(self.file_name)
        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate, initial_infected)
       
    def _create_population(self):
        """
            A method that is used to create the initial population by categorizing them

            Returns:
                list: A list of people (Person instances) equal to population size.
        """
        population = []
        person_id = 0
        # initially vaccinated population
        total_vaccinated = int( self.pop_size * self.vacc_percentage)

        # vaccinated population
        for vaccinated in range(total_vaccinated):
            person_id += 1
            vaccinated_person = Person(person_id, True, None)
            population.append(vaccinated_person)

        # infected population
        for infected in range(self.initial_infected):
            person_id  += 1
            infected_person = Person(person_id, False, self.virus)
            population.append(infected_person)
            
        # at-risk population
        for at_risk in range(self.pop_size - self.initial_infected - total_vaccinated):
            person_id  += 1
            at_risk_person = Person(person_id, False, None)
            population.append(at_risk_person)
        return population

    def _simulation_should_continue(self):
        """
            A method to define if the simulation should continue. 

            Returns:
                boolean: True if all of the people are dead, or if all of the living people have been vaccinated.
                then simulation should continue else False.
        """
        for person in self.population:
            if person.is_alive == True and person.is_vaccinated == False and len(self.new_infected) > 0:
                return True
        return False

    def run(self):
        """
           This method starts the simulation. It tracks the number of 
           steps the simulation has run and checks if the simulation should 
           continue at the end of each step.
           It will also write meta data to the logger
        """

        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step()
            self.logger.log_interactions(time_step_counter, self.interaction_number, len(self.new_infected))
            self.logger.log_infection_survival(time_step_counter, len(self.population), self.new_fatalities)
            should_continue = self._simulation_should_continue()
            self._infect_newly_infected()
    
        print(f"The simulation ran for {time_step_counter} times in total.")
        self.logger.log_final(time_step_counter, len(self.population), len(self.dead_population), self.total_vaccinated, self.interaction_number, self.infected, self.saved)

    def time_step(self):
        """This method will simulate interactions between people, calulate 
        new infections, and determine if vaccinations and fatalities from infections
        The goal here is have each infected person interact with a number of other 
        people in the population"""
        self.new_fatalities = 0
        if len(self.population) < 100:
            interact_limit = len(self.population)
        else:
            interact_limit = 100

        for person in self.population:
                if person.infection is not None and person.is_alive == True:
                    """picked random sample over random choice as random sample does not produce repeating elements
                    but random choice can generate repeat elements"""
                    random_sample = random.sample(self.population, interact_limit)
                    for random_person in random_sample:
                        self.interaction(person, random_person)
                    if person.did_survive_infection():
                        person.is_vaccinated = True
                        person.infection = None
                        self.total_vaccinated += 1
                        self.infected -= 1
                    else:
                        person.is_alive = False
                        person.infection = False
                        self.dead_population.append(person)
                        self.population.remove(person)
                        self.new_fatalities += 1
                        self.infected -= 1

    def interaction(self, infected_person, random_person):
        """The cases we cover in this method are:
            random_person is vaccinated:
                nothing happens to random person.
            random_person is already infected:
                nothing happens to random person.
            random_person is healthy, but unvaccinated:
                generate a random number between 0.0 and 1.0.
                If that number is smaller than repro_rate, 
                    add that person to the newly infected array
                    Simulation object's newly_infected array, so that their infected
                    attribute can be changed to True at the end of the time step."""
        self.interaction_number += 1

        if random_person.is_vaccinated == False and random_person.infection == None and (random_person.is_alive and infected_person.is_alive):
            infection_possibility = random.random()
            if infection_possibility < virus.repro_rate and random_person not in self.new_infected:
                    self.new_infected.append(random_person)
                    self.infected += 1
        elif random_person.infection == None or random_person.is_vaccinated and (random_person.is_alive and infected_person.is_alive):
            self.saved += 1
        
    def _infect_newly_infected(self):
        """this method is called at the end of every time step and infect each Person."""
        for person in self.new_infected:
            person.infection = self.virus
            person.is_vaccinated = True
            self.infected += 1
        self.new_infected = []

if __name__ == "__main__":
    #  Reference https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
    """
        As python captured and stored the arguments in a list, we are calling all the indexes from 1
        The first one returns simulation.py in this case.
        
        Return:
            list
    """

    # virus_name = "Ebola"
    # repro_rate = 0.70
    # mortality_rate = 0.25
    # virus = Virus(virus_name, repro_rate, mortality_rate)

    # # Set some values used by the simulation

    # pop_size = 10000
    # vacc_percentage = 0.90
    # initial_infected = 10

    # simulation = Simulation(virus, pop_size, vacc_percentage, initial_infected)


    # simulation.run()

    param= sys.argv[1:]
    pop_size = int(param[0])
    vacc_percentage = float(param[1])
    virus_name = param[2]
    mortality_rate = float(param[3])
    repro_rate= float(param[4])
    initial_infected = int(param[5])

    virus = Virus(virus_name, repro_rate, mortality_rate)

    simulation = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    simulation.run()
