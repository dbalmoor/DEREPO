/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - derepo
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`derepo` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `derepo`;

/*Table structure for table `amazon_requests` */

DROP TABLE IF EXISTS `amazon_requests`;

CREATE TABLE `amazon_requests` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fid` int(100) DEFAULT NULL,
  `oname` varchar(100) DEFAULT NULL,
  `uname` varchar(100) DEFAULT NULL,
  `demail` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `pkey` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `amazon_requests` */

insert  into `amazon_requests`(`id`,`fid`,`oname`,`uname`,`demail`,`fname`,`pkey`,`status`) values (1,1,'lakshmi','siri','cse.takeoff@gmail.com','cloud','123456','Accepted');

/*Table structure for table `amezon` */

DROP TABLE IF EXISTS `amezon`;

CREATE TABLE `amezon` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `files` longblob,
  `time` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT NULL,
  `share` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'safe',
  `request` varchar(100) DEFAULT 'waiting',
  `adate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `amezon` */

insert  into `amezon`(`id`,`email`,`name`,`fname`,`files`,`time`,`skey`,`share`,`status`,`request`,`adate`) values (1,'lakshmi@gmail.com','lakshmi','cloud','I���|�W\nhOW�����x���J����A�n�&9��\r�DO@�!ev1-��\ne~��Ń��D���)�O*5��tȎ(d�{�w�]��O8�i~Υ�C��F�|7>ߠ��&Ҏ��M�-�@��K��\n,/C0Z����p�a�r�a�g�,|�\'�n��Y>�l�*�?*�iY�`X����B�������%QǤ˒�M?�;�]w1�2\Z!��>=OC���L1^�w}i�9fk	v��zY��������r9͡�pTҏ\Z���KHםg��^S.�=\0˩����i�y=�L�9;p\n�ܡک��o���Nʨ�_<��F���є������Q�l/ڦ�B/�,�����qJ���ٓ�f��� ��XD�G@gֺ��v�LW��^�Z�����}�\"���Haz��*~ʏ�v�?�x�Y��=`rGd�[��݌0S�*r:����J]JY��[�#KtLy\Z%q��:���\rA���*M�g�\\�̟��n����B*�̦g�E�{u�XWhM�w�1J�G��5ɡS�=:����c����ve�LVᘌez�l��sp�j+���B	����D�qP�2���Z�ĥ>�u��ҷI;�\r\"�}+ˑ&R�xi����[�\"T��2�|:�����-+��$�%N�Z��yދ\0^�mF�6�O0sφn5qKϙb�q̂g�ܹ�E�Z��|$��Ģ��+*̰xq::���.�=���M�b��W�đ |�\"O�6[���SI�+2eì����<�� JM4?�+=.�_��lMW{[z%8�\0���r�z�p\"��9�Bk��\'+��lV�Q�g�0Jݮ����\Z�~А�xup\n0�;�S��fS�\\����Ϲ���Q�Z\\���q.��\0��|��s��01GΘN��F�4���+ַ��j��q�@a�D�xT2��v�.���V�̥;�b$�V','2021/05/04,16:26:57','5f7b9e2c','Share to all','Protected','waiting','2021/06/26,18:49:31'),(5,'cse.takeoff@gmail.com','siri','corona virus','���������ĢCO�,�Mh&8~�k�<�-��Y7��{z����`[ɺ��S.��R�p����#�����Į�\r�$1��uLI�\0	���� 6|�����ʘ#��p����\Z¾��oē3��=��6)0D���A�e\Zu֦�V+�1�������\'�qCH���h�� ��D��&���ݍ�u��t1�]i䅎������̶�j�M�A��u��n����W���`�,,F^����Z�#YӦ����R�f��J����$+�-��W�����`��L5I?-Vר�Ѵ𛿮��8�3m��v��1��$�g޲H�����c_x������Nµ���*���TI���m���4�A��M(^�P]�W������5z=F�j�?����֖S��F8�\"uL�Jl�(�ҽ	�yQg�-����ϯ=rʅ�\08�\n��g�\':���\"87H�q��{���Qzڰ�Ƅ��n80��?�@J�&GtW�VP�l��a*e�\"�aoŝ<�1�_����	����ɧ�P����B����a v�D��jmrH]�:���X|Ѥ�S��$��L�;��z9\"K��p\'/)1�5tϜ\0p\Zc��?){l}�7_ȀI�AA�K|0<h־��\'TtЛ���-j�;ǭ���1�-�{�n���[���M$�� �bv�٬N[���v�\0�ڰ\Z�oƉ���c���\nG�b�3�o�?q�\Z�o̐���ba4\0T�DDǁ�t��O{�yG�&��BJ<���#O���P�X��0Sp�{A���?ՠ��\r�ț���3�M�U|�^��q����qJ��ݸd�E��u�݆d?���¦�<H!wY?��W�\0C�:���g�^f���0�C8ʛ���>�C��Pq�R~���(!��r��K,�qAE�=�93v1�\n� UK��k(�=K�x|\rZÐ��*�WH��U�','2021/06/26,11:10:44','c20d5a82',NULL,'safe','waiting',NULL);

