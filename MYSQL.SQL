mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| companydb          |
| db1                |
| food               |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| studentdb          |
| sys                |
| universitydb       |
| world              |
+--------------------+
11 rows in set (0.29 sec)

mysql> create database collegedb;
Query OK, 1 row affected (0.69 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| collegedb          |
| companydb          |
| db1                |
| food               |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| studentdb          |
| sys                |
| universitydb       |
| world              |
+--------------------+
12 rows in set (0.00 sec)

mysql> use collegedb;
Database changed
mysql> show tables;
Empty set (0.14 sec)

mysql> create table studenttb
    -> (id int(5) primary key,
    -> sname varchar(20),
    -> saddr varchar(20),
    -> sclass varchar(20)
    -> );
Query OK, 0 rows affected, 1 warning (1.82 sec)

mysql> show tables;
+---------------------+
| Tables_in_collegedb |
+---------------------+
| studenttb           |
+---------------------+
1 row in set (0.00 sec)

mysql> desc studenttb;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   | PRI | NULL    |       |
| sname  | varchar(20) | YES  |     | NULL    |       |
| saddr  | varchar(20) | YES  |     | NULL    |       |
| sclass | varchar(20) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.07 sec)

mysql> select * from studenttb;
Empty set (0.03 sec)

mysql> insert into studenttb values(100,'AAA','Daund','MCA');
Query OK, 1 row affected (0.18 sec)

mysql> select * from studenttb;
+-----+-------+-------+--------+
| id  | sname | saddr | sclass |
+-----+-------+-------+--------+
| 100 | AAA   | Daund | MCA    |
+-----+-------+-------+--------+
1 row in set (0.01 sec)

mysql> insert into studenttb values(101,'BBB','Pune','MBBS');
Query OK, 1 row affected (0.07 sec)

mysql> select * from studenttb;
+-----+-------+-------+--------+
| id  | sname | saddr | sclass |
+-----+-------+-------+--------+
| 100 | AAA   | Daund | MCA    |
| 101 | BBB   | Pune  | MBBS   |
+-----+-------+-------+--------+
2 rows in set (0.00 sec)

mysql> update studenttb set saddr = 'Mumbai' where id = 100;
Query OK, 1 row affected (0.16 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from studenttb;
+-----+-------+--------+--------+
| id  | sname | saddr  | sclass |
+-----+-------+--------+--------+
| 100 | AAA   | Mumbai | MCA    |
| 101 | BBB   | Pune   | MBBS   |
+-----+-------+--------+--------+
2 rows in set (0.06 sec)

mysql> delete from studenttb where id = 100;
Query OK, 1 row affected (0.20 sec)

mysql> select * from studenttb;
+-----+-------+-------+--------+
| id  | sname | saddr | sclass |
+-----+-------+-------+--------+
| 101 | BBB   | Pune  | MBBS   |
+-----+-------+-------+--------+
1 row in set (0.00 sec)

mysql>