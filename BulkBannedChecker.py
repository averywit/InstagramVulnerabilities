import json
import threading
from queue import Queue
from urllib.parse import quote_plus
import random
import requests
from termcolor import colored
from colorama import init
init(autoreset=True)


# All the Instagram versions to add more randomization to requests.
def random_version():
    versions = [
        "359.2.0.64.89",
        "359.0.0.59.89",
        "358.0.0.51.97",
        "357.0.0.51.100",
        "356.0.0.41.101",
        "355.1.0.46.103",
        "355.1.0.44.103",
        "354.2.0.47.100",
        "353.2.0.49.90",
        "353.1.0.47.90",
        "352.1.0.41.100",
        "352.0.0.38.100",
        "352.0.0.32.100",
        "349.3.0.42.104",
        "346.1.0.46.104",
        "344.1.0.42.92",
        "344.0.0.42.92",
        "343.0.0.33.101",
        "341.0.0.45.100",
        "340.0.0.22.109",
        "339.0.0.30.105",
        "338.0.0.31.95",
        "336.0.0.35.90",
        "335.0.0.39.93",
        "334.0.0.42.95",
        "330.0.0.40.92",
        "328.0.0.42.90",
        "327.2.0.50.93",
        "326.0.0.42.90",
        "325.0.0.35.91",
        "324.0.0.27.50",
        "323.0.0.35.65",
        "322.0.0.37.95",
        "320.0.0.42.101",
        "319.0.0.43.110",
        "317.0.0.34.109",
        "316.0.0.38.109",
        "315.0.0.29.109",
        "314.0.0.20.114",
        "312.0.0.33.111",
        "311.0.0.32.118",
        "309.1.0.41.113",
        "309.0.0.40.113",
        "308.0.0.36.109",
        "307.0.0.34.111",
        "306.0.0.35.109",
        "304.0.0.35.106",
        "303.0.0.40.109",
        "302.1.0.36.111",
        "302.0.0.34.111",
        "301.1.0.33.110",
        "301.0.0.33.110",
        "301.0.0.28.110",
        "301.0.0.27.110",
        "300.0.0.29.110",
        "300.0.0.0.44",
        "299.0.0.34.111",
        "298.0.0.31.110",
        "297.0.0.33.109",
        "296.0.0.35.109",
        "295.0.0.32.109",
        "294.0.0.33.87",
        "294.0.4.0.15",
        "293.0.2.28.93",
        "293.0.2.0.28",
        "293.0.2.0.20",
        "293.0.2.0.11",
        "293.0.2.0.6",
        "292.0.0.31.110",
        "292.0.0.26.110",
        "292.0.0.18.110",
        "292.0.0.16.110",
        "291.1.0.34.111",
        "290.0.0.13.76",
        "289.0.0.25.49",
        "288.1.0.22.66",
        "287.0.0.25.77",
        "286.0.0.20.69",
        "285.0.0.25.62",
        "284.0.0.22.85",
        "283.0.0.20.105",
        "282.0.0.22.119",
        "281.0.0.19.105",
        "280.0.0.18.114",
        "279.0.0.23.112",
        "279.0.0.18.112",
        "278.0.0.22.117",
        "278.0.0.21.117",
        "277.0.0.17.107",
        "276.1.0.26.103",
        "276.0.0.26.103",
        "275.0.0.27.98",
        "274.0.0.26.90",
        "274.0.0.21.90",
        "273.1.0.16.72",
        "273.0.0.16.72",
        "272.0.0.16.73",
        "271.1.0.21.84",
        "271.0.0.20.84",
        "270.2.0.24.82",
        "270.0.0.23.82",
        "269.0.0.18.75",
        "269.0.0.14.75",
        "268.0.0.18.72",
        "268.0.0.13.72",
        "268.0.0.9.72",
        "267.0.0.18.93",
        "266.0.0.19.106",
        "265.0.0.19.301",
        "265.0.0.1.301",
        "264.0.0.22.106",
        "264.0.0.0.99",
        "263.2.0.19.104",
        "263.0.0.19.104",
        "262.0.0.24.327",
        "261.0.0.21.111",
        "260.0.0.23.115",
        "259.1.0.29.104",
        "259.0.0.29.104",
        "259.0.0.16.104",
        "258.1.0.26.100",
        "258.0.0.26.100",
        "257.1.0.16.110",
        "257.0.0.16.110",
        "256.0.0.18.105",
        "255.1.0.17.102",
        "254.0.0.19.109",
        "253.0.0.23.114",
        "253.0.0.20.114",
        "253.0.0.17.114",
        "252.0.0.17.111",
        "252.0.0.10.111",
        "251.1.0.11.106",
        "251.0.0.11.106",
        "250.0.0.21.109",
        "249.0.0.20.105",
        "248.0.0.17.109",
        "247.0.0.17.113",
        "247.0.0.11.113",
        "246.0.0.16.113",
        "245.0.0.18.108",
        "244.1.0.19.110",
        "244.0.0.17.110",
        "243.0.0.16.111",
        "242.0.0.16.111",
        "242.0.0.13.111",
        "241.1.0.18.114",
        "240.2.0.18.107",
        "239.0.0.14.111",
        "238.0.0.14.112",
        "238.0.0.0.105",
        "236.0.0.20.109",
        "235.0.0.21.107",
        "234.0.0.19.113",
        "233.0.0.13.112",
        "230.0.0.20.108",
        "230.0.0.16.108",
        "229.0.0.17.118",
        "228.0.0.15.111",
        "227.0.0.12.117",
        "226.0.0.16.117",
        "225.0.0.19.115",
        "225.0.0.0.42",
        "224.1.0.20.116",
        "224.0.0.0.43",
        "223.0.0.12.103",
        "223.0.0.9.103",
        "223.0.0.0.97",
        "223.0.0.0.84",
        "222.0.0.15.114",
        "221.0.0.16.118",
        "220.0.0.16.115",
        "219.0.0.12.117",
        "218.0.0.19.108",
        "216.1.0.21.137",
        "215.0.0.27.359",
        "215.0.0.0.230",
        "214.1.0.29.120",
        "214.0.0.27.120",
        "214.0.0.24.120",
        "214.0.0.21.120",
        "214.0.0.6.120",
        "213.0.0.29.120",
        "212.0.0.38.119",
        "212.0.0.29.119",
        "212.0.0.14.119",
        "210.0.0.28.71",
        "209.0.0.21.119",
        "208.0.0.32.135",
        "208.0.0.0.101",
        "207.0.0.25.120",
        "206.1.0.34.121",
        "205.0.0.34.114",
        "204.0.0.30.119",
        "203.0.0.29.118",
        "203.0.0.0.100",
        "202.0.0.26.123",
        "202.0.0.19.123",
        "202.0.0.6.123",
        "200.1.0.29.121",
        "200.0.0.29.121",
        "200.0.0.26.121",
        "199.1.0.34.119",
        "199.0.0.34.119",
        "199.0.0.32.119",
        "198.0.0.32.120",
        "198.0.0.23.120",
        "197.0.0.26.119",
        "196.0.0.32.126",
        "195.0.0.31.123",
        "195.0.0.30.123",
        "194.0.0.36.172",
        "194.0.0.32.172",
        "194.0.0.23.172",
        "194.0.0.18.172",
        "193.0.0.45.120",
        "192.0.0.35.123",
        "191.1.0.41.124",
        "191.0.0.40.124",
        "191.0.0.37.124",
        "191.0.0.32.124",
        "190.0.0.36.119",
        "190.0.0.2.119",
        "188.0.0.35.124",
        "187.0.0.32.120",
        "187.0.0.23.120",
        "186.0.0.36.128",
        "185.0.0.38.116",
        "184.0.0.30.117",
        "183.0.0.35.116",
        "183.0.0.27.116",
        "183.0.0.0.40",
        "182.0.0.2.124",
        "181.0.0.33.117",
        "180.0.0.31.119",
        "179.0.0.26.132",
        "178.1.0.37.123",
        "177.0.0.30.119",
        "176.0.0.38.116",
        "175.1.0.25.119",
        "175.0.0.23.119",
        "175.0.0.19.119",
        "174.0.0.31.132",
        "173.0.0.39.120",
        "173.0.0.31.120",
        "172.0.0.21.123",
        "171.0.0.29.121",
        "171.0.0.21.121",
        "170.0.0.30.474",
        "169.3.0.30.135",
        "169.1.0.29.135",
        "169.0.0.28.135",
        "169.0.0.17.135",
        "169.0.0.11.135",
        "170.0.0.0.18",
        "169.0.0.7.135",
        "170.0.0.0.1",
        "169.0.0.0.136",
        "169.0.0.0.121",
        "168.0.0.40.355",
        "168.0.0.37.355",
        "169.0.0.0.83",
        "168.0.0.36.355",
        "169.0.0.0.60",
        "168.0.0.30.355",
        "168.0.0.21.355",
        "168.0.0.8.355",
        "168.0.0.4.355",
        "169.0.0.0.2",
        "168.0.0.1.354",
        "167.1.0.25.120",
        "168.0.0.0.188",
        "168.0.0.0.146",
        "167.0.0.24.120",
        "167.0.0.22.120",
        "167.0.0.16.120",
        "167.0.0.12.120",
        "168.0.0.0.19",
        "167.0.0.7.120",
        "166.1.0.42.245",
        "168.0.0.0.10",
        "167.0.0.4.120",
        "166.0.0.41.245",
        "168.0.0.0.1",
        "167.0.0.0.109",
        "166.0.0.37.245",
        "166.0.0.33.245",
        "167.0.0.0.55",
        "166.0.0.29.245",
        "167.0.0.0.41",
        "166.0.0.19.245",
        "166.0.0.8.245",
        "167.0.0.0.13",
        "166.0.0.6.245",
        "166.0.0.0.184",
        "166.0.0.0.149",
        "166.0.0.0.139",
        "165.1.0.29.119",
        "165.0.0.28.119",
        "166.0.0.0.100",
        "165.0.0.25.119",
        "165.0.0.22.119",
        "165.0.0.17.119",
        "164.0.0.46.123",
        "163.0.0.45.122",
        "163.0.0.39.122",
        "163.0.0.30.122",
        "163.0.0.15.122",
        "162.0.0.42.125",
        "161.0.0.37.121",
        "161.0.0.20.121",
        "161.0.0.1.121",
        "160.0.0.25.132",
        "159.0.0.40.122",
        "159.0.0.29.122",
        "158.0.0.30.123",
        "157.0.0.37.120",
        "157.0.0.29.120",
        "156.0.0.26.109",
        "155.0.0.37.107",
        "155.0.0.23.107",
        "156.0.0.0.41",
        "154.0.0.26.123",
        "153.0.0.34.96",
        "152.0.0.25.117",
        "152.0.0.20.117",
        "151.0.0.23.120",
        "152.0.0.1.60",
        "150.0.0.33.120",
        "149.0.0.25.120",
        "148.0.0.33.121",
        "149.0.0.0.116",
        "148.0.0.15.121",
        "147.0.0.42.124",
        "147.0.0.22.124",
        "146.0.0.27.125",
        "145.0.0.32.119",
        "145.0.0.28.119",
        "145.0.0.11.119",
        "144.0.0.20.119",
        "143.0.0.25.121",
        "142.0.0.34.110",
        "141.0.0.32.118",
        "140.0.0.30.126",
        "139.0.0.28.121",
        "138.0.0.28.117",
        "137.0.0.31.123",
        "137.0.0.17.122",
        "136.0.0.34.124",
        "135.0.0.28.119",
        "134.0.0.26.121",
        "133.0.0.32.120",
        "132.0.0.26.134",
        "132.0.0.21.134",
        "132.0.0.8.134",
        "131.0.0.25.116",
        "132.0.0.0.118",
        "132.0.0.0.67",
        "131.0.0.18.116",
        "131.0.0.1.116",
        "130.0.0.31.121",
        "129.0.0.29.119",
        "129.0.0.17.119",
        "128.0.0.26.128",
        "128.0.0.19.128",
        "128.0.0.7.128",
        "127.0.0.30.121",
        "127.0.0.22.121",
        "126.0.0.25.121",
        "126.0.0.18.121",
        "126.0.0.8.121",
        "124.0.0.17.473",
        "124.0.0.11.473",
        "124.0.0.8.473",
        "124.0.0.2.473",
        "123.0.0.21.114",
        "123.0.0.11.114",
        "122.0.0.29.238",
        "122.0.0.1.238",
        "121.0.0.29.119",
        "121.0.0.24.119",
        "120.0.0.29.118",
        "120.0.0.15.115",
        "119.0.0.33.147",
        "119.0.0.19.147",
        "117.0.0.28.123",
        "116.0.0.34.121",
        "116.0.0.25.121",
        "115.0.0.26.111",
        "115.0.0.25.111",
        "115.0.0.18.111",
        "114.0.0.30.120",
        "113.0.0.39.122",
        "112.0.0.29.121",
        "112.0.0.16.121",
        "111.0.0.24.152",
        "111.0.0.9.152",
        "110.0.0.16.119",
        "110.0.0.11.119",
        "109.0.0.18.124",
        "109.0.0.15.124",
        "109.0.0.13.124",
        "108.0.0.23.119",
        "109.0.0.3.124",
        "107.0.0.21.121",
        "106.0.0.24.118",
        "106.0.0.22.118",
        "106.0.0.17.118",
        "105.0.0.18.119",
        "104.0.0.21.118",
        "103.1.0.15.119",
        "103.0.0.7.119",
        "104.0.0.0.45",
        "103.0.0.3.119",
        "102.0.0.20.117",
        "103.0.0.0.80",
        "102.0.0.13.117",
        "103.0.0.0.61",
        "102.0.0.10.117",
        "103.0.0.0.51",
        "102.0.0.8.117",
        "103.0.0.0.32",
        "102.0.0.5.117",
        "101.0.0.15.120"
    ]
    return random.choice(versions)


