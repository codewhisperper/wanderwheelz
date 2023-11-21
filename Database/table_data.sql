INSERT INTO rentee_verification (identification, license, insurance, verification_status)
VALUES
    ('ID123456', 'DL789012', 'INS456789', TRUE),
    ('ID789012', 'DL345678', 'INS123456', TRUE),
    ('ID234567', 'DL567890', 'INS789012', FALSE),
    ('ID567890', 'DL123456', 'INS234567', TRUE),
    ('ID345678', 'DL678901', 'INS345678', FALSE);

INSERT INTO rentee (rentee_verification_id, first_name, last_name, email, password, phone)
VALUES
    (1, 'John', 'Doe', 'john.doe@email.com', 'hashedpassword1', '123-456-7890'),
    (2, 'Jane', 'Smith', 'jane.smith@email.com', 'hashedpassword2', '987-654-3210'),
    (3, 'Bob', 'Johnson', 'bob.johnson@email.com', 'hashedpassword3', '456-789-0123'),
    (4, 'Alice', 'Williams', 'alice.williams@email.com', 'hashedpassword4', '789-012-3456'),
    (5, 'Charlie', 'Brown', 'charlie.brown@email.com', 'hashedpassword5', '234-567-8901');


INSERT INTO renter_verification (identification, license, insurance, registration, verification_status)
VALUES
    ('ID987654', 'DL901234', 'INS901234', 'REG567890', TRUE),
    ('ID345678', 'DL678901', 'INS345678', 'REG123456', FALSE),
    ('ID567890', 'DL123456', 'INS234567', 'REG789012', TRUE),
    ('ID234567', 'DL567890', 'INS789012', 'REG345678', TRUE),
    ('ID789012', 'DL345678', 'INS123456', 'REG901234', FALSE);

INSERT INTO renter (renter_verification_id, first_name, last_name, email, password, phone)
VALUES
    (1, 'Michael', 'Jordan', 'michael.jordan@email.com', 'hashedpassword6', '111-222-3333'),
    (2, 'LeBron', 'James', 'lebron.james@email.com', 'hashedpassword7', '444-555-6666'),
    (3, 'Kobe', 'Bryant', 'kobe.bryant@email.com', 'hashedpassword8', '777-888-9999'),
    (4, 'Stephen', 'Curry', 'stephen.curry@email.com', 'hashedpassword9', '123-456-7890'),
    (5, 'Kevin', 'Durant', 'kevin.durant@email.com', 'hashedpassword10', '987-654-3210');


INSERT INTO admin (username, password, name, contact)
VALUES
    ('admin1', 'adminpassword1', 'Admin One', '123-456-7890'),
    ('admin2', 'adminpassword2', 'Admin Two', '987-654-3210'),
    ('admin3', 'adminpassword3', 'Admin Three', '456-789-0123'),
    ('admin4', 'adminpassword4', 'Admin Four', '789-012-3456'),
    ('admin5', 'adminpassword5', 'Admin Five', '234-567-8901');

INSERT INTO ride (renter_id, ride_verification_id, availability_from, availability_to, model, number_plate, rate, capacity, color, branch, description)
VALUES
    (1, 1, '2023-11-18 08:00:00', '2023-11-18 18:00:00', 'Toyota Camry', 'ABC123', 50.00, 4, 'Blue', 'Main Branch', 'Comfortable sedan'),
    (2, 3, '2023-11-19 10:00:00', '2023-11-19 20:00:00', 'Honda Accord', 'XYZ789', 45.00, 5, 'Red', 'Downtown Branch', 'Spacious and stylish'),
    (4, 2, '2023-11-20 12:00:00', '2023-11-20 22:00:00', 'Ford Mustang', 'DEF456', 70.00, 2, 'Yellow', 'Suburb Branch', 'Sporty and fast'),
    (3, 4, '2023-11-21 14:00:00', '2023-11-21 23:59:59', 'Chevrolet Suburban', 'GHI789', 90.00, 7, 'Black', 'Main Branch', 'Spacious SUV for family trips'),
    (5, 5, '2023-11-22 16:00:00', '2023-11-22 23:00:00', 'Tesla Model S', 'JKL012', 100.00, 4, 'Silver', 'Downtown Branch', 'Luxury electric car');

INSERT INTO rental (ride_id, rentee_id, rental_name, date)
VALUES
    (1, 2, 'Business Trip', '2023-11-18 12:00:00'),
    (2, 3, 'Weekend Getaway', '2023-11-19 15:30:00'),
    (3, 4, 'Date Night', '2023-11-20 18:45:00'),
    (4, 5, 'Family Vacation', '2023-11-21 21:00:00'),
    (5, 1, 'Special Occasion', '2023-11-22 19:30:00');

INSERT INTO ride_review (ride_id, date, car_score, rate, driver_score, description)
VALUES
    (1, '2023-11-18 14:30:00', 4.5, 4.5, 5, 'Smooth ride, friendly renter'),
    (2, '2023-11-19 18:00:00', 5.0, 5.0, 4.8, 'Clean and comfortable car, punctual renter'),
    (3, '2023-11-20 21:15:00', 3.5, 3.5, 3.8, 'Car had some issues, but renter was helpful'),
    (4, '2023-11-21 23:30:00', 4.5, 4.0, 4.5, 'Spacious and comfortable for family trip'),
    (5, '2023-11-22 20:00:00', 5.0, 4.8, 5.0, 'Luxurious experience with the Tesla Model S');
