-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 05, 2024 at 03:53 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `waterbillingsystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `firstname` varchar(200) NOT NULL,
  `lastname` varchar(200) NOT NULL,
  `accnumber` varchar(100) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`firstname`, `lastname`, `accnumber`, `username`, `password`) VALUES
('Savindu', 'Ruhunuhewa', '123/456/789/900', 'savinduruhunuhewa@gmail.com', '1234'),
('Gajindu', 'Bandara', '123/890/567/890', 'gaji@gmail.com', '8907'),
('Nilukshi', 'Anandan', '134/456/789/100', 'nilukshi123@gmail.com', 'nilukshi@123'),
('Ridmi', 'Yatigammana', '109/709/809/200', 'ridmi123@gmail.com', 'ridmi@456'),
('Prabu', 'Pemekumar', '109809/345/678', 'prabu@gmail.com', 'prabu123@gmail.com'),
('Chathurika', 'Weerasingha', '109456789/100', 'chathurika@gmail.com', 'chathu@345'),
('Nimal', 'Jayakodi', '12/34/56/789', 'nimal@gmail.com', 'nimal123'),
('Kushan', 'Warnakoolasooriya', '123/456/7890A', 'kusha@gmail.com', '123'),
('Samith', 'Senarathne', '134/456/789/000A', 'samith@gmail.com', '900');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
