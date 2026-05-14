CREATE TABLE records (

    record_id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id TEXT,

    mentor_id TEXT,

    interview_datetime TEXT,

    problem_statement TEXT,

    interview_summary TEXT,

    follow_up_actions TEXT
);

CREATE TABLE logs (

    log_id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id TEXT,

    login_time TEXT,

    logout_time TEXT,

    used_function TEXT
);