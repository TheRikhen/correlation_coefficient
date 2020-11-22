from csv import DictReader
import pandas as pd


def fill_cluster(args):
    data = pd.read_csv('users_info.csv')
    new_data = data.dropna(subset=['Age', 'Photos', 'City_id'])
    df = pd.DataFrame(new_data, columns=args)
    df['Age'] = df['Age'].astype(int)
    cor_coef(df)


def cor_coef(varieties):
    print(varieties)
    print(varieties.corr())


def main():
    fill_cluster(['Age', 'Profile_entries'])


if __name__ == '__main__':
    main()
