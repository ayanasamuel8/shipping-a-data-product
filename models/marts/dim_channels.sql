SELECT DISTINCT
    channel AS channel_name
FROM {{ ref('stg_telegram_messages') }}