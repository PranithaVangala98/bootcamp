def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_settings(theme="dark", font="Arial", size=12)
