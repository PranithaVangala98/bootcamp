def role_required(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user["role"] != required_role:
                print(f"Access denied: User must have the '{required_role}' role.")
                return
            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@role_required("admin")
def delete_account(user):
    print(f"Account deleted for user {user['name']}.")


@role_required("moderator")
def moderate_content(user):
    print(f"Content moderated for user {user['name']}.")


# Example users
admin_user = {"name": "Alice", "role": "admin"}
moderator_user = {"name": "Bob", "role": "moderator"}
regular_user = {"name": "Charlie", "role": "user"}

# Call the decorated functions with different users
delete_account(admin_user)  # This should work
delete_account(moderator_user)  # This should deny access
moderate_content(moderator_user)  # This should work
moderate_content(regular_user)  # This should deny access
