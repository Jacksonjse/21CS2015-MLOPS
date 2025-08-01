from list_sort import l_sort

def test_list():
    assert l_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
def test_empty_list():
    assert l_sort([]) == []
def test_repeated_elm_list():
    assert l_sort([3, 2, 3]) == [2, 3, 3]