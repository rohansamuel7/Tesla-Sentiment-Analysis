-- YouTube data table
CREATE TABLE IF NOT EXISTS youtube_data (
    id SERIAL PRIMARY KEY,
    video_id VARCHAR(255),
    title TEXT,
    description TEXT,
    comment TEXT,
    published_at TIMESTAMP,
    like_count INTEGER,
    view_count INTEGER,
    sentiment_score FLOAT
);

-- Reddit data table
CREATE TABLE IF NOT EXISTS reddit_data (
    id SERIAL PRIMARY KEY,
    post_id VARCHAR(255),
    title TEXT,
    post_text TEXT,
    comment TEXT,
    created_at TIMESTAMP,
    upvotes INTEGER,
    sentiment_score FLOAT
);

-- News data table
CREATE TABLE IF NOT EXISTS news_data (
    id SERIAL PRIMARY KEY,
    article_id VARCHAR(255),
    title TEXT,
    description TEXT,
    published_at TIMESTAMP,
    source_name VARCHAR(255),
    sentiment_score FLOAT
);
