1. 运行main.py会自动爬取数据并保存为json文件
2. 配置数据库后运行mysql.py即可保存到数据库内，注意数据库的字段

建表语句：

```mysql
CREATE TABLE `teacher` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(15) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `fax` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `field` varchar(500) DEFAULT NULL,
  `resume` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

