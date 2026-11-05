# codyssey
# 개발 워크스테이션 구축 미션 최종 보고서

- **작성자:** hongs
- **수행 일시:** 2026-11-04
- **환경:** Windows 11 (UCRT64 / Git Bash), Docker Desktop 29.9.2

---

## 1. git 설정 및 github연동 

''hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ git config --global user.name "홍슬기"
git config --global user.email "hongsk0219@naver.com"
git config --global init.defaultBranch main
git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
user.name=홍슬기
user.email=hongsk0219@naver.com
init.defaultbranch=main''


<img width="1497" height="537" alt="image" src="https://github.com/user-attachments/assets/d4398b5b-b1b3-4a2c-8b24-368d9bca0d0f" />


##권한관리 
''hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ pwd
/c/Users/hongs

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -al #숨겨진 파일 전부 확인 
total 28404
drwxr-xr-x 1 hongs 197609        0 Nov  5 15:58  ./
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  ../
drwxr-xr-x 1 hongs 197609        0 Nov 18  2025  .android/
-rw-r--r-- 1 hongs 197609     6304 Nov  5 15:52  .bash_history
drwxr-xr-x 1 hongs 197609        0 Nov  4 12:30  .config/
drwxr-xr-x 1 hongs 197609        0 Nov  5 15:59  .copilot/
drwxr-xr-x 1 hongs 197609        0 Nov  4 12:28  .docker/
-rw-r--r-- 1 hongs 197609       84 Nov  5 15:53  .gitconfig
-rw-r--r-- 1 hongs 197609       26 Nov  5 15:53  .lesshst
-rw-r--r-- 1 hongs 197609       29 Sep 27  2025  .minttyrc
drwxr-xr-x 1 hongs 197609        0 Nov  5 15:58  .vscode/
drwxr-xr-x 1 hongs 197609        0 Nov  5 15:58  .vscode-shared/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  AppData/
lrwxrwxrwx 1 hongs 197609       30 Apr  6  2025 'Application Data' -> /c/Users/hongs/AppData/Roaming/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  Contacts/
lrwxrwxrwx 1 hongs 197609       58 Apr  6  2025  Cookies -> /c/Users/hongs/AppData/Local/Microsoft/Windows/INetCookies/
drwxr-xr-x 1 hongs 197609        0 Nov  5 16:00  Desktop/
drwxr-xr-x 1 hongs 197609        0 Oct 16 21:35  Documents/
drwxr-xr-x 1 hongs 197609        0 Nov  5 15:55  Downloads/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  Favorites/
drwxr-xr-x 1 hongs 197609        0 Nov  4 12:26  KakaoTalk/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  Links/
lrwxrwxrwx 1 hongs 197609       28 Apr  6  2025 'Local Settings' -> /c/Users/hongs/AppData/Local/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  Music/
lrwxrwxrwx 1 hongs 197609       24 Apr  6  2025 'My Documents' -> /c/Users/hongs/Documents/
-rw-r--r-- 1 hongs 197609 20447232 Nov  4 21:11  NTUSER.DAT
-rw-r--r-- 1 hongs 197609    73728 Oct  6 12:14  NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TM.blf
-rw-r--r-- 1 hongs 197609     4096 Nov  4 21:11  NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TM.blf.cnpf
-rw-r--r-- 1 hongs 197609   561152 Oct  6 12:14  NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000001.regtrans-ms
-rw-r--r-- 1 hongs 197609     4096 Nov  4 21:11  NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000001.regtrans-ms.cnpf
-rw-r--r-- 1 hongs 197609   561152 Oct  6 12:14  NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000002.regtrans-ms
-rw-r--r-- 1 hongs 197609     4096 Nov  4 21:11  NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000002.regtrans-ms.cnpf
lrwxrwxrwx 1 hongs 197609       66 Apr  6  2025  NetHood -> '/c/Users/hongs/AppData/Roaming/Microsoft/Windows/Network Shortcuts'/
drwxr-xr-x 1 hongs 197609        0 Nov  5 15:07  OneDrive/
drwxr-xr-x 1 hongs 197609        0 Sep 21 21:34  Pictures/
lrwxrwxrwx 1 hongs 197609       66 Apr  6  2025  PrintHood -> '/c/Users/hongs/AppData/Roaming/Microsoft/Windows/Printer Shortcuts'/
drwxr-xr-x 1 hongs 197609        0 Sep 12  2025 'PyCharm Community Edition 2025.2.1.1'/
drwxr-xr-x 1 hongs 197609        0 Sep 27  2025  PyCharmMiscProject/
drwxr-xr-x 1 hongs 197609        0 Sep 12  2025  PycharmProjects/
lrwxrwxrwx 1 hongs 197609       55 Apr  6  2025  Recent -> /c/Users/hongs/AppData/Roaming/Microsoft/Windows/Recent/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025 'Saved Games'/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  Searches/
lrwxrwxrwx 1 hongs 197609       55 Apr  6  2025  SendTo -> /c/Users/hongs/AppData/Roaming/Microsoft/Windows/SendTo/
lrwxrwxrwx 1 hongs 197609       58 Apr  6  2025  Templates -> /c/Users/hongs/AppData/Roaming/Microsoft/Windows/Templates/
drwxr-xr-x 1 hongs 197609        0 Apr  6  2025  Videos/
-rw-r--r-- 1 hongs 197609  5382144 Apr  6  2025  ntuser.dat.LOG1
-rw-r--r-- 1 hongs 197609  1572864 Apr  6  2025  ntuser.dat.LOG2
-rw-r--r-- 1 hongs 197609       20 Apr  6  2025  ntuser.ini
drwxr-xr-x 1 hongs 197609        0 Nov  4 13:19  practice/
lrwxrwxrwx 1 hongs 197609       59 Apr  6  2025 '시작 메뉴' -> '/c/Users/hongs/AppData/Roaming/Microsoft/Windows/Start Menu'/

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ mkdir test_dir

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ touch hello.text #오탈자 

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ touch hello.txt


hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -l hello.txt
-rw-r--r-- 1 hongs 197609 0 Nov  5 16:01 hello.txt


hongs@LAPTOP-BAB5FBTD UCRT64 ~
$

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ chmod 444 hello.txt

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -l hello.twt
ls: cannot access 'hello.twt': No such file or directory

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -l hello txt
ls: cannot access 'hello': No such file or directory
ls: cannot access 'txt': No such file or directory

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ^C

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -l hello.txt
-r--r--r-- 1 hongs 197609 0 Nov  5 16:01 hello.txt

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ chomod 700 test_dir #오탈자
bash: chomod: command not found

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ chmod 700 test_dir #실행후 

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -ld test_dir #권한확인 
drwxr-xr-x 1 hongs 197609 0 Nov  5 16:01 test_dir/

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ chmod 755 test_dir #복구 후 

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -ld test_dir #권한 변경 
drwxr-xr-x 1 hongs 197609 0 Nov  5 16:01 test_dir/

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ chmod 644 hello.txt #복구 후 

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls -l hello.txt #권한 확인 
-rw-r--r-- 1 hongs 197609 0 Nov  5 16:01 hello.txt''

''hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ mkdir -p ~/practice && cd ~/practice

hongs@LAPTOP-BAB5FBTD UCRT64 ~/practice (main)
$ echo "hello docker" > test.txt

hongs@LAPTOP-BAB5FBTD UCRT64 ~/practice (main)
$ cp test.txt copy.txt

hongs@LAPTOP-BAB5FBTD UCRT64 ~/practice (main)
$ my copy.txt renamed.txt
bash: my: command not found

hongs@LAPTOP-BAB5FBTD UCRT64 ~/practice (main)
$ mv copy.txt renamed.txt

hongs@LAPTOP-BAB5FBTD UCRT64 ~/practice (main)
$ cat renamed.txt
hello docker

hongs@LAPTOP-BAB5FBTD UCRT64 ~/practice (main)
$ rm renamed.txt

''


---

## 2. Docker 기초 및 이미지 관리

