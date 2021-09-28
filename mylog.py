import logging.config
import time


class MyLog:

    def __init__(self):
        timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logfile_path = r'F:/PycharmProjects/ApiTestByPytest/logs'
        log_file_name = logfile_path + '/' + timestr + '.log'
        # 日志配置
        log_config = {
            'version': 1,  # 版本号
            'disable_existing_loggers': False,   # 固定写法，不需要理解
            'formatters': {  # 日志输出格式
                'simple': {
                    'format': '%(asctime)s %(name)s %(levelname)s %(pathname)s %(funcName)s line:%(lineno)d %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'INFO',
                    'formatter': 'simple',
                    'stream': 'ext://sys.stdout'
                },
                'console_err': {
                    'class': 'logging.StreamHandler',
                    'level': 'ERROR',
                    'formatter': 'simple',
                    'stream': 'ext://sys.stderr'  # 这一行不是很明白什么意思（定义屏幕名称？），但是不用也可以
                },
                # 按文件大小分割
                'file': {
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动按大小分割
                    'filename': log_file_name,  # 日志文件
                    'maxBytes': 1024 * 1024 * 300,  # 日志大小300M，
                    'backupCount': 3,  # 最多备份3个日志文件
                    'formatter': 'simple',
                    'encoding': 'utf8',
                }
            },
            'loggers': {
                'root': {
                    # 既有 console Handler，还有 file Handler
                    'handlers': ['console', 'console_err', 'file'],
                    'level': 'DEBUG',
                    # 'propagate': True,
                }
            }
        }

        logging.config.dictConfig(log_config)
        self.logger = logging.getLogger()
