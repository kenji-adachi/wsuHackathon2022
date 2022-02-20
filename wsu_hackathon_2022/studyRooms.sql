
CREATE TABLE building (
    buildingName VARCHAR(50) PRIMARY KEY
);

CREATE TABLE building_hours (
    buildingName VARCHAR(50) PRIMARY KEY,
    weekhoursopen TIME,
    weekhoursclose TIME,
    weekendhoursopen TIME,
    weekendhoursclose TIME,
    FOREIGN KEY (buildingName) REFERENCES building(buildingName)
);

CREATE TABLE room (
    roomNumber VARCHAR(8),
    pop INTEGER,
    roomDescription VARCHAR(255),
    buildingName VARCHAR(50),
    PRIMARY KEY (roomNumber, buildingName),
    FOREIGN KEY (buildingName) REFERENCES building(buildingName)
);

CREATE TABLE reservations (
    roomNumber VARCHAR(8),
    buildingName VARCHAR(50),
    startTime TIME,
    endTime TIME,
    PRIMARY KEY (roomNumber, buildingName),
    FOREIGN KEY (roomNumber, buildingName) REFERENCES room(roomNumber,buildingName)
);

CREATE TABLE tags (
    roomNumber VARCHAR(8),
    buildingName VARCHAR(50),
    tagName VARCHAR(15),
    PRIMARY KEY (roomNumber, buildingName),
    FOREIGN KEY (roomNumber, buildingName) REFERENCES room(roomNumber,buildingName)
);