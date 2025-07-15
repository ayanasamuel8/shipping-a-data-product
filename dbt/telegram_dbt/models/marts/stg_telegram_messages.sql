WITH source AS (
    SELECT *
    FROM raw.telegram_messages
)

SELECT
    id AS message_id,
    date,
    message,
    from_id,
    channel,
    has_photo,
    raw_json
FROM source