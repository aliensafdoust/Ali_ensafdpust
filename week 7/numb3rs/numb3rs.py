def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ips):
    ips = ips.split(".")
    try:
        for ip in ips:
            if len(ips) == 4 and int(ip) <= 255 and int(ip) >= 0:
                continue
            else:
                raise ValueError
    except ValueError:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
