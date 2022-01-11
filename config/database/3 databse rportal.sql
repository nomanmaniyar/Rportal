CREATE DATABASE IF NOT EXISTS `rportal` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `rportal`;
SET GLOBAL sql_mode = '';
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE IF NOT EXISTS `userdetails` (
	`uid` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
    `name` varchar(50) NOT NULL,
	`password` varchar(255) NOT NULL,
    `mobile` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL UNIQUE,
    `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`uid`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(1, 'jay', 'Jay Sharma', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9420829593', 'jais65142@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(2, 'shinde','Shivnath Sahebrao Shinde', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '9420829593','jay.sharma@matoshri.edu.in');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(3, 'aashutosh','Aashutosh Mali', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','aashutoshmali1460@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(4, 'jay','Dyaneshwar Rangnath Vadnere', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','aashutosh.mali@matoshri.edu.in');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(5, 'ashvini', 'Ashvini Sagar Dighe','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem3@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(6, 'chandrashekhar','Chandrashekhar Bhikchand Joshi', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem4@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(7, 'ashok','Ashok Subhash Kolhe', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem5@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(8, 'kalpana','Kalpana Shibaji Mali', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem6@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(9, 'sachin', 'Sachin Yashwant Shiral','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem7@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(10, 'sangita', 'Sangita Vinay Virari','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem8@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(11, 'nishant','Nishant Dhiren Loyada', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem9@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(12, 'vishvanath','Vishwanath Baburao Tayde', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem10@gmail.com');
INSERT INTO `userdetails` (`uid`, `username`, `name`, `password`, `mobile`, `email`) VALUES(13, 'sharad', 'Sharad Damu Borase','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','9922338265','mem11@gmail.com');
alter table userdetails auto_increment = 14;
select * from userdetails;

CREATE TABLE IF NOT EXISTS `secretary` (
	`Sid` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
  	`Scode` varchar(30) NOT NULL,
	`Semail` varchar(100) NOT NULL,
  	`Sname` varchar(255) NOT NULL,
  	`Sflatno` int(20) NOT NULL,
  	`Swing` varchar(50) NOT NULL,
  	`Smobile` varchar(255) NOT NULL,
    `secretary_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`secretarty_status` varchar(255) default 'request',
    PRIMARY KEY (`Sid`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `secretary` (`Sid`,  `username`,`Scode`, `Semail`,`Sname`,`Sflatno`,`Swing`,`Smobile`) VALUES (1, 'jay', 'GOKU11', 'jais65142@gmail.com','Jay Sharma','1001','A','9420829593');
INSERT INTO `secretary` (`Sid`,  `username`, `Scode`, `Semail`,`Sname`,`Sflatno`,`Swing`,`Smobile`) VALUES (2, 'shinde','SAIR11', 'jay.sharma@matoshri.edu.in','Shivnath Sahebrao Shinde','1','B','9420829593');
alter table secretary auto_increment = 3;
SELECT * FROM secretary;

CREATE TABLE IF NOT EXISTS `member` (
	`Mid` int(11) NOT NULL AUTO_INCREMENT,
	`username` varchar(50) NOT NULL,
  	`Mcode` varchar(30) NOT NULL,
	`Memail` varchar(100) NOT NULL ,
  	`Mname` varchar(255) NOT NULL,
  	`Mflatno` int(20) NOT NULL,
  	`Mwing` varchar(50) NOT NULL,
  	`Mmobile` varchar(255) NOT NULL,
    `member_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`member_status` varchar(255) default 'request',
    PRIMARY KEY (`Mid`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('1', 'aashutosh',  'GOKU11', 'aashutoshmali1460@gmail.com','Aashutosh Mali','1002','A','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('2', 'jay', 'SAIR11', 'aashutosh.mali@matoshri.edu.in','Dyaneshwar Rangnath Vadnere','2','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('3', 'ashvini',  'SAIR11', 'mem3@gmail.com','Ashvini Sagar Dighe','3','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('4', 'chandrashekhar',  'SAIR11', 'mem4@gmail.com','Chandrashekhar Bhikchand Joshi','4','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('5', 'ashok', 'SAIR11', 'mem5@gmail.com','Ashok Subhash Kolhe','5','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('6', 'kalpana',  'SAIR11', 'mem6@gmail.com','Kalpana Shibaji Mali','6','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('7', 'sachin',  'SAIR11', 'mem7@gmail.com','Sachin Yashwant Shiral','7','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('8', 'sangita',  'SAIR11', 'mem8@gmail.com','Sangita Vinay Virari','8','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('9', 'nishant',  'SAIR11', 'mem9@gmail.com','Nishant Dhiren Loyada','9','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('10', 'vishvanath', 'SAIR11', 'mem10@gmail.com','Vishwanath Baburao Tayde','10','B','9922338265');
INSERT INTO `member` (`Mid`, `username`, `Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('11', 'sharad',  'SAIR11', 'mem11@gmail.com','Sharad Damu Borase','11','B','9922338265');
alter table member auto_increment = 12;
select * from member;

CREATE TABLE IF NOT EXISTS `society` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`code` varchar(30) NOT NULL UNIQUE,
  	`name` varchar(50) NOT NULL,
	`city` varchar(50) NOT NULL,
	`road` varchar(255) NOT NULL,
  	`area` varchar(30) NOT NULL,
	`state` varchar(100) NOT NULL,
  	`pin` int(15) NOT NULL,
  	`acname` varchar(255) NOT NULL,
  	`acno` varchar(200) NOT NULL,
  	`mmid` varchar(50),
  	`bankname` varchar(255) NOT NULL,
    `branch` varchar(200) NOT NULL,
  	`ifsc` varchar(255) NOT NULL,
	`soc_bal` float(50),
	`kyc_file` varchar(255),
    `society_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`society_status` varchar(255) default 'request',
    PRIMARY KEY (`id`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `society` (`id`, `code`, `name`,`city`, `road`,`area`,`state`,`pin`,`acname`,`acno`,`mmid`,`bankname`,`branch`,`ifsc`,`soc_bal`,`kyc_file`) VALUES (1, 'GOKU11', 'Gokuldham Society', 'Goregaon East', 'Powder Gali','Goregaon','Maharastra','422001','Gokuldham CO OP Hsg Society','85858858585858','5155755','DBS Bank','Singapour','SBIN0006333','00.00','path');
INSERT INTO `society` (`id`, `code`, `name`,`city`, `road`,`area`,`state`,`pin`,`acname`,`acno`,`mmid`,`bankname`,`branch`,`ifsc`,`soc_bal`,`kyc_file`) VALUES (2, 'SAIR11', 'Sai Residency', 'Nasik', 'Gajpanth','Mhasrul','Maharastra','422003','Sai Residency Account','5454545455454545','2525255','Bank of Maharastra','Panchvati','DBSS0IN0811','00.00','path');
alter table society auto_increment = 3;
select * from society;

CREATE TABLE IF NOT EXISTS `admin` (
	`Aid` int(11) NOT NULL AUTO_INCREMENT,
	`Ausername` varchar(255) NOT NULL,
  	`Apassword` varchar(255) NOT NULL,
	`Aemail` varchar(100),
  	PRIMARY KEY (`Aid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
INSERT INTO `admin` (`Aid`, `Ausername`, `Apassword`,`Aemail`) VALUES ('1', 'ajinfotics', '0252f322f644f82a06ff668230996a0a4ef2b90cc27fc61c9cd014febe6ec4a4', NULL);
select * from admin;

CREATE TABLE IF NOT EXISTS `security` (
	`security_id` int(11) NOT NULL AUTO_INCREMENT,
	`security_username` varchar(255) NOT NULL,
  	`security_password` varchar(255) NOT NULL,
	`security_name` varchar(255) NOT NULL,
	`security_mobile` varchar(255) NOT NULL,
	`security_code` varchar(30) NOT NULL,
    `security_status` varchar(255) default 'active',
  	PRIMARY KEY (`security_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `security` (`security_id`, `security_username`, `security_password`,`security_name`, `security_mobile`, `security_code`) VALUES ('1', 'noman', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Noman', '8889597458', 'GOKU11');
INSERT INTO `security` (`security_id`, `security_username`, `security_password`,`security_name`, `security_mobile`, `security_code`) VALUES ('2', 'anita', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Anita Balasaheb Dalvi', '8942314516', 'SAIR11');
alter table security auto_increment = 3;
select * from security;

CREATE TABLE IF NOT EXISTS `staff` (
	`staff_id` int(11) NOT NULL AUTO_INCREMENT,
	`staff_username` varchar(255) NOT NULL,
  	`staff_password` varchar(255) NOT NULL,
	`staff_name` varchar(255) NOT NULL,
	`staff_mobile` varchar(255) NOT NULL,
    `post` varchar(255),
	`staff_code` varchar(30) NOT NULL,
    `staff_status` varchar(255) default 'active',
  	PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `staff` (`staff_id`, `staff_username`, `staff_password`,`staff_name`, `staff_mobile`, `post`, `staff_code`) VALUES ('1', 'samadhan', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Samadhan', '9515645454', 'gardener', 'GOKU11');
INSERT INTO `staff` (`staff_id`, `staff_username`, `staff_password`,`staff_name`, `staff_mobile`, `post`, `staff_code`) VALUES ('2', 'sitaram', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Sitaram Narayan Kapadnis', '945121415', 'cleaner', 'SAIR11');
alter table staff auto_increment = 3;
select * from staff;

CREATE TABLE IF NOT EXISTS `notification` (
	`notification_id` int(11) NOT NULL AUTO_INCREMENT,
	`notification_message` varchar(500) NOT NULL,
  	PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `notification` (`notification_id`, `notification_message`) VALUES ('1', 'New Member Request');
INSERT INTO `notification` (`notification_id`, `notification_message`) VALUES ('2', 'You have a new notification');
alter table notification auto_increment = 3;
select * from notification;

CREATE TABLE `contactus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `message` varchar(500) NOT NULL,
  `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `contactus` (`id`, `name`, `email`,`message`) VALUES ('1', 'Jay', 'jais65142@gmail.com', 'Test Contact Message');
alter table contactus auto_increment = 2;
select * from contactus;

CREATE TABLE IF NOT EXISTS `complaint` (
	`complaint_id` int(11) NOT NULL AUTO_INCREMENT,
	`complaint_username` varchar(50) NOT NULL,
	`complaint_name` varchar(255) NOT NULL,
	`complaint_subject` varchar(500) NOT NULL,
	`complaint_message` varchar(500) NOT NULL,
	`complaint_code` varchar(30) NOT NULL,
	`complaint_against` varchar(255),
    `complaint_status` varchar(255) DEFAULT 'active',
    `complaint_reply` varchar(255),
    `complaint_reply_closing` varchar(255),
    `complaint_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `complaint` (`complaint_id`, `complaint_username`, `complaint_name`, `complaint_subject`, `complaint_message`, `complaint_code`, `complaint_against`) VALUES ('1', 'aashutosh', 'Aashutosh Mali', 'Cleaning', 'Test Complaint Message', 'GOKU11', 'gardener');
INSERT INTO `complaint` (`complaint_id`, `complaint_username`, `complaint_name`, `complaint_subject`, `complaint_message`, `complaint_code`, `complaint_against`) VALUES ('2', 'dyaneshwar', 'dyaneshwar Rangnath Vadnere', 'Maintainance', 'Test complaint Message', 'SAIR11', 'cleaner');
alter table complaint auto_increment = 3;
select * from complaint;

CREATE TABLE IF NOT EXISTS `notice` (
	`notice_id` int(11) NOT NULL AUTO_INCREMENT,
	`notice_subject` varchar(500) NOT NULL,
	`notice_message` varchar(500) NOT NULL,
	`notice_code` varchar(30) NOT NULL,
    `notice_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`notice_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `notice` (`notice_id`,`notice_subject`, `notice_message`, `notice_code`) VALUES ('1', 'Test Subject', 'Test Notice Message', 'GOKU11');
INSERT INTO `notice` (`notice_id`,`notice_subject`, `notice_message`, `notice_code`) VALUES ('2', 'Test Subject', 'Test Notice Message', 'SAIR11');
alter table notice auto_increment = 3;
select * from notice;

UPDATE complaint SET complaint_reply = 'sry', complaint_status = 'review'  WHERE complaint_id = '1';

CREATE TABLE IF NOT EXISTS `contact` (
	`contact_id` int(11) NOT NULL AUTO_INCREMENT,
	`contact_label` VARCHAR(255) NOT NULL,
	`contact_no` int(40) NOT NULL,
	`society_code` varchar(255) NOT NULL,
  	PRIMARY KEY (`contact_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `document` (
	`doc_id` int(11) NOT NULL AUTO_INCREMENT,
	`doc_filename` varchar(255) NOT NULL,
	`society_code` varchar(255) NOT NULL,
    `document` varchar(255)NOT NULL,
  	PRIMARY KEY (`doc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `chat` (
	`msg_id` int(11) NOT NULL AUTO_INCREMENT,
	`msg_username` varchar(255) NOT NULL,
	`message` varchar(255) NOT NULL,
	`society_code` varchar(255) NOT NULL,
	`msg_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`msg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `visitor` (
  `vid` INT NOT NULL AUTO_INCREMENT,
  `vname` VARCHAR(255) NOT NULL,
  `vmobile` VARCHAR(255) NOT NULL,
  `vehical_no` VARCHAR(255) DEFAULT NULL,
  `in_time` TIME DEFAULT (CURRENT_TIME()),
  `in_date` DATE DEFAULT (CURRENT_DATE()),
  `out_date` DATE DEFAULT NULL,
  `out_time` TIME DEFAULT NULL,
  `vpic` VARCHAR(255) NOT NULL,
  `Mname` VARCHAR(255) NOT NULL,
  `Mflatno` VARCHAR(255) NOT NULL,
  `Mwing` VARCHAR(255) NOT NULL,
  `vstatus` VARCHAR(255) NOT NULL,
  `society_code` VARCHAR(255) NOT NULL,
  `added_by` VARCHAR(255) NOT NULL,
  `entry_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`vid`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
select * from visitor;

CREATE TABLE `meetings` (
  `meet_id` int NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `start_time` varchar(255) NOT NULL,
  `duration` int NOT NULL,
  `url` varchar(255) NOT NULL,
  `agenda` varchar(255) NOT NULL,
  `society_code` varchar(255) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`meet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
select * from meetings;

CREATE TABLE IF NOT EXISTS `maintenance` (
	`main_id` int(11) NOT NULL AUTO_INCREMENT,
	`Musername` varchar(255) NOT NULL,
    `code` varchar(50) NOT NULL,
	`bill_date` timestamp NOT NULL,
    `due_date` timestamp,
    `paid_date` timestamp,
    `amount` float,
    `pending_amount` float,
    `payment_status` varchar(255),
  	PRIMARY KEY (`main_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
select * from maintenance;


CREATE TABLE IF NOT EXISTS `permission` (
	`pid` int(11) NOT NULL AUTO_INCREMENT,
	`username` varchar(255) NOT NULL,
	`subject` varchar(255) NOT NULL,
	`text` varchar(355) NOT NULL,
	`pstatus` varchar(255) NOT NULL,
	`society_code` varchar(255) NOT NULL,
	`per_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;