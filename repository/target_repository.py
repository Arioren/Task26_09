from typing import List

from returns.maybe import Nothing, Maybe
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import Target, TargetType


def insert_target(target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            type = session.get(TargetType, target.target_type_id)
            if not type:
                return Failure("no for you!!1")
            target.type = type
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            return Failure(str(e))

def delete_target(t_id:int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(t_id)
            if maybe_target is Nothing:
                return Failure(f"No target by the id {t_id}")
            target_to_delete = maybe_target.unwrap()
            session.delete(target_to_delete)
            session.commit()
            return Success(target_to_delete)
        except SQLAlchemyError as e:
            return Failure(str(e))

def find_target_by_id(t_id) -> Maybe[Target]:
    with session_factory() as session:
        target = session.get(Target, t_id)
        return Maybe.from_optional(target)


def update_target(target: Target, target_id:int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure(f"No user {target}")
            target_to_update = session.merge(maybe_target.unwrap())

            target_to_update.target_type_id = target.target_type_id
            target_to_update.target_industry = target.target_industry
            target_to_update.target_priority = target.target_priority
            target_to_update.city_id = target.city_id

            session.commit()
            session.refresh(target_to_update)

            return Success(target_to_update)
        except SQLAlchemyError as e:
            return Failure(str(e))


def find_all_target() -> Maybe[List[Target]]:
    with session_factory() as session:
        targets = session.query(Target).all()
        return Maybe.from_optional(targets)



