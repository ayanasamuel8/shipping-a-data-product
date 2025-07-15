SELECT DISTINCT
    DATE(date) AS date,
    EXTRACT(DOW FROM date) AS weekday,
    EXTRACT(WEEK FROM date) AS week,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(YEAR FROM date) AS year
FROM {{ ref('stg_telegram_messages') }}