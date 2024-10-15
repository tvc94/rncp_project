USE watches_website;

CREATE TABLE Certified_Pre_Owned (
    ID INT PRIMARY KEY,
    Description VARCHAR(255)
);

INSERT INTO Certified_Pre_Owned (ID, Description) VALUES
(0, 'Not Certified Pre-Owned'),
(1, 'Certified Pre-Owned');

CREATE TABLE Special_Edition (
    ID INT PRIMARY KEY,
    Description VARCHAR(255)
);

INSERT INTO Special_Edition (ID, Description) VALUES
(0, 'Not Special Edition'),
(1, 'Special Edition');

CREATE TABLE Availability (
    ID INT PRIMARY KEY,
    Description VARCHAR(255)
);

INSERT INTO Availability (ID, Description) VALUES
(0, 'Not Available'),
(1, 'In Stock');


ALTER TABLE `watches_website`.`Watches`
ADD CONSTRAINT `fk_Certified_Pre_Owned`
  FOREIGN KEY (`Certified_Pre_Owned_ID`)  -- Local column in Watches
  REFERENCES `watches_website`.`Certified_Pre_Owned`(`ID`)  -- Referenced column in Certified_Pre_Owned
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
DESCRIBE Watches;
DESCRIBE Certified_Pre_Owned;
ALTER TABLE Watches
MODIFY Certified_Pre_Owned_ID INT;

ALTER TABLE `watches_website`.`Watches`
ADD CONSTRAINT `fk_Certified_Pre_Owned`
  FOREIGN KEY (`Certified_Pre_Owned_ID`)
  REFERENCES `watches_website`.`Certified_Pre_Owned`(`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  ALTER TABLE Watches
MODIFY Special_Edition_ID INT;

ALTER TABLE Watches
MODIFY Availability_ID INT;

ALTER TABLE `watches_website`.`Watches`
ADD CONSTRAINT `fk_Special_Edition`
  FOREIGN KEY (`Special_Edition_ID`)
  REFERENCES `watches_website`.`Special_Edition`(`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
  ALTER TABLE `watches_website`.`Watches`
ADD CONSTRAINT `fk_Availability`
  FOREIGN KEY (`Availability_ID`)
  REFERENCES `watches_website`.`Availability`(`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
