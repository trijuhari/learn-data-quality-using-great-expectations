CREATE SCHEMA IF NOT EXISTS app;

CREATE TABLE IF NOT EXISTS app.order(
    order_id varchar(10),
    customer_order_id varchar(15),
    order_status varchar(20),
    order_purchase_timestamp timestamp
);
