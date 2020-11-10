-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 09, 2020 at 10:35 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `id15359619_airtraffic`
--

-- --------------------------------------------------------

--
-- Table structure for table `airlines`
--

CREATE TABLE `airlines` (
  `carrier` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airports`
--

CREATE TABLE `airports` (
  `faa` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `lat` decimal(10,0) NOT NULL,
  `lon` int(11) NOT NULL,
  `alt` int(11) NOT NULL,
  `tz` int(11) NOT NULL,
  `dst` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `tzone` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

CREATE TABLE `flights` (
  `id` int(11) NOT NULL,
  `year` year(4) NOT NULL,
  `month` int(11) NOT NULL,
  `day` int(11) NOT NULL,
  `dep_time` time NOT NULL,
  `arr_time` time NOT NULL,
  `sched_dep_time` time NOT NULL,
  `sched_arr_time` time NOT NULL,
  `dep_delay` int(11) NOT NULL,
  `arr_delay` int(11) NOT NULL,
  `hour` int(11) NOT NULL,
  `minute` int(11) NOT NULL,
  `carrier` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `tailnum` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `flight` int(11) NOT NULL,
  `origin` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `destination` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `time_hour` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `planes`
--

CREATE TABLE `planes` (
  `tailnum` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `year` int(11) NOT NULL,
  `type` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `manufacturer` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `engines` int(11) NOT NULL,
  `seats` int(11) NOT NULL,
  `speed` int(11) NOT NULL,
  `engine` varchar(200) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `weather`
--

CREATE TABLE `weather` (
  `origin` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `day` int(11) NOT NULL,
  `hour` int(11) NOT NULL,
  `temp` decimal(10,0) NOT NULL,
  `dewp` decimal(10,0) NOT NULL,
  `humid` decimal(10,0) NOT NULL,
  `wind_dir` int(11) NOT NULL,
  `wind_speed` decimal(10,0) NOT NULL,
  `wind_gust` decimal(10,0) NOT NULL,
  `precip` decimal(10,0) NOT NULL,
  `pressure` decimal(10,0) NOT NULL,
  `visib` decimal(10,0) NOT NULL,
  `time_hour` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airlines`
--
ALTER TABLE `airlines`
  ADD PRIMARY KEY (`carrier`);

--
-- Indexes for table `airports`
--
ALTER TABLE `airports`
  ADD PRIMARY KEY (`faa`);

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`id`),
  ADD KEY `flights_airlines` (`carrier`),
  ADD KEY `flights_planes` (`tailnum`),
  ADD KEY `flights_weather_dest` (`destination`),
  ADD KEY `flights_weather_origin` (`origin`);

--
-- Indexes for table `planes`
--
ALTER TABLE `planes`
  ADD PRIMARY KEY (`tailnum`);

--
-- Indexes for table `weather`
--
ALTER TABLE `weather`
  ADD PRIMARY KEY (`origin`,`year`,`month`,`day`,`hour`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `flights`
--
ALTER TABLE `flights`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `flights`
--
ALTER TABLE `flights`
  ADD CONSTRAINT `flights_airlines` FOREIGN KEY (`carrier`) REFERENCES `airlines` (`carrier`),
  ADD CONSTRAINT `flights_airport_dest` FOREIGN KEY (`destination`) REFERENCES `airports` (`faa`),
  ADD CONSTRAINT `flights_airport_origin` FOREIGN KEY (`origin`) REFERENCES `airports` (`faa`),
  ADD CONSTRAINT `flights_planes` FOREIGN KEY (`tailnum`) REFERENCES `planes` (`tailnum`),
  ADD CONSTRAINT `flights_weather_dest` FOREIGN KEY (`destination`) REFERENCES `weather` (`origin`),
  ADD CONSTRAINT `flights_weather_origin` FOREIGN KEY (`origin`) REFERENCES `weather` (`origin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
