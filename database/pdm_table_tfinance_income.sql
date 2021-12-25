create table tfinance_income
(
    c_date            varchar(20)  comment '收益日期' not null,
    c_channel         varchar(20)  comment '销售渠道' not null,
    c_user_code       varchar(20)  comment '用户代码' not null,
    c_fina_code       varchar(20)  comment '金融代码' not null,
    c_fina_type       varchar(20)  comment '金融类型' not null,
    n_cost            double(16,4) comment '成本',
    n_sell            double(16,4) comment '卖出金额',
    n_share           double(16,4) comment '当前份额', 
    n_price           double(16,4) comment '当日价格',
    n_pre_price       double(16,4) comment '昨日价格',
    n_today_cost      double(16,4) comment '当日成本(新增)',
    n_today_sell      double(16,4) comment '当日卖出金额(新增)',
    n_today_inc_share double(16,4) comment '当日买入份额(新增)',
    n_today_dec_share double(16,4) comment '当日卖出份额(新增)',
    n_today_income    double(16,4) comment '当日收益', -- 需要计算
    n_total_income    double(16,4) comment '累计收益', -- 需要计算
    c_create_time     varchar(20)  comment '创建时间',
    c_update_time     varchar(20)  comment '修改时间',
    primary key(c_date,c_channel,c_user_code,c_fina_code,c_fina_type)
)
engine=innodb default charset=utf8mb4;

-- c_channel 
-- antfortune    蚂蚁财富
-- eastmoney     东方财富
-- eastmoneyfund 天天基金
-- danjuan       蛋卷基金
-- xqfund        兴证全球基金