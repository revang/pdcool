-- V1.0.0 初始化表
/*
create table tfund
(
    c_code              varchar(20) comment '基金代码' not null,
    c_name              varchar(64) comment '基金名称',
    c_full_name         varchar(64) comment '基金全称',
    c_company_code      varchar(64) comment '基金公司代码',
    c_company_name      varchar(64) comment '基金公司名称',
    c_company_full_name varchar(64) comment '基金公司全称',
    c_foundation_type   varchar(20) comment '基金运作方式',
    c_float_type        varchar(20) comment '发售方式',
    c_source            varchar(20) comment '数据来源',
    c_create_time       varchar(20) comment '创建时间',
    c_update_time       varchar(20) comment '修改时间',
    primary key(c_code),
    key idx_fund_1(c_name)
) engine=innodb default charset=utf8mb4;
*/


-- V1.0.1 增加fina_code, 包含历史数据迁移
alter table tfund rename to tbak_fund;

create table tfund
(
    c_fina_code         varchar(20) comment '金融代码' not null,
    c_code              varchar(20) comment '基金代码',
    c_name              varchar(64) comment '基金名称',
    c_full_name         varchar(64) comment '基金全称',
    c_company_code      varchar(64) comment '基金公司代码',
    c_company_name      varchar(64) comment '基金公司名称',
    c_company_full_name varchar(64) comment '基金公司全称',
    c_foundation_type   varchar(20) comment '基金运作方式',
    c_float_type        varchar(20) comment '发售方式',
    c_source            varchar(20) comment '数据来源',
    c_create_time       varchar(20) comment '创建时间',
    c_update_time       varchar(20) comment '修改时间',
    primary key(c_fina_code),
    key idx_fund_1(c_code),
    key idx_fund_2(c_name)
) engine=innodb default charset=utf8mb4;