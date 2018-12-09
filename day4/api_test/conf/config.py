
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'

# 邮件配置

# log配置
import  logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="../log/log.txt",
                    )


if  __name__ == "__main__":
    logging.info("hello, world")
    logging.info("中文日志")