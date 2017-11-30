import os

def dirMaker(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
            os.chdir(dir)
            return True
        else:
            os.chdir(dir)
            return True

    except Exception as e:
        return e