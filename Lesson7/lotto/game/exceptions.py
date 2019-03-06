class StopGameEvent(Exception):
    pass


class ExcludeUser(Exception):
    def __init__(self, target, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self._target = target

    @property
    def target(self):
        return self._target
