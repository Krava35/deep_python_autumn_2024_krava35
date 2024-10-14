from functools import wraps


def retry_deco(
        n_repeat: int | None = None,
        errors: list[BaseException] | None = None
):

    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("".join([f"run '{fn.__name__}' - ",
                           f"with possitional arguments {args}; ",
                           f"with keyword kwargs {kwargs}:",]))
            res = None
            for i in range(n_repeat):
                try:
                    res = fn(*args, **kwargs)
                    # pylint: disable=broad-except
                except BaseException as exception:
                    if (errors) and (type(exception) in errors):
                        print(f"    attemp={i+1} | {type(exception).__name__}")
                        break

                    print(f"    attemp={i+1} | {type(exception).__name__}")
                else:
                    print(f"    attemp={i+1} | {res=}")
                    break
            print()
            return res
        return wrapper
    return deco
