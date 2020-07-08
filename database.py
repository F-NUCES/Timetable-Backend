# type: ignore
# flake8: noqa
import json

from pony.orm import *


db = Database()


class Courses(db.Entity):
    name = Required(str)
    section = Required(str)
    start_time = Required(str)
    end_time = Required(str)
    room = Required(str)
    day = Required(str)


class CoursesInfo(db.Entity):
    name = Required(str)


# https://github.com/ponyorm/pony/issues/72 (info about to_dict)


@db_session
# noqa: F821
def list_courses():
    query = select(c.name for c in Courses)
    return json.dumps({"courses": list(query)})


@db_session
# noqa: F821
def fetch_course(name):
    query = select(c for c in Courses if c.name == name)
    result = list(map(lambda x: x.to_dict(), query))
    return json.dumps(result)


def db_init(fn="latest.db"):
    db.bind(
        provider="sqlite", filename=fn, create_db=False,
    )
    db.generate_mapping(create_tables=True)


db_init()
