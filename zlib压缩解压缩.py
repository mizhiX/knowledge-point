import zlib
"""
命令
字符串：使用zlib.compress可以压缩字符串。使用zlib.decompress可以解压字符串。
数据流：压缩：compressobj，解压：decompressobj
"""
#TODO 压缩解压缩字符串
str = "hello world,0000000000000000000000000000"
print(len(str))# 输出 40

c_str = zlib.compress(str.encode('utf8'))
print(len(c_str))# 输出22
print(c_str)# 输出二进制

d_str=zlib.decompress(c_str)
print(d_str)# 输出hello world,0000000000000000000000000000


# TODO 压缩解压缩文件
# level 压缩等级, 0不压缩, 1最快压缩后的文件大, 9最慢压缩后的文件小
def compress(in_file, dst, level=9):
    in_file = open(in_file, 'rb')
    dst = open(dst, 'wb')
    compress = zlib.compressobj(level)
    data = in_file.read(1024)
    while data:
        dst.write(compress.compress(data))
        data = in_file.read(1024)
    dst.write(compress.flush())


def decompress(in_file, dst):
    in_file = open(in_file, 'rb')
    dst = open(dst, 'wb')
    decompress = zlib.decompressobj()
    data = in_file.read(1024)
    while data:
        dst.write(decompress.decompress(data))
        data = in_file.read(1024)
    dst.write(decompress.flush())


if __name__ == "__main__":
    in_file = "1.txt"
    dst = "1.zlib.txt"
    compress(in_file, dst)

    in_file = "1.zlib.txt"
    dst = "2.txt"
    decompress(in_file, dst)
    print("done~")