import pytest


@pytest.fixture()
def root():
    import tree
    root = tree.Node('COM')
    a = tree.Node('A')
    b = tree.Node('B')
    c = tree.Node('C')
    d = tree.Node('D')
    e = tree.Node('E')

    root.add_kid(a)
    a.add_kid(b)
    b.add_kid(c)
    b.add_kid(d)
    d.add_kid(e)

    return root


def test_finding(root):
    assert root.find('E').name == 'E'
    assert root.find('C').name == 'C'