/*Table structure for table `bigrock` */

DROP TABLE IF EXISTS `bigrock`;

CREATE TABLE `bigrock` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `files` longblob,
  `time` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT NULL,
  `share` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'safe',
  `request` varchar(100) DEFAULT 'waiting',
  `adate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bigrock` */

insert  into `bigrock`(`id`,`email`,`name`,`fname`,`files`,`time`,`skey`,`share`,`status`,`request`,`adate`) values (1,'lakshmi@gmail.com','lakshmi','google',';�N���~�*���|�ĳ��0���������3�\"�\0}�����=aw,���2�)���\"ZAȴM����\'���Ӆ��e������C�o�:{ާd�\r0N����5��7��	d��.���W����J|��7��t��H\"7�u�3C�J�u���I���1��w��fʇ�8��e7IF�c�r���]ث�$�#�\\ 9�I*|b�t�+�7���=����w\'��s�Q��~)�AT��	I\\�璇�ǈ.k�l�LtBZQ�mw�8G���ƿ=�wnssd��S�Ky��w@�\rV}\\#0d�LB�','2021/05/04,16:27:15','960564b9','Name hide on share','safe','Accepted',NULL),(2,'cse.takeoff@gmail.com','siri','heart attack','O���7��L\Z5���\ZLŜ��u���󤴈$?	���o�q�RJ5�TW�m]g��N�e��8J�!l5�K��T��$�wq��*N��L����\n��ml&��y6�����raA�6®����uqT�SkO�\n�JT���5�*�ά�\rB�.�Ձ״\"�L��X\n���xEDCl;��y�N$K�Xo��\nô��]\\}�b]��\0�[Z�����ǖ�O)��j]��4��W�\Z�o]����}=����w�}���o��Bz��Va��}M+s\n�����\'��4��9Ĉ��͐901��iv(�1�~4�z?;�K5¦SZ�&�+�9KT�)��J<=�ه���o^.��_�N3��<*�酲ڡ]��}��&��H�*���/�_�!�5$$���eH*��{����NQ7JݔS�I������q��]r�5Z�%�1Y�2$��\'�FǪ\0��K��s،\'ȯ]��q�mF%)�)6��ףݽ(ee�o�N���EPuT�*I�P�D�� �x�CR�$>E�\n��k�{�+�`Q����H5\Z �','2021/06/26,11:28:13','801e801b',NULL,'Protected','waiting','2021/06/26,19:17:10');

/*Table structure for table `bigrock_requests` */

DROP TABLE IF EXISTS `bigrock_requests`;

CREATE TABLE `bigrock_requests` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fid` int(100) DEFAULT NULL,
  `oname` varchar(100) DEFAULT NULL,
  `uname` varchar(100) DEFAULT NULL,
  `demail` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `pkey` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bigrock_requests` */

insert  into `bigrock_requests`(`id`,`fid`,`oname`,`uname`,`demail`,`fname`,`pkey`,`status`) values (1,1,'lakshmi','siri','cse.takeoff@gmail.com','google','987654','Accepted');

/*Table structure for table `icloud` */

DROP TABLE IF EXISTS `icloud`;

