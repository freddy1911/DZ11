import json
from candidates import Candidates


def load_candidates_from_json(path: str) -> list[Candidates]:

    """ возвращает список всех кандидатов """
    arr = []
    data = None

    with open(path, 'r', encoding='utf-8') as f:
       data = json.load(f)

    for item in data:
        id_ = item['id']
        name = item['name']
        picture = item['picture']
        position = item['position']
        gender = item['gender']
        age = item['age']
        skills = item['skills']
        arr.append(Candidates(id_, name, picture, position, gender, age, skills))

    return arr


def get_candidate(candidate_id: int, arr: list[Candidates]) -> Candidates:

    """возвращает одного кандидата по его id"""

    for item in arr:
        if item.id == candidate_id:
            return item


def get_candidates_by_name(candidate_name: str, arr: list[Candidates]) -> Candidates:

    """ возвращает кандидатов по имени """

    ret_arr = []
    for item in arr:
        if candidate_name.lower() in item.name.lower():
            ret_arr.append(item)
        return ret_arr

def get_candidates_by_skill(skill_name: str, arr: list[Candidates]) -> Candidates:

    """возвращает кандидатов по навыку"""

    ret_arr = []
    for item in arr:
        if skill_name.lower() in item.skills.lower():
            ret_arr.append(item)
        return ret_arr