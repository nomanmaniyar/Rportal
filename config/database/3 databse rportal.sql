CREATE DATABASE IF NOT EXISTS `rportal` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `rportal`;

CREATE TABLE IF NOT EXISTS `secretary` (
	`Sid` int(11) NOT NULL AUTO_INCREMENT,
  	`Susername` varchar(50) NOT NULL,
  	`Spassword` varchar(255) NOT NULL,
  	`Scode` varchar(30) NOT NULL,
	`Semail` varchar(100) NOT NULL,
  	`Sname` varchar(255) NOT NULL,
  	`Sflatno` int(20) NOT NULL,
  	`Swing` varchar(50) NOT NULL,
  	`Smobile` varchar(255) NOT NULL,
    PRIMARY KEY (`Sid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
ALTER TABLE secretary ADD CONSTRAINT UNIQUE (semail);
INSERT INTO `secretary` (`Sid`, `Susername`, `Spassword`,`Scode`, `Semail`,`Sname`,`Sflatno`,`Swing`,`Smobile`) VALUES (1, 'stest', 'stestpw', 'ZZZZ55', 'jais65142@gmail.com','sec test','1001','A','9420829593');
select * from secretary;

CREATE TABLE IF NOT EXISTS `member` (
	`Mid` int(11) NOT NULL AUTO_INCREMENT,
  	`Musername` varchar(50) NOT NULL,
  	`Mpassword` varchar(255) NOT NULL,
  	`Mcode` varchar(30) NOT NULL,
	`Memail` varchar(100) NOT NULL,
  	`Mname` varchar(255) NOT NULL,
  	`Mflatno` int(20) NOT NULL,
  	`Mwing` varchar(50) NOT NULL,
  	`Mmobile` varchar(255) NOT NULL,
    PRIMARY KEY (`Mid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
ALTER TABLE member ADD CONSTRAINT UNIQUE (Memail);
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('1', 'mtest', 'mtestpw', 'ZZZZ55', 'aashutoshmali1460@gmail.com','mem test','2002','A','9922338265');
select * from member;

CREATE TABLE IF NOT EXISTS `society` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`code` varchar(30) NOT NULL,
  	`name` varchar(50) NOT NULL,
	`city` varchar(50) NOT NULL,
	`road` varchar(255) NOT NULL,
  	`area` varchar(30) NOT NULL,
	`state` varchar(100) NOT NULL,
  	`pin` int(15) NOT NULL,
  	`acname` varchar(255) NOT NULL,
  	`acno` varchar(200) NOT NULL,
  	`mmid` varchar(50) NOT NULL,
  	`bankname` varchar(255) NOT NULL,
    `branch` varchar(200) NOT NULL,
  	`ifsc` varchar(255) NOT NULL,
  	`socrule` varchar(2000),
	`mainrule` varchar(2000),
	`kyc_file` varchar(255),
    PRIMARY KEY (`id`,`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
ALTER TABLE society ADD CONSTRAINT UNIQUE (code);
INSERT INTO `society` (`id`, `code`, `name`,`city`, `road`,`area`,`state`,`pin`,`acname`,`acno`,`mmid`,`bankname`,`branch`,`ifsc`,`socrule`,`mainrule`,`kyc_file`) VALUES (2, 'ZZZZ56', 'SOciety', 'east', 'gali','gaon','rastra','4223','op','8265','515','footi bank','sa','aaja',NULL,NULL,'path');
select * from society;

alter table staff auto_increment = 2;
SELECT * FROM member INNER JOIN society ON member.Mcode = society.code INNER JOIN secretary ON member.Mcode = secretary.Scode;
SET GLOBAL sql_mode = '';
SELECT Musername, Mpassword, Memail, Mname, Mflatno, Mwing, Mmobile, code, name, city, road, area, state, pin FROM member INNER JOIN society ON member.Mcode = society.code WHERE Mid = 1;


CREATE TABLE IF NOT EXISTS `admin` (
	`Aid` int(11) NOT NULL AUTO_INCREMENT,
	`Ausername` varchar(255) NOT NULL,
  	`Apassword` varchar(255) NOT NULL,
	`Aemail` varchar(100),
  	PRIMARY KEY (`Aid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
INSERT INTO `admin` (`Aid`, `Ausername`, `Apassword`,`Aemail`) VALUES ('1', 'ajinfotics', '65142', NULL);
select * from admin;

CREATE TABLE IF NOT EXISTS `security` (
	`security_id` int(11) NOT NULL AUTO_INCREMENT,
	`security_username` varchar(255) NOT NULL,
  	`security_password` varchar(255) NOT NULL,
	`security_name` varchar(255) NOT NULL,
	`security_mobile` varchar(255) NOT NULL,
	`security_code` varchar(30) NOT NULL,
    `security_status` varchar(255) default 'false',
  	PRIMARY KEY (`security_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
INSERT INTO `security` (`security_id`, `security_username`, `security_password`,`security_name`, `security_mobile`, `security_code`) VALUES ('1', 'noman', '1234', 'Noman', '5154545', 'ZZZZ55');
select * from security;

CREATE TABLE IF NOT EXISTS `staff` (
	`staff_id` int(11) NOT NULL AUTO_INCREMENT,
	`staff_username` varchar(255) NOT NULL,
  	`staff_password` varchar(255) NOT NULL,
	`staff_name` varchar(255) NOT NULL,
	`staff_mobile` varchar(255) NOT NULL,
	`staff_code` varchar(30) NOT NULL,
    `staff_status` varchar(255) default 'false',
  	PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
INSERT INTO `staff` (`staff_id`, `staff_username`, `staff_password`,`staff_name`, `staff_mobile`, `staff_code`) VALUES ('1', 'samadhan', '1234', 'Samadhan', '5154545', 'ZZZZ55');
select * from staff;