user = {
    'id':1,
    'username':'guru',
    'role':'admin'
}

def check_permission(func):
    def wrapper(*args,**kwargs):
        if user.get("role") == 'admin':
            return func(*args,**kwargs)
        else:
            raise PermissionError("User {} with {} role is not permitted to perform this operation".format(user.get('name'),user.get('role')))
    return wrapper

@check_permission(user)
def delete_user():
    print("User is deleted")

print(delete_user())

user['role'] == 'manager'
print(delete_user())