def error(func):
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except Exception as e:
            type_error = str(e.__class__)[7:-1]
            function = str(e.__traceback__.tb_frame.f_locals["func"])[10:-18]
            print(
                f"Congrats you have raised a {type_error} in {function} with arguments"
                f" {[*args]}"
            )
            return e

    return inner
