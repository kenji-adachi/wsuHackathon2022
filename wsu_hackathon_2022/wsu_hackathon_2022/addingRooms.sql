INSERT INTO building(buildingname)
VALUES ('Spark');

INSERT INTO building(buildingname)
VALUES ('EME');

INSERT INTO room(roomnumber,pop,roomdescription,buildingname)
VALUES ('101',5,'Sparky','Spark');

INSERT INTO room(roomnumber,pop,roomdescription,buildingname)
VALUES ('201',6,'Sparky too','Spark');

INSERT INTO room(roomnumber,pop,roomdescription,buildingname)
VALUES ('10',3,'Corner room','EME');

INSERT INTO building_hours(buildingname,weekhoursopen,weekhoursclose,weekendhoursopen,weekendhoursclose)
VALUES ('Spark', '7:00:00', '22:00:00','7:00:00','20:00:00');

INSERT INTO building_hours(buildingname,weekhoursopen,weekhoursclose,weekendhoursopen,weekendhoursclose)
VALUES ('EME', '10:00:00', '23:00:00','10:00:00','23:00:00');

INSERT INTO reservations(roomnumber,buildingname,starttime,endtime,roomstate)
VALUES ('101','Spark','10:00:00','11:00:00','0');

INSERT INTO tags(roomnumber,buildingname,tagname)
VALUES ('201','Spark','Fun');

