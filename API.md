# API

| HTTP Verb | Path             | Request Content-Type | Request body | Response Content-Type | Example response body |
|-----------|------------------|----------------------|--------------|-----------------------|-----------------------|
| GET       | `/people`        | `application/json`   | -            | `application/json`    | `[ { "uuid": "49dc24bd-906d-4497-bcfc-ecc8c309ecfc", survived": true, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}, ... ]` |
| POST      | `/people`        | `application/json`   | `{ "survived": true, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}` | `application/json`    |  `{ "uuid": "49dc24bd-906d-4497-bcfc-ecc8c309ecfc", survived": true, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}` |
| GET       | `/people/{uuid}` | `application/json`   | -            | `application/json`    | `{ "uuid": "49dc24bd-906d-4497-bcfc-ecc8c309ecfc", survived": true, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}` |
| DELETE    | `/people/{uuid}` | `application/json`   | -            | `application/json`    | - |
| PUT       | `/people/{uuid}` | `application/json`   | `{ "survived": true, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}` | `application/json`    | - |

