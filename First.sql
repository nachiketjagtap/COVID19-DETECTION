CREATE TABLE BASICINFO ( USERID VARCHAR (7) PRIMARY KEY,
    USERNAME TEXT (50) NOT NULL ,
    IP_ADD VARCHAR (12) UNIQUE ,
    FEVER BIT(1) NOT NULL ,
    COUGH BIT(1) NOT NULL ,
    NOSE BIT(1) NOT NULL ,
    SHORT_BR BIT(1) NOT NULL ,
    FRG_TRV BIT(1) NOT NULL ,
    PREGNANT BIT(1) NOT NULL );
