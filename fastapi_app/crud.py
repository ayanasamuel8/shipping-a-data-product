from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_top_products(db: Session, limit: int = 10):
    keywords = ['paracetamol', 'amoxicillin', 'ibuprofen', 'vitamin', 'insulin', 'metformin', 'antibiotic', 'cream', 'syrup', 'tablet']

    union_queries = [
        f"""
        SELECT '{kw}' AS product, COUNT(*) AS count
        FROM analytics.fct_messages
        WHERE LOWER(message) LIKE '%{kw}%'
        """ for kw in keywords
    ]

    final_query = f"""
        SELECT product, SUM(count) AS count
        FROM (
            {" UNION ALL ".join(union_queries)}
        ) AS all_products
        GROUP BY product
        ORDER BY count DESC
        LIMIT :limit
    """

    return db.execute(text(final_query), {"limit": limit}).fetchall()




def get_channel_activity(db: Session, channel: str):
    query = text("""
        SELECT date, COUNT(*) AS message_count
        FROM analytics.fct_messages
        WHERE channel = :channel
        GROUP BY date
        ORDER BY date
    """)
    return db.execute(query, {"channel": channel}).fetchall()


def search_messages(db: Session, query_string: str):
    query = text("""
        SELECT message_id, message, channel
        FROM analytics.fct_messages
        WHERE message ILIKE :query
        LIMIT 50
    """)
    return db.execute(query, {"query": f"%{query_string}%"}).fetchall()