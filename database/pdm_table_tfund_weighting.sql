-- V1.0.0 初始化表(基金权重表/基金成分股票) 
drop table tfund_weighting;
create table tfund_weighting 
(
    c_date           varchar(20)  comment '公布日期' not null,
    c_fund_code      varchar(20)  comment '基金代码' not null,
    c_stock_code     varchar(20)  comment '股票代码' not null,
    c_stock_name     varchar(20)  comment '股票名称',
    n_stock_price    double(16,4) comment '股票价格',
    n_percent        double(16,4) comment '权重比例(%)',
    n_change_percent double(16,4) comment '权重变化比例(%)',
    c_source         varchar(20)  comment '数据来源',
    c_create_time    varchar(20)  comment '创建时间',
    c_update_time    varchar(20)  comment '修改时间',
    primary key(c_date,c_fund_code,c_stock_code)
) engine=innodb default charset=utf8mb4;