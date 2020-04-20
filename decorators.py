from functools import wraps

def retry(attempts=5, exception=ValueError):
    @wraps(f)
    def h(*args, **kwargs):
        for i in range(attempts):
            try:
                return f(*args, **kwargs)
            except Exception as err:
                if err.with_traceback() == exception:
                    pass
                else:
                    return err
        return f(*args, **kwargs)
    return h




@retry
def fetch_user_data(id):
    raise ValueError("Just an error")

