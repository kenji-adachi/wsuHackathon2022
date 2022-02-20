INSERT INTO building(buildingname)
VALUE ('Spark');

INSERT INTO building(buildingname)
VALUE ('EME');

INSERT INTO room(roomnumber,pop,roomdescription,buildingname)
VALUE ('101',5,'Sparky in here','Spark');

INSERT INTO room(roomnumber,pop,roomdescription,buildingname)
VALUE ('201',6,'Sparky in here too','Spark');

INSERT INTO room(roomnumber,pop,roomdescription,buildingname)
VALUE ('10',3,'Corner room','EME');

INSERT INTO building_hours(buildingname,weekhoursopen,weekhoursclose,weekendhoursopen,weekendhoursclose)
VALUE ('Spark', '7:00:00', '22:00:00','7:00:00','20:00:00');

INSERT INTO reservations(roomnumber,buildingname,starttime,endtime)
VALUE ('101','Spark','10:00:00','11:00:00');

INSERT INTO tags(roomnumber,buildingname,tagname)
VALUE ('201','Spark','Fun');

