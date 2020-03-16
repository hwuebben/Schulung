# Created by HEW at 16.03.2020
from test import perform_operation

def test_test():
    for x in range(10):
        assert perform_operation(x) > 0
