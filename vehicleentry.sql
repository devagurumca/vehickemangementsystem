-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2022 at 04:39 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shorepoint`
--

-- --------------------------------------------------------

--
-- Table structure for table `vehicleentry`
--

CREATE TABLE `vehicleentry` (
  `id` int(11) NOT NULL,
  `vehicletype` varchar(30) NOT NULL,
  `vehiclenumber` varchar(10) NOT NULL,
  `ownerfullname` varchar(30) NOT NULL,
  `vehiclemodel` varchar(30) NOT NULL,
  `servicetype` varchar(30) NOT NULL,
  `phonenumber` int(12) NOT NULL,
  `date` date NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicleentry`
--

INSERT INTO `vehicleentry` (`id`, `vehicletype`, `vehiclenumber`, `ownerfullname`, `vehiclemodel`, `servicetype`, `phonenumber`, `date`, `address`) VALUES
(0, '2wheeler', 'TN58NH7865', 'FAZIL', 'splendor', 'wash', 765434567, '2022-01-05', 'mdu'),
(1, '2wheeler', 'TN58NH7865', 'FAZIL', 'splendor', 'wash', 1234567890, '2022-01-05', 'mdu');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `vehicleentry`
--
ALTER TABLE `vehicleentry`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
