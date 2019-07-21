import inspect
import json
from collections import OrderedDict
from models import Titanic, session
from aiohttp.http_exceptions import  HttpBadRequest
from aiohttp.web_exceptions import HTTPMethodNotAllowed
from aiohttp.web import Request, Response
from aiohttp.web_urldispatcher import UrlDispatcher

# This is where all the API endpoints are defined.

DEFAULT_METHODS = ('GET', 'POST', 'PUT', 'DELETE')


class RestEndpoint:

    def __init__(self):
        self.methods = {}

        for method_name in DEFAULT_METHODS:
            method = getattr(self, method_name.lower(), None)
            if method:
                self.register_method(method_name, method)

    def register_method(self, method_name, method):
        self.methods[method_name.upper()] = method

    async def dispatch(self, request: Request):
        method = self.methods.get(request.method.upper())
        if not method:
            raise HTTPMethodNotAllowed('', DEFAULT_METHODS)

        wanted_args = list(inspect.signature(method).parameters.keys())
        available_args = request.match_info.copy()
        available_args.update({'request': request})

        unsatisfied_args = set(wanted_args) - set(available_args.keys())
        if unsatisfied_args:
            # Expected match info that doesn't exist
            raise HttpBadRequest('')

        return await method(**{arg_name: available_args[arg_name] for arg_name in wanted_args})


class CollectionEndpoint(RestEndpoint):
    def __init__(self, resource):
        super().__init__()
        self.resource = resource

    async def get(self) -> Response:
        data = []

        person = session.query(Titanic).all()
        for instance in self.resource.collection.values():
            data.append(self.resource.render(instance))
        data = self.resource.encode(data)
        return Response ( status=200, body=self.resource.encode({
            'person': [
                {
                'survived'                  : person.survived,
                'passengerClass'            : person.passengerClass,
                'name'                      : person.name,
                'sex'                       : person.sex,
                'age'                       : person.age,
                'siblingsOrSpousesAboard'   : person.siblingsOrSpousesAboard,
                'parentsOrChildrenAboard'   : person.parentsOrChildrenAboard,
                'fare'                      : person.fare
                }

                    for person in session.query(Titanic)

                    ]
            }), content_type='application/json')


    async def post(self, request):
        data = await request.json()
        person=Titanic(
            survived                = data['survived'],
            passengerClass          = data['passengerClass'],
            name                    = data['name'],
            sex                     = data['sex'],     
            age                     = data['age'],
            siblingsOrSpousesAboard = data['siblingsOrSpousesAboard'],
            parentsOrChildrenAboard = data['parentsOrChildrenAboard'],
            fare                    = data['fare'])

        session.add(person)
        session.commit()
        
        sensible_response = Response(status=201, body=self.resource.encode({
            'person': [
                {
                'uuid'                      : person.uuid,
                'survived'                  : person.survived,
                'passengerClass'            : person.passengerClass,
                'name'                      : person.name,
                'sex'                       : person.sex,
                'age'                       : person.age,
                'siblingsOrSpousesAboard'   : person.siblingsOrSpousesAboard,
                'parentsOrChildrenAboard'   : person.parentsOrChildrenAboard,
                'fare'                      : person.fare
                }

                    for person in session.query(Titanic)

                    ]
            }), content_type='application/json')
        
        return json.loads(sensible_response)

class InstanceEndpoint(RestEndpoint):
    def __init__(self, resource):
        super().__init__()
        self.resource = resource

    async def get(self, uuid):
        instance = session.query(Titanic).filter(Titanic.id == uuid).first()
        if not instance:
            return Response(status=404, body=json.dumps({'not found': 404}), content_type='application/json')
        data = self.resource.render_and_encode(instance)
        return Response(status=200, body=data, content_type='application/json')

    async def put(self, request, uuid):

        data = await request.json()

        person = session.query(Titanic).filter(Titanic.id == uuid).first()
        person.survived                 = data['survived']
        person.passengerClass           = data['passengerClass']
        person.name                     = data['name']
        person.sex                      = data['sex']
        person.age                      = data['age']
        person.siblingsOrSpousesAboard  = data['siblingsOrSpousesAboard']
        person.parentsOrChildrenAboard  = data['parentsOrChildrenAboard']
        person.fare                     = data['fare']
        session.add(person)
        session.commit()

        return Response(status=201, body=self.resource.render_and_encode(person),
                        content_type='application/json')

    async def delete(self, uuid):
        person = session.query(Titanic).filter(Titanic.id == uuid).first()
        if not person:
            abort(404, message="Passenger {} doesn't exist".format(id))
        session.delete(person)
        session.commit()
        return Response(status=204)


class RestResource:
    def __init__(self, people, factory, collection, properties, id_field):
        self.people     = people
        self.factory    = factory
        self.collection = collection
        self.properties = properties
        self.id_field   = id_field

        self.collection_endpoint = CollectionEndpoint(self)
        self.instance_endpoint = InstanceEndpoint(self)

    def register(self, router: UrlDispatcher):
        router.add_route('*', '/{people}'.format(people=self.people), self.collection_endpoint.dispatch)
        router.add_route('*', '/{people}/{{uuid}}'.format(people=self.people), self.instance_endpoint.dispatch)


    def render(self, instance):
        return OrderedDict((people, getattr(instance, people)) for people in self.properties)

    @staticmethod
    def encode(data):
        return json.dumps(data, indent=4).encode('utf-8')

    def render_and_encode(self, instance):
        return self.encode(self.render(instance))
