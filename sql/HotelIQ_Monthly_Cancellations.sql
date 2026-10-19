-- View: public.vw_monthly_cancellations

-- DROP VIEW public.vw_monthly_cancellations;

CREATE OR REPLACE VIEW public.vw_monthly_cancellations
 AS
 SELECT hotel,
    EXTRACT(year FROM arrival_date)::integer AS arrival_year,
    EXTRACT(month FROM arrival_date)::integer AS arrival_month,
    count(*) AS total_bookings,
    sum(is_canceled) AS canceled_bookings,
    round(avg(is_canceled::numeric) * 100::numeric, 2) AS cancellation_rate
   FROM bookings
  GROUP BY hotel, (EXTRACT(year FROM arrival_date)), (EXTRACT(month FROM arrival_date));

ALTER TABLE public.vw_monthly_cancellations
    OWNER TO postgres;

