class User:

    def __init__(self,
                 name: str = "@slesarevpr",
                 first_name: str = "0",
                 last_name: str = "0",
                 bachelor_year: str = "0",
                 magister_year: str = "0",
                 country: str = "0",
                 city: str = "0",
                 company: str = "0",
                 position: str = "0",
                 linkedin: str = "0",
                 instagram: str = "0",
                 hobbies: str = "0"):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.bachelor_year = bachelor_year
        self.magister_year = magister_year
        self.country = country
        self.city = city
        self.company = company
        self.position = position
        self.linkedin = linkedin
        self.instagram = instagram
        self.hobbies = hobbies

    def __str__(self):
        return " ".join(["name:", self.name, "\n",
                         "first_name:", self.first_name, "\n",
                         "last_name:", self.last_name, "\n",
                         "bachelor_year:", self.bachelor_year, "\n",
                         "magister_year:", self.magister_year, "\n",
                         "country:", self.country, "\n",
                         "city:", self.city, "\n",
                         "company:", self.company, "\n",
                         "position:", self.position, "\n",
                         "linkedin:", self.linkedin, "\n",
                         "instagram:", self.instagram, "\n",
                         "hobbies:", self.hobbies, "\n"])

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
