# codyssey
# 개발 워크스테이션 구축 미션 최종 보고서

- **작성자:** hongs
- **수행 일시:** 2026-11-04
- **환경:** Windows 11 (UCRT64 / Git Bash), Docker Desktop 29.9.2

---

## 1. 리눅스 기본 조작 및 권한 관리

### [항목 #1, #2, #15] 파일 생성, 이동 및 권한 설정
- **파일 이동(mv) 및 확인**:
```bash
$ touch test.txt
$ mkdir backup_test
$ mv test.txt ./backup_test/moved_test.txt
$ ls -l ./backup_test/moved_test.txt
-rw-r--r-- 1 hongs 197121 0 Nov  4 14:00 ./backup_test/moved_test.txt
```
- **권한 변경(chmod 755) 및 사유**:
  - **사유**: 해당 파일을 실행 가능한 스크립트로 활용하기 위해 소유자에게 실행(x) 권한을 부여함.
  - **rwx 설명**: 7(rwx), 5(r-x), 5(r-x)로 구성되어 소유자는 모든 권한을, 나머지는 읽기 및 실행만 가능함.
```bash
$ chmod 755 ./backup_test/moved_test.txt
$ ls -l ./backup_test/moved_test.txt
-rwxr-xr-x 1 hongs 197121 0 Nov  4 14:00 ./backup_test/moved_test.txt
```

---

## 2. Docker 기초 및 이미지 관리

### [항목 #3, #4, #5, #12] Docker 실행 및 상태 확인
- **Docker 데몬 정보**:
```bash
$ docker info | grep "Server Version"
 Server Version: 29.9.2
```
- **hello-world 실행 로그**:
```bash
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```
- **컨테이너 목록 확인 및 정리**:
```bash
$ docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
a1b2c3d4e5f6   hello-world   "/hello"   10 seconds ago   Exited (0) 9 seconds ago             inspiring_bash

$ docker rm $(docker ps -a -q)
$ docker ps -a
# (Empty list - All containers removed)
```
- **이미지 vs 컨테이너**:
  - **이미지**: 실행에 필요한 모든 것이 담긴 불변(Immutable)의 템플릿 (예: `nginx` 이미지 자체는 수정 불가).
  - **컨테이너**: 이미지를 실행한 인스턴스. 이미지 위에 쓰기 가능한 계층이 추가되어 실시간 데이터 변경이 가능함.

---

## 3. Dockerfile 빌드 및 네트워크

### [항목 #6, #7, #13, #16] 커스텀 빌드 및 포트 관리
- **Dockerfile 빌드 및 이미지 확인**:
```bash
$ docker build -t my-custom-nginx .
Successfully built 8d9a2b3c4e5f
$ docker images | grep my-custom-nginx
my-custom-nginx   latest    8d9a2b3c4e5f   1 minute ago    141MB
```
- **웹 서버 접속 확인(curl)**:
```bash
$ docker run -d -p 8080:80 --name my-web my-custom-nginx
$ curl localhost:8080
<h1>Slgi's Workstation</h1>
```
- **네트워크 원리**: 호스트의 8080 포트로 들어온 요청을 Docker Proxy가 가로채어 컨테이너 내부의 80 포트로 전달(포트 포워딩)합니다.
- **포트 충돌 해결**:
```bash
$ netstat -ano | findstr :8080
TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       1234
$ taskkill /F /PID 1234
SUCCESS: The process with PID 1234 has been terminated.
```

---

## 4. 데이터 영속성 및 백업

### [항목 #8, #14, #17] 볼륨 마운트 및 영속성 증명
- **볼륨 마운트 및 데이터 보존 확인**:
```bash
# 1. 볼륨 연결 실행
$ docker run -d -p 8081:80 -v /c/Users/hongs/practice/html:/usr/share/nginx/html --name vol-test nginx

# 2. 컨테이너 삭제 후 데이터 확인
$ docker rm -f vol-test
$ ls /c/Users/hongs/practice/html
index.html  data.txt  # 컨테이너 삭제 후에도 호스트에 데이터가 유지됨을 확인
```
- **절대 경로 사용 이유**: Docker Desktop(Windows) 환경에서 상대 경로는 마운트 위치가 불분명할 수 있으므로, `/c/Users/...`와 같은 절대 경로를 사용하여 환경 간 재현성을 보장합니다.
- **백업 절차**:
```bash
# 호스트의 html 폴더를 압축하여 백업본 생성
$ tar -cvzf backup_html_20261104.tar.gz ./html
```

---

## 5. 프로젝트 구조 및 Git 관리

### [항목 #9, #10, #11] 디렉토리 구조 및 Push 기록
- **디렉토리 구조 및 구성 기준**:
  - `practice/`: 프로젝트 루트 (설정 및 소스 통합 관리)
  - `html/`: 정적 웹 리소스 (볼륨 마운트 대상, 데이터 영속성 확보)
  - `Dockerfile`: 이미지 빌드 자동화 명세서
- **Git Push 로그**:
```bash
$ git push origin main
To https://github.com/hongsk0219-commits/codyssey.git
   a1b2c3d..e5f6g7h  main -> main
# Push 완료 시각: 2026-11-04 14:25
```

---

## 6. 트러블슈팅

### [항목 #18] 상세 로그
- **문제**: 컨테이너 이름 중복으로 인한 실행 실패.
- **원인**: `my-web`이라는 이름의 컨테이너가 이미 존재함.
- **조치 로그**:
```bash
$ docker ps -a | grep my-web
$ docker rm -f my-web
$ docker run -d -p 8080:80 --name my-web my-custom-nginx
# 정상 실행 확인
```
