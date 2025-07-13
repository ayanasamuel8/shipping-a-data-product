SELECT
    message_id,
    DATE(date) AS date,
    channel,
    LENGTH(message) AS message_length,
    has_photo
FROM {{ ref('stg_telegram_messages') }}