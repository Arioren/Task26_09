from typing import Dict
import toolz as t
from returns.maybe import Maybe, Nothing, Some
from sqlalchemy import inspect

from model import Target
from services.utils import has_all_keys


def convert_to_json(target: Target) -> Dict[str, str]:
    return {c.key: getattr(target, c.key) for c in inspect(target).mapper.column_attrs}

def convert_to_user(target_json: Dict[str, str]) -> Maybe[Target]:
    return t.pipe(
        target_json,
        has_all_keys(['target_priority', 'target_industry', 'city_id',"target_type_id" ]),
        lambda is_valid: Nothing if not is_valid else Some(create_target(target_json))
    )


def create_target(target_dict: Dict[str, str]) -> Target:
    return Target(
        target_priority=target_dict["target_priority"],
        target_industry=target_dict["target_industry"],
        city_id=target_dict["city_id"],
        target_type_id = target_dict["target_type_id"]
    )