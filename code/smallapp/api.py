import falcon
import re


# Your code here

def email_checker(email: str) -> bool:
    regex = r'\b[a-z]+@raymon.ai\b'
    if re.match(regex, email):
        return True
    else:
        return False


class Resource:
    # noinspection PyMethodMayBeStatic
    def on_get(self, req, resp):
        """To handle GET requests"""
        # print("path: ", req.path)
        # print("Request:", req.query_string)
        d = req.params.items()

        if len(req.params) != 3:
            raise falcon.HTTPBadRequest(
                title="Wrong number of parameters.",
                description="A request should consist of exactly three parameters: "
                            "first_name, last_name, and an email address."
            )

        if not {'first_name', 'last_name', 'email'} == set([i[0] for i in list(d)]):
            raise falcon.HTTPBadRequest(
                title="Wrong parameters queried",
                description="The parameters should be: "
                            "first_name, last_name, and an email address."
            )

        lowercase_items = list(map(lambda t: t[1].lower(), list(d)))
        new_d = list(zip([i[0] for i in list(d)], lowercase_items))

        email_ind = email_checker(next(x[1] for x in new_d if x[0] == 'email'))
        first_name_letters = set(next(x[1] for x in new_d if x[0] == 'first_name'))
        last_name_letters = set(next(x[1] for x in new_d if x[0] == 'last_name'))

        common_letters = first_name_letters.intersection(last_name_letters)
        common_letters_list = sorted(list(common_letters))

        resp.media = dict(new_d)
        resp.media['email_ok'] = email_ind
        resp.media['common_letters'] = common_letters_list
        resp.status = falcon.HTTP_200


def create_api():
    api = falcon.API(media_type="application/json")
    api.add_route('/check', Resource())
    return api

