from dataclasses import dataclass


@dataclass(frozen=True)
class APIResponse:

    status_code: int
    data: dict
