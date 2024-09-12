import dataclasses


@dataclasses.dataclass
class User:
    user_id: int
    email: str
    first_name: str
    last_name: str
