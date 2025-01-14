
IF EXISTS (SELECT * FROM sys.schemas WHERE name = 'CW2')
    DROP SCHEMA CW2;
GO

CREATE SCHEMA CW2;
GO

-- Create "CW2" Tables
CREATE TABLE CW2.TRAIL (
    TrailID INT PRIMARY KEY,
    Trail_name VARCHAR(255),
    Trail_Summary VARCHAR(255),
    Trail_Description TEXT,
    Difficulty VARCHAR(50),
    Location VARCHAR(255),
    Length DECIMAL(10, 2),
    Elevation_gain INT,
    Route_type VARCHAR(50),
    OwnerID INT,
    Pt1_Lat DECIMAL(10, 6),
    Pt1_Long DECIMAL(10, 6),
    Pt1_Desc VARCHAR(255),
    Pt2_Lat DECIMAL(10, 6),
    Pt2_Long DECIMAL(10, 6),
    Pt2_Desc VARCHAR(255)
);

CREATE TABLE CW2.FEATURE (
    Trail_FeatureID INT PRIMARY KEY,
    Trail_Feature VARCHAR(255)
);

CREATE TABLE CW2.TRAIL_FEATURE (
    TrailID INT,
    Trail_FeatureID INT,
    FOREIGN KEY (TrailID) REFERENCES CW2.TRAIL(TrailID),
    FOREIGN KEY (Trail_FeatureID) REFERENCES CW2.FEATURE(Trail_FeatureID)
);

CREATE TABLE CW2.USERS (
    UserID INT PRIMARY KEY,
    Email_address VARCHAR(255),
    Role VARCHAR(50)
);

INSERT INTO CW2.TRAIL(TrailID, Trail_name, Trail_Summary, Trail_Description, Difficulty, [Location], Length, Elevation_gain, Route_type,OwnerID, Pt1_Lat,Pt1_Long,Pt1_Desc,Pt2_Lat,Pt2_Long,Pt2_Desc) 
VALUES
    (1, 'Monmouth Loop', 'A scenic loop trail with river views.', 'Explore the beautiful Wye Valley on this moderately challenging loop trail.', 'Moderate', 'Monmouth, Monmouthshire', 8.1, 1312, 'Loop', NULL, 51.80195, -2.271887, 'Start of the trail', 51.80195, -2.271887, 'End of the trail'),
    (2, 'Easy Trail', 'A gentle walk with stunning scenery.', 'Enjoy a leisurely stroll through the picturesque countryside.', 'Easy', 'Monmouth, Monmouthshire', 5.0, 179, 'Loop', NULL, 51.75629, -2.72493, 'Start of the trail', 51.75629, -2.72493, 'End of the trail'),
    (3, 'Woodland Walk', 'A peaceful walk through the woods.', 'Discover a tranquil woodland path with scenic viewpoints.', 'Moderate', 'Monmouth, Monmouthshire', 6.9, 222, 'Loop', NULL, 51.72311, -2.96195, 'Start of the trail', 51.72311, -2.96195, 'End of the trail');


INSERT INTO CW2.TRAIL_FEATURE (TrailID, Trail_FeatureID)
VALUES
    (1, 1),
    (1, 2),
    (2, 1),
    (3, 3);

INSERT INTO CW2.FEATURE (Trail_FeatureID, Trail_Feature)
VALUES
    (1, 'River Views'),
    (2, 'Historic Sites'),
    (3, 'Woodland Path');

INSERT INTO CW2.USERS (UserID, Email_address, Role)
VALUES
    (1, 'user1@example.com', 'User'),
    (2, 'admin@example.com', 'Administrator');
GO


CREATE PROCEDURE CW2.CreateTrail
    @TrailID INT,
    @Trail_name NVARCHAR(255),
    @Trail_Summary NVARCHAR(255),
    @Trail_Description NVARCHAR(MAX),
    @Difficulty NVARCHAR(50),
    @Location NVARCHAR(255),
    @Length FLOAT,
    @Elevation_gain INT,
    @Route_type NVARCHAR(50),
    @OwnerID INT,
    @Pt1_Lat FLOAT,
    @Pt1_Long FLOAT,
    @Pt1_Desc NVARCHAR(255),
    @Pt2_Lat FLOAT,
    @Pt2_Long FLOAT,
    @Pt2_Desc NVARCHAR(255)
AS
BEGIN
    INSERT INTO CW2.TRAIL (
        TrailID,
        Trail_name, 
        Trail_Summary, 
        Trail_Description, 
        Difficulty, 
        Location, 
        Length, 
        Elevation_gain, 
        Route_type, 
        OwnerID,
        Pt1_Lat,
        Pt1_Long,
        Pt1_Desc,
        Pt2_Lat,
        Pt2_Long,
        Pt2_Desc
    )
    VALUES (
        @TrailID,
        @Trail_name, 
        @Trail_Summary, 
        @Trail_Description, 
        @Difficulty, 
        @Location, 
        @Length, 
        @Elevation_gain, 
        @Route_type, 
        @OwnerID,
        @Pt1_Lat,
        @Pt1_Long,
        @Pt1_Desc,
        @Pt2_Lat,
        @Pt2_Long,
        @Pt2_Desc
    );
END;


