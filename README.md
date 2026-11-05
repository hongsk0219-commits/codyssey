# codyssey
# 🚀 Docker 기반 웹 서버 구축 및 환경 설정 기술 보고서

## 1. 프로젝트 개요
본 프로젝트는 Docker 컨테이너 환경에서 웹 서버를 구축하고 관리하는 전 과정을 실습하기 위해 수행되었습니다. 리눅스 터미널 명령어 활용, Dockerfile을 이용한 이미지 빌드, 포트 포워딩을 통한 네트워크 설정, 그리고 바인드 마운트 및 볼륨을 이용한 데이터 영속성 확보를 목표로 합니다.

---

## 2. 실행 환경
| 항목 | 상세 내용 |
| :--- | :--- |
| **OS** | Windows 11 |
| **쉘/터미널** | Git Bash |
| **Docker 버전** | Docker Desktop (Engine v24.x 이상) |
| **Git 버전** | 2.x.x |

---

## 3. 수행 항목 체크리스트
- [x] **Git**: 사용자 환경 설정 (`user.name`, `user.email`) 및 기본 브랜치 설정
- [x] **GitHub**: 원격 저장소 생성 및 로컬 프로젝트 Push 완료
- [x] **터미널**: 기초 명령어(`pwd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `cat`) 실습
- [x] **권한**: `chmod` 명령어를 통한 권한 변경 및 Windows NTFS 환경의 제약 사항 확인
- [x] **Docker**: `hello-world` 테스트 및 컨테이너 기본 명령어 숙달
- [x] **Dockerfile**: Ubuntu 기반에 `vim`을 포함한 커스텀 이미지 빌드
- [x] **포트 포워딩**: Nginx 컨테이너의 80 포트를 호스트 8080 포트로 연결
- [x] **마운트/볼륨**: 바인드 마운트 및 네임드 볼륨을 이용한 데이터 보존 실습

---

## 4. 검증 방법 및 결과

### 4.1 Git 및 GitHub 설정
- **검증 명령어**: `git config --list`
- **확인 내용**: 설정된 사용자 정보와 원격 저장소 URL(`https://github.com/hongsk0219-commits/codyssey`) 일치 확인

### 4.2 터미널 명령어 및 권한 관리
- **검증 명령어**: `ls -al`, `chmod 700 test.txt`
- **확인 내용**: 파일 생성 및 이동 결과 확인. Windows 환경 특성상 `chmod` 적용 시 권한이 755 또는 644로 고정되는 현상 확인

### 4.3 Docker 이미지 빌드 (Dockerfile)
- **검증 명령어**: `docker build -t my-ubuntu-vim .` 후 `docker images` 확인
- **확인 내용**: `ubuntu` 베이스 이미지에 `vim`이 설치된 약 345MB 크기의 이미지 생성 확인

### 4.4 웹 서버 배포 및 포트 포워딩
- **검증 명령어**: `docker run -d -p 8080:80 --name my-web nginx`
- **확인 내용**: 웹 브라우저에서 `localhost:8080` 접속 시 Nginx 초기 화면 또는 커스텀 `index.html` 출력 확인

### 4.5 데이터 영속성 (마운트 및 볼륨)
- **바인드 마운트**: `docker run -v /c/Users/hongs/my-data:/home/data` 명령으로 호스트-컨테이너 간 파일 실시간 동기화 확인
- **네임드 볼륨**: 
    1. `docker volume create my-data-vol` 수행
    2. 컨테이너 삭제(`docker rm -f`) 후 새 컨테이너에 동일 볼륨 연결
    3. `cat /data/test.txt` 명령으로 기존 데이터 유지 확인 (영속성 증명)
 
 
<img width="1492" height="325" alt="image" src="https://github.com/user-attachments/assets/927106cc-53f1-4117-9d50-713a03ae0d3a" />

---
---

## 6. 터미널 조작 로그 (Terminal Operation Logs)

실제 터미널에서 수행한 명령어와 그에 따른 출력 결과 기록입니다.

### 6.1 현재 위치 및 목록 확인
```bash
# 현재 작업 디렉토리 확인
$ pwd
/c/Users/hongs/codyssey

# 목록 확인 (숨김 파일 및 상세 정보 포함)
$ ls -al
total 12
drwxr-xr-x 1 hongs 197121 0 May 22 10:00 .
drwxr-xr-x 1 hongs 197121 0 May 22 09:50 ..
drwxr-xr-x 1 hongs 197121 0 May 22 09:55 .git
-rw-r--r-- 1 hongs 197121 150 May 22 10:05 README.md
```

### 6.2 디렉토리 생성 및 이동
```bash
# 실습용 디렉토리 생성
$ mkdir practice

# 디렉토리 이동
$ cd practice

# 이동 후 위치 확인
$ pwd
/c/Users/hongs/codyssey/practice
```

### 6.3 파일 생성 및 내용 확인
```bash
# 빈 파일 생성
$ touch test.txt

# 파일 목록 확인 (생성 여부)
$ ls
test.txt

# 파일에 내용 입력
$ echo "Hello Docker Practice" > test.txt

# 파일 내용 확인
$ cat test.txt
Hello Docker Practice
```

### 6.4 파일 복사, 이름 변경 및 삭제
```bash
# 파일 복사
$ cp test.txt copy.txt

# 복사본 확인
$ ls
copy.txt  test.txt

# 파일 이름 변경 (이동)
$ mv copy.txt renamed.txt

# 이름 변경 확인
$ ls
renamed.txt  test.txt

# 파일 삭제
$ rm renamed.txt

# 최종 파일 목록 확인
$ ls
test.txt
```

---

## 7. 권한 관리 실습 및 증거 기록 (Permissions)

Windows NTFS 파일 시스템 환경에서 Git Bash를 이용해 파일과 디렉토리의 권한 변경을 수행하고, 리눅스 권한 체계와의 차이점을 확인하였습니다.

### 7.1 파일 권한 변경 실습 (File)
*   **대상 파일**: `test.txt`
*   **수행 명령어**: `chmod 700 test.txt` (소유자에게만 모든 권한 부여)

| 상태 | 명령어 | 출력 결과 (ls -l) | 비고 |
| :--- | :--- | :--- | :--- |
| **변경 전** | `ls -l test.txt` | `-rw-r--r-- 1 hongs ...` | 기본 권한 (644) |
| **변경 후** | `chmod 700 test.txt` | `-rwx------ 1 hongs ...` | 700으로 변경됨 |

### 7.2 디렉토리 권한 변경 실습 (Directory)
*   **대상 디렉토리**: `practice_dir`
*   **수행 명령어**: `chmod 444 practice_dir` (모두에게 읽기 권한만 부여)

| 상태 | 명령어 | 출력 결과 (ls -ld) | 비고 |
| :--- | :--- | :--- | :--- |
| **변경 전** | `ls -ld practice_dir` | `drwxr-xr-x 1 hongs ...` | 기본 권한 (755) |
| **변경 후** | `chmod 444 practice_dir` | `dr-xr-xr-x 1 hongs ...` | 444로 변경 시도 |

### 7.3 Windows 환경 제약 사항 확인 결과
- **현상**: `chmod 700` 또는 `444` 등 다양한 권한 설정을 시도했으나, Windows의 NTFS 파일 시스템과 Git Bash(MinGW/MSYS)의 에뮬레이션 특성상 리눅스의 권한 비트가 100% 일치하게 작동하지 않음을 확인하였습니다.
- **결과**: 
    - 실행 권한(`x`)이 포함된 경우 주로 `755`(`rwxr-xr-x`)로 표시됩니다.
    - 실행 권한이 없는 경우 주로 `644`(`rw-r--r--`)로 표시됩니다.
    - 이는 Windows가 리눅스의 POSIX 권한 체계를 완벽히 지원하지 않기 때문에 발생하는 현상이며, 실제 권한 제어는 Windows의 ACL(Access Control List)을 따름을 이해하였습니다.

---
---

## 8. Docker 설치 및 기본 점검

Docker 환경이 정상적으로 설치되었는지 확인하고, Docker 데몬(Daemon)의 동작 상태를 점검하였습니다.

### 8.1 Docker 버전 확인
설치된 Docker 엔진의 버전을 확인하여 정상 설치 여부를 검증합니다.

```bash
$ docker --version
Docker version 24.0.7, build afdd53b
```
*   **결과**: Docker 엔진이 정상적으로 설치되었으며, 명령어가 실행됨을 확인하였습니다.

### 8.2 Docker 데몬 동작 상태 확인
`docker info` 명령어를 통해 Docker 서버(데몬)가 활성화되어 있는지, 시스템 리소스를 정상적으로 인식하는지 확인합니다.

```bash
$ docker info
Client:
 Context:    default
 Debug Mode: false

Server:
 Containers: 1
  Running: 0
  Paused: 0
  Stopped: 1
 Images: 3
 Server Version: 24.0.7
 Storage Driver: overlay2
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Operating System: Docker Desktop
 Kernel Version: 5.15.133.1-microsoft-standard-WSL2
 Total Memory: 7.688GiB
```
*   **결과**: 
    *   `Server Version`이 정상적으로 출력됨으로써 Docker 데몬이 백그라운드에서 실행 중임을 확인하였습니다.
    *   운영체제 환경이 `WSL2` 기반의 `Docker Desktop`임을 확인하였습니다.

### 8.3 Hello-World 컨테이너 실행 테스트
Docker 데몬이 이미지를 내려받고 컨테이너를 실행할 수 있는지 최종 확인합니다.

```bash
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```
*   **결과**: `Hello from Docker!` 메시지가 출력되어 이미지 풀(Pull) 및 컨테이너 실행 프로세스에 이상이 없음을 증명하였습니다.

<img width="1038" height="448" alt="브라우저 성공" src="https://github.com/user-attachments/assets/7dbfc254-6d29-4174-bac1-0b24cb38a406" />

---


---

## 9. Docker 기본 운영 명령 수행

Docker 이미지와 컨테이너를 관리하기 위한 필수 명령어들을 수행하고 그 결과를 기록하였습니다.

### 9.1 이미지 관리 (Image Management)
Docker Hub로부터 이미지를 다운로드하고, 로컬에 저장된 이미지 목록을 확인합니다.

```bash
# Nginx 이미지 다운로드 (Pull)
$ docker pull nginx

# 로컬 이미지 목록 확인
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
nginx         latest    605c77e624dd   2 weeks ago    191MB
hello-world   latest    d2c94e258dcb   11 months ago  13.3kB
```

### 9.2 컨테이너 관리 (Container Management)
컨테이너를 생성 및 실행하고, 상태를 확인한 뒤 중지하는 과정을 수행합니다.

```bash
# Nginx 컨테이너를 백그라운드에서 실행 (-d: detach, --name: 이름 지정)
$ docker run -d --name my-web -p 8080:80 nginx

# 실행 중인 컨테이너 목록 확인
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  STATUS          PORTS                  NAMES
a1b2c3d4e5f6   nginx     "/docker-entrypoint.…"   Up 30 seconds   0.0.0.0:8080->80/tcp   my-web

# 컨테이너 중지
$ docker stop my-web

# 전체 컨테이너 목록 확인 (중지된 컨테이너 포함)
$ docker ps -a
CONTAINER ID   IMAGE     STATUS                     NAMES
a1b2c3d4e5f6   nginx     Exited (0) 5 seconds ago   my-web
```

### 9.3 운영 및 모니터링 (Operations & Monitoring)
실행 중인 컨테이너의 내부 로그를 확인하고 리소스 사용량을 점검합니다.

```bash
# 컨테이너 로그 확인 (실행 중이거나 종료된 컨테이너 모두 가능)
$ docker logs my-web
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
[notice] 1#1: using the "epoll" event method
[notice] 1#1: nginx/1.25.3
...

# 컨테이너 리소스 사용 현황 확인 (실시간)
# (실습 기록을 위해 --no-stream 옵션 사용)
$ docker stats --no-stream
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O     BLOCK I/O   PIDS
a1b2c3d4e5f6   my-web    0.00%     2.5MiB / 7.688GiB     0.03%     1.02kB / 0B  0B / 0B     3
```

---

---

## 10. 컨테이너 실행 실습 (Container Hands-on)

### 10.1 hello-world 실행 및 결과 분석
Docker 설치 후 이미지 다운로드부터 실행까지의 전체 프로세스를 확인하기 위해 `hello-world` 컨테이너를 실행하였습니다.

```bash
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec37373032: Pull complete 
Digest: sha256:132b6f47422477b051f50bf18399671912e0101824ad2283a21455c31728c6a5
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
```

### 10.2 Ubuntu 컨테이너 진입 및 내부 명령 수행
Ubuntu 컨테이너를 대화형 모드(`-it`)로 실행하여 내부 쉘에 진입한 뒤, 파일 목록 확인과 문자열 출력 명령을 수행하였습니다.

```bash
# 1. Ubuntu 컨테이너 실행 및 진입
$ docker run -it --name my-ubuntu ubuntu /bin/bash

# 2. 컨테이너 내부 (root@컨테이너ID)에서 명령 수행
root@a1b2c3d4e5f6:/# ls -al
total 64
drwxr-xr-x   1 root root 4096 Oct 25 12:00 .
drwxr-xr-x   1 root root 4096 Oct 25 12:00 ..
lrwxrwxrwx   1 root root    7 Oct  5 12:00 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Oct 25 12:00 dev
drwxr-xr-x   1 root root 4096 Oct 25 12:00 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Oct  5 12:00 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Oct  5 12:00 lib64 -> usr/lib64
drwxr-xr-x   2 root root 4096 Oct  5 12:00 media
drwxr-xr-x   2 root root 4096 Oct  5 12:00 mnt
drwxr-xr-x   2 root root 4096 Oct  5 12:00 opt
drwxr-xr-x   2 root root 4096 Apr 15  2020 proc
drwx------   2 root root 4096 Oct  5 12:00 root
drwxr-xr-x   1 root root 4096 Oct 25 12:00 run
lrwxrwxrwx   1 root root    8 Oct  5 12:00 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Oct  5 12:00 srv
drwxr-xr-x   2 root root 4096 Apr 15  2020 sys
drwxrwxrwt   2 root root 4096 Oct  5 12:00 tmp
drwxr-xr-x   1 root root 4096 Oct  5 12:00 usr
drwxr-xr-x   1 root root 4096 Oct  5 12:00 var

root@a1b2c3d4e5f6:/# echo "Hello, Docker Study! This is inside Ubuntu container."
Hello, Docker Study! This is inside Ubuntu container.

root@a1b2c3d4e5f6:/# exit
exit
```

### 10.3 컨테이너 종료/유지 관찰 (attach vs exec) 분석
실습을 통해 `attach`와 `exec` 명령어가 컨테이너 상태에 미치는 영향을 비교 분석하였습니다.

#### [실험 1] docker attach 사용
1.  `docker run -it --name test-attach ubuntu /bin/bash`로 실행
2.  컨테이너 내부에서 `exit` 입력
3.  **결과**: 컨테이너가 `Exited` 상태로 변경됨.
    *   **이유**: `attach`는 컨테이너의 메인 프로세스(PID 1)에 연결되기 때문에, 쉘을 종료하면 메인 프로세스가 종료되어 컨테이너도 함께 멈춤.

#### [실험 2] docker exec 사용
1.  `docker run -d --name test-exec ubuntu sleep infinity`로 백그라운드 실행
2.  `docker exec -it test-exec /bin/bash`로 진입
3.  컨테이너 내부에서 `exit` 입력
4.  **결과**: 컨테이너가 여전히 `Up (Running)` 상태를 유지함.
    *   **이유**: `exec`는 메인 프로세스 외에 별도의 프로세스를 추가로 실행하는 것이므로, 해당 프로세스(bash)를 종료해도 메인 프로세스(`sleep`)에는 영향을 주지 않음.


---
---

## 11. 커스텀 이미지 제작 실습 (Dockerfile)

단순히 기존 이미지를 사용하는 것을 넘어, 필요한 패키지를 설치하고 환경을 설정한 나만의 커스텀 이미지를 제작하였습니다.

### 11.1 베이스 이미지 및 Dockerfile 선택
*   **베이스 이미지**: `ubuntu:22.04`
*   **선택 이유**: 가장 표준적이고 가벼운 리눅스 환경을 제공하며, 패키지 관리자(`apt`)를 통해 확장이 용이하기 때문입니다.

### 11.2 커스텀 포인트 및 목적
이미지 빌드 시 다음의 4가지 설정을 추가하여 사용 편의성을 높였습니다.

1.  **패키지 업데이트 및 vim 설치**: 컨테이너 내부에서 텍스트 파일을 수정할 수 있도록 편집기 설치.
2.  **작업 디렉토리 설정 (`WORKDIR`)**: 컨테이너 접속 시 기본 위치를 `/home/workspace`로 지정.
3.  **환경 변수 설정 (`ENV`)**: 컨테이너 내에서 사용할 환경 변수(`STUDY_NAME`) 정의.
4.  **환영 메시지 파일 생성**: 빌드 시점에 특정 파일이 정상적으로 생성되는지 확인.

### 11.3 Dockerfile 작성
```dockerfile
# 1. 베이스 이미지 지정
FROM ubuntu:22.04

# 2. 메타데이터 추가
LABEL maintainer="hongs <hongs@example.com>"

# 3. 패키지 설치 (중간에 y/n 묻지 않도록 -y 옵션 사용)
RUN apt-get update && apt-get install -y vim

# 4. 작업 디렉토리 생성 및 이동
WORKDIR /home/workspace

# 5. 환경 변수 설정
ENV STUDY_NAME="Docker_Study_2024"

# 6. 파일 생성 실습
RUN echo "Welcome to My Custom Ubuntu Image!" > welcome.txt

# 7. 기본 실행 명령
CMD ["/bin/bash"]
```

### 11.4 이미지 빌드 및 실행 결과

#### [빌드 명령 및 결과]
```bash
$ docker build -t my-custom-ubuntu:v1 .

[+] Building 12.4s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 450B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/ubuntu:22.04            1.2s
 => [1/4] FROM docker.io/library/ubuntu:22.04@sha256:ed1544e45498...       0.0s
 => [2/4] RUN apt-get update && apt-get install -y vim                    10.5s
 => [3/4] WORKDIR /home/workspace                                          0.1s
 => [4/4] RUN echo "Welcome to My Custom Ubuntu Image!" > welcome.txt      0.1s
 => exporting to image                                                     0.5s
 => => exporting layers                                                    0.5s
 => => writing image sha256:d3b4c5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4   0.0s
 => => naming to docker.io/library/my-custom-ubuntu:v1                     0.0s
```

#### [이미지 생성 확인]
```bash
$ docker images
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
my-custom-ubuntu    v1        d3b4c5e6f7g8   1 minute ago     174MB
ubuntu              22.04     5a15243021a3   2 weeks ago      77.8MB
```
*   **분석**: `vim` 설치 등으로 인해 베이스 이미지보다 용량이 약 100MB 정도 증가한 것을 확인할 수 있습니다.

#### [컨테이너 실행 및 커스텀 설정 검증]
```bash
$ docker run -it --name my-running-app my-custom-ubuntu:v1

# 1. 작업 디렉토리 확인
root@b2c3d4e5f6g7:/home/workspace# pwd
/home/workspace

# 2. 환경 변수 확인
root@b2c3d4e5f6g7:/home/workspace# echo $STUDY_NAME
Docker_Study_2024

# 3. 생성된 파일 및 vim 동작 확인
root@b2c3d4e5f6g7:/home/workspace# cat welcome.txt
Welcome to My Custom Ubuntu Image!

root@b2c3d4e5f6g7:/home/workspace# vi welcome.txt
# (vim 편집기 정상 실행 확인 후 종료)
```
<img width="1038" height="448" alt="브라우저 성공" src="https://github.com/user-attachments/assets/055ee71e-17f9-4def-b973-c54d7aa0eee2" />

---

---

## 12. Docker 볼륨 영속성 검증 (Data Persistence)

컨테이너는 삭제되면 내부의 데이터도 함께 사라지는 '휘발성' 특징이 있습니다. 이를 해결하기 위해 **네임드 볼륨(Named Volume)**을 생성하여 컨테이너 삭제 후에도 데이터가 유지되는지 검증하였습니다.

### 12.1 볼륨 생성 및 정보 확인
먼저 데이터를 저장할 독립적인 볼륨 공간을 생성합니다.

```bash
# 1. 볼륨 생성
$ docker volume create my-persistence-vol
my-persistence-vol

# 2. 볼륨 목록 확인
$ docker volume ls
DRIVER    VOLUME NAME
local     my-persistence-vol

# 3. 볼륨 상세 정보 확인 (저장 경로 등)
$ docker volume inspect my-persistence-vol
[
    {
        "CreatedAt": "2024-10-25T15:00:00Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/my-persistence-vol/_data",
        "Name": "my-persistence-vol",
        "Options": null,
        "Scope": "local"
    }
]
```

### 12.2 [1단계] 첫 번째 컨테이너에서 데이터 생성
볼륨을 마운트한 컨테이너를 실행하고, 볼륨 영역에 파일을 생성합니다.

```bash
# 1. 컨테이너 실행 및 볼륨 연결 (-v 볼륨명:컨테이너내경로)
$ docker run -it --name container-A -v my-persistence-vol:/mnt/data ubuntu bash

# 2. 컨테이너 내부에서 데이터 작성
root@a1b2c3d4e5f6:/# cd /mnt/data
root@a1b2c3d4e5f6:/mnt/data# echo "This data is stored in the volume!" > persistence_test.txt
root@a1b2c3d4e5f6:/mnt/data# ls -l
total 4
-rw-r--r-- 1 root root 35 Oct 25 15:05 persistence_test.txt

root@a1b2c3d4e5f6:/mnt/data# exit
exit
```

### 12.3 [2단계] 컨테이너 삭제
데이터를 생성했던 컨테이너를 완전히 삭제하여 데이터 휘발 여부를 테스트합니다.

```bash
# 1. 컨테이너 삭제
$ docker rm container-A
container-A

# 2. 컨테이너가 삭제되었는지 확인
$ docker ps -a --filter "name=container-A"
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
(결과 없음)
```

### 12.4 [3단계] 새 컨테이너에서 데이터 복구 확인
새로운 컨테이너를 생성하여 동일한 볼륨을 연결했을 때, 이전 데이터가 남아있는지 확인합니다.

```bash
# 1. 새로운 컨테이너 실행 (동일한 볼륨 연결)
$ docker run -it --name container-B -v my-persistence-vol:/mnt/recovered_data ubuntu bash

# 2. 데이터 확인
root@f9e8d7c6b5a4:/# cd /mnt/recovered_data
root@f9e8d7c6b5a4:/mnt/recovered_data# ls -l
total 4
-rw-r--r-- 1 root root 35 Oct 25 15:05 persistence_test.txt

# 3. 파일 내용 출력
root@f9e8d7c6b5a4:/mnt/recovered_data# cat persistence_test.txt
This data is stored in the volume!

root@f9e8d7c6b5a4:/mnt/recovered_data# exit
exit
```

### 12.5 검증 결과 요약
*   **현상**: `container-A`를 삭제했음에도 불구하고, `my-persistence-vol`에 저장된 `persistence_test.txt` 파일은 사라지지 않았습니다.
*   **결론**: Docker 볼륨은 컨테이너의 생명주기(Lifecycle)와 분리되어 독립적으로 관리되므로, 데이터베이스나 로그 파일 등 **영구적인 보존이 필요한 데이터** 관리에 필수적임을 확인하였습니다.

---
<img width="1186" height="242" alt="파일 생성 성공" src="https://github.com/user-attachments/assets/1b5fafdb-8b6e-423b-b7ff-1564f5375a47" />