### Docker 실행 및 상태 확인
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker --version #설치확인 
Docker version 29.9.2, build a82e528

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker info #정보 확인
Client:
 Version:    29.9.2
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent: Docker AI Agent Runner (Docker Inc.)
    Version:  v1.152.0
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-agent.exe
  ai: Docker AI Agent - Ask Gordon (Docker Inc.)
    Version:  v1.33.0
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-ai.exe
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.1
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-buildx.exe
  compose: Docker Compose (Docker Inc.)
    Version:  v5.6.1
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-compose.exe
  debug: Get a shell into any image or container (Docker Inc.)
    Version:  0.49.0
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-debug.exe
  desktop: Docker Desktop commands (Docker Inc.)
    Version:  4.97.0
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-desktop.exe
  dhi: CLI for managing Docker Hardened Images (Docker Inc.)
    Version:  v0.0.9
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-dhi.exe
  extension: Manages Docker extensions (Docker Inc.)
    Version:  v0.2.32
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-extension.exe
  init: Creates Docker-related starter files for your project (Docker Inc.)
    Version:  v1.4.1
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-init.exe
  mcp: Docker MCP Plugin (Docker Inc.)
    Version:  v0.44.2
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-mcp.exe
  model: Docker Model Runner (Docker Inc.)
    Version:  v1.2.9
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-model.exe
  offload: Docker Offload (Docker Inc.)
    Version:  v0.7.21
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-offload.exe
  pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
    Version:  v0.3.2
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-pass.exe
  sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
    Version:  v0.13.0
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-sandbox.exe
  scout: Docker Scout (Docker Inc.)
    Version:  v1.27.0
    Path:     C:\Users\hongs\.docker\cli-plugins\docker-scout.exe

Server:
failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.


hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run hello-world #도커 실행

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


##이미지 만들기 
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ mkdir my workstation

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ cd my-workstation
bash: cd: my-workstation: No such file or directory

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ touch Dockerfile

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker build -t my-workstation:1.0 .
[+] Building 33.9s (6/6) FINISHED                                              docker:desktop-linux
 => [internal] load build definition from Dockerfile                                           0.1s
 => => transferring dockerfile: 489B                                                           0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                               0.1s
 => [internal] load .dockerignore                                                              0.1s
 => => transferring context: 2B                                                                0.0s
 => [1/2] FROM docker.io/library/ubuntu:latest@sha256:6a06111c3b0a8600feadb270aec771dc239bf40  1.8s
 => => resolve docker.io/library/ubuntu:latest@sha256:6a06111c3b0a8600feadb270aec771dc239bf40  0.1s
 => => extracting sha256:edafa32f5d9e4d9629f0dbc6c01e63c79ff08133c01cfb7d3363aa8bd8a614cf      1.5s
 => => extracting sha256:f3f25b84a7d74315d94ee4108231f8f5e0cd2a44725a7204d5dd6ce91c151697      0.1s
 => [2/2] RUN apt-get update && apt-get install -y vim                                        24.8s
 => exporting to image                                                                         6.7s
 => => exporting layers                                                                        5.2s
 => => exporting manifest sha256:52f8e26c96712d17fdcd341dd06ccaf03af847488f3020a58a52eb447813  0.0s
 => => exporting config sha256:977181c590319cc4e3a9fd2d888b3eaf57ddcd96f4530316333f59b8007608  0.1s
 => => exporting attestation manifest sha256:32b35a3756d2c84e94c0b9278ad5a4059fc5d4ffa283ea34  0.1s
 => => exporting manifest list sha256:d671d7bb2e1735aba013bd3ac3b05a736528db1866b5a2b97454bf8  0.1s
 => => naming to docker.io/library/my-workstation:1.0                                          0.0s
 => => unpacking to docker.io/library/my-workstation:1.0        

 ## 이미지 확인
 hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker images
                                                                               i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   c567b231f656       25.9kB         9.49kB    U
