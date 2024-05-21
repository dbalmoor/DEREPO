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

insert  into `amezon`(`id`,`email`,`name`,`fname`,`files`,`time`,`skey`,`share`,`status`,`request`,`adate`) values (1,'lakshmi@gmail.com','lakshmi','cloud','IÂıÌ|ÂW\nhOW¡‡üğèxŸªÆJ†—æœÔA‹nì&9Æá\rãDO@!ev1-±û\ne~“ÓÅƒ“©D¹»ø)èŒO*5 µtÈ(d”{ßw¹]½­O8±i~Î¥’C²¥Fª|7>ß ‡†&Ò€úM£-Š@ «K°Û\n,/C0ZÑÌÁ£p±aşr¿aàgÏ,|Õ\'–nõÆY>‘l—*¡?*óiYñ´”`X¤ÃÁò¹B•‰´©œ´%QÇ¤Ë’ÜM?ğ¹;×]w1¸2\Z!’>=OC×ÿòL1^²w}iæ9fk	vÑÀzYî®ÒÁ·ÄÔé«¨r9Í¡°pTÒ\Z‹½‚KH×g×î^S.Í=\0Ë©œ°Èêiõy=ëLú9;p\náÜ¡Ú©ñÉoÿ£†NÊ¨£_<çñF’ÆôÑ”‰”ßàäQğl/Ú¦ôB/Ì,ÙĞĞÙûqJ¬£›Ù“†fïªÕ ›‰XDÊG@gÖºÃåv“LW¯„^«Z„‘âïü}ğ\"œ¤öHaz—¾*~ÊŸv­?€x®Y“³=`rGdÿ[‚¯İŒ0SÄ*r:ÈÇÀJ]JYõÌ[#KtLy\Z%q„é:àÇÄ\rAÿà*M­g…\\‹ÌŸä÷n µ¢·B*ìÌ¦g©E¡{ušXWhM¨w´1JG©Ê5É¡S¦=:ü ‚²cƒÍâïve‰LVá˜ŒezúlÇşspµj+”óŸÒB	¡¿¾üD¹qPú2ÜÎáZ¾Ä¥>ŒuØô…Ò·I;¤\r\"›}+Ë‘&RëxiØÛòı[Å\"TÍÃ2¸|:“«‚•-+±î$è%NÑZ™ÇyŞ‹\0^½mFó6¯O0sÏ†n5qKÏ™b²qÌ‚gÔÜ¹ïEìZÓõ|$ƒÕÄ¢Æé+*Ì°xq::¹‹.Ã=ì°ÏÈM¥b±—WóÄ‘ |³\"O‚6[ÖŠ„SI¬+2eÃ¬‚šãÏ<à’ JM4?™+=.á_œ€lMW{[z%8º\0¦·‚rÌzúp\"ãÌ9«Bk×å\'+Ë‹lVÒQ§g¥0Jİ®ëÛ×Ø\Zˆ~Ğáxup\n0Ç;›Sû·fSŸ\\ú½ÃùÏ¹ş¹ˆQíZ\\ı¢¸q.œ˜\0ûÎ|¯øs‚01GÎ˜N„€F«4¸Å£+Ö·‰³j³†q”@aÒD¯xT2¸‚v×.¯ÙVœÌ¥;¨b$ÒV','2021/05/04,16:26:57','5f7b9e2c','Share to all','Protected','waiting','2021/06/26,18:49:31'),(5,'cse.takeoff@gmail.com','siri','corona virus','ÀÇª¶«†…ğÄ¢COñ,ŸMh&8~ˆk°<Û-™òY7ï{z·¨¼æº`[Éº½úS.‚ØR—p‘º¯æ#âŒü¢šÄ®Ò\rõ$1¥æuLI\0	üÖÈø 6|€õÎòÙÊ˜#éãpÀç®ø¹\ZÂ¾ªÖoÄ“3âˆí=¿„6)0D·‰£A´e\ZuÖ¦›V+¸1ÍæáÉÁè¸\'ÒqÂŒCH¬¾Œhó¬´Ã â¤—Dõ‡&¿š•İ÷uÿöt1¹]iä…ğÑú‘¹˜Ì¶µjëMçAµë¶uÁÑnÿ±³°WÉş§`Ñ,,F^ ÆÜÆZÀ#YÓ¦Ğæúç¢R‘fÑãJ†ø ª$+î-˜W¹úÕ÷¤`¿âL5I?-V×¨ÎÑ´ğ›¿®¹£8Á3m­õv€î1–$†gŞ²H¨†¿Şc_xØù‰½˜İNÂµöá´ò*¢¦ŞTIÍËÃmŞûÑ4‡AËM(^óP]ÀW‘“Ÿ¼ÄÈ5z=Fì‘jˆ?ÅÛ½ÍÖ–S­ê…F8„\"uL”Jlş(ñ¾‡Ò½	®yQgÑ-”şöÏ¯=rÊ…Ğ\08ì\n³ğ˜g‰\':ŠÿÚ\"87HîqÂé{ºœ‚QzÚ°Æ„¡×n80ô¾?Ù@JØ&GtWÌVP²lêäa*eê\"‰aoÅ<©1ë_„ÆÃê	‰„°–É§ÃP°âÙ”Bòîíæa vDğÆjmrH]™:ŞãØX|Ñ¤ÜSõ©$ùL²;äz9\"Kÿˆp\'/)1£5tÏœ\0p\Zc‰ƒ?){l}ë7_È€IóAAÌK|0<hÖ¾Ëó\'TtĞ›ıÿ©-jû;Ç­¶´±1í-ˆ{¿n–ÖÉ[ÙùåM$òÈ ¯bvıÙ¬N[´ÀŒvó\0ıÚ°\Z¦oÆ‰Š­±c­•\nG°bÏ3Èo¦?qÊ\Z»oÌôûÓba4\0TùDDÇİtí¨áO{¥yG±&·BJ<³‘#O¥ÁàPÆXÇú0SpÂ§{A·Î?Õ ­İ\r“È›–ÄÌ3¼MÔU|â^ÒqÑÑïèqJ¢Ğİ¸dÔEëu±İ†d?¡ÏöÂ¦Š<H!wY?ÛõWĞ\0C‹:‰´‚gí^fş‘ö0çC8Ê›ØË>¸CÛüPqöR~©™¯(!şèr¿K,—qAEÜ=š93v1ä½\n UKµæk(œ=KÊx|\rZÃœÌ*ïWHäÂUË','2021/06/26,11:10:44','c20d5a82',NULL,'safe','waiting',NULL);

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