CREATE TABLE `icloud` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `files` longblob,
  `time` varchar(100) DEFAULT NULL,
  `skey` varchar(100) DEFAULT NULL,
  `share` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'safe',
  `request` varchar(100) DEFAULT 'waiting',
  `adate` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `icloud` */

insert  into `icloud`(`id`,`email`,`name`,`fname`,`files`,`time`,`skey`,`share`,`status`,`request`,`adate`) values (2,'lakshmi@gmail.com','lakshmi','python','��b8�sb��̮�ִ�0�	�_Ri�\'S��-��e�Z�������C!�������eF+RD�h6�k9Ux�i4v\r�����G�u��ƛ�v���(mgOU��e���r��d��)ǎ�Y�P�����h8�Y\ZG�����%ԫ��po�7��Ζ�CC�_e�SF�]�P��K���ȑ�D�P�~*M-8o������_]v��Tv��|9t���T�lp��e�o��i��K������:���G6���I����ܑ���������0D��lx��Y��c%¬f�d\\��3���*��ճ����','2021/05/04,16:29:17','09dcb36a','Share to all','safe','waiting',NULL),(3,'lakshmi@gmail.com','lakshmi','decryption data in python','��b8�sb��̮�ִ�0�	�_Ri�\'S��-��e�Z�������C!�������eF+RD�h6�k9Ux�i4v\r�����G�u��ƛ�v���(mgOU��e���r��d��)ǎ�Y�P�����h8�Y\ZG�����%ԫ��po�7��Ζ�CC�_e�SF�]�P��K���ȑ�D�P�~*M-8o������_]v��Tv��|9t���T�lp��e�o��i��K������:���G6���I����ܑ���������0D��lx��Y��c%¬f�d\\��3���*��ճ����','2021/06/23,09:53:58','5bd5600e','Name hide on share','Protected','waiting','2021/06/26,19:03:00'),(4,'cse.takeoff@gmail.com','siri','brain tumor','�3-�>�>���+i���XǑ���dὙ�j�1J�6��Ybw��(\"����Y��*>����D�p�Էe�\':��F9�R�\ZV{������8�\0�?\'�9Į�[ڃ=*g����7�!!�7���s\\������iP��g�-�ĵ+���l��R���p`辒+ۑ(���No�b��F�wF\rl<�l�z5��+Y\'�z��_�B�K���5c����uP����MEH$��,H�ֲ�\Z���\'�ƴ�E1-m8<xwY����*%io����(��u���dSh1��D�A�.z�����[1�\"N#\0�����}<���\"�U���*���#�p� c��K�z\\\'���(�����?�+m_?�^�哱^�5���6�<�Ģ��zH\"{1�\'���\rHП�9������_\Z��\0dѿS�H�0�J�]��\rڑ�T}d��Kw�ܯ\\Q�����On�C.��\\���OF]a�uY~��)��2<w24`8}���.ӄ�LC�z!\\��d�28<#��9���\n�Z\"�҉�����֫�n\n���zό�?O;Y���E��C�ͩ�^Dx�z_8������E.�R#��������Nl\Z��.�B�(���\\����כ�i!Z�u�d�2\\	�\0�a�u�f�`4W�','2021/06/26,11:20:55','3e7168eb',NULL,'safe','waiting',NULL);

/*Table structure for table `icloud_requests` */

DROP TABLE IF EXISTS `icloud_requests`;

CREATE TABLE `icloud_requests` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fid` int(100) DEFAULT NULL,
  `oname` varchar(100) DEFAULT NULL,
  `uname` varchar(100) DEFAULT NULL,
  `demail` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `pkey` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `icloud_requests` */

insert  into `icloud_requests`(`id`,`fid`,`oname`,`uname`,`demail`,`fname`,`pkey`,`status`) values (1,3,'lakshmi','siri','cse.takeoff@gmail.com','decryption data in python','234567','Accepted');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'Inactive',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`email`,`pwd`,`addr`,`status`) values (1,'lakshmi','lakshmi@gmail.com','1','ongole','Activated'),(2,'siri','cse.takeoff@gmail.com','1','Vijayawada, Andhra Pradesh','Activated');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
