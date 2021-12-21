-- 关注金融产品
create table tfinance_follow
(
    c_user_code   varchar(20) comment '用户代码' not null,
    c_fina_code   varchar(20) comment '金融代码' not null,
    c_fina_type   varchar(20) comment '金融类型' not null,
    c_create_time varchar(20) comment '创建时间',
    c_update_time varchar(20) comment '修改时间',
    primary key(c_user_code,c_fina_code,c_fina_type)
)
engine=innodb default charset=utf8mb4;