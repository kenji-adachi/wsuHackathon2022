

CREATE TABLE Building (
    buildingName VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Room (
    roomNumber VARCHAR(8),
    pop INTEGER,
    roomState INTEGER,
    roomDescription VARCHAR(255),
    buildingName VARCHAR(50),
    PRIMARY KEY (roomNumber, buildingName),
    FOREIGN KEY (buildingName) REFERENCES building(buildingName)
);

CREATE TABLE Reservations (
    roomNumber VARCHAR(8),
    buildingName VARCHAR(50),
    startTime TIME,
    endTime TIME,
    PRIMARY KEY (roomNumber, buildingName),
    FOREIGN KEY (roomNumber, buildingName) REFERENCES room(roomNumber,buildingName)
);

CREATE TABLE Tags (
    roomNumber VARCHAR(8),
    buildingName VARCHAR(50),
    tagName VARCHAR(15),
    PRIMARY KEY (roomNumber, buildingName),
    FOREIGN KEY (roomNumber, buildingName) REFERENCES room(roomNumber,buildingName)
);