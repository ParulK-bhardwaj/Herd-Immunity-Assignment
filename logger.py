class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
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

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        file = open(self.file_name, "w")
        metadata = (f"""Herd Immunity Simulation for {virus_name.title()}\tPopulation Size: {pop_size}\tVaccination Percent: {vacc_percentage}%\tMortality Rate: {mortality_rate}%\tReproduction Rate: {basic_repro_num}%\n""")
        file.write(metadata)
        file.close()
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        file = open(self.file_name, "a")
        interaction_data = f"\nTime Step: {step_number}.\nTotal number of Interactions: {number_of_interactions}.\n Total Number of New Infections: {number_of_new_infections}.\n "
        file.write(interaction_data)
        file.close()
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        file = open(self.file_name, "a")
        survival_data = f"\nTime Step: {step_number}.\nNumber of Survivors: {population_count}.\nTotal Number of New Fatalities: {number_of_new_fatalities}.\n "
        file.write(survival_data)
        file.close()
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile

    def log_final(self, step_number, population, fatalities, vaccinated, interactions, infections):
        file = open(self.file_name, "a")
        final_data = f"\nTime Step: {step_number}.\nTotal Population: {population}.\nTotal Number of Fatalities: {fatalities}.\nTotal number of Vaccinated people: {vaccinated}.\nTotal Interactions: {interactions}.\nTotal Infections: {infections} "
        file.write(final_data)
        file.close()