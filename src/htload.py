from bs4 import BeautifulSoup

def loads(html):
    """(str) -> object

    Deserialize HTML, and return a Python object.
    """
    pass # TODO

def load(file):
    """(stream) -> object

    Deserialize HTML from an input stream, and return a Python object.
    """
    return loads(file.read())

if __name__ == '__main__':

    expected = [
        {   "tag"           : "hl",
            "attributes"    : { },
            "children"      : [ "Algorithm Requirements" ]
        },
        "\n\n",
        {   "tag"           : "p",
            "attributes"    : { },
            "children"      : [
                "Per ",
                {   "tag"           : "a",
                    "attributes"    : {
                        "id"            : "credit",
                        "href"          : "http://www-history.mcs.st-andrews.ac.uk/Biographies/Knuth.html"
                    },
                    "children"      : [ "Knuth" ]
                },
                ":"
            ]
        },
        "\n\n",
        {   "tag"           :  "ol",
            "attributes"    : { },
            "children"      : [
                "\n  ",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Finiteness" ]
                },
                "\n  ",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Definiteness" ]
                },
                "\n  ",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Input" ]
                },
                "\n  ",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Output" ]
                },
                "\n  ",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Correctness" ]
                },
                "\n"
            ]
        },
        "\n"
    ]

    with open("test.html") as file:
        actual = load(file)

    assert(expected == actual)
