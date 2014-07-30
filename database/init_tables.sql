

CREATE DATABASE IF NOT EXISTS manong;

DROP TABLE IF EXISTS Issue;

CREATE TABLE Issue
(
    Num int not null,
    Title varchar(200) not null,
    Url varchar(200) not null,
    PRIMARY KEY(Num)
);

DROP TABLE IF EXISTS Post;

CREATE TABLE Post
(
    ID int not null AUTO_INCREMENT,
    Issue int not null,
    Title varchar(200) not null,
    Description varchar(200) not null,
    PRIMARY KEY(ID)
);

DROP TABLE IF EXISTS Job;

CREATE TABLE Job
(
    ID int not null AUTO_INCREMENT,
    Company varchar(200) not null,
    Position varchar(200) not null,
    PRIMARY KEY(ID)
);