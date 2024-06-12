-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2024 at 10:21 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `placement_cell`
--

-- --------------------------------------------------------

--
-- Table structure for table `alumini`
--

CREATE TABLE `alumini` (
  `alumini__id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `mail` varchar(45) NOT NULL,
  `phone` int(11) NOT NULL,
  `career_path` varchar(45) NOT NULL,
  `experience` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alumini`
--

INSERT INTO `alumini` (`alumini__id`, `name`, `mail`, `phone`, `career_path`, `experience`, `status`, `password`) VALUES
(1, 'abhi', 'abhi@gmail.com', 2147483647, 'hjjj', '5', 'accepted', 'abhi');

-- --------------------------------------------------------

--
-- Table structure for table `announcement`
--

CREATE TABLE `announcement` (
  `announcement_id` int(11) NOT NULL,
  `vacancy` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `company_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `announcement`
--

INSERT INTO `announcement` (`announcement_id`, `vacancy`, `date`, `company_id`, `job_id`) VALUES
(1, 'hkg', '2024-04-01', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `applications`
--

CREATE TABLE `applications` (
  `application_id` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `job_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add alumini', 7, 'add_alumini'),
(26, 'Can change alumini', 7, 'change_alumini'),
(27, 'Can delete alumini', 7, 'delete_alumini'),
(28, 'Can view alumini', 7, 'view_alumini'),
(29, 'Can add announcement', 8, 'add_announcement'),
(30, 'Can change announcement', 8, 'change_announcement'),
(31, 'Can delete announcement', 8, 'delete_announcement'),
(32, 'Can view announcement', 8, 'view_announcement'),
(33, 'Can add applications', 9, 'add_applications'),
(34, 'Can change applications', 9, 'change_applications'),
(35, 'Can delete applications', 9, 'delete_applications'),
(36, 'Can view applications', 9, 'view_applications'),
(37, 'Can add company', 10, 'add_company'),
(38, 'Can change company', 10, 'change_company'),
(39, 'Can delete company', 10, 'delete_company'),
(40, 'Can view company', 10, 'view_company'),
(41, 'Can add jobs', 11, 'add_jobs'),
(42, 'Can change jobs', 11, 'change_jobs'),
(43, 'Can delete jobs', 11, 'delete_jobs'),
(44, 'Can view jobs', 11, 'view_jobs'),
(45, 'Can add login', 12, 'add_login'),
(46, 'Can change login', 12, 'change_login'),
(47, 'Can delete login', 12, 'delete_login'),
(48, 'Can view login', 12, 'view_login'),
(49, 'Can add student', 13, 'add_student'),
(50, 'Can change student', 13, 'change_student'),
(51, 'Can delete student', 13, 'delete_student'),
(52, 'Can view student', 13, 'view_student'),
(53, 'Can add test round', 14, 'add_testround'),
(54, 'Can change test round', 14, 'change_testround'),
(55, 'Can delete test round', 14, 'delete_testround'),
(56, 'Can view test round', 14, 'view_testround');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL,
  `alumini_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `message` varchar(100) NOT NULL,
  `sendertype` varchar(50) NOT NULL,
  `rectype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`chat_id`, `alumini_id`, `student_id`, `message`, `sendertype`, `rectype`) VALUES
(1, 1, 1, 'hlo', 'student', 'alumini'),
(2, 1, 1, 'hi', 'alumini', 'student');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `about` varchar(45) NOT NULL,
  `mail` varchar(45) NOT NULL,
  `phone` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`company_id`, `name`, `about`, `mail`, `phone`, `status`, `password`) VALUES
