from hour_formatting import get_hour, sum_hours


def main():
    hour_1 = get_hour('Introduce una hora a continuación')
    hour_2 = get_hour('Introduce una hora a continuación')

    print(sum_hours(hour_1, hour_2))


if __name__ == '__main__':
    main()