insert  into `bigrock`(`id`,`email`,`name`,`fname`,`files`,`time`,`skey`,`share`,`status`,`request`,`adate`) values (1,'lakshmi@gmail.com','lakshmi','google',';âNÉæò¹~ù*ú¹Ø|ÔÄ³Ë×0¾²¾ò£î¶›Ñ3ã\"\0}»¾ÒúŞ=aw, Õ2Ò)Âô¤\"ZAÈ´Mš–Êü\'—ˆœÓ…çÿeÌÿ¸­ÄCÔoŒ:{Ş§dƒ\r0NĞû·ı5ˆ¯7Ü	d£—.éêÃW¶ı”ÇJ|†ì›7ı™t–ÍH\"7ğuÑ3CàJuø¬¢I¸š±1¢ğwëìfÊ‡Ö8ƒíe7IF–c±r¨ ûÂ†]Ø«Ì$Ì#à\\ 9èI*|bØtƒ+7Ñış=…ëïÊw\'Ìêsì­Q™«~)ÔATßÇ	I\\€ç’‡àÇˆ.kølÇLtBZQÇmwŠ8GƒÙéÆ¿=·wnssd•¯SìKyµ›w@¾\rV}\\#0dæŠLBÅ','2021/05/04,16:27:15','960564b9','Name hide on share','safe','Accepted',NULL),(2,'cse.takeoff@gmail.com','siri','heart attack','O¶úƒ7ãL\Z5­ãíƒ\ZLÅœ¯‚uËÉåó¤´ˆ$?	ºÉûoùq²RJ5õTWím]g×ïN´eÅÁ8J”!l5ğKÁ¬T÷â$Úwqç”Á*NÜğLê¬Úùï\n‰Áml&Çìy6àËê¯ÃúraAã6Â®ªûı‘uqTÜSkO’\nJT–¥¢5§*¼Î¬£\rBÊ.öÕ×´\"­LÆ¦X\n‚ÅóxEDCl;´ŠyˆN$KXo£íµ¨\nÃ´½—]\\}æb]°ñ\0ö[ZµãÍÿ³Ç–åO)˜İj]›÷4¶›Wé\Z‰o]¸•€Ö}=·¢¤á¶w²}“Òêo—‚BzèŞVa´}M+s\nÀúêûÀ\'ãÊ4ˆ9Äˆ§ÈÍ901ùïiv(Ù1â~4¯z?;²K5Â¦SZ·&÷+Ù9KTŞ)ºØJ<=ºÙ‡÷šÊo^.éä_N3•ü<*îé…²Ú¡]ŒÄ}ìİ&ŸãHê*ÖÁ /Ú_û!ã±5$$º¯ªeH*¦{´±¤ÓNQ7Jİ”SèI¶¥Âõ©qùÄ]ró¿5Z²%¸1YÙ2$èÌ\'ŸFÇª\0ÂñK¬ƒsØŒ\'È¯]–Æq£mF%)µ)6­í×£İ½(eeşo•N­ºEPuTÒ*I„P·Dè±¿ ÊxCR…$>Eá£\n½õkÔ{œ+Ç`Q„›çH5\Z È','2021/06/26,11:28:13','801e801b',NULL,'Protected','waiting','2021/06/26,19:17:10');

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

