import requests
from src.baseclasses.response import Response

#from src.enums.global_enums import GlobalErrorMessages
#from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.users import User

# def test_getting_posts():
#     r = requests.get(url=SERVICE_URL)
#     response = Response(r)
#     response.assert_status_code(200).validate(Post)
#resp = requests.get(SERVICE_URL)

def test_getting_user_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)



def test_another():
    assert 1 == 1

