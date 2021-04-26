# simple_server

App-client send "Ping" by HTTP get with parametr, app-server check request and answer "Pong".
If request is not "Ping", server answer with "Please send ping."

STEPS to start:

1 ---Git_clone---
sudo apt install git
git clone https://github.com/mzoorg/simple_server

2 ---Ansible install---
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

3 ---Docker install and Deploy---
ansible-playbook deploy_myapp.yml -bK

For test:

docker exec -it app-client bash

1
root@544495b10b10:/var/app# curl http://app-server/?ping
-Pong

2
tcpdump -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'

Output will be like:

15:26:09.385009 IP app-server.appnet.http > 544495b10b10.37684: Flags [FP.], seq 117:121, ack 146, win 508, options [nop,nop,TS val 968141732 ecr 1561737683], length 4: HTTP
E..8?.@.@............P.4............XT.....
9...].9.Pong
15:26:14.393781 IP 544495b10b10.37686 > app-server.appnet.http: Flags [P.], seq 2890977484:2890977630, ack 2125079668, win 502, options [nop,nop,TS val 1561742692 ecr 968146740], length 146: HTTP: GET /?ping HTTP/1.1
E.....@.@..%.........6.P.P..~.$t....X......
].Md9..4GET /?ping HTTP/1.1
Host: app-server
User-Agent: python-requests/2.25.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive


15:26:14.394061 IP app-server.appnet.http > 544495b10b10.37686: Flags [P.], seq 1:117, ack 146, win 508, options [nop,nop,TS val 968146741 ecr 1561742692], length 116: HTTP: HTTP/1.0 200 OK
E...[.@.@..w.........P.6~.$t.P.^....X......
9..5].MdHTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.6.9
Date: Mon, 26 Apr 2021 15:26:14 GMT
Content-type: text/html


15:26:14.394113 IP app-server.appnet.http > 544495b10b10.37686: Flags [FP.], seq 117:121, ack 146, win 508, options [nop,nop,TS val 968146741 ecr 1561742692], length 4: HTTP
E..8[.@.@............P.6~.$..P.^....XT.....
9..5].MdPong
