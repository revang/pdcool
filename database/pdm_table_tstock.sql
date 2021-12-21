-- V1.0.0 初始化表
/*
create table tstock
(
    c_code            varchar(20) comment '股票代码' not null,
    c_exchange_market varchar(20) comment '交易市场' not null,
    c_name            varchar(64) comment '股票名称',
    c_source          varchar(20) comment '数据来源',
    c_create_time     varchar(20) comment '创建时间',
    c_update_time     varchar(20) comment '修改时间',
    primary key(c_code,c_exchange_market),
    key idx_stock_name(c_name)
) engine=innodb default charset=utf8mb4;
 */

-- V1.0.1 基于恒有数扩展字段（包含历史数据迁移）
/*
alter table tstock rename to tbak_stock;

create table tstock
(
    c_code            varchar(20) comment '股票代码' not null,
    c_exchange_market varchar(20) comment '交易市场' not null,
    c_name            varchar(64) comment '股票名称',
    c_full_name       varchar(64) comment '公司全称',
    c_listed_state    varchar(20) comment '上市状态',
    c_listed_sector   varchar(20) comment '上市板块',
    c_source          varchar(20) comment '数据来源',
    c_create_time     varchar(20) comment '创建时间',
    c_update_time     varchar(20) comment '修改时间',
    primary key(c_code,c_exchange_market),
    key idx_stock_name(c_name)
) engine=innodb default charset=utf8mb4;

insert into tstock(c_code,c_exchange_market,c_name,c_source,c_create_time,c_update_time) 
select c_code,c_exchange_market,c_name,c_source,c_create_time,c_update_time from tbak_stock;

select * from tstock;

drop table tbak_stock;
 */

/*
create table tstock
(
    c_code            varchar(20) comment '股票代码' not null,
    c_exchange_market varchar(20) comment '交易市场' not null,
    c_name            varchar(64) comment '股票名称',
    c_full_name       varchar(64) comment '公司全称',
    c_listed_state    varchar(20) comment '上市状态',
    c_listed_sector   varchar(20) comment '上市板块',
    c_source          varchar(20) comment '数据来源',
    c_create_time     varchar(20) comment '创建时间',
    c_update_time     varchar(20) comment '修改时间',
    primary key(c_code,c_exchange_market),
    key idx_stock_name(c_name)
) engine=innodb default charset=utf8mb4;
 */

-- V1.0.2 增加fina_code，配合stock_daily_quote调整（包含历史数据迁移）
/*
alter table tstock rename to tbak_stock;

create table tstock
(
    c_fina_code       varchar(20) comment '证券代码' not null,
    c_code            varchar(20) comment '股票代码' not null,
    c_exchange        varchar(20) comment '交易市场' not null,
    c_name            varchar(64) comment '股票名称',
    c_full_name       varchar(64) comment '公司全称',
    c_listed_state    varchar(20) comment '上市状态',
    c_listed_sector   varchar(20) comment '上市板块',
    c_source          varchar(20) comment '数据来源',
    c_create_time     varchar(20) comment '创建时间',
    c_update_time     varchar(20) comment '修改时间',
    primary key(c_fina_code),
    key idx_stock_1(c_code),
    key idx_stock_2(c_name)
) engine=innodb default charset=utf8mb4;

insert into tstock(c_fina_code, c_code,c_exchange,c_name,c_source,c_create_time,c_update_time) 
select concat(c_code,'.',c_exchange_market),
       c_code,
       c_exchange_market,
       c_name,
       c_source,
       c_create_time,
       c_update_time
  from tbak_stock;

select * from tstock;

drop table tbak_stock;
 */

/*
create table tstock
(
    c_fina_code       varchar(20) comment '证券代码' not null,
    c_code            varchar(20) comment '股票代码' not null,
    c_exchange        varchar(20) comment '交易市场' not null,
    c_name            varchar(64) comment '股票名称',
    c_full_name       varchar(64) comment '公司全称',
    c_listed_state    varchar(20) comment '上市状态',
    c_listed_sector   varchar(20) comment '上市板块',
    c_source          varchar(20) comment '数据来源',
    c_create_time     varchar(20) comment '创建时间',
    c_update_time     varchar(20) comment '修改时间',
    primary key(c_fina_code),
    key idx_stock_1(c_code),
    key idx_stock_2(c_name)
) engine=innodb default charset=utf8mb4;
 */

-- V1.0.3 基于tushare扩展字段和调整列名
create table tstock
(
    c_fina_code       varchar(20)  comment '证券代码' not null,
    c_code            varchar(20)  comment '股票代码' not null,
    c_exchange        varchar(20)  comment '交易市场' not null,
    c_name            varchar(64)  comment '股票名称',
    c_fullname        varchar(64)  comment '股票全称',
    c_enname          varchar(128) comment '英文全称',
    c_cnspell         varchar(64)  comment '拼音缩写',
    c_area            varchar(64)  comment '地域',
    c_industry        varchar(64)  comment '所属行业',
    c_list_status     varchar(20)  comment '上市状态',
    c_list_board      varchar(20)  comment '上市板块',
    c_list_date       varchar(20)  comment '上市日期',
    c_delist_date     varchar(20)  comment '退市日期',
    c_curr_type       varchar(20)  comment '交易货币',
    c_shsc            varchar(20)  comment '沪港通标的',
    c_source          varchar(20)  comment '数据来源',
    c_create_time     varchar(20)  comment '创建时间',
    c_update_time     varchar(20)  comment '修改时间',
    primary key(c_fina_code),
    key idx_stock_1(c_code),
    key idx_stock_2(c_name)
) engine=innodb default charset=utf8mb4;