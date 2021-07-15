# git intro

## git 명령어

1. `ls` : 파일, 폴더 목록 출력
2. `mkdir` : 폴더 생성
3. `cd` : 이동 명령
   - `..` 으로 상위 폴더 이동
4. `touch`는 파일 생성
5. `rm -r`  : 파일 삭제
6. `ls -a` : 숨긴 폴더나 파일까지 확인

***

- ```
  git --global user.email""
  git --global user.name ""
  //초기 설정 필요
  ```

---

### 초기설정

1. `git init` : .git폴더를 생성 - git이 관리하는 공간 생성
2. `git status` : 1번과 2번 상태를 확인 (working directory, staging area, commits)
3. `git add` : staging area로 파일을 올림
4. `git commit -m ""` : commits 으로 보내는것, 동시에 모든것이 된다.
5. `git log` : 커밋된걸 확인하는 명령어

---

### 원격 저장소

- <u>**Git != Github**</u>
- 
