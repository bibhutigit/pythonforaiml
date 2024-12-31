import pandas as pd

# SF Salaries Kaggle
sal = pd.read_csv("Salaries.csv")
print(sal.columns)

# Check head of the dataframe
sal_head = sal.head()

# Get Avg BasePay
base_pay_df = pd.to_numeric(sal["BasePay"],errors="coerce")
print(base_pay_df.mean())

# Get Maximum OvertimePay
overtime_pay_df = pd.to_numeric(sal["OvertimePay"],errors="coerce")
print(overtime_pay_df.max())

# Get Job Title Of "JOSEPH DRISCOLL"
job_title_df = sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]
print(job_title_df)

# How much "JOSEPH DRISCOLL" make including benefits
total_pay_benefits_df = sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"]
print(total_pay_benefits_df)

# What is the name of highest paid person including benefits
highest_paid_df = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]["EmployeeName"]
print(highest_paid_df)

# What is the name of lowest paid person including benefits
lowest_paid_df = sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()]["EmployeeName"]
print(lowest_paid_df)
# OR
alternate_lowest_paid_df = sal.iloc[sal["TotalPayBenefits"].argmin()]["EmployeeName"]
print(alternate_lowest_paid_df)

# Average BasePay of all Employees per year
sal["BasePay"] = pd.to_numeric(sal["BasePay"],errors="coerce")
base_pay_year_wise_df = sal[["Year","BasePay"]]
avg_base_pay_year_df = sal.groupby("Year")["BasePay"].mean()
print(avg_base_pay_year_df)

# How many unique job titles are there.
unique_job_titles_df = sal["JobTitle"].nunique()
print(unique_job_titles_df)

# 5 most common Jobs
job_title_group_by_df = sal.groupby("JobTitle")["Id"].count()
job_title_count = job_title_group_by_df.reset_index(name="title_count")
top_job_titles = job_title_count.sort_values("title_count",ascending=False)
top_5_job_titles = top_job_titles.head(5)
print(top_5_job_titles)
# Or
top_five_job_titles_df = sal["JobTitle"].value_counts().head(5)
print(top_five_job_titles_df)

# How many Job Titles were represented by only one person in 2013?
filtered_df = sal[sal["Year"] == 2013][["Id","JobTitle","Year"]]
value_count_df = filtered_df.groupby("JobTitle")["Id"].count()
job_title_count = value_count_df.reset_index(name="title_count")
top_job_titles = job_title_count.sort_values("title_count")
only_one_job_title_count = top_job_titles[top_job_titles["title_count"] == 1]["JobTitle"]
print(only_one_job_title_count.count())

#Or
job_title_count_2013 = sal[sal["Year"] == 2013]["JobTitle"].value_counts().reset_index(name="title_count")
only_one_job_titles = job_title_count_2013[job_title_count_2013["title_count"] == 1]["title_count"]
print(sum(only_one_job_titles))

# How many people have the word Chief in their job title.
def check_substr_in_job_title(title):
    if "chief" in title.lower().split():
        return 1
    else:
        return 0

sal["Is_Contains_Chief"] = sal["JobTitle"].apply(check_substr_in_job_title)
final_df = sal[sal["Is_Contains_Chief"] == 1]["Id"].count()
print(final_df)