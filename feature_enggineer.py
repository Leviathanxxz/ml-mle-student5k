# feature engineering (gunakan def agar bisa dipakai di pipeline)

def feature_engineering(X):
    X = X.copy()
    # buat fitur ratio antara study dan sleep hours 
    X['study_sleep_ratio'] = X['study_hours'] / (X['sleep_hours'] + 1e-5)

    # buat fitur interaksi antara attendance dan study hours
    X['attendance_study_interaction'] = X['attendance'] * X['study_hours']
    return X