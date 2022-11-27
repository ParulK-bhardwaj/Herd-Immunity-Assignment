class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

if __name__ == "__main__":
    virus = Virus("Covid-19", 2.5, 3.4)
    assert virus.name == "Covid-19"
    assert virus.repro_rate == 2.5
    assert virus.mortality_rate == 3.4

if __name__ == "__main__":
    virus = Virus("RSV", 2.8, 0.5)
    assert virus.name == "RSV"
    assert virus.repro_rate == 2.8
    assert virus.mortality_rate == 0.5