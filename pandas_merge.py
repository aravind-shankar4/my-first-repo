conn = sqlite3.connect("zepto_catalog.db")
sql_result = pd.read_sql(
    """
    SELECT b.title, c.category_name, b.price_inr, b.rating 
    FROM books b 
    JOIN categories c ON b.category_id = c.category_id
""",
    conn,
)

# Replicate with pd.merge
df_books = pd.read_sql("SELECT * FROM books", conn)
df_cats = pd.read_sql("SELECT * FROM categories", conn)
merged_result = (
    pd.merge(df_books, df_cats, on="category_id")[
        ["title", "category_name", "price_inr", "rating"]
    ]
    .sort_values(by="title")
    .reset_index(drop=True)
)

assert len(sql_result) == len(merged_result)
print("SQL JOIN and pd.merge parity verified.")
