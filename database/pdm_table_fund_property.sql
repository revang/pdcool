drop table fund_property
create table fund_property
(
    fund_code   varchar(20)  comment '基金代码' not null,
    fund_name   varchar(64)  comment '基金名称',
    fund_type   varchar(20)  comment '基金类型',
    fund_asset  double(16,2) comment '资产规模',
    stock_list  varchar(20)  comment '持仓股票',
    update_date varchar(20)  comment '修改日期',
    primary key(fund_code)
) engine=innodb default charset=utf8mb4;

insert into fund_property(fund_code,fund_name)
select c_fina_code,c_name from tfund;