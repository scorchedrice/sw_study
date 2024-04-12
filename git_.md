# Branch
- 독립적으로 작업할 수 있도록 도와주는 Git의 도구

## Branch 장점
1. 독립 공간을 형성, 원본(master)이 안전
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적으로 협업과 개발이 가능하다.
3. 쉽게 브랜치를 생성하고 브랜치 사이를 이동할 수 있다. (Commit의 이동 자유)

- Master(main) 브랜치
  - 상용버전 / 세상에 공개되어 있으므로 함부로 수정하거나 버전을 돌려선 안된다.

### Example
- 상용중인 서비스에 에러 발생, 개선 방안은?
  1. 브랜치를 통해 별도의 작업 공간 생성
  2. 브랜치에서 에러가 발생한 버전을 이전 버전으로 돌리거나 삭제
  3. 브랜치는 완전하게 독립되어 있기에, 작업 내용이 master에 영향 끼치지 않음.
  4. 문제 해결 이후 master에 반영
 
### git branch
- git branch
  - 브랜치 목록 확인
- git branch -r
  - 저장소 브랜치 목록 확인
- git branch <new_branch_name>
  - 브랜치 생성
- git branch -d <del_branch_name>
- git branch -D <del_branch_name>
  - -d : 병합된 브랜치만 삭제 가능
  - -D : 강제삭제(병합되지 않았더라도)
------------------------------------
- git switch <another_branch_name>
  - 브랜치 이동
- git switch -c <branch_name>
  - 생성과 동시에 브랜치 이동

### HEAD는 가장 최근에 commit한 branch를 바라본다.
