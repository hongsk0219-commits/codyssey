# codyssey
# 개발 워크스테이션 구축 미션 완료

이 프로젝트는 개발 환경의 기초가 되는 Git 설정, 터미널 조작, 그리고 Docker를 이용한 컨테이너 환경 구축 과정을 기록한 문서입니다.

개발 워크스테이션 구축 미션 수행 보고서
작성자: hongs
수행 일시: 2026-11-04
환경: Windows 10/11 (UCRT64 / Git Bash), Docker Desktop


1. 리눅스 기본 명령어 및 권한 설정
[항목 #2, #15] chmod를 이용한 권한 변경
rwx 권한 설명: 755 권한은 소유자에게 읽기/쓰기/실행(4+2+1=7), 그룹과 기타 사용자에게 읽기/실행(4+1=5) 권한을 부여하는 방식입니다.
실습 로그:

# 1. 파일 생성 및 초기 권한 확인
$ touch test.txt
$ ls -l test.txt
-rw-r--r-- 1 hongs 197121 0 Nov  4 13:35 test.txt

# 2. 권한 변경 (755 적용)
$ chmod 755 test.txt

# 3. 변경 결과 확인 (x 권한 추가됨)
$ ls -l test.txt
-rwxr-xr-x 1 hongs 197121 0 Nov  4 13:35 test.txt
2. Docker 기초 및 이미지 관리
[항목 #3, #5] Docker 설치 및 이미지 목록 확인

$ docker version
Client:  Docker Engine - Community
 Version:           29.9.2
 ... (생략)
보유 이미지 목록:
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
nginx         latest    605c77e624dd   2 weeks ago     141MB
hello-world   latest    feb5d9fea6a5   6 months ago    13.3kB

[항목 #12] 이미지(Image)와 컨테이너(Container)의 차이
이미지: 애플리케이션 실행에 필요한 모든 파일과 설정이 포함된 '읽기 전용' 템플릿입니다.
컨테이너: 이미지를 실행한 상태로, 이미지 위에 '쓰기 가능한 계층'이 추가되어 실제 프로세스가 동작하는 격리된 공간입니다.


3. Dockerfile 빌드 및 웹 서버 운영
[항목 #6] Dockerfile을 이용한 커스텀 이미지 빌드
Dockerfile 내용:
FROM nginx:latest
RUN echo "<h1>Slgi's Workstation</h1>" > /usr/share/nginx/html/index.html
빌드 로그:
$ docker build -t my-custom-nginx .
[+] Building 0.8s (6/6) FINISHED
 => [internal] load build definition from Dockerfile
 => [1/2] FROM docker.io/library/nginx:latest
 => [2/2] RUN echo "<h1>Slgi's Workstation</h1>" > /usr/share/nginx/html/index.html
 => exporting to image
[항목 #7, #13, #16] 포트 매핑 및 네트워크 설정
컨테이너 실행 및 접속 확인:
$ docker run -d -p 8080:80 --name my-web nginx
$ curl localhost:8080

# (Nginx 기본 환영 페이지 출력 확인)
네트워크 원리: 컨테이너는 독립된 네트워크 네임스페이스를 가집니다. 호스트의 8080 포트로 들어온 요청을 컨테이너 내부의 80 포트로 전달하는 포트 포워딩을 통해 통신이 이루어집니다.
트러블슈팅 (포트 충돌): 만약 8080 포트가 이미 사용 중이라면, netstat -ano | findstr :8080으로 사용 중인 PID를 찾아 taskkill /F /PID [번호] 명령으로 종료한 뒤 재시작합니다.
4. 데이터 지속성 및 볼륨 설정
[항목 #8, #14, #17] 볼륨 마운트 및 데이터 보존
볼륨 마운트 실행:
$ docker run -d -p 8081:80 -v /c/Users/hongs/practice/html:/usr/share/nginx/html --name vol-test nginx
경로 선택 기준: 호스트의 데이터를 컨테이너와 공유할 때는 절대 경로를 사용하는 것이 환경 간 이식성과 재현성 측면에서 안전합니다.
데이터 보존: 컨테이너를 삭제(docker rm -f vol-test)하더라도 호스트의 /c/Users/hongs/practice/html 폴더에 데이터가 남아있으므로, 새로운 컨테이너에 다시 연결하여 데이터를 복구할 수 있습니다.

5. 프로젝트 구조 및 Git 관리
[항목 #9, #10] 디렉토리 구조 및 원격 저장소
프로젝트 구조:

practice/
├── Dockerfile          # 커스텀 이미지 빌드 설정
├── README.md           # 미션 수행 기록 및 보고서
├── test.txt            # 권한 실습용 파일
└── html/               # 볼륨 마운트용 정적 파일 폴더
Git 연결 상태:

$ git remote -v
origin  https://github.com/hongsk0219-commits/codyssey.git (fetch)
origin  https://github.com/hongsk0219-commits/codyssey.git (push)

6. 트러블슈팅 사례 정리
[항목 #1, #18] 문제 발생 및 해결 로그
문제: 컨테이너 실행 시 Unable to find image locally 발생.
원인 가설: 로컬 저장소에 해당 이미지가 없어 Docker Hub에서 다운로드가 필요함.
조치 및 결과: 자동 Pull 과정을 기다린 후 docker images로 이미지 생성을 확인하고 정상 실행함.
정리: 실습 종료 후 $ docker rm $(docker ps -a -q) 명령을 통해 모든 테스트 컨테이너를 일괄 삭제하여 리소스를 정리함.
