date_list = [ '1983-06-15', '1991-12-07', '1987-03-24', '2001-08-19', '2015-04-03', '1980-11-21', '1999-02-28', '2008-09-12', '1995-01-05', '2020-07-09', '1986-10-30', '1993-05-14', '2011-06-26', '1989-12-18', '2005-03-11', '2018-09-01', '1997-07-20', '2012-11-03', '2023-01-22', '1990-04-09' ]
septembers_date=[]
years_before_2000=0
last_year = '0000'

for date in date_list:
    for year in date:
        if year=='1':
            years_before_2000+=1
            break
        else:
            break
print(years_before_2000)

for date in date_list:
    if '-09-' in date:
        septembers_date.append(date)
print(septembers_date)

for date in date_list:
    year = ''
    for i in range(4):
        year += date[i]
    if year > last_year:
        last_year = year
print(last_year)
