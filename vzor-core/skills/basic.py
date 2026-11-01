# VZOR SmartGlasses - Anti-Recursive Core
_visited = set()

def anti_recursive(func):
    def wrapper(task: str):
        if task in _visited:
            return f"VZOR: уже делал '{task}' - стоп рекурсии!"
        _visited.add(task)
        result = func(task)
        _visited.remove(task)
        return result
    return wrapper

@anti_recursive
def vzor_check(task: str) -> str:
    return f"VZOR checked: {task} -> OK"

def vzor_talk(message: str) -> str:
    return f"VZOR says: {message}"

# test
print(vzor_check("cloud sync"))
print(vzor_talk("Привет, я VZOR SmartGlasses!"))
