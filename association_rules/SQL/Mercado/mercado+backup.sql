CREATE DATABASE  IF NOT EXISTS `mercado` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `mercado`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: mercado
-- ------------------------------------------------------
-- Server version	5.7.14-log

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
-- Table structure for table `produtos`
--

DROP TABLE IF EXISTS `produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produtos` (
  `idproduto` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`idproduto`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos`
--

LOCK TABLES `produtos` WRITE;
/*!40000 ALTER TABLE `produtos` DISABLE KEYS */;
INSERT INTO `produtos` VALUES (1,'Leite'),(2,'Café'),(3,'Cerveja'),(4,'Pão'),(5,'Manteiga'),(6,'Arroz'),(7,'Feijão');
/*!40000 ALTER TABLE `produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venda_produtos`
--

DROP TABLE IF EXISTS `venda_produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `venda_produtos` (
  `idvenda_produto` int(11) NOT NULL AUTO_INCREMENT,
  `idvenda` int(11) NOT NULL,
  `idproduto` int(11) NOT NULL,
  `valor` float NOT NULL,
  PRIMARY KEY (`idvenda_produto`),
  KEY `fk_venda_produtos_produto` (`idproduto`),
  KEY `fk_venda_produtos_venda` (`idvenda`),
  CONSTRAINT `fk_venda_produtos_produto` FOREIGN KEY (`idproduto`) REFERENCES `produtos` (`idproduto`),
  CONSTRAINT `fk_venda_produtos_venda` FOREIGN KEY (`idvenda`) REFERENCES `vendas` (`idvenda`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venda_produtos`
--

LOCK TABLES `venda_produtos` WRITE;
/*!40000 ALTER TABLE `venda_produtos` DISABLE KEYS */;
INSERT INTO `venda_produtos` VALUES (1,1,2,5.5),(2,1,4,5.5),(3,1,5,3),(4,2,1,1.7),(5,2,3,4),(6,2,4,7),(7,2,5,1),(8,3,2,5),(9,3,4,3),(10,3,5,10),(11,4,1,1),(12,4,2,6),(13,4,4,7),(14,4,5,8),(15,5,3,9),(16,6,5,15),(17,7,4,10),(18,8,4,15),(19,9,4,8),(20,9,4,10),(21,10,4,5);
/*!40000 ALTER TABLE `venda_produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendas`
--

DROP TABLE IF EXISTS `vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendas` (
  `idvenda` int(11) NOT NULL AUTO_INCREMENT,
  `data_venda` date NOT NULL,
  PRIMARY KEY (`idvenda`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendas`
--

LOCK TABLES `vendas` WRITE;
/*!40000 ALTER TABLE `vendas` DISABLE KEYS */;
INSERT INTO `vendas` VALUES (1,'2017-04-03'),(2,'2017-04-09'),(3,'2017-04-15'),(4,'2017-04-18'),(5,'2017-04-18'),(6,'2017-04-20'),(7,'2017-04-20'),(8,'2017-04-22'),(9,'2017-04-23'),(10,'2015-04-27');
/*!40000 ALTER TABLE `vendas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-02 16:45:54