(1, 'bluegen', 'yju', 'b@gmail.com', 1454155511, 'accepted', 'bb');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'alumini', 'alumini'),
(8, 'announcement', 'announcement'),
(9, 'applications', 'applications'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(10, 'company', 'company'),
(5, 'contenttypes', 'contenttype'),
(11, 'jobs', 'jobs'),
(12, 'login', 'login'),
(6, 'sessions', 'session'),
(13, 'student', 'student'),
(14, 'test_round', 'testround');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-03-28 09:58:00.786332'),
(2, 'auth', '0001_initial', '2024-03-28 09:58:28.931620'),
(3, 'admin', '0001_initial', '2024-03-28 09:58:36.681785'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-03-28 09:58:36.772793'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-28 09:58:36.816764'),
(6, 'alumini', '0001_initial', '2024-03-28 09:58:37.454082'),
(7, 'jobs', '0001_initial', '2024-03-28 09:58:38.164936'),
(8, 'company', '0001_initial', '2024-03-28 09:58:38.597746'),
(9, 'announcement', '0001_initial', '2024-03-28 09:58:42.194255'),
(10, 'student', '0001_initial', '2024-03-28 09:58:43.810887'),
(11, 'applications', '0001_initial', '2024-03-28 09:58:47.563765'),
(12, 'contenttypes', '0002_remove_content_type_name', '2024-03-28 09:58:48.553784'),
(13, 'auth', '0002_alter_permission_name_max_length', '2024-03-28 09:58:49.619341'),
(14, 'auth', '0003_alter_user_email_max_length', '2024-03-28 09:58:49.826636'),
(15, 'auth', '0004_alter_user_username_opts', '2024-03-28 09:58:49.890079'),
(16, 'auth', '0005_alter_user_last_login_null', '2024-03-28 09:58:50.796325'),
(17, 'auth', '0006_require_contenttypes_0002', '2024-03-28 09:58:50.824006'),
(18, 'auth', '0007_alter_validators_add_error_messages', '2024-03-28 09:58:50.893664'),
(19, 'auth', '0008_alter_user_username_max_length', '2024-03-28 09:58:51.009308'),
(20, 'auth', '0009_alter_user_last_name_max_length', '2024-03-28 09:58:51.402680'),
(21, 'auth', '0010_alter_group_name_max_length', '2024-03-28 09:58:51.527671'),
(22, 'auth', '0011_update_proxy_permissions', '2024-03-28 09:58:51.590733'),
(23, 'auth', '0012_alter_user_first_name_max_length', '2024-03-28 09:58:51.745621'),
(24, 'login', '0001_initial', '2024-03-28 09:58:55.735040'),
(25, 'sessions', '0001_initial', '2024-03-28 09:58:58.535886'),
(26, 'test_round', '0001_initial', '2024-03-28 09:58:59.421619'),
(27, 'alumini', '0002_alter_alumini_options', '2024-04-01 10:08:43.580564'),
(28, 'announcement', '0002_alter_announcement_options', '2024-04-01 10:08:44.077396'),
(29, 'applications', '0002_alter_applications_options', '2024-04-01 10:08:44.261812'),
(30, 'company', '0002_alter_company_options', '2024-04-01 10:08:44.303753'),
(31, 'jobs', '0002_alter_jobs_options', '2024-04-01 10:08:44.416767'),
(32, 'login', '0002_alter_login_options', '2024-04-01 10:08:44.833244'),
(33, 'student', '0002_alter_student_options', '2024-04-01 10:08:44.991069'),
(34, 'test_round', '0002_alter_testround_options', '2024-04-01 10:08:45.086013');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('d380jtez4tli1qfxzx7ybgvthzlsxgnb', 'eyJ1X2lkIjoyfQ:1rzXee:9AcmS459kIWnoTnwzDsC9726WQHIXoZVI8iUMTM6paU', '2024-05-08 08:07:00.061575'),
('hp9n73jfqq7n3o1jacq14es4rpacjo8e', 'eyJ1X2lkIjoxfQ:1rrFdy:UkdZBoK5m_PGlGDB61zmJ_mh4i_Ik5QBCwjnaYX3zGQ', '2024-04-15 11:16:02.828208');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `job_id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `role` varchar(45) NOT NULL,
  `skills` varchar(45) NOT NULL,
  `compensation` int(11) NOT NULL,
  `location` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  `company_id` int(11) NOT NULL,
  `post_time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`job_id`, `name`, `role`, `skills`, `compensation`, `location`, `description`, `company_id`, `post_time`) VALUES
