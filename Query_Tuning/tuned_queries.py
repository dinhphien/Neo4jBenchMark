from typing import List


def get_all_relations_in_set_news(dao, set_news_id: List[str], entity_id: str, entity_type: List[str]):
    id_set_news = list(set(set_news_id))
    query = """
    PROFILE
    UNWIND $set_news_id as news_id
    MATCH (news:News{entityID:news_id})-[:HAS_FACT]->(facts:Fact)-[rel]->(entity)
    USING INDEX news:News(entityID)
    RETURN facts, rel, entity
    """
    result = dao.run_read_query(query, set_news_id=id_set_news)
    return result


def get_entity_relations_in_set_news(dao, set_news_id: List[str], entity_id: str, entity_type: List[str]):
    id_set_news = list(set(set_news_id))
    query = """
    PROFILE
    UNWIND $set_id_news as news_id
    MATCH (news:News{entityID: news_id})-[:HAS_FACT]->(facts:Fact)-[]->({entityID:$id_entity})
    USING INDEX news:News(entityID)
    WITH facts
    MATCH (facts)-[rel]->(entity)
    RETURN facts, rel, entity
    """
    result = dao.run_read_query(query, {"set_id_news": id_set_news, "id_entity": entity_id})
    return result


def get_number_appearance_in_set_news(dao, set_news_id: List[str], entity_id: str, entity_type: List[str]):
    query = """
    PROFILE
    UNWIND $set_id_news as news_id
    MATCH (news:News{entityID: news_id})-[:HAS_FACT]->(facts:Fact)-[]->({entityID:$id_entity})
    USING INDEX news:News(entityID)
    RETURN count(facts) as numberAppearance
    """
    result = dao.run_read_query(query, {"set_id_news": set_news_id, "id_entity": entity_id})
    return result


def get_entity_type_relations_in_set_news(dao, set_news_id: List[str], entity_id: str, entity_type: List[str]):
    query = """
       PROFILE
       UNWIND $set_id_news as news_id
       MATCH (news:News{entityID: news_id})-[:HAS_FACT]->(facts:Fact)-[rel]->(entity)
       USING INDEX news:News(entityID)
       WHERE any( label IN labels(entity) WHERE label IN $type_entity)
       RETURN facts, rel, entity
       """
    result = dao.run_read_query(query, {"set_id_news": list(set(set_news_id)),
                                        "type_entity": list(set(entity_type))})
    return result

tuned_queries_dict = {
    "Q1" : get_all_relations_in_set_news,
    "Q2" : get_entity_relations_in_set_news,
    "Q3" : get_entity_type_relations_in_set_news,
    "Q4" : get_number_appearance_in_set_news,
}