insert  into `icloud`(`id`,`email`,`name`,`fname`,`files`,`time`,`skey`,`share`,`status`,`request`,`adate`) values (2,'lakshmi@gmail.com','lakshmi','python','Ùõb8üsb¸õÌ®õÖ´ğ0µ	ß_Ri„\'S§œ-¨İeíZ¿¿«¬ÒñğC!èúˆ¦Ğà»ÎeF+RDÂh6‘k9Ux³i4v\r’È¡—Gôu§ûÆ›ÜvÔÿø(mgOU¬Æe¼ˆ­rú©dĞë)ÇÌY±PŸ–¾ªèh8øY\ZG¤²œŸ¥%Ô«ºÚpoä7²Î–‰CC€_eÏSFØ]PÕÂKéïÛÈ‘õDúP»~*M-8o™šÈõ½_]vº³Tv¾„|9tô­ÓT£lp£í eÜoÌñiÄÁKòåíãíø:İóøG6†ÆÜI¦µ…µÜ‘—¿·†äı„ô0D¶¿lxËùY”ıc%Â¬f¶d\\¸¦3–½*ì™àÕ³½·œ¥','2021/05/04,16:29:17','09dcb36a','Share to all','safe','waiting',NULL),(3,'lakshmi@gmail.com','lakshmi','decryption data in python','Ùõb8üsb¸õÌ®õÖ´ğ0µ	ß_Ri„\'S§œ-¨İeíZ¿¿«¬ÒñğC!èúˆ¦Ğà»ÎeF+RDÂh6‘k9Ux³i4v\r’È¡—Gôu§ûÆ›ÜvÔÿø(mgOU¬Æe¼ˆ­rú©dĞë)ÇÌY±PŸ–¾ªèh8øY\ZG¤²œŸ¥%Ô«ºÚpoä7²Î–‰CC€_eÏSFØ]PÕÂKéïÛÈ‘õDúP»~*M-8o™šÈõ½_]vº³Tv¾„|9tô­ÓT£lp£í eÜoÌñiÄÁKòåíãíø:İóøG6†ÆÜI¦µ…µÜ‘—¿·†äı„ô0D¶¿lxËùY”ıc%Â¬f¶d\\¸¦3–½*ì™àÕ³½·œ¥','2021/06/23,09:53:58','5bd5600e','Name hide on share','Protected','waiting','2021/06/26,19:03:00'),(4,'cse.takeoff@gmail.com','siri','brain tumor','‹3-í>÷>Åì+iª›ÇXÇ‘¼¾Ûdá½™jº1JÄ6‹´Ybw¦¥(\"ÑÏäœÏYæ•ã*>§÷·ıDŞpè»Ô·eø\':½ëF9ŒR\ZV{‚µşóÁ’8”\0?\'ì9Ä®Á[Úƒ=*g°Öıÿ7¶!!Á7ŠÉÜs\\—¦õ¡ƒïiPŒåg…-Äµ+××³l·„R”¤£p`è¾’+Û‘(¤şˆNo©bÃìFÑwF\rl<ólüz5æú+Y\'…zŸì_ƒBÜKÖù–5cµ™¼˜uP¶¬­MEH$–œ,HµÖ²¦\ZåÁŒ\'÷Æ´ªE1-m8<xwY©ó«À*%io˜«²¼(•Îuı…ßdSh1¦DƒA·.z²â¾³[1—\"N#\0«ÖÁ‡Ê}<»ÚÃ\"åU ‰Ÿ*°–¡#“pÍ cáØK‹z\\\'¢ŒÕ(íü‡„ò?+m_?È^¦å“±^¡5àÍÃ6ö<£Ä¢ åzH\"{1™\'’ø´\rHĞŸ—9îş¬šÑƒ_\Zåè\0dÑ¿S„HÆ0ÿJ”]œŠ\rÚ‘T}d ‰KwùÜ¯\\QšÇÛñÈOnÔC.ÿ¹\\†“üÂ—OF]a®uY~Óäœ)âè2<w24`8}¡ƒË.Ó„äŒLC¬z!\\êádü28<#¢9ÿµ\n²Z\"ÃÒ‰¤Ïÿ¥Ö«¹n\n±§¬zÏŒ»?O;YÏéá¿E½›Cê€Í©í^DxÜz_8ˆÛàäøôE.ûR#ÏşÀ¢˜“‚Nl\Z«Ú.”Bä(¹ï…Ã\\¾–Ğ××›ô‡i!ZÖušdš2\\	û\0‚a–uËf`4W³','2021/06/26,11:20:55','3e7168eb',NULL,'safe','waiting',NULL);

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
