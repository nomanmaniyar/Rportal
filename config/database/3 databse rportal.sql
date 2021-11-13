CREATE DATABASE IF NOT EXISTS `rportal` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `rportal`;
SET GLOBAL sql_mode = '';
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE IF NOT EXISTS `secretary` (
	`Sid` int(11) NOT NULL AUTO_INCREMENT,
  	`Susername` varchar(50) NOT NULL,
  	`Spassword` varchar(255) NOT NULL,
  	`Scode` varchar(30) NOT NULL,
	`Semail` varchar(100) NOT NULL UNIQUE,
  	`Sname` varchar(255) NOT NULL,
  	`Sflatno` int(20) NOT NULL,
  	`Swing` varchar(50) NOT NULL,
  	`Smobile` varchar(255) NOT NULL,
    `secretary_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`secretarty_status` varchar(255) default 'request',
    PRIMARY KEY (`Sid`, `Susername`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `secretary` (`Sid`, `Susername`, `Spassword`,`Scode`, `Semail`,`Sname`,`Sflatno`,`Swing`,`Smobile`) VALUES (1, 'jay', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'GOKU11', 'jais65142@gmail.com','Jay Sharma','1001','A','9420829593');
INSERT INTO `secretary` (`Sid`, `Susername`, `Spassword`,`Scode`, `Semail`,`Sname`,`Sflatno`,`Swing`,`Smobile`) VALUES (2, 'shinde', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'jay.sharma@matoshri.edu.in','Shivnath Sahebrao Shinde','1','B','9420829593');
alter table secretary auto_increment = 3;
select * from secretary;

CREATE TABLE IF NOT EXISTS `member` (
	`Mid` int(11) NOT NULL AUTO_INCREMENT,
  	`Musername` varchar(50) NOT NULL,
  	`Mpassword` varchar(255) NOT NULL,
  	`Mcode` varchar(30) NOT NULL,
	`Memail` varchar(100) NOT NULL UNIQUE,
  	`Mname` varchar(255) NOT NULL,
  	`Mflatno` int(20) NOT NULL,
  	`Mwing` varchar(50) NOT NULL,
  	`Mmobile` varchar(255) NOT NULL,
    `member_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`member_status` varchar(255) default 'request',
    PRIMARY KEY (`Mid`, `Musername`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('1', 'aashutosh', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'GOKU11', 'aashutoshmali1460@gmail.com','Aashutosh Mali','1002','A','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('2', 'dyaneshwar', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'aashutosh.mali@matoshri.edu.in','dyaneshwar Rangnath Vadnere','2','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('3', 'ashvini', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem3@gmail.com','Ashvini Sagar Dighe','3','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('4', 'chandrashekhar', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem4@gmail.com','Chandrashekhar Bhikchand Joshi','4','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('5', 'ashok', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem5@gmail.com','Ashok Subhash Kolhe','5','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('6', 'kalpana', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem6@gmail.com','Kalpana Shibaji Mali','6','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('7', 'sachin', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem7@gmail.com','Sachin Yashwant Shiral','7','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('8', 'sangita', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem8@gmail.com','Sangita Vinay Virari','8','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('9', 'nishant', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem9@gmail.com','Nishant Dhiren Loyada','9','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('10', 'vishvanath', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem19@gmail.com','Vishwanath Baburao Tayde','10','B','9922338265');
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('11', 'sharad', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'SAIR11', 'mem11@gmail.com','Sharad Damu Borase','11','B','9922338265');
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
  	`socrule` varchar(2000),
	`mainrule` varchar(2000),
	`kyc_file` varchar(255),
    `society_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`society_status` varchar(255) default 'request',
    PRIMARY KEY (`id`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `society` (`id`, `code`, `name`,`city`, `road`,`area`,`state`,`pin`,`acname`,`acno`,`mmid`,`bankname`,`branch`,`ifsc`,`socrule`,`mainrule`,`kyc_file`) VALUES (1, 'GOKU11', 'Gokuldham Society', 'Goregaon East', 'Powder Gali','Goregaon','Maharastra','422001','Gokuldham CO OP Hsg Society','85858858585858','5155755','DBS Bank','Singapour','SBIN0006333','Sample Society Rules','Sample Maintanance Rules','path');
INSERT INTO `society` (`id`, `code`, `name`,`city`, `road`,`area`,`state`,`pin`,`acname`,`acno`,`mmid`,`bankname`,`branch`,`ifsc`,`socrule`,`mainrule`,`kyc_file`) VALUES (2, 'SAIR11', 'Sai Residency', 'Nasik', 'Gajpanth','Mhasrul','Maharastra','422003','Sai Residency Account','5454545455454545','2525255','Bank of Maharastra','Panchvati','DBSS0IN0811','Sample Society Rules','Sample Maintanance Rules','path');
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
	`staff_code` varchar(30) NOT NULL,
    `staff_status` varchar(255) default 'active',
  	PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `staff` (`staff_id`, `staff_username`, `staff_password`,`staff_name`, `staff_mobile`, `staff_code`) VALUES ('1', 'samadhan', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Samadhan', '9515645454', 'GOKU11');
INSERT INTO `staff` (`staff_id`, `staff_username`, `staff_password`,`staff_name`, `staff_mobile`, `staff_code`) VALUES ('2', 'sitaram', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'Sitaram Narayan Kapadnis', '945121415', 'SAIR11');
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

CREATE TABLE IF NOT EXISTS `notice` (
	`notice_id` int(11) NOT NULL AUTO_INCREMENT,
	`notice_message` varchar(500) NOT NULL,
	`notice_code` varchar(30) NOT NULL,
    `notice_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`notice_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `notice` (`notice_id`, `notice_message`, `notice_code`) VALUES ('1', 'Test Notice Message', 'GOKU11');
INSERT INTO `notice` (`notice_id`, `notice_message`, `notice_code`) VALUES ('2', 'Test Notice Message', 'SAIR11');
alter table notice auto_increment = 3;
select * from notice;