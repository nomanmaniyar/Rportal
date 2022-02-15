CREATE DATABASE IF NOT EXISTS `rportal` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `rportal`;
SET GLOBAL sql_mode = '';
SET SQL_SAFE_UPDATES = 0;
set sql_mode="NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION";

CREATE TABLE IF NOT EXISTS `userdetails` (
	`uid` int NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
    `name` varchar(50) NOT NULL,
	`password` varchar(255) NOT NULL,
    `mobile` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL UNIQUE,
    `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`uid`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `secretary` (
	`Sid` int NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
  	`Scode` varchar(30) NOT NULL,
	`Semail` varchar(100) NOT NULL,
  	`Sname` varchar(255) NOT NULL,
  	`Sflatno` int NOT NULL,
  	`Swing` varchar(50) NOT NULL,
  	`Smobile` varchar(255) NOT NULL,
    `secretary_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`secretarty_status` varchar(255) default 'request',
    PRIMARY KEY (`Sid`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `member` (
	`Mid` int NOT NULL AUTO_INCREMENT,
	`username` varchar(50) NOT NULL,
  	`Mcode` varchar(30) NOT NULL,
	`Memail` varchar(100) NOT NULL ,
  	`Mname` varchar(255) NOT NULL,
  	`Mflatno` int NOT NULL,
  	`Mwing` varchar(50) NOT NULL,
  	`Mmobile` varchar(255) NOT NULL,
    `member_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	`member_status` varchar(255) default 'request',
    PRIMARY KEY (`Mid`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `society` (
	`id` int NOT NULL AUTO_INCREMENT,
	`code` varchar(30) NOT NULL UNIQUE,
  	`name` varchar(50) NOT NULL,
	`city` varchar(50) NOT NULL,
	`road` varchar(255) NOT NULL,
  	`area` varchar(30) NOT NULL,
	`state` varchar(100) NOT NULL,
  	`pin` int NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `admin` (
	`Aid` int NOT NULL AUTO_INCREMENT,
	`Ausername` varchar(255) NOT NULL,
  	`Apassword` varchar(255) NOT NULL,
	`Aemail` varchar(100),
  	PRIMARY KEY (`Aid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
INSERT INTO `admin` (`Aid`, `Ausername`, `Apassword`,`Aemail`) VALUES ('1', 'ajinfotics', '0252f322f644f82a06ff668230996a0a4ef2b90cc27fc61c9cd014febe6ec4a4', NULL);

CREATE TABLE IF NOT EXISTS `security` (
	`security_id` int NOT NULL AUTO_INCREMENT,
	`security_username` varchar(255) NOT NULL,
  	`security_password` varchar(255) NOT NULL,
	`security_name` varchar(255) NOT NULL,
	`security_mobile` varchar(255) NOT NULL,
	`security_code` varchar(30) NOT NULL,
    `security_status` varchar(255) default 'active',
  	PRIMARY KEY (`security_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `staff` (
	`staff_id` int NOT NULL AUTO_INCREMENT,
	`staff_username` varchar(255) NOT NULL,
  	`staff_password` varchar(255) NOT NULL,
	`staff_name` varchar(255) NOT NULL,
	`staff_mobile` varchar(255) NOT NULL,
    `post` varchar(255),
	`staff_code` varchar(30) NOT NULL,
    `staff_status` varchar(255) default 'active',
  	PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `contactus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `message` varchar(500) NOT NULL,
  `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `complaint` (
	`complaint_id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `notice` (
	`notice_id` int NOT NULL AUTO_INCREMENT,
	`notice_subject` varchar(500) NOT NULL,
	`notice_message` LONGTEXT NOT NULL,
	`notice_code` varchar(30) NOT NULL,
    `notice_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`notice_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `contact` (
	`contact_id` int NOT NULL AUTO_INCREMENT,
	`contact_label` VARCHAR(255) NOT NULL,
	`contact_no` bigint NOT NULL,
	`society_code` varchar(255) NOT NULL,
  	PRIMARY KEY (`contact_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `document` (
	`doc_id` int NOT NULL AUTO_INCREMENT,
	`doc_filename` varchar(255) NOT NULL,
	`society_code` varchar(255) NOT NULL,
    `document` varchar(255)NOT NULL,
  	PRIMARY KEY (`doc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `chat` (
	`msg_id` int NOT NULL AUTO_INCREMENT,
	`msg_username` varchar(255) NOT NULL,
	`message` LONGTEXT NOT NULL,
	`society_code` varchar(255) NOT NULL,
	`msg_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`msg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `maintenance` (
	`main_id` int NOT NULL AUTO_INCREMENT,
	`Musername` varchar(255),
	`Mname` varchar(255),
    `code` varchar(50),
	`bill_date` timestamp DEFAULT CURRENT_TIMESTAMP, 
    `due_date` date default (CONCAT(year(now()), '-12-31')),
    `amount` float,
    `pending_amount` float,
    `paid_date` timestamp,
    `payment_status` varchar(255) default 'unpaid',
  	PRIMARY KEY (`main_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `permission` (
	`pid` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`subject` varchar(255) NOT NULL,
	`text` varchar(355) NOT NULL,
	`pstatus` varchar(255) NOT NULL,
	`society_code` varchar(255) NOT NULL,
	`per_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `expense` (
	`exp_id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `date` DATE,
	`amount` float,
	`society_code` varchar(255) NOT NULL,
    `document` varchar(255),
  	PRIMARY KEY (`exp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;