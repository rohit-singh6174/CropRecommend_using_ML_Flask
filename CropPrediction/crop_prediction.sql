-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2023 at 10:32 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crop_prediction`
--

-- --------------------------------------------------------

--
-- Table structure for table `farmers`
--

CREATE TABLE `farmers` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `farmerid` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `farmers`
--

INSERT INTO `farmers` (`id`, `name`, `phone`, `gender`, `district`, `farmerid`, `username`, `password`) VALUES
(3, 'abc', 1111111111, 'MALE', 'Ahmednaga', '1234567891', 'abc', '$2b$12$AyYHBLmJbO891H8.DqcDcOhK.1IqjE6Q.QLJLI.xIWf5QkP4pmxXe'),
(4, 'cde', 2222222222, 'MALE', 'Akola', '2222222222', 'cde', '$2b$12$TZCQEH034h5Fu779ta9wIef4maluZaJzaaMbl70.jUJ9bH.UkjIUW');

-- --------------------------------------------------------

--
-- Table structure for table `farmers__details`
--

CREATE TABLE `farmers__details` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `district` varchar(20) NOT NULL,
  `farmerid` varchar(20) NOT NULL,
  `adharcard_no` varchar(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `pincode` int(11) NOT NULL,
  `bankaccount_no` bigint(20) NOT NULL,
  `bank_name` varchar(40) NOT NULL,
  `ifsc` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `farmers__details`
--

INSERT INTO `farmers__details` (`id`, `name`, `phone`, `gender`, `district`, `farmerid`, `adharcard_no`, `address`, `pincode`, `bankaccount_no`, `bank_name`, `ifsc`) VALUES
(1, 'abc', 1111111111, 'MALE', 'Akola', '1234567891', '981924562314', 'Apurva Space Apartments', 400026, 9876543211, 'SBI', 'SBI004321'),
(2, 'cde', 4444444444, 'MALE', 'Akola', '2222222222', '111111111111', 'sdfsdfsadwdasdas', 400027, 3333333333, 'SBI', 'SBI004321');

-- --------------------------------------------------------

--
-- Table structure for table `farmer_details`
--

CREATE TABLE `farmer_details` (
  `id` int(255) NOT NULL,
  `farmer_id` bigint(20) NOT NULL,
  `name` text NOT NULL,
  `phone` bigint(10) NOT NULL,
  `adharcard_no` bigint(20) NOT NULL,
  `state` text NOT NULL,
  `address` longtext NOT NULL,
  `pincode` int(10) NOT NULL,
  `bankaccount_no` bigint(30) NOT NULL,
  `bank_name` text NOT NULL,
  `ifsc` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `farmers`
--
ALTER TABLE `farmers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `farmerid` (`farmerid`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `farmers__details`
--
ALTER TABLE `farmers__details`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `farmerid` (`farmerid`),
  ADD UNIQUE KEY `adharcard_no` (`adharcard_no`),
  ADD UNIQUE KEY `bankaccount_no` (`bankaccount_no`);

--
-- Indexes for table `farmer_details`
--
ALTER TABLE `farmer_details`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `farmer_id` (`farmer_id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `adharcard_no` (`adharcard_no`),
  ADD UNIQUE KEY `bankaccount_no` (`bankaccount_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `farmers`
--
ALTER TABLE `farmers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `farmers__details`
--
ALTER TABLE `farmers__details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `farmer_details`
--
ALTER TABLE `farmer_details`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
