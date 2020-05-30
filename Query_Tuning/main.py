from Query_Tuning.dao import DataAccessObject
from Query_Tuning.queries import queries_dict
from Query_Tuning.tuned_queries import tuned_queries_dict
import time
import timeit
import numpy as np


HOST = "127.0.0.1"
PORT = 7687
USER = "neo4j"
PASSWORD = "xyzzy"

def total_dbhits(result):
    dbhits = 0
    dbhits += result.db_hits
    if result.children:
        for child in result.children:
            dbhits += total_dbhits(child)
    return dbhits




def main():
    time_exec = []
    db_hits = []
    # parameters:
    dao = DataAccessObject(HOST, PORT, USER, PASSWORD)
    set_news_id_test = ["news100", "news200", "news300", "news400", "news500", "news600", "news700", "news800", "news900", "news1000"]
    entity_id_test = ["event89263", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    entity_type_test = ["Person", "Country", "Location", "Organization", "Event", "Agreement", "Time"]

    # set_news_id = set_news_id_test
    set_news_id = []
    n = 10
    for i in range(1, n+1):
        set_news_id.append("news" + str(i))
    print(set_news_id)
    entity_id = entity_id_test[0]
    entity_type = entity_type_test
    for key in tuned_queries_dict:
        result = tuned_queries_dict[key](dao, set_news_id, entity_id, entity_type)
        db_hits.append(total_dbhits(result.summary().profile))
        avail = result.summary().result_available_after
        # print(avail)
        cons = result.summary().result_consumed_after
        # print(cons)
        exec_time_query = avail + cons
        # print(exec_time_query)
        time_exec.append(exec_time_query)
        # print("------------------------------------------------------------------")
    # result_time = np.reshape(np.array(time_exec), (-1, len(queries_dict)))
    print(time_exec)
    print(db_hits)

if __name__ == '__main__':
    main()
