from django.conf import settings

DEFAULT_AOS_PARAMS = {
    "disable": False,
    "offset": 120,
    "duration": 400,
    "delay": 0,
}


def get_aos_init_params():
    return {**DEFAULT_AOS_PARAMS, **getattr(settings, "AOS_INIT_PARAMS", {})}
