import chardet

# Определим кодировку файла
with open(r'D:\AQA\aqaenv\Lib\site-packages\IPython\core\tests\nonascii.py', 'rb') as f:
    result = chardet.detect(f.read())
    print(result)
