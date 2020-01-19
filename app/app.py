from aiohttp.web import Application, run_app
from http_rest import RestResource
from models import Titanic
from sqlalchemy import engine_from_config


people = {}
app = Application()
person_resource = RestResource(
    "people",
    Titanic,
    people,
    (
        "uuid",
        "survived",
        "passengerClass",
        "name",
        "sex",
        "age",
        "siblingsOrSpousesAboard",
        "parentsOrChildrenAboard",
        "fare",
    ),
    "uuid",
)
person_resource.register(app.router)


if __name__ == "__main__":

    run_app(app)
