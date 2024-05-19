# 데이터베이스 종류
- 계층형/네트워크형/관계형 ...
    - 계층형 : Tree 구조 .. 1:N 관계 표현
    - 네트워크 : Owner, Member 형태 .. 1:N, M:N 관계 표현
    - 관게형 : 릴레이션에 데이터 저장 관리. 릴레이션을 활용해 집합연산 및 관계연산 가능

## 관계형 데이터베이스 집합연산, 관계연산
- 집합연산 : 합집합 차집합 교집합 곱집합
- 관계연산 : 선택(select) 투영(projection, 조건 걸기) 결합(join, 새로운 릴레이션) 나누기(division)

## SQL의 종류
1. DDL(Data Definition Language) : 관계형 DB 구조를 정의하는 언어로, CREATE, ALTER, DROP, RENAME, TRUNCATE문 등
2. DML(Data Manipulate Language) : 테이블에서 데이터를 입력 및 수정, INSERT, UPDATE, DELETE, SELECT ...
3. DCL(Data Control Language) : 권한 부여 및 회수, GRANT, REVOKE ...
4. TCL(Transaction Control Language) : 트랜잭션을 제어하는 명령어, COMMIT, ROLLBACK, SACEPOINT ...
### 트랜잭션
- 데이터 베이스의 작업을 처리하는 단위
#### 트랜잭션 특성
1. 원자성 : 데이터 베이스 연산의 전부가 실행되거나 전혀 실행되지 않아야 한다. (완전한 처리가 끝나지 않았다면, 실행되지 않은 상태와 같아야 한다.)
2. 일관성 : 실행 후 데이터베이스의 상태가 모순되지 않아야한다. (일관성유지)
3. 고립성 : 연산 중간의 결과는 다른 트랜잭션이 접근할 수 없다.
4. 영속성 : 트랜잭션이 실행을 성공적으로 완료하면 그 결과는 영구적 보장되어야 함.

## SQL문의 실행 순서
1. 파싱(Parsing) : SQL문의 문법을 확인하고 구문을 분석, 분석한 SQL문은 Library Cache에 저장
2. 실행(Execution) : Optimizer가 수립한 실행 계획에 따라 SQL을 실행한다.
3. 인출(Fetch) : 데이터를 읽어서 전송한다.

# SELECT
```sql
SELECT *
FROM EMP
WHERE 사원번호 =  1000;
```
- SELECT * : 모든 칼럼을 받을 예정
- FROM EMP : EMP라는 테이블에서
- 근데 사원번호가 1000인
## ORDER BY
- 모든 실행이 끝난 후 데이터를 출력하기 전에 정렬을 실행함
- 대량의 데이터를 정렬하게 된다면, 성능 저하가 발생할 수 있다.
- 

```sql
SELECT *
FROM EMP
ORDER BY ENAME, SAL DESC;
```
- Ename으로 오름차순 정렬하고, SAL로 내림차순 정렬!

## DISTINCT와 Alias
- DISTINCT : 칼럼명 앞에 지정해 중복된 데이터를 한번만 조회하게 한다.
```sql
SELECT DISTINCT DEPNO FROM EMP;
```
- Alias : 칼럼, 테이블명에 별명
```sql
SELECT ENAME AS "별명" FROM EMP a
WHERE a.EMPNO=1000;
```
- ENAME이라는 칼럼을 "별명"으로 출력되게 하고, EMP라는 테이블을 a로 사용한다.

## WHERE
- 부정 비교 연산자
  ```
  !=, ^=, <>, NOT 칼럼명 = : 같지 않은 것 조회
  NOT 칼럼명 > : 크지 않은 것 조회
  ```
- SQL 연산자
  ```
  LIKE '%, _ ...' : 뒤 설명 참고
  BETWEEN A AND B : A, B 사이의 값 조회
  IN : OR를 의미하며 list 값 중 하나만 일치해도 조회된다.
  IS NULL : NULL 값 조회
  ```
  - LIKE : %, _ 와일드카드 사용 조회
    ```sql
    SELECT * FROM EMP
    WHERE ENAME LIKE '%est%';
    ```
      - 중간에 est로 존재하는 것 출력
    ```sql
    SELECT * FROM EMP
    WHERE ENAME LIKE 'test_';
    ```
      - test1, test2 처럼 test이후 한글자만 있는 것
## GROUP BY
- HAVING으로 조건에 맞는 GROUP화 가능
  ```spl
  SELECT DEPTNO, SUM(SAL)
  FROM EMP
  GROUP BY DEPTNO
  HAVING SUM(SAL) > 10000;
  ```

# 명시적 형변환과 암시적 형변환
- 명시적 형변환은 함수를 사용해 타입을 일치시키는 것으로, 함수를 사용
1. TO_NUMBER('~~') : 문자열을 숫자로
2. TO_CHAR(숫자 혹은 날짜.[FORMAT]) : 지정된 format의 문자로 변환
3. TO_DATE(문자열, FORMAT) : 문자열을 지정된 FORMAT의 날짜형으로 변환

# 내장형 함수
- 133p

# 이론 확인 문제 (140p)
1. Join : 릴레이션 형성
2. ON DELETE CASCADE 옵션 : 참조한 테이블의 데이터까지 자동 삭제, 참조 무결성 보장하는 옵션
3. View의 특징 : 테이블에서 유도된 가상의 테이블로, 데이터 관리가 간편하고 보안성을 높일 수 있다는 장점이 있다.




