from typing import List


class User:
    headers = ["id", "name", "first_name", "last_name", "bachelor_year", "master_year", "country",
               "city", "company", "position", "linkedin", "instagram", "hobbies"]

    def __init__(self,
                 id: int = 0,
                 name: str = "unknown",
                 first_name: str = "unknown",
                 last_name: str = "unknown",
                 bachelor_year: str = "unknown",
                 master_year: str = "unknown",
                 country: str = "unknown",
                 city: str = "unknown",
                 company: str = "unknown",
                 position: str = "unknown",
                 linkedin: str = "unknown",
                 instagram: str = "unknown",
                 hobbies: str = "unknown"):
        self.id = id
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.bachelor_year = bachelor_year
        self.master_year = master_year
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
                         "master_year:", self.master_year, "\n",
                         "country:", self.country, "\n",
                         "city:", self.city, "\n",
                         "company:", self.company, "\n",
                         "position:", self.position, "\n",
                         "linkedin:", self.linkedin, "\n",
                         "instagram:", self.instagram, "\n",
                         "hobbies:", self.hobbies, "\n"])

    def to_str_array(self) -> List[str]:
        return [str(self.id), self.name, self.first_name, self.last_name, self.bachelor_year, self.master_year,
                self.country, self.city, self.company, self.position, self.linkedin, self.instagram, self.hobbies]

    def full_name(self):
        return f"{self.name}: {self.first_name} {self.last_name}"

    def description(self) -> str:
        description: str = ""
        if self.bachelor_year != "unknown" and self.master_year != "unknown":
            description += f"bachelor: {self.bachelor_year}, magister: {self.master_year}\n"
        elif self.bachelor_year != "unknown":
            description += f"bachelor: {self.bachelor_year}\n"
        elif self.master_year != "unknown":
            description += f"magister: {self.master_year}\n"

        if self.country != "unknown":
            if self.city != "unknown":
                description += f"location: {self.country}, {self.city}\n"
            else:
                description += f"location: {self.country}\n"

        if self.company != "unknown":
            if self.position != "unknown":
                description += f"working: {self.company}, {self.position}\n"
            else:
                description += f"working: {self.company}\n"

        return description

    def full_meta(self):
        description: str = self.description()
        if self.linkedin != "unknown":
            description += f"linkedin: {self.linkedin}\n"
        if self.instagram != "unknown":
            description += f"instagram: {self.instagram}\n"
        if self.hobbies != "unknown":
            description += f"hobbies: {self.hobbies}\n"

        return description
