-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para url

-- Volcando estructura para tabla url.urls
DROP TABLE IF EXISTS `urls`;
CREATE TABLE IF NOT EXISTS `urls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `nueva` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla url.urls: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `urls` DISABLE KEYS */;
INSERT IGNORE INTO `urls` (`id`, `url`, `nueva`) VALUES
	(3, 'https://www.zonarutoppuden.com/2017/04/boruto-anime-capitulos.html', 'https://tinyurl.com/y9bpwxw9'),
	(4, 'https://pixabay.com/es/photos/nubes-cielo-ambiente-cielo-azul-7050884/', 'https://tinyurl.com/yd4yyshm'),
	(5, 'https://pixabay.com/es/photos/campo-ma%c3%b1ana-amanecer-6574455/', 'https://tinyurl.com/ybomruhj'),
	(6, 'https://smodin.io/es/reproduzca-automaticamente-texto-en-espanol-gratis', 'https://tinyurl.com/yamlzyrj');
/*!40000 ALTER TABLE `urls` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
