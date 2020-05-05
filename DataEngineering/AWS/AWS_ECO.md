## DATABASE

#### 1.RDS

1.1. Create RDS

   `데이터 베이스 -> 데이터베이스 생성 -> 엔진 선택 -> 프리티어 및 기본설정` 

​    

1.2. Setting

- 퍼블릭 액세스 가능성 : 아니오 -> 예

- 보안 -> VPC 보안 그룹 -> 인바운드 규칙 -> 편집
  - 유형 : [RDBMS] 
  - 프로토콜 : TCP
  - 포트 : [RDBMS] 사용포트 
  - 소스 : 위치무관



1.3 CLI 접속 

- **RDBMS : Mysql**

  - ```CLI
    mysql --help
    mysql -h [hostname] -P [port] -u [username] -p [password]
    
    mysql -h dataengineering.cbhogyukzuua.ap-northeast-2.rds.amazonaws.com -P 3306 -u datamaster -p
    ```

    