CREATE DATABASE IF NOT EXISTS manong;
USE manong;

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
    ID MEDIUMINT not null AUTO_INCREMENT,
    Issue int not null,
    Title varchar(200) not null,
    Origin varchar(200) null,
    Link varchar(300) null,
    PRIMARY KEY(ID),
    FOREIGN KEY(Issue) REFERENCES Issue(Num)
);


DROP PROCEDURE IF EXISTS GetLastIssue;
DELIMITER $$
CREATE PROCEDURE GetLastIssue(OUT issue_no INT)
BEGIN
    select MAX(Num) into issue_no
    from manong.Issue;
END$$
DELIMITER ;


drop procedure if exists PushWeeklyPost;
delimiter $$
create procedure PushWeeklyPost(IN issue_no int, IN title varchar(200), IN Origin varchar(200), IN Link varchar(300))
begin
    insert into manong.WeeklyPost(Issue, Title, Origin, Link) value(issue_no, title, Origin, Link);
end$$
delimiter ;


drop procedure if exists PushNewIssue;
delimiter $$
create procedure PushNewIssue(IN issue_no int, IN title varchar(200), IN pub_date date)
begin
    insert into manong.Issue value(issue_no, title, pub_date);
end$$
delimiter ;
