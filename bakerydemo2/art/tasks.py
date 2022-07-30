import dramatiq


@dramatiq.actor
def add(a, b):
    return a + b
