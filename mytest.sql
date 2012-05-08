-- MySQL dump 10.13  Distrib 5.1.61, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: mytest
-- ------------------------------------------------------
-- Server version	5.1.61-0ubuntu0.11.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CompilableCodeGenerationConfig`
--

DROP TABLE IF EXISTS `CompilableCodeGenerationConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CompilableCodeGenerationConfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_meta_id` int(11) DEFAULT NULL,
  `code_type_id` int(11) DEFAULT NULL,
  `generation_method` varchar(254) DEFAULT NULL,
  `requirment` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association7` (`problem_meta_id`),
  CONSTRAINT `FK_association7` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CompilableCodeGenerationConfig`
--

LOCK TABLES `CompilableCodeGenerationConfig` WRITE;
/*!40000 ALTER TABLE `CompilableCodeGenerationConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `CompilableCodeGenerationConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CompileConfig`
--

DROP TABLE IF EXISTS `CompileConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CompileConfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_meta_id` int(11) DEFAULT NULL,
  `code_type` int(11) DEFAULT NULL,
  `config` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association8` (`problem_meta_id`),
  CONSTRAINT `FK_association8` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CompileConfig`
--

LOCK TABLES `CompileConfig` WRITE;
/*!40000 ALTER TABLE `CompileConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `CompileConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Description`
--

DROP TABLE IF EXISTS `Description`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Description` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(254) DEFAULT NULL,
  `content` varchar(254) DEFAULT NULL,
  `input` varchar(254) DEFAULT NULL,
  `output` varchar(254) DEFAULT NULL,
  `sample_input` varchar(254) DEFAULT NULL,
  `sample_output` varchar(254) DEFAULT NULL,
  `hint` varchar(254) DEFAULT NULL,
  `source` varchar(254) DEFAULT NULL,
  `problem_meta_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Relationship_29` (`problem_meta_id`),
  CONSTRAINT `FK_Relationship_29` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Description`
--

LOCK TABLES `Description` WRITE;
/*!40000 ALTER TABLE `Description` DISABLE KEYS */;
/*!40000 ALTER TABLE `Description` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InputOutputData`
--

DROP TABLE IF EXISTS `InputOutputData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InputOutputData` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(254) DEFAULT NULL,
  `problem_meta_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association10` (`problem_meta_id`),
  CONSTRAINT `FK_association10` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InputOutputData`
--

LOCK TABLES `InputOutputData` WRITE;
/*!40000 ALTER TABLE `InputOutputData` DISABLE KEYS */;
/*!40000 ALTER TABLE `InputOutputData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `KeywordCheckConfig`
--

DROP TABLE IF EXISTS `KeywordCheckConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `KeywordCheckConfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_meta_id` int(11) DEFAULT NULL,
  `code_type` int(11) DEFAULT NULL,
  `word` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association6` (`problem_meta_id`),
  CONSTRAINT `FK_association6` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `KeywordCheckConfig`
--

LOCK TABLES `KeywordCheckConfig` WRITE;
/*!40000 ALTER TABLE `KeywordCheckConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `KeywordCheckConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OutputCheckConfig`
--

DROP TABLE IF EXISTS `OutputCheckConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OutputCheckConfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_meta_id` int(11) DEFAULT NULL,
  `check_method` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association11` (`problem_meta_id`),
  CONSTRAINT `FK_association11` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OutputCheckConfig`
--

LOCK TABLES `OutputCheckConfig` WRITE;
/*!40000 ALTER TABLE `OutputCheckConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `OutputCheckConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Permission`
--

DROP TABLE IF EXISTS `Permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Permission`
--

LOCK TABLES `Permission` WRITE;
/*!40000 ALTER TABLE `Permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `Permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Problem`
--

DROP TABLE IF EXISTS `Problem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Problem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_meta_id` int(11) DEFAULT NULL,
  `judge_flow` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association18` (`problem_meta_id`),
  CONSTRAINT `FK_association18` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Problem`
--

LOCK TABLES `Problem` WRITE;
/*!40000 ALTER TABLE `Problem` DISABLE KEYS */;
/*!40000 ALTER TABLE `Problem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProblemMeta`
--

DROP TABLE IF EXISTS `ProblemMeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProblemMeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(254) DEFAULT NULL,
  `judge_flow` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProblemMeta`
--

LOCK TABLES `ProblemMeta` WRITE;
/*!40000 ALTER TABLE `ProblemMeta` DISABLE KEYS */;
/*!40000 ALTER TABLE `ProblemMeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RunConfig`
--

DROP TABLE IF EXISTS `RunConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RunConfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_meta_id` int(11) DEFAULT NULL,
  `code_type` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `memory` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association9` (`problem_meta_id`),
  CONSTRAINT `FK_association9` FOREIGN KEY (`problem_meta_id`) REFERENCES `ProblemMeta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RunConfig`
--

LOCK TABLES `RunConfig` WRITE;
/*!40000 ALTER TABLE `RunConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `RunConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Submission`
--

DROP TABLE IF EXISTS `Submission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Submission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `sub_time` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `used_time` int(11) DEFAULT NULL,
  `used_memory` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_association20` (`user_id`),
  KEY `FK_association5` (`problem_id`),
  CONSTRAINT `FK_association20` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`),
  CONSTRAINT `FK_association5` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Submission`
--

LOCK TABLES `Submission` WRITE;
/*!40000 ALTER TABLE `Submission` DISABLE KEYS */;
/*!40000 ALTER TABLE `Submission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TGroup`
--

DROP TABLE IF EXISTS `TGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TGroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TGroup`
--

LOCK TABLES `TGroup` WRITE;
/*!40000 ALTER TABLE `TGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `TGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(254) DEFAULT NULL,
  `password` varchar(254) DEFAULT NULL,
  `nickname` varchar(254) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `submit` int(11) DEFAULT NULL,
  `accept` int(11) DEFAULT NULL,
  `reg_time` datetime DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `last_login` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (16,'admin','pbkdf2_sha256$10000$3I88NnOII2iQ$SKInJWBJhcb6HdBJnRZ4e/hzXXOu5K6Z8v1HHuoHtZk=',NULL,NULL,NULL,NULL,NULL,1,'2012-04-26 10:45:21');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'content type','contenttypes','contenttype'),(2,'session','sessions','session'),(3,'site','sites','site');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('b7345af28096c80117a8e494155d8f53','ZjJlZTk2NWE3NDg1MTMxNWJjYTA3YzdjNWQzMjQ0YjE0ODM0MGM3ODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVR5jdXBfb2ouYXV0aC5iYWNrZW5kcy5TQUJhY2tlbmRxA1UNX2F1dGhfdXNl\ncl9pZHEEigEQdS4=\n','2012-05-10 10:45:21');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissionGroup`
--

DROP TABLE IF EXISTS `permissionGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissionGroup` (
  `permission_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`permission_id`,`group_id`),
  KEY `FK_permissionGroup1` (`group_id`),
  CONSTRAINT `FK_permissionGroup` FOREIGN KEY (`permission_id`) REFERENCES `Permission` (`id`),
  CONSTRAINT `FK_permissionGroup1` FOREIGN KEY (`group_id`) REFERENCES `TGroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissionGroup`
--

LOCK TABLES `permissionGroup` WRITE;
/*!40000 ALTER TABLE `permissionGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `permissionGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemCCGC`
--

DROP TABLE IF EXISTS `problemCCGC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problemCCGC` (
  `problem_id` int(11) NOT NULL,
  `ccgc_id` int(11) NOT NULL,
  PRIMARY KEY (`problem_id`,`ccgc_id`),
  KEY `FK_problemCCGC` (`ccgc_id`),
  CONSTRAINT `FK_problemCCGC` FOREIGN KEY (`ccgc_id`) REFERENCES `CompilableCodeGenerationConfig` (`id`),
  CONSTRAINT `FK_problemCCGC1` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemCCGC`
--

LOCK TABLES `problemCCGC` WRITE;
/*!40000 ALTER TABLE `problemCCGC` DISABLE KEYS */;
/*!40000 ALTER TABLE `problemCCGC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemCompileConfig`
--

DROP TABLE IF EXISTS `problemCompileConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problemCompileConfig` (
  `problem_id` int(11) NOT NULL,
  `compileconfig_id` int(11) NOT NULL,
  PRIMARY KEY (`problem_id`,`compileconfig_id`),
  KEY `FK_problemCompileConfig` (`compileconfig_id`),
  CONSTRAINT `FK_problemCompileConfig` FOREIGN KEY (`compileconfig_id`) REFERENCES `CompileConfig` (`id`),
  CONSTRAINT `FK_problemCompileConfig1` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemCompileConfig`
--

LOCK TABLES `problemCompileConfig` WRITE;
/*!40000 ALTER TABLE `problemCompileConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `problemCompileConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemDescription`
--

DROP TABLE IF EXISTS `problemDescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problemDescription` (
  `description_id` int(11) NOT NULL,
  `problem_id` int(11) NOT NULL,
  PRIMARY KEY (`description_id`,`problem_id`),
  KEY `FK_problemDescription1` (`problem_id`),
  CONSTRAINT `FK_problemDescription` FOREIGN KEY (`description_id`) REFERENCES `Description` (`id`),
  CONSTRAINT `FK_problemDescription1` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemDescription`
--

LOCK TABLES `problemDescription` WRITE;
/*!40000 ALTER TABLE `problemDescription` DISABLE KEYS */;
/*!40000 ALTER TABLE `problemDescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemIOData`
--

DROP TABLE IF EXISTS `problemIOData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problemIOData` (
  `problem_id` int(11) NOT NULL,
  `io_id` int(11) NOT NULL,
  PRIMARY KEY (`problem_id`,`io_id`),
  KEY `FK_problemIOData` (`io_id`),
  CONSTRAINT `FK_problemIOData` FOREIGN KEY (`io_id`) REFERENCES `InputOutputData` (`id`),
  CONSTRAINT `FK_problemIOData1` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemIOData`
--

LOCK TABLES `problemIOData` WRITE;
/*!40000 ALTER TABLE `problemIOData` DISABLE KEYS */;
/*!40000 ALTER TABLE `problemIOData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemKeywordCheckConfig`
--

DROP TABLE IF EXISTS `problemKeywordCheckConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problemKeywordCheckConfig` (
  `keyconfig_id` int(11) NOT NULL,
  `problem_id` int(11) NOT NULL,
  PRIMARY KEY (`keyconfig_id`,`problem_id`),
  KEY `FK_problemKeywordCheckConfig1` (`problem_id`),
  CONSTRAINT `FK_problemKeywordCheckConfig` FOREIGN KEY (`keyconfig_id`) REFERENCES `KeywordCheckConfig` (`id`),
  CONSTRAINT `FK_problemKeywordCheckConfig1` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemKeywordCheckConfig`
--

LOCK TABLES `problemKeywordCheckConfig` WRITE;
/*!40000 ALTER TABLE `problemKeywordCheckConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `problemKeywordCheckConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemOutputCheckConfig`
--

DROP TABLE IF EXISTS `problemOutputCheckConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problemOutputCheckConfig` (
  `problem_id` int(11) NOT NULL,
  `outputcheck_id` int(11) NOT NULL,
  PRIMARY KEY (`problem_id`,`outputcheck_id`),
  KEY `FK_problemOutputCheckConfig` (`outputcheck_id`),
  CONSTRAINT `FK_problemOutputCheckConfig` FOREIGN KEY (`outputcheck_id`) REFERENCES `OutputCheckConfig` (`id`),
  CONSTRAINT `FK_problemOutputCheckConfig1` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemOutputCheckConfig`
--

LOCK TABLES `problemOutputCheckConfig` WRITE;
/*!40000 ALTER TABLE `problemOutputCheckConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `problemOutputCheckConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemRunConfig`
--

DROP TABLE IF EXISTS `problemRunConfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `problemRunConfig` (
  `problem_id` int(11) NOT NULL,
  `runconfig_id` int(11) NOT NULL,
  PRIMARY KEY (`problem_id`,`runconfig_id`),
  KEY `FK_problemRunConfig1` (`runconfig_id`),
  CONSTRAINT `FK_problemRunConfig` FOREIGN KEY (`problem_id`) REFERENCES `Problem` (`id`),
  CONSTRAINT `FK_problemRunConfig1` FOREIGN KEY (`runconfig_id`) REFERENCES `RunConfig` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemRunConfig`
--

LOCK TABLES `problemRunConfig` WRITE;
/*!40000 ALTER TABLE `problemRunConfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `problemRunConfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userGroup`
--

DROP TABLE IF EXISTS `userGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userGroup` (
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`group_id`),
  KEY `FK_userGroup` (`group_id`),
  CONSTRAINT `FK_userGroup` FOREIGN KEY (`group_id`) REFERENCES `TGroup` (`id`),
  CONSTRAINT `FK_userGroup1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userGroup`
--

LOCK TABLES `userGroup` WRITE;
/*!40000 ALTER TABLE `userGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `userGroup` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-05-08  8:23:29
