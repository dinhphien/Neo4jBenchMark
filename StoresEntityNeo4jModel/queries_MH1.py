from typing import List


def get_all_relations_in_set_news(dao, set_news_id: List[str], entity_id: str, type_relation:str, type_entity:str):
    id_set_news = list(set(set_news_id))
    query = """
    PROFILE
    UNWIND $set_news_id as news_id
    MATCH (news:Entity{entityID:news_id})-[:HAS_FACT]->(facts)-[rel]->(entity)
    RETURN facts, rel, entity
    """
    result = dao.run_read_query(query, set_news_id=id_set_news)
    return result


def get_entity_relations_in_set_news(dao, set_news_id: List[str], entity_id: str, type_relation:str, type_entity:str):
    id_set_news = list(set(set_news_id))
    query = """
    PROFILE
    UNWIND $set_id_news as news_id
    MATCH (news:Entity{entityID:news_id})-[:HAS_FACT]->(facts)-[]->({entityID:$id_entity})
    WITH facts
    MATCH (facts)-[rel]->(entity)
    RETURN facts, rel, entity
    """
    result = dao.run_read_query(query, {"set_id_news": id_set_news, "id_entity": entity_id})
    return result


def get_entity_relations_via_type_relation(dao, set_news_id: List[str], entity_id: str, type_relation:str, type_entity:str):
    query = """
    PROFILE
    MATCH (entity:Entity{entityID:$id_entity})-[:HAS_SUBJECT|HAS_OBJECT]-(facts{relation: $type_relation})
    WITH facts
    MATCH (facts)-[rel]-(entity)
    RETURN facts, rel, entity
    """
    result = dao.run_read_query(query, {"type_relation": type_relation.replace(" ", "_").upper(), "id_entity": entity_id, "type_entity": type_entity})
    return result


queries_MH1_dict = {
    "Q1" : get_all_relations_in_set_news,
    "Q2" : get_entity_relations_in_set_news,
    "Q3" : get_entity_relations_via_type_relation
}