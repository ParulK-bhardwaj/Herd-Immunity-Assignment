import random, sys
# Cool reference to The Hitchhiker's Guide to the Galaxy :)
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
 

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus #virus
        self.pop_size = int(pop_size) #number: Population size
        self.vacc_percentage = vacc_percentage #number: Percent of population that are vaccinated
        self.initial_infected = initial_infected #number: initial number of infected people
        self.population =  self._create_population() #list: using create population method
        self.infected_population = [] #list
        self.new_infected = [] #list
        self.vaccinated_population = [] #list
        self.dead_population = [] #list

        # Set total infected to initial infected at the start before the virus
        self.infected = self.initial_infected #number 
        self.interaction_number = 0 #number
        
        # Created a Logger object and binded it to self.logger.
        self.file_name = f"{virus.name}_pop_{pop_size}_vp_{vacc_percentage}_infected_{initial_infected}.txt"
        self.logger = Logger(self.file_name)
        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)
       
    def _create_population(self):
        """
            A method that is used to create the initial population by categorizing them

            Returns:
                list: A list of people (Person instances) equal to population size.
        """
        population = []
        person_id = 0
        # initially vaccinated population
        total_vaccinated = int( self.pop_size * self.vacc_percentage / 100)
        for vaccinated in range(total_vaccinated):
            vaccinated_person = Person(person_id, True)
            population.append(vaccinated_person)
            person_id += 1
        # infected population
        for infected in range(self.initial_infected):
            infected_person = Person(person_id, False, self.virus)
            population.append(infected_person)
            person_id  += 1
        # at-risk population
        for at_risk in range(self.pop_size - self.initial_infected - total_vaccinated):
            at_risk_person = Person(person_id, True)
            population.append(at_risk_person)
        return population

    def _simulation_should_continue(self):
        """
            A method to define if the simulation should continue. 

            Returns:
                boolean: True if all of the people are dead, or if all of the living people have been vaccinated.
                then simulation should continue else False.
        """
        at_risk_person = None
        infected_person = None
        for person in self.population:
            if person.is_alive and person.is_vaccinated == False:
               at_risk_person == True
            if person.is_alive and person.infection is not None:
                infected_person == True
        return at_risk_person and infected_person  

    def run(self):
        """
           This method starts the simulation. It tracks the number of 
           steps the simulation has run and checks if the simulation should 
           continue at the end of each step.
        """

        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step()
            print(time_step_counter)
            self.logger.log_interactions(time_step_counter, self.interaction_number, len(self.new_infected))
            self.logger.log_infection_survival(time_step_counter, len(self.population), len(self.dead_population))
            should_continue = self._simulation_should_continue()
        
        self.logger.log_final(time_step_counter, len(self.population), len(self.dead_population), len(self.vaccinated_population), self.interaction_number, len(self.infected_population))


        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        for infected_person in self.infected_population:
            for i in range(100):
                if random_person.is_infected == False and random_person.is_alive:
                    random_person = random.choice(self.population)
                if infected_person.is_alive:
                    self.interaction(infected_person, random_person)
                

    def interaction(self, infected_person, random_person):

        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            self.interaction_number += 1
            if random_person.is_vaccinated:
                random_person.is_alive == True
            # random_person is already infected:
            #     nothing happens to random person.
            elif random_person.is_infected:
                random_person.is_alive == True
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.
            elif random_person.is_infected == False and random_person.is_vaccinated == False:
                random_number = random.random()
                # If that number is smaller than repro_rate, 
                #     add that person to the newly infected array
                #     Simulation object's newly_infected array, so that their infected
                #     attribute can be changed to True at the end of the time step.
                if random_number < self.virus.repro_rate:
                    self.new_infected.append(random_person)

        # TODO: Call logger method during this method.
                

    def _infect_newly_infected(self):
        for person in self.new_infected:
            person.is_infected = True
            self.infected_population.append(person)
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        


if __name__ == "__main__":

    virus_name = "Ebola"
    repro_rate = 0.70
    mortality_rate = 0.25
    virus = Virus(virus_name, repro_rate, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.50
    initial_infected = 10

    simulation = Simulation(virus, 10000, 0.50, 10)

    simulation.run()
