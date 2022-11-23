-- MySQL Script generated by MySQL Workbench
-- Sun Jan  9 18:44:41 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`stations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`stations` (
  `stationid` INT NOT NULL,
  `location` VARCHAR(48) NULL,
  `geo_point_2d` VARCHAR(45) NULL,
  PRIMARY KEY (`stationid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`readings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`readings` (
  `readingid` INT NOT NULL,
  `datetime` DATETIME NULL,
  `nox` FLOAT NOT NULL,
  `no2` FLOAT NULL,
  `no` FLOAT NULL,
  `pm10` FLOAT NULL,
  `nvpm10` FLOAT NULL,
  `vpm10` FLOAT NULL,
  `mvpm2.5` FLOAT NULL,
  `pm2.5` FLOAT NULL,
  `vpm2.5` FLOAT NULL,
  `co` FLOAT NULL,
  `o3` FLOAT NULL,
  `so2` FLOAT NULL,
  `temperature` REAL NULL,
  `rh` INT NULL,
  `airpressure` INT NULL,
  `datestart` DATETIME NULL,
  `dateend` DATETIME NULL,
  `current` TEXT(5) NULL,
  `instrumenttype` VARCHAR(32) NULL,
  `stationid` INT NULL,
  PRIMARY KEY (`readingid`, `nox`),
  INDEX `fk_stationid_idx` (`stationid` ASC) VISIBLE,
  CONSTRAINT `fk_stationid`
    FOREIGN KEY (`stationid`)
    REFERENCES `mydb`.`stations` (`stationid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`schema`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`schema` (
  `measure` VARCHAR(32) NULL,
  `description` VARCHAR(64) NULL,
  `unit` VARCHAR(24) NULL)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
