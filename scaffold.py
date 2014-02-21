

def main():
    """

    """
    object_meta = ('Product', 'name', 'price', 'desc')
    object_tmpl = """
    class %s(object):

        db = MongoClient().valentine

        def __init__(self, %s):
            self.%s =
    """


main()