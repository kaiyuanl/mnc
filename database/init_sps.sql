DROP FUNCTION IF EXISTS GetLastIssue;
DELIMITER $$
CREATE FUNCTION GetLastIssue()
RETURNS INT
BEGIN
    declare issue_no INT;
    select MAX(Num) into issue_no
    from manong.Issue;
    return(issue_no);
END$$
DELIMITER ;



drop function if exists GetDailyLastUpdateDate;
delimiter $$
create function GetDailyLastUpdateDate()
returns date 
begin 
    declare latest_date date;
    select MAX(PubDate) into latest_date
    from manong.DailyPost;
    return(latest_date);
end$$
delimiter ;



drop procedure if exists PushJob;
delimiter $$
create procedure PushJob(IN issue_no int, IN company varchar(200), IN position varchar(200))
begin
    insert into manong.Job value(issue_no, company, position);
end$$
delimiter ;



drop procedure if exist PushDailyPost;
delimiter $$
create procedure PushDailyPost(IN title varchar(200), IN src varchar(200), IN pub_date date);
begin
    insert into manong.DailyPost value(title, src, pub_date);
end$$
delimiter ;



drop procedure if exists PushWeeklyPost;
delimiter $$
create procedure PushWeeklyPost(IN issue_no int, IN title varchar(200), IN description varchar(200))
begin
    insert into manong.WeeklyPost value(issue_no, title, description);
end$$
delimiter ;



drop function if exists PushNewIssue;
delimiter $$
create procedure PushNewIssue(IN issue_no int, IN title varchar(200), IN pub_date date)
begin
    insert into manong.Issue value(issue_no, title, pub_date);
end$$
delimiter ;