

# HTTP 状态码不为 2xx
class HTTPResponseError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


# 条件错误，执行条件不满足
class ConditionError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


# 服务器返回错误，一般会带有返回码
class ServerResponseError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


class ParamError(Exception):
    def __init__(self, message="参数错误"):
        super(ParamError, self).__init__(message)
