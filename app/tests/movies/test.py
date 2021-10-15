# if a class is used, it must begin with Test
class TestFoo:

    # test functions must begin with test_
    def test_bar(self):
        assert "foo" != "bar"