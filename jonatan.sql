-- PostgreSQL syntax
DROP TABLE IF EXISTS Classes;
DROP TABLE IF EXISTS Teachers;
DROP TYPE IF EXISTS dayOFWeek;
CREATE TABLE Teachers (
    teacherID INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255),
    office VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    PRIMARY KEY(teacherID)
);
CREATE TYPE dayOfWeek AS ENUM ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday');
CREATE TABLE Classes (
    classID INT GENERATED ALWAYS AS IDENTITY,
    courseCode VARCHAR(5),
    dayOfWeek dayOfWeek,
    timeStart TIME,
    timeEnd TIME,
    teacherID INT,
    PRIMARY KEY(classID),
    CONSTRAINT fkTeacher FOREIGN KEY(teacherID) REFERENCES Teachers(teacherID)
);
INSERT INTO Teachers (teacherID, name) VALUES (1, 'Jonatan');
INSERT INTO Classes (courseCode, dayOfWeek, timeStart, timeEnd, teacherID) VALUES
                    ('SQL01', 'Monday', '9:00', '11:00', 1),
                    ('DEC55', 'Wednesday', '16:00', '18:00', 1),
                    ('PYT99', 'Friday', '9:00', '11:00', 1);
SELECT Teachers.name AS Teacher,
       Classes.courseCode AS CourseCode,
       Classes.dayOfWeek AS Day,
       Classes.timeStart AS Start,
       Classes.timeEnd AS End
    FROM Teachers
    JOIN Classes ON Teachers.teacherID = Classes.teacherID
    WHERE Teachers.name = 'Jonatan';
