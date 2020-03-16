//  CREATE TABLE :- //

CREATE TABLE BASIC_INFO (
    SR_NO INT(3) UNIQUE , 
    USER_ID VARCHAR(60) UNIQUE ,
    FIRST_NAME VARCHAR(120) NOT NULL ,
    LAST_NAME VARCHAR(120) NOT NULL ,
    GENDER VARCHAR(4) NOT NULL , 
    PREG VARCHAR(1) NOT NULL , 
    LOCATION VARCHAR(120) NOT NULL ,
    TEMP DECIMAL(6,3) NOT NULL ,
    COUGH VARCHAR(1) NOT NULL , 
    SHORT_BREATH VARCHAR(1) NOT NULL ,
    RUNNING_NOSE VARCHAR(1) NOT NULL , 
    COUNT INT(3)  DEFAULT 0, 
    ZONE VARCHAR(1) ,
    AFFECT VARCHAR(1) 
); SELECT * FROM BASIC_INFO;
        - - - - - - - - - - - - - - - - - - - - - - - - - -

//  INSERT VALUES: // 
// JUST CHANGE THE VALUES INSIDE TO INSERT MULTIPLE TIMES. //

INSERT INTO BASIC_INFO 
VALUES
(1,'1826228','ABHIRAJ','KALE','M','N','192.12.1.13',102.3,'Y','Y','Y',0,'');
SELECT * FROM BASIC_INFO;

        - - - - - - - - - - - - - - - - - - - - - - - - - -

// UPDATE COUNT VALUE 

// SETTING INITIAL COUNT ACCORDING TO TEMPERATURE

UPDATE BASIC_INFO SET COUNT = 0 
WHERE (TEMP<99);
UPDATE BASIC_INFO SET COUNT = 20    
WHERE (TEMP>99 AND TEMP<102);      
UPDATE BASIC_INFO SET COUNT = 40 
WHERE (TEMP>102);
SELECT * FROM BASIC_INFO;

        - - - - - - - - - - - - - - - - - - - - - - - - - -

// INCREASING COUNT VALUE BASED ON SYMPTOMS //

// IF ANY 1 SYMPTOM SHOWS 'Y' INCREASE 20 

UPDATE BASIC_INFO SET COUNT = COUNT + 20 
WHERE    
COUGH='Y' OR RUNNING_NOSE='Y' OR SHORT_BREATH='Y';

// IF ANY 2 SYMPTOMS SHOW 'Y' INCREASE 20 

UPDATE BASIC_INFO SET COUNT = COUNT + 20 
WHERE    
(
(COUGH='Y' AND SHORT_BREATH='Y' ) OR
(COUGH='Y' AND RUNNING_NOSE='Y') OR
(SHORT_BREATH='Y' AND RUNNING_NOSE='Y') 
);

// IF ALL 3 SYMPTOMS SHOW 'Y' INCREASE 20

UPDATE BASIC_INFO SET COUNT = COUNT + 20 
WHERE    
(
(COUGH='Y' AND SHORT_BREATH='Y' AND RUNNING_NOSE='Y') OR
(COUGH='Y' AND RUNNING_NOSE='Y' AND SHORT_BREATH='Y') OR
(SHORT_BREATH='Y' AND RUNNING_NOSE='Y' AND COUGH='Y') 
);
SELECT * FROM BASIC_INFO;

        - - - - - - - - - - - - - - - - - - - - - - - - - -

// CREATE PERCENTAGE OF PROBABILITY

ALTER TABLE BASIC_INFO
ADD COLUMN PERCENTAGE VARCHAR(10);
UPDATE BASIC_INFO
SET PERCENTAGE = CONCAT(COUNT,' ','%');  

        - - - - - - - - - - - - - - - - - - - - - - - - - -


//  SET ZONES :- //

UPDATE BASIC_INFO SET ZONE='G' 
WHERE COUNT=0; 
UPDATE BASIC_INFO SET ZONE='Y' 
WHERE ( COUNT>=20 AND COUNT<40);
UPDATE BASIC_INFO SET ZONE='R' 
WHERE COUNT>=40;
SELECT * FROM BASIC_INFO;


-- CREATE VIEW OF GREEN ZONE:- 

CREATE VIEW GREEN_ZONE AS
SELECT SR_NO,USER_ID,FIRST_NAME,LAST_NAME,GENDER,TEMP,ZONE
FROM BASIC_INFO
WHERE ZONE='G';

--  CREATE VIEW OF YELLOW ZONE:- 

CREATE VIEW YELLOW_ZONE AS
SELECT SR_NO,USER_ID,FIRST_NAME,LAST_NAME,GENDER,TEMP,ZONE
FROM BASIC_INFO
WHERE ZONE='Y';

--  CREATE VIEW OF RED ZONE:- 

CREATE VIEW RED_ZONE AS
SELECT SR_NO,USER_ID,FIRST_NAME,LAST_NAME,GENDER,LOCATION,TEMP,ZONE
FROM BASIC_INFO
WHERE ZONE='R';

-- LIKELY TO AFFECT PATIENTS
    UPDATE BASIC_INFO SET AFFECT = 'Y' 
    WHERE  LOCATION IN (SELECT LOCATION FROM BASIC_INFO WHERE ZONE != 'R') = LOCATION IN (SELECT LOCATION FROM RED_ZONE);


    


