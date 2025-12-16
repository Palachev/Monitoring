import time
import logging
import os

# Путь для логов
log_dir = r"C:\ShoeHubV2\logs"
os.makedirs(log_dir, exist_ok=True)  # Создаёт папку, если её нет
log_file = os.path.join(log_dir, "app.log")

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Формат сообщений
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# File handler
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def basic_levels():
    logger.info('{:-^100}'.format(' BASIC LEVELS '))
    logger.debug('This is a simple DEBUG level message.')
    logger.info('This is a simple INFO level message.')
    logger.warning('This is a simple WARNING level message.')
    logger.warn('This is a simple WARN level message.')
    logger.error('This is a simple ERROR level message.')
    logger.exception('This is an ERROR level message with exc_info.')

    try:
        raise Exception('Random exception!')
    except Exception:
        logger.exception('This is an ERROR level message with a stack trace!')

    logger.critical('This is a simple CRITICAL level message')
    logger.fatal('This is a simple FATAL level message')

    logger.log(logging.DEBUG, 'This is the same as logging.debug')
    logger.log(logging.INFO, 'This is the same as logging.info')
    logger.log(logging.WARNING, 'This is the same as logging.warning')
    logger.log(logging.WARN, 'This is the same as logging.warn')
    logger.log(logging.ERROR, 'This is the same as logging.exception', exc_info=True)
    logger.log(logging.CRITICAL, 'This is the same as logging.critical')
    logger.log(logging.FATAL, 'This is the same as logging.fatal')


def message_arguments():
    logger.info('{:-^100}'.format(' MESSAGE ARGUMENTS '))
    logger.info(
        'What %s is it? %.5f',
        'time', time.time()
    )

    logger.info(
        'Now with %(my_arg)s arguments!',
        {'my_arg': 'named'}
    )


def main():
    basic_levels()
    message_arguments()


if __name__ == '__main__':
    main()
