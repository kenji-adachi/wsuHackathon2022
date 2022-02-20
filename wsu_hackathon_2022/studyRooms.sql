
CREATE TABLE building (
    buildingname VARCHAR(50) PRIMARY KEY
);

CREATE TABLE building_hours (
    buildingname VARCHAR(50) PRIMARY KEY,
    weekhoursopen TIME,
    weekhoursclose TIME,
    weekendhoursopen TIME,
    weekendhoursclose TIME,
    FOREIGN KEY (buildingname) REFERENCES building(buildingname)
);

CREATE TABLE room (
    roomnumber VARCHAR(8),
    pop INTEGER,
    roomdescription VARCHAR(255),
    buildingName VARCHAR(50),
    PRIMARY KEY (roomnumber, buildingname),
    FOREIGN KEY (buildingname) REFERENCES building(buildingname)
);

CREATE TABLE reservations (
    roomnumber VARCHAR(8),
    buildingname VARCHAR(50),
    starttime CHAR(21),
    endtime CHAR(21),
    roomstate INTEGER,
    PRIMARY KEY (roomnumber, buildingname),
    FOREIGN KEY (roomnumber, buildingname) REFERENCES room(roomnumber,buildingname)
);

CREATE TABLE tags (
    roomnumber VARCHAR(8),
    buildingname VARCHAR(50),
    tagname VARCHAR(15),
    PRIMARY KEY (roomnumber, buildingname),
    FOREIGN KEY (roomnumber, buildingname) REFERENCES room(roomnumber,buildingname)
);