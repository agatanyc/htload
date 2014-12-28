import bs4

# TODO Is there a more Pythonic way of distinguishing tags, strings, comments,
# etc., than checking exact classes?

def is_tag(x):
    return bs4.element.Tag == type(x)

def is_text(x):
    return bs4.element.NavigableString == type(x)

def children_of(tag):
    """(bs4.BeautifulSoup or bs4.element.Tag) -> list

    Return a list of Python objects representing the children of `tag`.
    """
    return [from_soup(child) for child in tag]

def from_tag(tag):
    """(bs4.element.Tag) -> dict"""
    return {
        "tag"         : tag.name,
        "attributes"  : tag.attrs,
        "children"    : children_of(tag)
    }

def from_soup(element):
    """(bs4 element) -> str or dict

    Tag elements are converted to Python dictionaries.  NavigableString
    elements are converted to Python strings.  All other element types are
    converted to empty strings.
    """
    if is_tag(element):
        return from_tag(element)
    elif is_text(element):
        return str(element)
    else:
        return ""

def coalesce_text(nodes):
    """(list) -> list

    Returns the result of replacing each sequence of consecutive strings in
    `nodes` with a single string.  Does not modify `nodes`.
    """
    pass # TODO

def deep_compare(xs, ys):
    if type(xs) != type(ys):
        return False
    elif type(xs) == str:
        return xs == ys
    elif type(xs) == list:
        same_length = len(xs) == len(ys)
        return same_length and all(deep_compare(x, y) for x, y in zip(xs, ys))
    elif type(xs) == dict:
        keys = sorted(xs.keys())
        same_keys = keys == sorted(ys.keys())
        return same_keys and all(xs[k] == ys[k] for k in keys)
    else:
        raise "unexpected type"

def loads(html):
    """(str) -> list

    Deserialize HTML, and return a list of strings and dicts.
    """
    return children_of(bs4.BeautifulSoup(html))

def load(file):
    """(stream) -> list

    Deserialize HTML from a stream, and return a list of strings and dicts.
    """
    return loads(file.read())

def loadf(fname):
    """(str) -> list

    Return strings and dicts representing the HTML contents of the named file.
    """
    with open(fname) as file:
        return load(file)

if __name__ == '__main__':

    expected = [
        {   "tag"           : "h1",
            "attributes"    : { },
            "children"      : [ "Algorithm Requirements" ]
        },
        "\n", "", "\n",
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
        "\n",   # TODO Work around BeautifulSoup whitespace compression: "\n\n"
        {   "tag"           :  "ol",
            "attributes"    : { "class": ["big", "bad"] },
            "children"      : [
                "\n",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Finiteness" ]
                },
                "\n",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Definiteness" ]
                },
                "\n",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Input" ]
                },
                "\n",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Output" ]
                },
                "\n",
                {   "tag"           : "li",
                    "attributes"    : { },
                    "children"      : [ "Correctness" ]
                },
                "\n"
            ]
        },
        "\n"
    ]

    actual = loadf("test.html")

    assert(deep_compare(expected, actual))
