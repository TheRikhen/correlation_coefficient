from csv import DictReader
import pandas as pd


def fill_cluster(first, second):
    varieties = []
    with open('users_info.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        try:
            for row in csv_dict_reader:
                if row['Age'] != '' and row['City'] != '' and row['City_id'] != '':
                    varieties.append([int(row[first]), int(row[second])])
        except:
            pass
    cor_coef(varieties)


def cor_coef(varieties):
    df = pd.DataFrame(data=varieties)
    print(df)
    print(df.corr())


def main():
    fill_cluster('Photos', 'Profile_entries')


if __name__ == '__main__':
    main()