(1, 'abhi', 'j', 'j', 87, 'hj', 'jhk', 1, '16:25:50.954318');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `type` varchar(45) NOT NULL,
  `u_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `username`, `password`, `type`, `u_id`) VALUES
(1, 'admin', 'admin', 'admin', 1),
(2, 'anju@gmail.com', 'anju', 'student', 1),
(3, 'anju@gmail.com', 'anju', 'student', 1),
(4, 'anju@gmail.com', 'anju', 'student', 1),
(5, 'abhi@gmail.com', 'abhi', 'alumini', 1),
(6, 'b@gmail.com', 'bb', 'company', 1),
(7, 'none@gmail.com', '1111', 'student', 2);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `department` varchar(45) NOT NULL,
  `semester` varchar(45) NOT NULL,
  `mail` varchar(45) NOT NULL,
  `phone` int(11) NOT NULL,
  `cgpa` varchar(45) NOT NULL,
  `skills` varchar(45) NOT NULL,
  `certificates` varchar(45) NOT NULL,
  `applied_jobs` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `photo` varchar(45) NOT NULL,
  `year` int(11) NOT NULL,
  `place` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `name`, `department`, `semester`, `mail`, `phone`, `cgpa`, `skills`, `certificates`, `applied_jobs`, `status`, `password`, `photo`, `year`, `place`) VALUES
(1, 'anju', 'cs', '4', 'anju@gmail.com', 2147483647, '4', '', 'jhg', '', 'accepted', 'anju', '', 0, ''),
(2, 'Athul Krishna', 'Computer Science', '4', 'none@gmail.com', 1234567890, '7.52', 'HTML,CSS,Javascrpt,C, CPP', 'NSS', '', 'accepted', '1111', 'instructor.jpg', 2017, 'calicut');

-- --------------------------------------------------------

--
-- Table structure for table `test_round`
--

CREATE TABLE `test_round` (
  `test_id` int(11) NOT NULL,
  `test_link` varchar(45) NOT NULL,
  `interview_link` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alumini`
--
ALTER TABLE `alumini`
  ADD PRIMARY KEY (`alumini__id`);

--
-- Indexes for table `announcement`
--
ALTER TABLE `announcement`
  ADD PRIMARY KEY (`announcement_id`),
  ADD KEY `announcement_company_id_030dc65f_fk_company_company_id` (`company_id`),
  ADD KEY `announcement_job_id_56af895d_fk_jobs_job_id` (`job_id`);

--
-- Indexes for table `applications`
--
ALTER TABLE `applications`
  ADD PRIMARY KEY (`application_id`),
  ADD KEY `applications_job_id_9cc0e7d0_fk_jobs_job_id` (`job_id`),
  ADD KEY `applications_student_id_6df1c1fd_fk_student_student_id` (`student_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`chat_id`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`company_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `test_round`
--
ALTER TABLE `test_round`
  ADD PRIMARY KEY (`test_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumini`
--
ALTER TABLE `alumini`
  MODIFY `alumini__id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `announcement`
--
ALTER TABLE `announcement`
  MODIFY `announcement_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `applications`
--
ALTER TABLE `applications`
  MODIFY `application_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `chat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `company_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `job_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `test_round`
--
ALTER TABLE `test_round`
  MODIFY `test_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `announcement`
--
ALTER TABLE `announcement`
  ADD CONSTRAINT `announcement_company_id_030dc65f_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company` (`company_id`),
  ADD CONSTRAINT `announcement_job_id_56af895d_fk_jobs_job_id` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`);

--
-- Constraints for table `applications`
--
ALTER TABLE `applications`
  ADD CONSTRAINT `applications_job_id_9cc0e7d0_fk_jobs_job_id` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`),
  ADD CONSTRAINT `applications_student_id_6df1c1fd_fk_student_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
