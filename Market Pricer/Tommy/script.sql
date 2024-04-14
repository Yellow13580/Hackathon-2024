drop table item cascade constraints;
create table item(
    item_name varchar2(255),
    item_price number(10, 2),
    item_price_per_unit varchar2(255),
    primary key (item_name)
);
