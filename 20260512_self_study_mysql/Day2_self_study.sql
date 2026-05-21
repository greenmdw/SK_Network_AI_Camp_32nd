-- sql_day2_self_study.sql
-- ID: selfstudy
-- PW: Selfstudy80*
-- Day2 복습_constraint_alter

/* DDL(data definition language)
명령어: create, alter, drop 
	create table, alter table, drop table, rename, 
	constraints:
		- primary key, unique, foreing key, check, not null
*/

CREATE TABLE user_account (
	user_id int primary key comment '사용자 번호'
    , user_name varchar(50) not null comment '사용자 이름'
    , user_pwd varchar(30) not null comment '패스워드'
    , email varchar(50) not null comment '이메일'
    , created_at datetime default current_timestamp comment '최초 가입 날짜'
) comment='사용자 계정 정보';

DROP TABLE IF EXISTS MANAGE;
DROP TABLE USER_ACCOUNT;

-- 1. 제약조건(constraint) ********************************************************************
/* 
Not null 제약 조건: 필수 입력 항목에 해당 컬럼일 때 지정
*/
-- 1-A. not null 제약 조건 (컬럼 레벨)
create table tbl_notnull (
	nid   char(3)  not null,  -- 컬럼 레벨
    sname  varchar(20)
); 
insert into tbl_notnull (nid, sname)
value ('100', 'mysql');
value (null, 'mysql');
select * from tbl_notnull;

