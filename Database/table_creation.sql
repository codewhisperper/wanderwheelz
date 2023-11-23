-- Creating rentee_verification table
CREATE TABLE rentee_verification (
    rentee_verification_id INT AUTO_INCREMENT PRIMARY KEY,
    identification VARCHAR(255),
    license VARCHAR(255),
    insurance VARCHAR(255),
    verification_status BOOLEAN
);

-- Creating rentee table
CREATE TABLE rentee (
    rentee_id INT AUTO_INCREMENT PRIMARY KEY,
    rentee_verification_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(320), -- Adjusted for longer email addresses
    password VARCHAR(255), -- Assuming you store hashed passwords
    phone VARCHAR(15),
    FOREIGN KEY (rentee_verification_id) REFERENCES rentee_verification(rentee_verification_id)
);

-- Creating renter_verification table
CREATE TABLE renter_verification (
    renter_verification_id INT AUTO_INCREMENT PRIMARY KEY,
    identification VARCHAR(255),
    license VARCHAR(255),
    insurance VARCHAR(255),
    registration VARCHAR(255),
    verification_status BOOLEAN
);

-- Creating renter table
CREATE TABLE renter (
    renter_id INT AUTO_INCREMENT PRIMARY KEY,
    renter_verification_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(320), -- Adjusted for longer email addresses
    password VARCHAR(255), -- Assuming you store hashed passwords
    phone VARCHAR(15),
    FOREIGN KEY (renter_verification_id) REFERENCES renter_verification(renter_verification_id)
);

-- Creating admin table
CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255), -- Assuming you store hashed passwords
    name VARCHAR(255),
    contact VARCHAR(15),
);

-- Creating ride table
CREATE TABLE ride (
    ride_id INT AUTO_INCREMENT PRIMARY KEY,
    renter_id INT,
    ride_verification_id INT,
    availability_from DATETIME,
	availability_to DATETIME,
    model VARCHAR(255),
    number_plate VARCHAR(20),
    rate DECIMAL(5, 2),
    capacity INT,
    color VARCHAR(255),
    branch VARCHAR(255),
    description TEXT,
    city VARCHAR(255),
    Car_image VARCHAR(255),
    FOREIGN KEY (renter_id) REFERENCES renter(renter_id)
);

-- Creating rental table
CREATE TABLE rental (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,
    ride_id INT,
    rentee_id INT,
    rental_name VARCHAR(255),
    date DATETIME,
    FOREIGN KEY (ride_id) REFERENCES ride(ride_id),
    FOREIGN KEY (rentee_id) REFERENCES rentee(rentee_id)
);

-- Creating ride_review table
CREATE TABLE ride_review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
	ride_id INT,
    date DATETIME,
    car_score DECIMAL(5, 2),
    rate DECIMAL(5, 2), -- Adjusted precision and scale
    driver_score DECIMAL(5, 2),
    description TEXT,
    FOREIGN KEY (ride_id) REFERENCES ride(ride_id),
);
