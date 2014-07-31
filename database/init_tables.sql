CREATE DATABASE IF NOT EXISTS manong;

DROP TABLE IF EXISTS Issue;

CREATE TABLE Issue
(
    Num int not null,
    Title varchar(200) not null,
    PubDate date not null,
    PRIMARY KEY(Num)
);

DROP TABLE IF EXISTS WeeklyPost;

CREATE TABLE WeeklyPost
(
    ID int not null AUTO_INCREMENT,
    Issue int not null,
    Title varchar(200) not null,
    Description varchar(200) not null,
    PRIMARY KEY(ID),
    FOREIGN KEY(Issue) REFERENCES Issue(Num)
);

DROP TABLE IF EXISTS DailyPost;

CREATE TABLE DailyPost
(
    ID in not null AUTO_INCREMENT,
    Title varchar(200) not null,
    Src varchar(200) not null,
    PubDate date not null,
    PRIMARY KEY(ID)
);

DROP TABLE IF EXISTS Job;

CREATE TABLE Job
(
    ID int not null AUTO_INCREMENT,
    Issue int not null,
    Company varchar(200) not null,
    Position varchar(200) not null,
    PRIMARY KEY(ID),
    FOREIGN KEY(Issue) REFERENCES Issue(Num)
);