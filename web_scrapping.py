import threading
import requests
import time

websites = ['https://www.python.org', 'https://www.google.com', 'https://www.facebook.com']


def web_scrapping(url):
    try:
        # get response
        response = requests.get(url)
        print(f'Scrapped url: {url}, status: {response.status_code}')
    except Exception as e:
        print(f'Could not scrap url: {url}, error: {e}')


if __name__ == '__main__':
    # using threads
    threads = []
    for website in websites:
        # create thread
        thread = threading.Thread(target=web_scrapping, args=(website,))
        threads.append(thread)

    start_time = time.time()
    for thread in threads:
        # start thread
        thread.start()

    for thread in threads:
        # wait till all the threads are finished
        thread.join()

    end_time = time.time()
    total_time_using_threads = end_time - start_time

    print(f'All the websites scrapped using threads in {end_time - start_time} seconds')

    # without using threads
    start_time = time.time()
    for website in websites:
        web_scrapping(website)

    end_time = time.time()
    total_time_without_using_threads = end_time - start_time

    print(f'All the websites scrapped without using threads in {end_time - start_time} seconds')
    print(f'Difference {total_time_without_using_threads - total_time_using_threads} seconds')
