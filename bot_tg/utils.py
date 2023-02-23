import csv
from typing import List, NoReturn

from bot_tg.credentials import admin_list


def is_admin(id: int) -> bool:
    return id in admin_list


def export_to_csv(headers: List[str], data: List[List[str]], file_name: str) -> NoReturn:
    with open(file_name, "w") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(headers)
        writer.writerows(data)

# headers = ["id", "name"]
# users = [[user[0], user[1]] for user in users]
# with open('users.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=",")
#     writer.writerow(headers)
#     writer.writerows(users)
