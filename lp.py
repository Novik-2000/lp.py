def test_function():
    def inner_function():
        print('я в области видимости функции test_function()')
    inner_function()

b = test_function()
print(b)

inner_function()