-- 1-B. unique 제약 조건 (컬럼 레벨, 테이블 레벨)
create table tbl_unique (
	uid char(3) unique
    , sname varchar(20)
);
insert into tbl_unique values ('100', 'mysql');
insert into tbl_unique values ('100', 'mysql'); -- error
-- 단일키: 하나의 컬럼에 제약조건 하나 설정
-- 복합키: 여러 개의 컬럼을 묶어서 하나의 제약 조건 설정(테이블 레벨
create table tbl_unique2 (
	uid char(3) 
    , sname varchar(20)
    , scode char(2)
    , constraint uq_tun2_comp unique (uid, sname)
);
insert into tbl_unique2 values ('100', 'mysql', '01');
select * from tbl_unique2;
insert into tbl_unique2 values ('150', 'del', '01');
insert into tbl_unique2 values ('150', 'elee', '01');

-- 1-C. primary Key 제약조건
/*
테이블의 한 행(row, record)의 정보를 찾아내기 위한 식별(identifier) 키가 될 컬럼에 사용
not null + unique
단일 복합 다 가능
컬럼, 테이블 레벨
*/
create table tbl_pk (
	pid char(3) primary key
    , sname varchar(30)
);
insert into tbl_pk values ('100', 'mysql');
-- primary key 도 복합키 지정 가능
create table tbl_pk2 (
	pid char(3) 
    , sname varchar(30)
    , scode char(2)
    , -- 테이블 레벨
    constraint pk_tpk2_comp primary key (pid, sname)
);
insert into tbl_pk2 values ('100', 'mysql', '01');
insert into tbl_pk2 values ('100', 'sql', '02');
insert into  tbl_pk2 values('200', 'mysql', '01');

-- 1-D. check 제약조건
/* 
mysql 8.0에서만 동작해서 engine=InnoDB 마지막에 붙여야 함
컬럼에 조건 지정해서 조건을 만족하는 값만 기록
*/
create table tbl_check(
	emp_id char(3) primary key comment '사번'
    , salary int check (salary > 0)
    , marriage char(1)
    -- 테이블 레벨
    , constraint ck_tbchk_marriage check (marriage in ('Y', 'N'))
) engine=InnoDB;
insert into tbl_check values ('100', 350, 'Y');
select * from tbl_check;
insert into tbl_check values ('120', -40, 'N');
insert into tbl_check values ('200', -350, 'Y');
-- 주의: 체크 조건은 실행될 때 마다 바뀌는 값은 사용 불가. 설정시 사용하면 에러남. 

-- 1-E foreign key (외래키, 외부키) 제약조건
select * from sal_grade;
select count(*) from sal_grade; -- 행의 수: 5개
select * from department;
select count(*) from department; -- 7행
select * from job;
select count(*) from job; -- 7행
select * from employee;
select count(*) from employee; -- 22행
/*
외부(다른) 테이블의 값을 가져다 기록에 사용하는 컬럼에 설정하는 제약 조건
참조 = parent, 이용하는 테이블(child) , 둘 사이 관계를 relationship
참조한 값만 사용할 수 있고 이외값 사용하면 에러
null 사용 불가
일반적으로 참조 테이블의 컬럼은 primary 또는 unique
table level : 
	constraint 제약조건이름지정 FORIEGN KEY (적용할컬럼명) REFERENCE 참조할부모테이블 (갑제공컬럼명)
    [ON DELETE 삭제방법 [ON UPDATE 업데이트방법]]
    - SET NULL: 부모키 삭제되면 자식 NULL 됨
    - CONCADE: 부모키 삭제되면 자식레코드도 같이 삭제
-*/
-- ERD 생성 가능 :atabase 메뉴 > Reverse Engineer... 선택
-- 자식 레코드 테이블 만들기
create table tbl_fk (
	fid  char(3)
    , sname  varchar(20)
    , loc_id  char(2) references location (location_id)  -- 외래키(foreign key)로 지정
);
select * from location;
select * from tbl_fk;
insert into tbl_fk values ('100', 'mysql', 'A1');
-- insert into tbl_fk2 values ('333', 'web', 'B2'): -- error 참조값에 b2 없음
create table tbl_fk3 (
	fid  char(3)
    , sname  varchar(20)
    , loc_id  char(2) 
    -- 테이블 레벨
    , constraint fk_tblfk3_lid foreign key (loc_id) references location (location_id)
    ) engine=InnoDB;
insert into tbl_fk3 values ('333', 'web', 'B2');
-- 참조 테이블의 참조컬림이 복합키이면 외래키 설정하는 자식도 동일한 복합키로 만들어야 함
-- 주의: 자식 레코드에서 복합키를 단일키로 못 바꿈

-- DML (Data Manipulation Lanaguage)
select * from tbl_pk2;
delete from tbl_pk2 where pid = '100' and sname = 'sql';

-- 서브쿼리 (sub query)를 사용해서 새 테이블 만들기 
-- 테이블 복사본 만들기. 주로 select 한 결과를 테이블로 저장하고자 할 때 씀
/*
create table 테이블명
as
select 구문;
*/
create table emp_cpy
as
select * from employee where dept_id = '90';
select * from emp_cpy;
desc emp_cpy;

-- alter table: 테이블 구조 또는 정보 변경 **************************************************
CREATE TABLE DEPT_CPY
AS
SELECT * FROM DEPARTMENT;
desc dept_cpy;
-- add column
alter table dept_cpy add column mgr_id char(3);
select * from dept_cpy;
-- drop column
alter table dept_cpy drop column mgr_id;
-- add column + default
alter table dept_cpy add column mgr_id char(3) default '00';
-- 컬럼 자료형 변경 : modify column
alter table dept_cpy modify column mgr_id varchar(4);
desc dept_cpy;
alter table dept_cpy modify column mgr_id char(4);
-- 값이 비어있는 컬럼은 아무 자료형으로 변경 가능
-- default 값 변경. 자료형(크기)도 같이 서술해야 함. 다음 자료부터 적용 
select * from dept_cpy;
desc dept_cpy;
alter table dept_cpy modify column  mgr_id char(4) default '333';
insert into dept_cpy values ('30', 'eids', '01', '922');
insert into dept_cpy values ('30', 'eids', '01', default);

-- Not Null 제약조건 변경: modify column 사용
alter table dept_cpy modify column mgr_id char(4) not null;

-- 나머지 제약조건 추가/제거
-- add constraint / drop constraint 

-- 컬럼명 바꾸기: change column 사용
alter table dept_cpy change column mgr_id manager_id char(4) default '101';

-- View 객체 ***************************************************************************************
-- select 문 저장 용도
/*
create view 뷰어이름
as
select 문;

drop view 뷰이름

뷰실행: 뷰에 저장된 select 문을 실행함
뷰는 alter 제공 안함
create or replace 뷰이름
as 
select 문;
*/
create or replace view v_emp as select * from employee where salary > 5000000;
select * from v_emp;

-- TCL (transaction Control Language)
-- commit, rollback, savepoint : DML 구문 실행 후에 반드시 필요; 동시성 제어

/* 시작: 
