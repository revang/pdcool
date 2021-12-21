CREATE TABLE `tparameter` 
(
  `c_system`     varchar(64)  DEFAULT NULL,
  `c_module`     varchar(64)  DEFAULT NULL,
  `c_item`       varchar(64)  DEFAULT NULL,
  `c_describe`   varchar(128) DEFAULT NULL,
  `c_value`      varchar(128) DEFAULT NULL,
  `c_createtime` varchar(20)  DEFAULT NULL,
  `c_updatetime` varchar(20)  DEFAULT NULL
) 
ENGINE=InnoDB DEFAULT CHARSET=utf8;