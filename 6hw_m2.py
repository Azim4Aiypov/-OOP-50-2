users = [
    {"name": "Ardager","age": 26,"hobby":"Гонки"},
    {"name":"Ivan","age":30,"hobby":"Футбол"},
    {"name":"Elena","age":22,"hobby":"Чтение"}
]

def get_user_by_name(name):
    for user in users:
        if user["name"] == name:
            return f"NAME: {user['name']} AGE: {user['age']} HOBBY: {user['hobby']}"
    return "Пользователь не найден"

print(get_user_by_name("Ardager"))