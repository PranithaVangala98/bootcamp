from config_load import _load_config


def say_hello(name: str) -> str:
    config = _load_config()
    num_times = config.get("num_times", 1)
    return " ".join([f"Hello, {name}!" for _ in range(num_times)])
