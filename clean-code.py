
## 1. Prefer readability over cleverness

users = [
    {
        'id':'1',
        'name':'aman',
        'is_active':True
    },
    {
        'id':'2',
        'name':'nilesh',
        'is_active':False
    },
    {
        'id':'3',
        'name':'rahul',
        'is_active':True
    },
]

excluded = ['4']
# Bad — clever but harder to understand
active_users = [user for user in users if user['is_active'] and user['id'] not in excluded]

active_users_good = [
    user for user in users
    if user['is_active'] and user['id'] not in excluded
]
# print(active_users)


# 2. Use type hints


