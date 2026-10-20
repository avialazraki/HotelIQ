
-- HotelIQ Advanced SQL Analysis
-- Compare each hotel type's cancellation rate
-- against the overall cancellation rate.

SELECT
    h.hotel,
    COUNT(*) AS total_bookings,
    SUM(h.is_canceled) AS canceled_bookings,
    ROUND(
        AVG(h.is_canceled::numeric) * 100, 2
    ) AS hotel_cancellation_rate,
    overall.overall_cancellation_rate
FROM public.bookings AS h
CROSS JOIN (
    SELECT
        ROUND(
            AVG(is_canceled::numeric) * 100, 2
        ) AS overall_cancellation_rate
    FROM public.bookings
) AS overall
GROUP BY
    h.hotel,
    overall.overall_cancellation_rate
ORDER BY
    hotel_cancellation_rate DESC;
