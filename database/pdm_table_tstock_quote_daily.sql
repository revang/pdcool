create table tstock_quote_daily
(
    c_fina_code               varchar(20)  comment '证券代码' not null,
    c_trade_date              varchar(20)  comment '交易日期' not null,
    n_prev_close_price        double(16,4) comment '前收盘价',
    n_open_price              double(16,4) comment '开盘价',
    n_high_price              double(16,4) comment '最高价',
    n_low_price               double(16,4) comment '最低价',
    n_close_price             double(16,4) comment '收盘价',
    n_avg_price               double(16,4) comment '变动均价',
    n_px_change               double(16,4) comment '价格涨跌',
    n_px_change_rate          double(16,4) comment '涨跌幅',
    n_turnover_ratio          double(16,4) comment '换手率',
    n_business_balance        double(16,4) comment '成交额',
    l_turnover_deals          int          comment '成交笔数',
    n_amplitude               double(16,4) comment '振幅',
    n_issue_price_change      double(16,4) comment '相对发行价涨跌',
    n_issue_price_change_rate double(16,4) comment '相对发行价涨跌幅（%）',
    c_recently_trading_date   varchar(20)  comment '最近交易日期',
    n_ratio_adjust_factor     double(16,4) comment '复权因子',
    n_business_amount         double(16,4) comment '成交数量',
    c_up_down_status          varchar(20)  comment '涨跌停状态',
    c_turnover_status         varchar(20)  comment '交易状态',
    c_source                  varchar(20)  comment '数据来源',
    c_create_time             varchar(20)  comment '创建时间',
    c_update_time             varchar(20)  comment '修改时间',
    primary key(c_fina_code,c_trade_date)
) 
engine=innodb default charset=utf8mb4;
