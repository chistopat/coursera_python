from solution import FileReader

if __name__ == '__main__':
    reader = FileReader('not_exist_file.txt')
    text = reader.read()
    assert text == ''

    with open('some_file.txt', 'w') as file:
        file.write('some text')
    reader = FileReader('some_file.txt')
    text = reader.read()
    assert text =='some text'

    assert isinstance(reader, FileReader)
