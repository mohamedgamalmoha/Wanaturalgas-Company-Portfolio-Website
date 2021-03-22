import random
import string


def random_string_generator(size=10,
                            chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_request_id_generator(instance):
    request_new_id = random_string_generator(size=8)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(request_id=request_new_id).exists()
    if qs_exists:
        return unique_request_id_generator(instance)
    return request_new_id
