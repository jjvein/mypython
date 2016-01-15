def buildConnectionString(params):
    """Build a connection string from the directory of the params

    Return String """
    return ",".join(["%s=%s" % (k,v) for k,v in params.items()]);


if __name__ == '__main__':
    myParams = {
        "server": "localhost",
        "db"    : "test",
        "username": "jjvein",
        "passwd"  : "empty"
    }
    print buildConnectionString(myParams)
    

