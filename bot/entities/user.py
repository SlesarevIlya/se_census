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

    def full_name(self):
        return f"{self.name} {self.first_name} {self.last_name}"

    def description(self) -> str:
        description: str = ""
        if self.bachelor_year != "0" and self.magister_year != "0":
            description += f"bachelor: {self.bachelor_year}, magister: {self.bachelor_year}\n"
        elif self.bachelor_year != "0":
            description += f"bachelor: {self.bachelor_year}\n"
        elif self.magister_year != "0":
            description += f"magister: {self.bachelor_year}\n"

        if self.country != "0":
            if self.city != "0":
                description += f"location: {self.country}, {self.city}\n"
            else:
                description += f"location: {self.country}\n"

        if self.company != "0":
            if self.position != "0":
                description += f"working: {self.company}, {self.position}\n"
            else:
                description += f"working: {self.company}\n"

        return description

    def full_meta(self):
        description: str = self.description()
        if self.linkedin != "0":
            description += f"linkedin: {self.linkedin}\n"
        if self.instagram != "0":
            description += f"instagram: {self.instagram}\n"
        if self.hobbies != "0":
            description += f"hobbies: {self.hobbies}\n"

        return description
