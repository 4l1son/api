from ..context.json_context import JsonContext


class ApiContext:
    test_table: JsonContext = JsonContext("test.json")
    user_table: JsonContext = JsonContext("users.json")
<<<<<<< HEAD
    sprints_table: JsonContext = JsonContext("sprint.json")
    
=======
    times_table: JsonContext = JsonContext("teams.json")

>>>>>>> origin/back-teams
    def __init__(self) -> None:
        pass
