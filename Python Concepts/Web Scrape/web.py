from bs4 import BeautifulSoup
import requests,csv,openpyxl

# creating the xlsx file
excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'top rated movies'
print(excel.sheetnames)
sheet.append(['movie name','year','time','IMDB rating'])
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    

    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    
    movies = soup.find('ul',class_= 'ipc-metadata-list ipc-metadata-list--dividers-between sc-71ed9118-0 kxsUNk compact-list-view ipc-metadata-list--base')#.find_all('h3',class_='ipc-title__text')
    
    
    for movie in movies:

        title = movie.find('h3',class_= 'ipc-title__text')

        details = movie.find('div','sc-be6f1408-7 iUtHEN cli-title-metadata').find_all('span',class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item')

        if len(details) >= 3:
            year = details[0].text
            time = details[1].text
            rating = details[2].text

        user_rating = movie.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').get_text(strip=True).split('(')[0]

        # storing in a txt file
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(str(title.text + '---' + year + '---' + time + '---' + rating + '---' + user_rating + '\n'))

        # storing in csv file
        csv_file_name = 'top_movies.csv'

        data = [title.text,year,time,rating,user_rating]
        with open(csv_file_name , 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(data)

        # storing in a xlsx file
        sheet.append(data)





except Exception as e:
    print(e)

# naming the xlsx file
excel.save('top_movies_250.xlsx')