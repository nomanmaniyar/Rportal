CREATE DATABASE IF NOT EXISTS `rportal` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `rportal`;

CREATE TABLE IF NOT EXISTS `secretary` (
	`Sid` int(11) NOT NULL AUTO_INCREMENT,
  	`Susername` varchar(50) NOT NULL,
  	`Spassword` varchar(255) NOT NULL,
  	`Scode` varchar(30) NOT NULL,
	`Semail` varchar(100) NOT NULL,
  	`Sotp` int(15) ,
  	`Sname` varchar(255) NOT NULL,
  	`Sflatno` int(20) NOT NULL,
  	`Swing` varchar(50) NOT NULL,
  	`Smobile` varchar(255) NOT NULL,
    PRIMARY KEY (`Sid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
ALTER TABLE secretary ADD CONSTRAINT UNIQUE (semail);
INSERT INTO `secretary` (`Sid`, `Susername`, `Spassword`,`Scode`, `Semail`,`Sotp`,`Sname`,`Sflatno`,`Swing`,`Smobile`) VALUES (1, 'stest', 'stestpw', 'ZZZZ55', 'jais65142@gmail.com',NULL,'sec test','1001','A','9420829593');
select * from secretary;

CREATE TABLE IF NOT EXISTS `member` (
	`Mid` int(11) NOT NULL AUTO_INCREMENT,
  	`Musername` varchar(50) NOT NULL,
  	`Mpassword` varchar(255) NOT NULL,
  	`Mcode` varchar(30) NOT NULL,
	`Memail` varchar(100) NOT NULL,
  	`Motp` int(15) ,
  	`Mname` varchar(255) NOT NULL,
  	`Mflatno` int(20) NOT NULL,
  	`Mwing` varchar(50) NOT NULL,
  	`Mmobile` varchar(255) NOT NULL,
    PRIMARY KEY (`Mid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
ALTER TABLE member ADD CONSTRAINT UNIQUE (Memail);
INSERT INTO `member` (`Mid`, `Musername`, `Mpassword`,`Mcode`, `Memail`,`Motp`,`Mname`,`Mflatno`,`Mwing`,`Mmobile`) VALUES ('1', 'mtest', 'mtestpw', 'ZZZZ55', 'aashutoshmali1460@gmail.com',NULL,'mem test','2002','A','9922338265');
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
    PRIMARY KEY (`id`,`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
ALTER TABLE society ADD CONSTRAINT UNIQUE (code);
INSERT INTO `society` (`id`, `code`, `name`,`city`, `road`,`area`,`state`,`pin`,`acname`,`acno`,`mmid`,`bankname`,`branch`,`ifsc`,`socrule`,`mainrule`) VALUES (2, 'ZZZZ56', 'SOciety', 'east', 'gali','gaon','rastra','4223','op','8265','515','footi bank','sa','aaja',NULL,NULL);
select * from society;

alter table society auto_increment = 2;
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
