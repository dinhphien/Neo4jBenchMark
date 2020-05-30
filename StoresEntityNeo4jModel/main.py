from Query_Tuning.dao import DataAccessObject
from StoresEntityNeo4jModel.queries_MH1 import queries_MH1_dict
from StoresEntityNeo4jModel.queries_MH2 import queries_MH2_dict
from StoresEntityNeo4jModel.queries_MH3 import queries_MH3_dict


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
    set_news_id_test = ["news1111", "news1112", "news1113", "news1114", "news1115", "news1116", "news1117", "news1118", "news1119", "news1120"]
    entity_id_test = ["person482", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    entity_type_test = ["Person", "Country", "Location", "Organization", "Event", "Agreement", "Time"]
    relation_type_test = ["gặp gỡ", "tổ chức", "ký thỏa thuận", "tham gia", "ủng hộ", "phản đối", "phát biểu tại",
             "căng thẳng với", "hủy bỏ", "đàm phán với"]


    # set_news_id = []
    # n = 10
    # for i in range(1, n+1):
    #     set_news_id.append("news" + str(i))
    # print(set_news_id)
    set_news_id = set_news_id_test
    entity_id = entity_id_test[0]
    entity_type = entity_type_test[0]
    type_relation = relation_type_test[3]
    print(type_relation)
    i = 1
    for key in queries_MH3_dict:
        result = queries_MH3_dict[key](dao, set_news_id, entity_id, type_relation,  entity_type)
        # for res in result:
        #     print(res)
        print("------------------------------------------------------------------")
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
