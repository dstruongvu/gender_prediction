from logging import Handler, getLogger
from traceback import print_exc
import psycopg2
from app.settings import generic as gns
from app.utils.common import get_current_vn_time


class DBHandler(Handler):
    backup_logger = None

    def __init__(self, level=0, extra_info=None):
        super().__init__(level)

        #
        obj_db = gns.LOG_CONFIG
        connection_string = obj_db['drivername'] + '://' + obj_db['username'] + ':' + str(
            obj_db['password']) + '@' + str(
            obj_db['host']) + ':' + str(obj_db['port']) + '/' + obj_db['database']

        self.connection_string = connection_string
        self.table_name = obj_db['table_name']
        self.schema = obj_db['schema']

        # Connect to an existing database
        self.conn = psycopg2.connect(connection_string)

        # Create table
        # self.create_table()

        # Open a cursor to perform database operations
        self.cursor = self.conn.cursor()

        if extra_info:
            self.extra_info = extra_info[0] + ' _ ' + extra_info[1]

    def emit(self, record):

        try:
            message = self.format(record)
            try:
                last_line = message.rsplit('\n', 1)[-1]
            except:
                last_line = None

            try:
                tm = get_current_vn_time()
                message = message[:200]

                sql = """INSERT INTO {table_name}(module, thread_name, file_name, func_name, level_name, 
                                    line_no, process_name, message, last_line, time, extra_info)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

                sql = sql.format(table_name=self.schema + '.' + self.table_name)

                self.cursor.execute(sql, (record.module, record.threadName, record.filename, record.funcName,
                                          record.levelname, record.lineno, record.processName, message,
                                          last_line, tm, self.extra_info))
                self.conn.commit()
            except:
                print_exc()
                raise

        except:
            print_exc()
            raise

    def create_table(self):

        table_name = self.schema + '.' + self.table_name
        if self.check_table_exist(table_name):
            return

        sql = """
            CREATE TABLE {table_name} (
                id serial NOT NULL,
                time timestamp NOT NULL,
                level_name varchar(10) NULL,
                module varchar(200) NULL,
                thread_name varchar(200) NULL,
                file_name varchar(200) NULL,
                func_name varchar(200) NULL,
                line_no int4 NULL,
                process_name varchar(200) NULL,
                message text NULL,
                last_line text NULL,
                extra_info text NULL,
                CONSTRAINT log_etl_airflow_pkey PRIMARY KEY (id));"""

        sql = sql.format(table_name=table_name)

        try:

            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except:
            print_exc()
            pass

        return

    def check_table_exist(self, table):

        sql = """SHOW TABLES"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        print('All existing tables:', results)  # Returned as a list of tuples

        results_list = [item[0] for item in results]  # Conversion to list of str

        if table in results_list:
            return True
        else:
            False

