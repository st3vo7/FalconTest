import falcon
import re
from typing import Tuple

# Your code here


def is_email(t: Tuple[str, str]):
    if t[0] == 'email':
        return t[1]


def email_checker(email):
    regex = r'\b[a-z]+@raymon.ai\b'
    if re.match(regex, email):
        return True
    else:
        return False


def is_first_name(t: Tuple[str, str]):
    if t[0] == 'first_name':
        return t[1]


def is_last_name(t: Tuple[str, str]):
    if t[0] == 'last_name':
        return t[1]


def second_val(t) -> str:
    """
    :param t: <class 'filter'> type element.
    :return: Second item of a tuple filtered from the list using the `filter` function.
    """
    return next(t)[1]


class Resource:
    # noinspection PyMethodMayBeStatic
    def on_get(self, req, resp):
        """To handle GET requests"""
        # print("path: ", req.path)
        # print("Request:", req.query_string)
        d = req.params.items()
        # for key, value in d:
        #     print(key, value)

        assert len(req.params) == 3, "Wrong number of parameters."

        if not {'first_name', 'last_name', 'email'} == set([i[0] for i in list(d)]):
            raise Exception('Wrong parameters queried.')

        lowercase_items = list(map(lambda t: t[1].lower(), list(d)))
        new_d = list(zip([i[0] for i in list(d)], lowercase_items))

        email_ind = email_checker(second_val(filter(is_email, list(d))))  # True or False

        common_letters = set(second_val(filter(is_first_name, new_d))).intersection(set(second_val(filter(is_last_name, new_d))))
        common_letters_list = sorted(list(common_letters))

        resp.media = dict(new_d)
        resp.media['email_ok'] = email_ind
        resp.media['common_letters'] = common_letters_list
        resp.status = falcon.HTTP_200


def create_api():
    api = falcon.API(media_type="application/json")
    # Your Code here
    return api


app = create_api()
app.add_route('/hello', Resource())