my-workstation:1.0   d671d7bb2e17        345MB         98.5MB
nginx:latest         5ab5b0b01097        243MB         66.8MB
ubuntu:latest        6a06111c3b0a        163MB         45.9MB

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run -it my-workstation:1.0
root@7c619bb5a078:/# vim --version
VIM - Vi IMproved 9.1 (2024 Jan 02, compiled Oct 13 2026 12:47:02)
Included patches: 1-948, 950-2141
Modified by team+vim@tracker.debian.org
Compiled by team+vim@tracker.debian.org
Huge version without GUI.  Features included (+) or not (-):
+acl                 +jumplist            +sodium
+arabic              +keymap              -sound
+autocmd             +lambda              +spell
+autochdir           +langmap             +startuptime
-autoservername      +libcall             +statusline
-balloon_eval        +linebreak           -sun_workshop
+balloon_eval_term   +lispindent          +syntax
-browse              +listcmds            +tabpanel
++builtin_terms      +localmap            +tag_binary
+byte_offset         -lua                 -tag_old_static
+channel             +menu                -tag_any_white
+cindent             +mksession           -tcl
+clientserver        +modify_fname        +termguicolors
-clipboard           +mouse               +terminal
+clipboard_provider  -mouseshape          +terminfo
+cmdline_compl       +mouse_dec           +termresponse
+cmdline_hist        +mouse_gpm           +textobjects
+cmdline_info        -mouse_jsbterm       +textprop
+comments            +mouse_netterm       +timers
+conceal             +mouse_sgr           +title
+cryptv              -mouse_sysmouse      -toolbar
+cscope              +mouse_urxvt         +user_commands
+cursorbind          +mouse_xterm         +vartabs
+cursorshape         +multi_byte          +vertsplit
+dialog_con          +multi_lang          +vim9script
+diff                -mzscheme            +viminfo
+digraphs            +netbeans_intg       +virtualedit
-dnd                 +num64               +visual
-ebcdic              +packages            +visualextra
+emacs_tags          +path_extra          +vreplace
+eval                -perl                -wayland
+ex_extra            +persistent_undo     -wayland_clipboard
+extra_search        +popupwin            -wayland_focus_steal
-farsi               +postscript          +wildignore
+file_in_path        +printer             +wildmenu
+find_in_path        +profile             +windows
+float               -python              +writebackup
+folding             +python3             -X11
-footer              +quickfix            +xattr
+fork()              +reltime             -xfontset
+gettext             +rightleft           -xim
-hangul_input        -ruby                -xpm
+iconv               +scrollbind          -xsmp
+insert_expand       +signs               -xterm_clipboard
+ipv6                +smartindent         -xterm_save
+job                 +socketserver
   system vimrc file: "/etc/vim/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
 3rd user vimrc file: "~/.config/vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/usr/share/vim"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H -Wdate-time -g -O2 -Werror=implicit-function-declaration -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/vim-aU6mN3/vim-9.1.2141=. -flto=auto -ffat-lto-objects -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -fdebug-prefix-map=/build/vim-aU6mN3/vim-9.1.2141=/usr/src/vim-2:9.1.2141-1ubuntu4.10 -DSYS_VIMRC_FILE=\"/etc/vim/vimrc\" -DSYS_GVIMRC_FILE=\"/etc/vim/gvimrc\" -D_REENTRANT -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1
Linking: gcc -Wl,-Bsymbolic-functions -Wl,--package-metadata=%7B%22type%22:%22deb%22%2C%22os%22:%22ubuntu%22%2C%22name%22:%22vim%22%2C%22version%22:%222:9.1.2141-1ubuntu4.10%22%2C%22architecture%22:%22amd64%22%7D -flto=auto -ffat-lto-objects -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -o vim -lm -ltinfo -lselinux -lsodium -lacl -lattr -lgpm -L/usr/lib/python3.14/config-3.14-x86_64-linux-gnu -lpython3.14 -ldl -lm
root@7c619bb5a078:/# exit
exit


## 볼륨 연결 
# 컴퓨터에 공유 폴더 만들기 
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ pwd
/c/Users/hongs

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ mkdir my-data

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ ls
 AppData/
'Application Data'@
 Contacts/
 Cookies@
 Desktop/
 Dockerfile
 Documents/
 Downloads/
 Favorites/
 KakaoTalk/
 Links/
'Local Settings'@
 Music/
