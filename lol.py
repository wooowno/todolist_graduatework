from todolist.settings import BASE_DIR, env

print(BASE_DIR)
print(BASE_DIR + "\\" + 'db.sqlite3')
print(env.db())