class Worker(threading.Thread):

    def __init__(self, job_queue, max_retries=10):
        super().__init__()

        # Assigns the job queue to the worker.
        # This is filled with the Instagram usernames to check.
        self._job_queue = job_queue

        # Sets the maximum retries (10) for failed requests.
        self._max_retries = max_retries

    def run(self):

        # Runs worker until "None" is reached.
        # None = No combinations are left to check.
        while True:

            # Retrieves a "ue_entry" username:email from "job_queue".
            ue_entry = self._job_queue.get()

            # Breaks loop when "None" is retrieved from "job_queue".
            if ue_entry is None:
                break

            retries = 0

            # Retry loop that makes multithreading happy.
            # Most of the time, this will not loop. It is just for safety.
            while retries < self._max_retries:
                try:
                    # ADD RESIDENTIAL PROXIES HERE
                    # ******** REQUIRED *********
                    proxy_username = ""
                    proxy_password = ""
                    proxy_site = ""
                    proxy_port = ""

                    proxies = {
                        "http": f"http://{proxy_username}:{proxy_password}@{proxy_site}:{proxy_port}",
                        "https": f"http://{proxy_username}:{proxy_password}@{proxy_site}:{proxy_port}"
                    }

                    # Splits the "ue_entry" into a "user" and "email" variable.
                    user, email = ue_entry.strip().split(':')

                    # Data, including the email, required to make the banned account check.
                    data = "signed_body=SIGNATURE." + quote_plus(
                        json.dumps({"q": email, "skip_recovery": "1"}, separators=(",", ":")))

                    # Headers, including a random Instagram version, required to make the banned account check.
                    headers = {
                        "Accept-Language": "en-US",
                        "User-Agent": "Instagram " + random_version(),
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Accept-Encoding": "gzip, deflate",
                        "X-FB-HTTP-Engine": "Liger",
                        "Connection": "keep-alive",
                        "Content-Length": str(len(data))
                    }

                    # Make the request, completing banned account check.
                    # Timeout of 5 seconds in case of a bad proxy.
                    response = requests.post(url="https://i.instagram.com/api/v1/users/lookup/", headers=headers, data=data, proxies=proxies, timeout=5)

                    # Status code: 200 = Normal, user is not banned
                    if response.status_code == 200:
                        print(colored(f"Active user: {user}", "green"))
                        f = open("ClaimableUsers.txt", "a")
                        f.write(ue_entry)
                        f.close()

                        # Exits the retry loop because a successful check was completed.
                        break

                    # Status code: 404 = Normal, user is banned
                    elif response.status_code == 404:
                        print(colored(f"Banned user: {user}", "red"))

                        # Exits the retry loop because a successful check was completed.
                        break

                    # Status code: 429 = Your proxies are low quality
                    else:
                        print(colored(f"Failed check: {user}", "yellow"))

                    # Bad request, repeat it.
                    # Any bad request will trigger the exception below.

                # Increases the counter for total retries of checking the combination.
                except:
                    retries += 1


if __name__ == '__main__':
    
    # List that includes all the .txt user:email pairs
    entries = []

    # ADD .TXT FILE INTO "ue_list" TO CHECK USER:EMAIL PAIRS
    # ******************* REQUIRED *******************
    ue_list = ""
    with open(ue_list, 'r') as in_file:
        for line in in_file:
            entries.append(line)

    jobs = []
    job_queue = Queue()

    for i in range(120):
        p = Worker(job_queue)
        jobs.append(p)
        p.start()

    for entry in entries:
        job_queue.put(entry)

    for j in jobs:
        job_queue.put(None)

    for j in jobs:
        j.join()
