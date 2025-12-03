import module as m


def main() -> None:
    print(m.check_leap_yaer(1952))
    
    print(m.day_of_date(19,11,2002))
    
    print(f"{m.week_num(10,10,2024) = }")

if __name__ == "__main__":
    main()