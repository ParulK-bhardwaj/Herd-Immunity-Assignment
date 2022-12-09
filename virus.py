class Virus(object):
    """Properties and attributes of the virus used in Simulation."""
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Test >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if __name__ == "__main__":
    """Virus class attribute test by making an instance and confirming it has the attributes we defined"""
   
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

if __name__ == "__main__":
    virus = Virus("Covid-19", 0.03, 0.034)
    assert virus.name == "Covid-19"
    assert virus.repro_rate == 2.5
    assert virus.mortality_rate == 3.4

if __name__ == "__main__":
    virus = Virus("RSV", 0.03, 0.5)
    assert virus.name == "RSV"
    assert virus.repro_rate == 2.8
    assert virus.mortality_rate == 0.5