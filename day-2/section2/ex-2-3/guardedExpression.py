is_admin = True
user_id = 123


def delete_user(user_id):
    print(f"User with ID {user_id} has been deleted.")


is_admin and delete_user(user_id)


is_admin = False
is_admin and delete_user(user_id)
