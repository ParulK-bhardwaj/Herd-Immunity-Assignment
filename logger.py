class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        """
            This line of metadata is tab-delimited.
            It creates the text file that stores all logs in.
        """
        
        file = open(self.file_name, "w")
        metadata = (f"Herd Immunity Simulation for {virus_name.title()}\tPopulation Size: {pop_size}\tVaccination Percent: {vacc_percentage}%\tMortality Rate: {mortality_rate}%\tReproduction Rate: {basic_repro_num}%\n")
        file.write(metadata)
        file.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        """
            This method represents all the possible edge cases.
            Using the values passed along with each person, number of new infections and number of interactions.
        """
        file = open(self.file_name, "a")
        interaction_data = f"\nTime Step: {step_number}.\nTotal number of Interactions: {number_of_interactions}.\n Total Number of New Infections: {number_of_new_infections}.\n "
        file.write(interaction_data)
        file.close()
        

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        """
            This method appends results (survivors, number_of_new_fatalities) of the infection to the logfile.
        """ 
        file = open(self.file_name, "a")
        survival_data = f"\nTime Step: {step_number}.\nNumber of Survivors: {population_count}.\nTotal Number of New Fatalities: {number_of_new_fatalities}.\n "
        file.write(survival_data)
        file.close()

    def log_final(self, step_number, population, fatalities, vaccinated, interactions, infections):
        """
            This method appends the final data to the logfile.
        """ 
        file = open(self.file_name, "a")
        final_data = f"\nTime Step: {step_number}.\nTotal Population: {population}.\nTotal Number of Fatalities: {fatalities}.\nTotal number of Vaccinated people: {vaccinated}.\nTotal Interactions: {interactions}.\nTotal Infections: {infections} "
        file.write(final_data)
        file.close()