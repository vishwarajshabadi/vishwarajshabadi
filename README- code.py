class Vishwaraj:

    def human(self):
        self.name = "Vishwaraj Shabadi"
        self.location = "Terra (pro tempore)"
        self.language_spoken = ["English", "French", "German", "Hindi", "Kannada", "Odia"]
        self.interests = ["Cryptocurrency", "Physics", "Programming", "Photography"]
        self.website = ""
    
    def work(self):
        self.company = "Fervium"
        self.position = ["Founder", "CEO", "etc."]

    def studies(self):
        self.diplomas = {
            "Diplôme National du Brevet" : "2020"
        }
        self.education = {
            "Collège Saint Adrien La Salle" : "2015-2020",
            "Lycée Saint Adrien La Salle" : "2020-2023"
        }

    def hi(self):
        print("Hello there. Welcome to my profile")
        print("Here's some Advice : 'There are two rules for success: 1) Never tell anyone everything you know.'")

Vishwaraj.hi(())