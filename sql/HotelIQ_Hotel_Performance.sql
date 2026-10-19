-- View: public.vw_hotel_performance

-- DROP VIEW public.vw_hotel_performance;

CREATE OR REPLACE VIEW public.vw_hotel_performance
 AS
 SELECT hotel,
    count(*) AS total_bookings,
    sum(is_canceled) AS canceled_bookings,
    round(avg(is_canceled::numeric) * 100::numeric, 2) AS cancellation_rate,
    round(avg(adr), 2) AS average_adr,
    round(avg(total_nights), 2) AS average_nights
   FROM bookings
  GROUP BY hotel;

ALTER TABLE public.vw_hotel_performance
    OWNER TO postgres;

