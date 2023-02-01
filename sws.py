
#timeout should be ~30 seconds

#TODO:
    # 200 ok
    # persistent connection
    # correct return large file
    # 404 not found
    # 400 bad request (2 pts)
    # multiple clients
    # timeout
    # back-to-back request
    # server output format

server = socket()
setsocketopt(server, non-blocking)
bind(server)
listen(server)
sockets = server
select(sockets) #workers?
buf = recv(server)
line = gets(buf)
keepalive(worker) = 1


