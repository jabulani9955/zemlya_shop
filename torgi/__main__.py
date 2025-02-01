import os
import time
import datetime
import logging

import schedule

from torgi.src.data_processing import data_processing


logging.basicConfig(
    filename=os.path.join('data', 'torgi.log'), 
    encoding='utf-8',
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] (%(filename)s) %(message)s"
)
logger = logging.getLogger(__name__)


def main(lot_subject=None):
    try:
        start_time = datetime.datetime.now()
        print(f"Начало: {start_time.strftime('%H:%M:%S')}")
        logger.info(f'Скрипт запущен.')
        
        data_processing(lot_subject)

        print(f"Конец: {datetime.datetime.now().strftime('%H:%M:%S')}\nВремя выполнения скрипта: {datetime.datetime.now() - start_time}")
        logger.info(f"Скрипт завершён. Время исполнения: {datetime.datetime.now() - start_time}\n")

    except Exception as e:
        logger.critical(e, exc_info=True)


if __name__ == '__main__':
    # TEST
    # main(
    #     lot_subject=[
    #         'Астраханская область'
    #     ]
    # )
    
    # PROD
    ## 1. 

    # schedule.every().day.at('04:00').do(main)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(10)

    ## 2.
    main()
