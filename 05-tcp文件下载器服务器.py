from socket import *
import sys


def get_file_content(filename):
    """获取文件内容"""
    try:
        with open(filename, "rb") as f:
            content = f.read()
        return content
    except:
        print("没有下载的文件:%s" % filename)


def main():
    # print(sys.argv)
    if len(sys.argv) != 2:
        print("请按照如下方式运行：python3 xx.py 7890")
        return
    else:
        # 运行方式为python3 xx.py 7890
        port = int(sys.argv[1])
    # 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 本地信息
    address = ('', port)
    # 绑定本地信息
    tcp_server_socket.bind(address)
    # 将主动套接字变为被动套接字
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端的链接，即为这个客户端发送文件
        client_socket, client_addr = tcp_server_socket.accept()
        # 接受对方发送过来的数据
        recv_data = client_socket.recv(1024)  # 接收1024个字节
        file_name = recv_data.decode("utf-8")
        print("对方请求下载的文件名为:%s" % file_name)
        file_content = get_file_content(file_name)
        # 发送文件的数据给客户端
        # 因为获取打开文件时是以rb方式打开，所以file_content中的数据已经是二进制的格式，因此不需要encode编码
        if file_content:
            client_socket.send(file_content)
        # 关闭这个套接字
        client_socket.close()

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
