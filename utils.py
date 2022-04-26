import json


def load_candidates_from_json(path) -> list:
    """
    Функция загружает данные и json файла.
    :param path: "data/candidats.json"
    :return: list
    """
    with open(path, "r", encoding="utf8") as file_candidates:
        return json.load(file_candidates)


def get_candidate_id(candidate_id, path) -> dict:
    """
    Функция выбирает кандидатов по id
    :param candidate_id: int
    :param path: "data/candidats.json"
    :return: dict
    """
    candidates_list = load_candidates_from_json(path)
    for candidat in candidates_list:
        if candidat["id"] == candidate_id:
            return candidat


def get_candidates_by_name(candidate_name, path) -> list:
    """
    Функция выбирает кандидатов по имени.
    :param candidate_name: string
    :param path: "data/candidats.json"
    :return: list
    """
    candidates_list = load_candidates_from_json(path)
    candidat_name_list = []
    for candidat in candidates_list:
        if candidate_name.lower() in candidat["name"].lower():
            candidat_name_list.append(candidat)

    return candidat_name_list


def get_candidates_by_skill(skill_name, path) -> list:
    """
    Функция выбирает кандидатов по навыку
    :param skill_name: string
    :param path: "data/candidats.json"
    :return: list
    """
    candidat_skill_list = []
    candidates_list = load_candidates_from_json(path)
    for candidat in candidates_list:
        skill_list = candidat["skills"].lower().split(", ")
        if skill_name.lower() in skill_list:
            candidat_skill_list.append(candidat)

    return candidat_skill_list

print(type(get_candidate_id(2, "data/candidats.json")))