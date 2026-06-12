import pandas as pd

def calculate_demographic_data(print_data=True):
    # Đọc dữ liệu từ file csv
    df = pd.read_csv('adult.data.csv')

    # 1. Có bao nhiêu người thuộc mỗi chủng tộc? (Trả về một Series)
    race_count = df['race'].value_counts()

    # 2. Độ tuổi trung bình của nam giới (sex == 'Male')
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Phần trăm những người có bằng Cử nhân (Bachelors)
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 1)

    # 4. Tính toán trình độ học vấn nâng cao (Bachelors, Masters, Doctorate)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # 5. Phần trăm người có học vấn nâng cao lương >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)

    # 6. Phần trăm người KHÔNG có học vấn nâng cao lương >50K
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

    # 7. Số giờ làm việc tối thiểu mỗi tuần là bao nhiêu?
    min_work_hours = df['hours-per-week'].min()

    # 8. Phần trăm những người làm việc tối thiểu mà vẫn có lương >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100, 1)

    # 9. Quốc gia nào có tỷ lệ người kiếm được >50K cao nhất?
    # Tính tổng số người mỗi nước
    country_counts = df['native-country'].value_counts()
    # Tính số người lương >50K mỗi nước
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    # Tính tỷ lệ phần trăm và tìm nước cao nhất
    percentage_rich_by_country = (country_rich_counts / country_counts * 100).round(1)
    
    highest_earning_country = percentage_rich_by_country.idxmax()
    highest_earning_country_percentage = percentage_rich_by_country.max()

    # 10. Nghề nghiệp phổ biến nhất của những người kiếm >50K ở Ấn Độ (India)
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # KHÔNG ĐƯỢC SỬA PHẦN DƯỚI NÀY (Để freeCodeCamp in kết quả)
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }