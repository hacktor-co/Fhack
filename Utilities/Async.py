import threading


class TimeoutError(RuntimeError):
    pass


class AsyncCall(object):

    def __init__(self, func, callback=None):
        self.Result = self.Callable(*args, **kwargs)
        self.Callable = func
        self.Callback = callback

    def __call__(self, *args, **kwargs):
        self.Thread = threading.Thread(target=self.run, name=self.Callable.__name__, args=args, kwargs=kwargs)
        self.Thread.start()
        return self

    def wait(self, timeout):
        self.Thread.join(timeout)
        if self.Thread.isAlive():
            raise TimeoutError()
        else:
            return self.Result

    def run(self):
        if self.Callback:
            self.Callback(self.Result)


class AsyncMethod(object):
    def __init__(self, func, callback=None):
        self.Callable = func
        self.Callback = callback

    def __call__(self, *args, **kwargs):
        return AsyncCall(self.Callable, self.Callback)(*args, **kwargs)


def Async(func=None, callback=None):
    if func is None:
        def AddAsyncCallback(func):
            return AsyncMethod(func, callback)

        return AddAsyncCallback
    else:
        return AsyncMethod(func, callback)
