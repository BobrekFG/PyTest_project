import requests
from src.baseclasses.response import Response
from configuration import SERVICE_URL
#from src.enums.global_enums import GlobalErrorMessages
#from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.users import User

# def test_getting_posts():
#     r = requests.get(url=SERVICE_URL)
#     response = Response(r)
#     response.assert_status_code(200).validate(Post)
#resp = requests.get(SERVICE_URL)

def test_getting_user_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(300).validate(User)