'My Documents'@
 NTUSER.DAT
 NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TM.blf
 NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TM.blf.cnpf
 NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000001.regtrans-ms.cnpf
 NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000002.regtrans-ms
 NTUSER.DAT{e3996a02-12b3-11f0-86f5-c49c9b9e17ea}.TMContainer00000000000000000002.regtrans-ms.cnpf
 NetHood@
 OneDrive/
 Pictures/
 PrintHood@
'PyCharm Community Edition 2025.2.1.1'/
 PyCharmMiscProject/
 PycharmProjects/
 Recent@
'Saved Games'/
 Searches/
 SendTo@
 Templates@
 Videos/
 hello.text
 hello.txt
 my/
 my-data/ #내가 만든거 
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 ntuser.ini
 practice/
 test_dir/
 workstation/
'시작 메뉴'@

#컨테이너 안에 파일 만들기 
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run -it -v /c/Users/hongs/my-data:/home/data my-workstation:1.0
root@b8265d069ca2:/# cd /home/data #폴더로 이동 
bash: cd: /home/data: No such file or directory
root@b8265d069ca2:/# echo "Docker is fun!" > success.txt #파일 생성
root@b8265d069ca2:/# ls #파일 확인
'\Program Files\Git\home\data'   dev    lib     mnt    root   srv           tmp
 bin                             etc    lib64   opt    run    success.txt   usr
 boot                            home   media   proc   sbin   sys           var
root@b8265d069ca2:/# cat success.txt
Docker is fun!
root@b8265d069ca2:/# exit
exit

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run -it -v "C:\Users\hongs\my-data:/home/data" my-workstation:1.0
root@1f524fa70820:/# cd /home/data
root@1f524fa70820:/home/data# ls
root@1f524fa70820:/home/data# touch hello_from_docker.txt #텍스트 만들고 파일에서 확인 
root@1f524fa70820:/home/data# ls
hello_from_docker.txt 
root@1f524fa70820:/home/data# ls #파일에서 테스트 불러오기 
hello_from_docker.txt  win.txt.txt
root@1f524fa70820:/home/data#

## html 파일 웹 서버에 띄우기 
hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ echo "<h1>Hello, Docker Study! My Web Server is Running!</h1>" > index.html

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker rm -f my-web
my-web

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker run -d \
  -p 8080:80 \
  -v "C:\Users\hongs\my-data:/usr/share/nginx/html" \
  --name my-custom-server \
  nginx
docker: Error response from daemon: Conflict. The container name "/my-custom-server" is already in use by container "0f6ab48e407505b2a65bd59c89583831f4626f2eadbec8ece9780dbc517feb01". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information

What's next:
    Debug this container error with Gordon → docker ai "help me fix this container error"

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ docker rm -f my-custom-server
my-custom-server

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ mkdir -p /c/Users/hongs/my-data
mv index.html /c/Users/hongs/my-data/

hongs@LAPTOP-BAB5FBTD UCRT64 ~
$ MSYS_NO_PATHCONV=1 docker run -d \
  -p 8080:80 \
  -v "C:\Users\hongs\my-data:/usr/share/nginx/html" \
  --name my-custom-server \
  nginx
1e3a654058a7f2399425c0b1ad1a2bd2c3d2203d6fad5ef5831a9777bfad6e4e












## 트러블슈팅 사례 
1. 트러블슈팅 사례 
문제: docker run 실행 시 failed to connect to the docker API 에러 발생.
원인: Docker Desktop 엔진이 실행되지 않은 상태에서 명령어를 입력함.
해결: Docker Desktop 프로그램을 실행하고 고래 아이콘이 활성화된 것을 확인한 후 재시도하여 해결함.

2. 컨테이너 이름 충돌 (Name Conflict)
증상: Conflict. The container name "/my-custom-server" is already in use... 에러 발생.
원인: 도커는 같은 이름을 가진 컨테이너를 동시에 생성할 수 없습니다. 이전에 실행했거나 멈춰있는 컨테이너가 이름을 점유하고 있기 때문입니다.
해결: docker rm -f [컨테이너이름] 명령어로 기존 컨테이너를 강제 삭제 후 다시 생성합니다.
