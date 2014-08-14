DROP PROCEDURE IF EXISTS GetLastIssue;
DELIMITER $$
CREATE PROCEDURE GetLastIssue(OUT issue_no INT)
BEGIN
    select MAX(Num) into issue_no
    from manong.Issue;
END$$
DELIMITER ;



drop procedure if exists GetDailyLastUpdateDate;
delimiter $$
create procedure GetDailyLastUpdateDate(OUT latest_date date)
begin 
    select MAX(PubDate) into latest_date
    from manong.DailyPost;
end$$
delimiter ;



drop procedure if exists PushJob;
delimiter $$
create procedure PushJob(IN issue_no int, IN company varchar(200), IN position varchar(200))
begin
    insert into manong.Job(Issue, Company, Position) value(issue_no, company, position);
end$$
delimiter ;



drop procedure if exists PushDailyPost;
delimiter $$
create procedure PushDailyPost(IN title varchar(200), IN src varchar(200), IN pub_date date)
begin
    insert into manong.DailyPost(Title, Src, PubDate) value(title, src, pub_date);
end$$
delimiter ;



drop procedure if exists PushWeeklyPost;
delimiter $$
create procedure PushWeeklyPost(IN issue_no int, IN title varchar(200), IN description varchar(200))
begin
    insert into manong.WeeklyPost(Issue, Title, Description) value(issue_no, title, description);
end$$
delimiter ;



drop procedure if exists PushNewIssue;
delimiter $$
create procedure PushNewIssue(IN issue_no int, IN title varchar(200), IN pub_date date)
begin
    insert into manong.Issue value(issue_no, title, pub_date);
end$$
delimiter ;
