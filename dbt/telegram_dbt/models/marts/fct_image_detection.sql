SELECT
    id AS detection_id,
    message_id,
    object_class,
    confidence
FROM analytics.fct_image_detections