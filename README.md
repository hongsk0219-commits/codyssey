# codyssey
# 개발 워크스테이션 구축 미션 완료

이 프로젝트는 개발 환경의 기초가 되는 Git 설정, 터미널 조작, 그리고 Docker를 이용한 컨테이너 환경 구축 과정을 기록한 문서입니다.

## 1. 실행 환경 (Environment)
- **OS**: Windows 10/11 (WSL2 사용)
- **Terminal**: Git Bash / UCRT64
- **Docker Version**: 29.9.2 (최신 버전)

## 2. 미션 체크리스트 (Checklist)
- [x] Git 사용자 정보 설정 및 기본 브랜치(main) 변경
- [x] GitHub 원격 저장소 생성 및 로컬 연동
- [x] Docker Desktop 설치 및 WSL2 연동 확인
- [x] `hello-world` 컨테이너 실행 성공
- [x] `ubuntu` 컨테이너 진입 및 리눅스 기본 명령어 실습
- [x] `nginx` 웹 서버 포트 매핑(8080:80) 및 브라우저 접속 성공

## 3. 주요 수행 로그 (Execution Log)

### ✅ Docker 컨테이너 실행 및 정리
```bash
# Ubuntu 컨테이너 실행 및 내부 탐색
$ docker run -it ubuntu bash
root@18f5b654bd25:/# ls
root@18f5b654bd25:/# whoami
root

# 사용 완료한 컨테이너 일괄 삭제
$ docker rm $(docker ps -a -q)

#Nginx 웹서버 구동

## docker check
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker --version
Docker version 29.9.2, build a82e528

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


hongs@LAPTOP-BAB5FBTD UCRT64 ~
$
$
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker --version
Docker version 29.9.2, build a82e528

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash


For more examples and ideas, visit:
 https://docs.docker.com/get-started/

##docker 활용하기 
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
edafa32f5d9e: Pull complete
f3f25b84a7d7: Pull complete
21594acc2d8b: Download complete
Digest: sha256:6a06111c3b0a8600feadb270aec771dc239bf407b25625f93f44ab00e11f4d3c
Status: Downloaded newer image for ubuntu:latest
root@18f5b654bd25:/#
root@18f5b654bd25:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@18f5b654bd25:/# whoami
root
root@18f5b654bd25:/# exit
exit

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
18f5b654bd25   ubuntu        "bash"     11 minutes ago   Exited (0) 8 seconds ago              determined_khayyam
ad80151e2904   hello-world   "/hello"   15 minutes ago   Exited (0) 15 minutes ago             exciting_gauss

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker rm $(docker ps -a -q)
18f5b654bd25
ad80151e2904

#docker로 웹 서버 띄워보기 

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run -d -p 8080:80 --name my-web nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
a670537bed70: Pull complete
9f604dae09b2: Pull complete
6fc242d221a6: Pull complete
6e2ab1f3ef4e: Pull complete
a071113ac575: Pull complete
c139fe92686d: Pull complete
d322f1bf41d8: Pull complete
05a7d8870b4b: Download complete
ca81da665177: Download complete
Digest: sha256:5ab5b0b01097420873a3f3330f44248e34a3c2a3e8d5ee30658aeae8cb7435da
Status: Downloaded newer image for nginx:latest
84474b86cac28f855f35407265ca6feda25335d372bfc48d57ade3f22e1b4e6b

git add README.md
git commit -m "Finalize mission documentation"
git push origin main
