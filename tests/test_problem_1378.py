import pytest
import pandas as pd
from common.parse_input import parse_data_to_dataframe
from solutions.problem_1378 import replace_employee_id


@pytest.mark.skip(reason="TODO: Implement two pandas dataframes comparison.")
def test_replace_employee_id():
    employees_str = """
        | id | name     |
        | -- | -------- |
        | 1  | Alice    |
        | 7  | Bob      |
        | 11 | Meir     |
        | 90 | Winston  |
        | 3  | Jonathan |
    """

    employees_uni_str = """
        | id | unique_id |
        | -- | --------- |
        | 3  | 1         |
        | 11 | 2         |
        | 90 | 3         |
    """

    employees: pd.DataFrame = parse_data_to_dataframe(employees_str)
    employees_uni: pd.DataFrame = parse_data_to_dataframe(employees_uni_str)

    correct_answer_str = """
        | unique_id | name     |
        |-----------|----------|
        | null      | Alice    |
        | null      | Bob      |
        | 2         | Meir     |
        | 3         | Winston  |
        | 1         | Jonathan |
    """

    correct_answer = parse_data_to_dataframe(correct_answer_str)

    print(correct_answer)
    print(replace_employee_id(employees, employees_uni))

    assert replace_employee_id(employees, employees_uni).equals(correct_answer)
