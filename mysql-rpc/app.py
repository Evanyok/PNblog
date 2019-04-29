import zerorpc
from rpc.MysqlRPC import MysqlRPC

server = zerorpc.Server(MysqlRPC())
server.bind('tcp://127.0.0.1:9100')
print('MySQL RPC Server is running on 127.0.0.1:9100')
server.run()