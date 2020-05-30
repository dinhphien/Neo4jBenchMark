import math, random, string
import xlrd
def randomStringDigits(stringLength=6, type=3):
    """Generate a random string of letters and digits """
    if(type == 0):
        lettersAndDigits = string.ascii_uppercase
    elif(type == 1):
        lettersAndDigits = string.ascii_letters
    elif(type == 2):
        lettersAndDigits = string.ascii_lowercase
    elif(type == 3):
        lettersAndDigits = string.ascii_uppercase + string.digits
    else:
        lettersAndDigits = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.sample(lettersAndDigits,stringLength))

TOPIC_NEWS = ["Society", "Politics", "Business", "Education"]
class Store:
    def __init__(self, number_entity, number_relation, dirname):
        self.number_entity = number_entity
        self.number_relation = number_relation
        self.dirname = dirname
        self.fileEntityObject1 = open(dirname + 'type1_entities'+ str(self.number_entity) + '.csv', "a+" )
        self.fileRelationObject1 = open(dirname + 'type1_relationships' + str(self.number_entity) + '.csv', "a+")
        self.fileTimeEntityObject1 = open(dirname + 'type1_time_entities' + str(self.number_entity )+ '.csv', "a+")
        self.fileNewsEntityObject1 = open(dirname + 'type1_news_entities' + str(self.number_entity )+ '.csv', "a+")
        self.fileFactEntityObject1 = open(dirname + 'type1_fact_entities' + str(self.number_entity )+ '.csv', "a+")

        self.fileEntityObject2 = open(dirname + 'type2_entities' + str(self.number_entity) + '.csv', "a+")
        self.fileRelationObject2 = open(dirname + 'type2_relationships' + str(self.number_entity) + '.csv', "a+")
        self.fileTimeEntityObject2 = open(dirname + 'type2_time_entities' + str(self.number_entity) + '.csv', "a+")
        self.fileNewsEntityObject2 = open(dirname + 'type2_news_entities' + str(self.number_entity) + '.csv', "a+")
        self.fileFactEntityObject2 = open(dirname + 'type2_fact_entities' + str(self.number_entity) + '.csv', "a+")

        self.fileEntityObject3 = open(dirname + 'type3_entities' + str(self.number_entity) + '.csv', "a+")
        self.fileRelationObject3 = open(dirname + 'type3_relationships' + str(self.number_entity) + '.csv', "a+")
        self.fileTimeEntityObject3 = open(dirname + 'type3_time_entities' + str(self.number_entity) + '.csv', "a+")
        self.fileNewsEntityObject3 = open(dirname + 'type3_news_entities' + str(self.number_entity) + '.csv', "a+")
        self.fileFactEntityObject3 = open(dirname + 'type3_fact_entities' + str(self.number_entity) + '.csv', "a+")
    def close(self):
        self.fileEntityObject1.close()
        self.fileRelationObject1.close()
        self.fileTimeEntityObject1.close()
        self.fileNewsEntityObject1.close()
        self.fileFactEntityObject1.close()

        self.fileEntityObject2.close()
        self.fileRelationObject2.close()
        self.fileTimeEntityObject2.close()
        self.fileNewsEntityObject2.close()
        self.fileFactEntityObject2.close()

        self.fileEntityObject3.close()
        self.fileRelationObject3.close()
        self.fileTimeEntityObject3.close()
        self.fileNewsEntityObject3.close()
        self.fileFactEntityObject3.close()

    def writeToFile(self, fileObject, line):
        fileObject.write(line)

    def add_new_person(self, personid, personname, personrole):

        line_data1 = "person" + str(personid) + ','+ "Person" + ',"' + personrole + " " + personname + '",' \
                + '"' + personname + ' là ' + personrole + '",' + "Entity" + "\n"

        line_data23 = "person" + str(personid) + ',"' + personrole + " " + personname + '",' \
                        + '"' + personname + ' là ' + personrole + '",' + "Person" + "\n"
        self.writeToFile(self.fileEntityObject1, line_data1)
        self.writeToFile(self.fileEntityObject2, line_data23)
        self.writeToFile(self.fileEntityObject3, line_data23)
        return personid


    def add_new_organization(self, orgid, orgname):
        line_data1 = "organization" + str(orgid) + ','+ "Organization" +',"' + orgname + '",' \
                    + '"' + orgname + " là một tổ chức ....." + '",' + "Entity" + "\n"

        line_data23 = "organization" + str(orgid) + ',"' + orgname + '",' \
                        + '"' + orgname + " là một tổ chức ....." + '",' + "Organization" + "\n"

        self.writeToFile(self.fileEntityObject1, line_data1)
        self.writeToFile(self.fileEntityObject2, line_data23)
        self.writeToFile(self.fileEntityObject3, line_data23)
        return orgid

    def add_new_location(self, locationid, locationname):
        line_data1 = "location" + str(locationid) + ',' + "Location" + ',"' + locationname + '",' \
                    + '"' + locationname + ' là một địa danh ....' + '",' + "Entity" + "\n"
        line_data23 = "location" + str(locationid) + ',"' + locationname + '",' \
                    + '"' + locationname + ' là một địa danh ....' + '",' + "Location" + "\n"
        self.writeToFile(self.fileEntityObject1, line_data1)
        self.writeToFile(self.fileEntityObject2, line_data23)
        self.writeToFile(self.fileEntityObject3, line_data23)
        return locationid

    def add_new_country(self, countryid, countryname):
        population = random.randrange(10000000, 2000000000)
        squares = random.randrange(10000000, 2000000000)
        line_data1 = "country" + str(countryid) +',' + "Country" + ',"' + countryname + '",' \
                    + '"' + countryname + ' là quốc gia có dân số là ' + str(population) \
                                     + ' và diện tích là ' + str(squares) + '",' + "Entity" + "\n"

        line_data23 = "country" + str(countryid) +',"' + countryname + '",' \
                    + '"' + countryname + ' là quốc gia có dân số là ' + str(population) \
                    + ' và diện tích là ' + str(squares) + '",' + "Country" + "\n"
        self.writeToFile(self.fileEntityObject1, line_data1)
        self.writeToFile(self.fileEntityObject2, line_data23)
        self.writeToFile(self.fileEntityObject3, line_data23)
        return countryid

    def add_new_time(self, timeid, time):
        line_data1 = "time" + str(timeid) + ','+"Time"+ ',"' + time + '",' + time + "," + "Entity" + "\n"

        line_data23 = "time" + str(timeid) + ',"' + time + '",' + time + "," + "Time" + "\n"
        self.writeToFile(self.fileTimeEntityObject1, line_data1)
        self.writeToFile(self.fileTimeEntityObject2, line_data23)
        self.writeToFile(self.fileTimeEntityObject3, line_data23)
        return timeid

    def add_new_event(self, eventid, eventname):
        line_data1 = "event" + str(eventid) +','+ "Event" + ',"' + eventname + '",' \
                    + '"' + eventname + ' là sự kiện được tổ chức .....' + '",' + "Entity" + "\n"

        line_data23 = "event" + str(eventid) + ',"' + eventname + '",' \
                + '"' + eventname + ' là sự kiện được tổ chức .....' + '",' + "Event" + "\n"
        self.writeToFile(self.fileEntityObject1, line_data1)
        self.writeToFile(self.fileEntityObject2, line_data23)
        self.writeToFile(self.fileEntityObject3, line_data23)
        return eventid

    def add_new_agreement(self, agrid, agrname):
        line_data1 = "agreement" + str(agrid) + ',' + "Agreement"  + ',"' + agrname + '",' \
                    + '"' + agrname + ' được kí kết ....' + '",' + "Entity" + "\n"

        line_data23 = "agreement" + str(agrid) + ',"' + agrname + '",' \
                + '"' + agrname + ' được kí kết ....' + '",' + "Agreement" + "\n"
        self.writeToFile(self.fileEntityObject1, line_data1)
        self.writeToFile(self.fileEntityObject2, line_data23)
        self.writeToFile(self.fileEntityObject3, line_data23)
        return agrid
    def add_news (self, new_id):
        index_topic = random.randrange(0, len(TOPIC_NEWS))
        linkUrl = "http://samples.org/" + randomStringDigits(6, 4)
        new_data1 = "news" + str(new_id) +','+ "News"+ ',' + linkUrl + ',' + TOPIC_NEWS[index_topic] + ',' + "Entity" + '\n'

        new_data23 = "news" + str(new_id) + ',' + linkUrl + ',' + TOPIC_NEWS[index_topic] + ',' + "News" + '\n'
        self.writeToFile(self.fileNewsEntityObject1, new_data1)
        self.writeToFile(self.fileNewsEntityObject2, new_data23)
        self.writeToFile(self.fileNewsEntityObject3, new_data23)
        return new_id

    def add_fact_new_100(self, sub_index, obj_index, relation, time_id, location_id, location_type, fact_id, new_id):
        # create a new fact entity:
        fact_data1 = "fact" + str(fact_id)+','+ "Fact" + ','+relation[1].replace(" ", "_").upper() + ',' + "Entity" + '\n'
        self.writeToFile(self.fileFactEntityObject1, fact_data1)
        # add relationships:
        self.writeToFile(self.fileRelationObject1,
                         "news" + str(new_id) + ',' + "fact" + str(fact_id) + ',' + "HAS_FACT" + '\n')

        self.writeToFile(self.fileRelationObject1,
                         "fact" + str(fact_id) + ',' + relation[0] + str(sub_index) + ',' + "HAS_SUBJECT" + "\n")
        self.writeToFile(self.fileRelationObject1,
                         "fact" + str(fact_id) + ',' + relation[2] + str(obj_index) + ',' + "HAS_OBJECT" + "\n")

        if location_id != -1:
            self.writeToFile(self.fileRelationObject1,
                             "fact" + str(fact_id) + ',' + location_type + str(
                                 location_id) + ',' + "OCURRED_IN" + '\n')
        if time_id != -1:
            self.writeToFile(self.fileRelationObject1,
                             "fact" + str(fact_id) + ',' + "time" + str(time_id) + ',' + "OCCURRED_ON" + '\n')

        fact_data2 = "fact" + str(fact_id) + ',' + relation[1].replace(" ","_").upper() + ',' + "Fact" + '\n'
        self.writeToFile(self.fileFactEntityObject2, fact_data2)
        # add relationships:
        self.writeToFile(self.fileRelationObject2,
                         "news" + str(new_id) + ',' + "fact" + str(fact_id) + ',' + "HAS_FACT" + '\n')

        self.writeToFile(self.fileRelationObject2,
                         "fact" + str(fact_id) + ',' + relation[0] + str(sub_index) + ',' + "HAS_SUBJECT" + "\n")
        self.writeToFile(self.fileRelationObject2,
                         "fact" + str(fact_id) + ',' + relation[2] + str(obj_index) + ',' + "HAS_OBJECT" + "\n")

        if location_id != -1:
            self.writeToFile(self.fileRelationObject2,
                             "fact" + str(fact_id) + ',' + location_type + str(
                                 location_id) + ',' + "OCURRED_IN" + '\n')
        if time_id != -1:
            self.writeToFile(self.fileRelationObject2,
                             "fact" + str(fact_id) + ',' + "time" + str(time_id) + ',' + "OCCURRED_ON" + '\n')

        fact_data3 = "fact" + str(fact_id) + ',' + "Fact" + '\n'
        self.writeToFile(self.fileFactEntityObject3, fact_data3)
        # add relationships:
        self.writeToFile(self.fileRelationObject3,
                         "news" + str(new_id) + ',' + "fact" + str(fact_id) + ',' + "HAS_FACT" + '\n')

        self.writeToFile(self.fileRelationObject3,
                         "fact" + str(fact_id) + ',' + relation[0] + str(sub_index) + ',' + "HAS_SUBJECT_" +
                         relation[1].replace(" ", "_").upper() + "\n")
        self.writeToFile(self.fileRelationObject3,
                         "fact" + str(fact_id) + ',' + relation[2] + str(obj_index) + ',' + "HAS_OBJECT_" +
                         relation[1].replace(" ", "_").upper() + "\n")

        if location_id != -1:
            self.writeToFile(self.fileRelationObject3,
                             "fact" + str(fact_id) + ',' + location_type + str(
                                 location_id) + ',' + "OCURRED_IN" + '\n')
        if time_id != -1:
            self.writeToFile(self.fileRelationObject3,
                             "fact" + str(fact_id) + ',' + "time" + str(time_id) + ',' + "OCCURRED_ON" + '\n')

def add_relationships_100(store, book, num_entity, stringLen=6, typeRandomStr=4, rule_file_sheet="Rules"):
    sheet_rules = book.sheet_by_name(rule_file_sheet)

    n_relations = 1
    fact_id = 1
    news_id = 1
    store.add_news(news_id)
    numOfFact = random.randrange(1, 3)
    loc_or_cty = ['location', 'location', 'location', 'location', 'location',
                  'location', 'location', 'location', 'location', 'country']
    while(n_relations <= store.number_relation):
        type_index = random.randrange(0, 3)
        rule_index = random.randrange(0, sheet_rules.nrows)
        rule = sheet_rules.row_values(rule_index)[type_index * 3: type_index * 3 + 3]
        sub_index = random.randrange(1, num_entity[rule[0]]+1)
        obj_index = random.randrange(1, num_entity[rule[2]]+1)
        has_time = random.randrange(0, 2)
        if has_time == 0:
            time_id = -1
        else:
            time_id = random.randrange(1, num_entity['time'] + 1)
        has_place = random.randrange(0, 2)
        if has_place == 0:
            location_id = -1
            location_type = ""
        else:
            location_type = random.choice(loc_or_cty)
            location_id = random.randrange(1, num_entity[location_type] + 1)
        if numOfFact == 0:
            news_id += 1
            store.add_news(news_id)
            numOfFact = random.randrange(1, 3)

        store.add_fact_new_100(sub_index, obj_index, rule, time_id, location_id, location_type, fact_id, news_id)
        numOfFact -= 1
        fact_id += 1
        n_relations += 1

def add_relationships_5000(store, book, num_entity, stringLen=6, typeRandomStr=4, rule_file_sheet="Rules"):
    sheet_rules = book.sheet_by_name(rule_file_sheet)
    total_cty_rel = math.ceil(store.number_relation * num_entity['country'] / store.number_entity)

    n_relations = 1
    fact_id = 1
    news_id = 1
    store.add_news(news_id)
    numOfFact = random.randrange(1, 3)
    loc_or_cty = ['location', 'location', 'location', 'location', 'location',
                  'location', 'location', 'location', 'location', 'country']
    # add country relations:
    print("start creating country relations")
    n_cty_rel = 1
    while (n_cty_rel <= total_cty_rel):
        type_index = 2
        rule_index = random.randrange(0, 13)
        rule = sheet_rules.row_values(rule_index)[type_index * 3: type_index * 3 + 3]
        sub_index = random.randrange(1, num_entity["country"] + 1)
        obj_index = random.randrange(1, num_entity[rule[2]] + 1)

        has_time = random.randrange(0, 2)
        if has_time == 0:
            time_id = -1
        else:
            time_id = random.randrange(1, num_entity['time'] + 1)
        has_place = random.randrange(0, 2)
        if has_place == 0:
            location_id = -1
            location_type = ""
        else:
            location_type = random.choice(loc_or_cty)
            location_id = random.randrange(1, num_entity[location_type] + 1)
        if numOfFact == 0:
            news_id += 1
            store.add_news(news_id)
            numOfFact = random.randrange(1, 3)

        store.add_fact_new_100(sub_index, obj_index, rule, time_id, location_id, location_type, fact_id, news_id)
        numOfFact -= 1
        fact_id += 1
        n_relations += 1
        n_cty_rel += 1
    print("created country relations")
    # n_relations = n_event_loc_time_rel + n_cty_rel -1
    # add remain relations:
    while (n_relations <= store.number_relation):
        type_index = random.randrange(0, 2)
        rule_index = random.randrange(0, sheet_rules.nrows)
        rule = sheet_rules.row_values(rule_index)[type_index * 3: type_index * 3 + 3]
        sub_index = random.randrange(1, num_entity[rule[0]] + 1)
        obj_index = random.randrange(1, num_entity[rule[2]] + 1)

        has_time = random.randrange(0, 2)
        if has_time == 0:
            time_id = -1
        else:
            time_id = random.randrange(1, num_entity['time'] + 1)
        has_place = random.randrange(0, 2)
        if has_place == 0:
            location_id = -1
            location_type = ""
        else:
            location_type = random.choice(loc_or_cty)
            location_id = random.randrange(1, num_entity[location_type] + 1)
        if numOfFact == 0:
            news_id += 1
            store.add_news(news_id)
            numOfFact = random.randrange(1, 3)

        store.add_fact_new_100(sub_index, obj_index, rule, time_id, location_id, location_type, fact_id, news_id)
        numOfFact -= 1
        fact_id += 1
        n_relations += 1
    print("created completely relations")

def add_relationships_1M(store, book, num_entity, stringLen=6, typeRandomStr=4, rule_file_sheet="Rules"):
    sheet_rules = book.sheet_by_name(rule_file_sheet)
    # n_relations = 0
    # add relationships between events, times, locations and countries:
    # total_event_loc_time_rel = math.ceil(store.number_relation * (num_entity['time'] + num_entity['location'])
    #                                      / store.number_entity)
    # n_event_loc_time_rel = 1
    # print("start creating relations between times, locals and events")
    #
    # for event_id in range(1, num_entity['event'] + 1):
    #     obj_index = random.randrange(1, num_entity['time'] + 1)
    #     line_data = 'event' + str(event_id) + "," +"time" + str(obj_index) + "," + " ," + " ," + \
    #                 "DIỄN_RA_LÚC" + "\n"
    #     store.writeToFile(store.fileRelationObject, line_data)
    #     n_event_loc_time_rel += 1
    #     if n_event_loc_time_rel > total_event_loc_time_rel/2:
    #         break
    #
    # loc_or_cty = ['location', 'location', 'location', 'location','location',
    #               'location', 'location', 'location', 'location', 'country']
    # for event_id in range(num_entity['event'], 0, -1):
    #     obj_type = random.choice(loc_or_cty)
    #     obj_index = random.randrange(1, num_entity[obj_type] + 1)
    #     line_data = 'event' + str(event_id) + "," + obj_type + str(obj_index) + "," + " ," + " ," + \
    #                 "DIỄN_RA_TẠI" + "\n"
    #     store.writeToFile(store.fileRelationObject, line_data)
    #     n_event_loc_time_rel += 1
    #     if n_event_loc_time_rel > total_event_loc_time_rel:
    #         break
    #
    # print("created relations between times, locals and events")
    total_cty_rel = math.ceil(store.number_relation * num_entity['country'] / store.number_entity)
    n_cty_rel = 1
    linkid = 1
    relationid = 1
    # add country relations:
    print("start creating country relations")
    while (n_cty_rel <= total_cty_rel):
        type_index = 2
        rule_index = random.randrange(0, 13)
        rule = sheet_rules.row_values(rule_index)[type_index * 3: type_index * 3 + 3]
        sub_index = random.randrange(1, num_entity["country"] + 1)
        obj_index = random.randrange(1, num_entity[rule[2]] + 1)
        linkUrl = "http://samples.org/" + randomStringDigits(stringLen, typeRandomStr)
        date_modified = "27/03/2019"
        line_data = rule[0] + str(sub_index) + "," + rule[2] + str(obj_index) + ',"' + linkUrl + '","' + \
                    date_modified + '",' + rule[1].replace(" ", "_").upper() + "\n"
        store.writeToFile(store.fileRelationObject, line_data)
        linkid += 1
        relationid += 1
        n_cty_rel += 1
    print("created country relations")
    # n_relations = n_event_loc_time_rel + n_cty_rel -1
    n_relations = 0
    # add remain relations:
    while (n_relations <= store.number_relation):
        type_index = random.randrange(0, 2)
        rule_index = random.randrange(0, sheet_rules.nrows)
        rule = sheet_rules.row_values(rule_index)[type_index * 3: type_index * 3 + 3]
        sub_index = random.randrange(1, num_entity[rule[0]] + 1)
        obj_index = random.randrange(1, num_entity[rule[2]] + 1)
        linkUrl = "http://samples.org/" + randomStringDigits(stringLen, typeRandomStr)
        date_modified = "27/03/2019"
        line_data = rule[0] + str(sub_index) + "," + rule[2] + str(obj_index) + ',"' + linkUrl + '","' + \
                    date_modified + '",' + rule[1].replace(" ", "_").upper() + "\n"
        store.writeToFile(store.fileRelationObject, line_data)
        linkid += 1
        relationid += 1
        n_relations += 1
    print("created completely relations")
def main(argv=None):
    if not argv:
        pass
    else:
        store = Store(argv[0], argv[1], argv[2])
        print(argv[0])
        print(argv[1])

        num_entity = {}
        with xlrd.open_workbook('./data_entity.xlsx', on_demand=True) as book:

            sheet_country = book.sheet_by_name("Countries")
            country_names = [x for x in sheet_country.col_values(0)]

            sheet_people = book.sheet_by_name("People")
            first_name = [x for x in sheet_people.col_values(0)]
            last_name = [y for y in sheet_people.col_values(1)]
            role1 = [z for z in sheet_people.col_values(2)]

            sheet_location = book.sheet_by_name("Locations")
            location_pro = [x for x in sheet_location.col_values(2)]
            location_dis = [y for y in sheet_location.col_values(1)]
            location_town = [z for z in sheet_location.col_values(0)]

            sheet_org = book.sheet_by_name("Organizations")
            organizations_tw = [x for x in sheet_org.col_values(0)]
            organizations_local = [y for y in sheet_org.col_values(1)]
            organizations_ngo = [z for z in sheet_org.col_values(2)]
            organizations_uni = [t for t in sheet_org.col_values(3)]
            organizations_field = [m for m in sheet_org.col_values(4)]

            sheet_agr = book.sheet_by_name("Agreements")
            type_agr = [x for x in sheet_agr.col_values(0)]

            sheet_event = book.sheet_by_name("Events")
            type_event = [x for x in sheet_event.col_values(0)]
            topic_event = [y for y in sheet_event.col_values(1)]
            post_fix = [z for z in sheet_event.col_values(2)]
            if store.number_entity == 100:
                # create country entities:
                for ctyid in range(1, 19):
                    # pass
                    store.add_new_country(ctyid, country_names[ctyid])
                num_entity["country"] = ctyid
                # create person entities:
                personid = 1
                for m_name in range(1, 4):
                    for l_name in range(15, 21):
                        store.add_new_person(personid,
                                             first_name[1] + " " + last_name[m_name] + " " + last_name[l_name],
                                             role1[random.randrange(1, 5)])
                        personid += 1
                num_entity["person"] = personid -1
                # create location entities:
                for locid in range(1, 6):
                    # pass
                    store.add_new_location(locid, location_pro[0] + " " + location_pro[locid])
                num_entity["location"] = locid
                # create organization entities:
                for orgid in range(1, 19):
                    # pass
                    store.add_new_organization(orgid, organizations_tw[orgid])
                num_entity["organization"] = orgid
                # create agreement entities:
                agrid = 1
                for ty in range(1, 4):
                    for i in range(1, 7):
                        store.add_new_agreement(agrid, type_agr[ty] + " " + randomStringDigits(5))
                        agrid += 1
                num_entity["agreement"] = agrid -1
                # create event entities:
                eventid = 1
                for ty in range(1, 3):
                    for to in range(1, 4):
                        for po in range(1, 4):
                            store.add_new_event(eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[po])
                            eventid += 1
                num_entity["event"] = eventid - 1
                # create time entities:
                for i in range(1, 6):
                    date = random.randrange(1, 29)
                    month = random.randrange(1, 13)
                    year = random.randrange(2000, 2020)
                    if date <10:
                        str_date = "0" + str(date)
                    else:
                        str_date = str(date)
                    if month <10:
                        str_month = "0" + str(month)
                    else:
                        str_month = str(month)
                    store.add_new_time(i, str(year) + "-" + str_month + "-" + str_date)
                num_entity["time"] = i
                print(num_entity)
                # add relationships:
                add_relationships_100(store, book, num_entity, 6, 4, "RelationRules")
                # add_relationships(store, book, argv[1], num_entity, 6, 4, "Rules")

                #########################################################
                #########################################################
            if store.number_entity == 5000:
                # create country entities:
                print("starting create country")
                for ctyid in range(1, sheet_country.nrows):
                    store.add_new_country(ctyid, country_names[ctyid])
                    pass
                num_entity["country"] = sheet_country.nrows - 1
                print("creating country completed!")
                print(num_entity)
                # create time entities:
                print("starting create time")
                timeid = 1
                for date in range(1, 21):
                    for month in range(1, 11):
                        for year in range(2018, 2020):
                            if date < 10:
                                str_date = "0" + str(date)
                            else:
                                str_date = str(date)
                            if month < 10:
                                str_month = "0" + str(month)
                            else:
                                str_month = str(month)
                            store.add_new_time(timeid, str(year) + "-" + str_month + "-" + str_date)
                            timeid += 1
                    # print((i, str(date) + "/" + str(month) + "/" + str(year)))
                num_entity["time"] = timeid - 1
                print("creating time completed!")
                print(num_entity)
                # create location entities:
                print("starting create location")
                locid = 1
                for locid_town in range(1, 21):
                    for locid_dis in range(1, 11):
                        for locid_pro in range(45, 47):
                            # print((locid, location_town[0] + " " + location_town[locid_town] + " " +location_dis[0] + " " + location_dis[locid_dis]+ " "+ location_pro[0] + " " + location_pro[locid_pro]))
                            store.add_new_location(locid,
                                                   location_town[0] + " " + location_town[locid_town] + " " +
                                                   location_dis[0] + " " + location_dis[locid_dis] + " " +
                                                   location_pro[0] + " " + location_pro[locid_pro])
                            locid = locid + 1
                num_entity["location"] = locid - 1
                print("creating location completed!")
                print(num_entity)
                # create person entities:
                print("starting create person")
                personid = 1
                for fid_name in range(1, 72):
                    for mid_name in range(1, 3):
                        for lid_name in range(90, 97):
                            store.add_new_person(personid,
                                                 first_name[fid_name] + " " + last_name[mid_name] + " " + last_name[
                                                     lid_name],
                                                 role1[random.randrange(0, 5)])
                            # print(role1[random.randrange(0, 5)])
                            personid += 1
                # print(personid)
                num_entity["person"] = personid - 1
                print("creating person completed!")
                print(num_entity)
                # create organization entities:
                print("Start create organization")
                orgid = 1
                for org_index in range(1, 49):
                    store.add_new_organization(orgid, organizations_tw[org_index])
                    orgid += 1
                for orgid_local in range(1, 23):
                    for loc_pro_index in range(1, 44):
                        # print((orgid, organizations_local[orgid_local] + " " + location_pro[0] + " " + location_pro[loc_pro_index]))
                        store.add_new_organization(orgid,
                                                   organizations_local[orgid_local] + " " + location_pro[0] + " " +
                                                   location_pro[loc_pro_index])
                        orgid = orgid + 1
                num_entity["organization"] = orgid - 1
                print("creating organization completed!")
                print(num_entity)
                # create agreement entities:
                print("Start create agreements!")
                agrid = 1
                for ty in range(1, 3):
                    for i in range(1, 498):
                        # print((agrid, type_agr[ty] + " " + randomStringDigits(5)))
                        store.add_new_agreement(agrid, type_agr[ty] + " " + randomStringDigits(6))
                        agrid += 1
                num_entity["agreement"] = agrid - 1
                print("creating agreement completed!")
                print(num_entity)
                # create event entities:
                eventid = 1
                for index in range(1, 3):
                    for ty in range(0, 4):
                        for to in range(1, 7):
                            for po in range(1, 22):
                                # print((eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[po]+ " lần "+ str(index)))
                                store.add_new_event(eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[
                                    po] + " lần " + str(index))
                                eventid += 1
                num_entity["event"] = eventid - 1
                print("creating event completed!")
                print(num_entity)
                # add relationships:
                add_relationships_5000(store, book, num_entity, 6, 4, "Rules")
                print("creating relationships completed!")
                # pass
                #########################################################
                #########################################################

            if store.number_entity == 60000:
                # create country entities:
                print("starting create country")
                for ctyid in range(1, sheet_country.nrows):
                    store.add_new_country(ctyid, country_names[ctyid])
                    # pass
                num_entity["country"] = sheet_country.nrows - 1
                print("creating country completed!")
                print(num_entity)
                #create time entities:
                print("starting create time")
                timeid = 1
                for date in range(1, 16):
                    for month in range(1, 12):
                        for year in range(1985, 2020):
                            if date < 10:
                                str_date = "0" + str(date)
                            else:
                                str_date = str(date)
                            if month < 10:
                                str_month = "0" + str(month)
                            else:
                                str_month = str(month)
                            store.add_new_time(timeid, str(year) + "-" + str_month + "-" + str_date)
                            timeid += 1
                    # print((i, str(date) + "/" + str(month) + "/" + str(year)))
                num_entity["time"] = timeid - 1
                print("creating time completed!")
                print(num_entity)
                # create location entities:
                print("starting create location")
                locid = 1
                for locid_town in range(1, 21):
                    for locid_dis in range(1, 11):
                        for locid_pro in range(1, 31):
                            # print((locid, location_town[0] + " " + location_town[locid_town] + " " +location_dis[0] + " " + location_dis[locid_dis]+ " "+ location_pro[0] + " " + location_pro[locid_pro]))
                            store.add_new_location(locid,
                                                   location_town[0] + " " + location_town[locid_town] + " " +
                                                   location_dis[0] + " " + location_dis[locid_dis] + " " +
                                                   location_pro[0] + " " + location_pro[locid_pro])
                            locid = locid + 1
                num_entity["location"] = locid - 1
                print("creating location completed!")
                print(num_entity)
                # create person entities:
                print("starting create person")
                personid = 1
                for fid_name in range(1, 21):
                    for mid_name in range(1, 21):
                        for lid_name in range(60, 90):
                            store.add_new_person(personid,
                                                 first_name[fid_name] + " " + last_name[mid_name] + " " + last_name[
                                                     lid_name],
                                                 role1[random.randrange(0, 5)])
                            # print(role1[random.randrange(0, 5)])
                            personid += 1
                # print(personid)
                num_entity["person"] = personid - 1
                print("creating person completed!")
                print(num_entity)
                # create organization entities:
                print("Start create organization")
                orgid = 1
                for org_index in range(1, 39):
                    store.add_new_organization(orgid, organizations_tw[org_index])
                    orgid += 1
                for orgid_local in range(1, 39):
                    for loc_pro_index in range(1, 64):
                        # print((orgid, organizations_local[orgid_local] + " " + location_pro[0] + " " + location_pro[loc_pro_index]))
                        store.add_new_organization(orgid,
                                                   organizations_local[orgid_local] + " " + location_pro[0] + " " +
                                                   location_pro[loc_pro_index])
                        orgid = orgid + 1
                    for loc_dis_index in range(1, 161):
                        # print((orgid, organizations_local[orgid_local] + " " + location_dis[0] + " " + location_dis[loc_dis_index]))
                        store.add_new_organization(orgid,
                                                   organizations_local[orgid_local] + " " + location_dis[0] + " " +
                                                   location_dis[loc_dis_index])
                        orgid = orgid + 1
                for orgid_ngo in range(1, 17):
                    for cty_index in range(1, 219):
                        # print((orgid, organizations_ngo[orgid_ngo] + " " + " " +country_names[cty_index]))
                        store.add_new_organization(orgid,organizations_ngo[orgid_ngo] + " " +country_names[cty_index])
                        orgid = orgid + 1
                num_entity["organization"] = orgid - 1
                print("creating organization completed!")
                print(num_entity)
                # create agreement entities:
                print("Start create agreements!")
                agrid = 1
                for ty in range(1, 5):
                    for i in range(1, 3001):
                        # print((agrid, type_agr[ty] + " " + randomStringDigits(5)))
                        store.add_new_agreement(agrid, type_agr[ty] + " " + randomStringDigits(6))
                        agrid += 1
                num_entity["agreement"] = agrid - 1
                print("creating agreement completed!")
                print(num_entity)
                # create event entities:
                eventid = 1
                for index in range(1, 7):
                    for ty in range(0, 5):
                        for to in range(1, 21):
                            for po in range(1, 21):
                                # print((eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[po]+ " lần "+ str(index)))
                                store.add_new_event(eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[
                                    po] + " lần " + str(index))
                                eventid += 1
                num_entity["event"] = eventid - 1
                print("creating event completed!")
                print(num_entity)
                # add relationships:
                add_relationships_5000(store, book, num_entity, 6, 4, "Rules")
                print("creating relationships completed!")

                pass
                #########################################################
                #########################################################
            if store.number_entity == 1000000:
                # create country entities:
                print("starting create country")
                for ctyid in range(1, sheet_country.nrows):
                    store.add_new_country(ctyid, country_names[ctyid])
                    # pass
                num_entity["country"] = sheet_country.nrows - 1
                print("creating country completed!")
                print(num_entity)
                # create time entities:
                print("starting create time")
                timeid = 1
                for date in range(1, 29):
                    for month in range(1, 13):
                        for year in range(1817, 2070):
                            if date < 10:
                                str_date = "0" + str(date)
                            else:
                                str_date = str(date)
                            if month < 10:
                                str_month = "0" + str(month)
                            else:
                                str_month = str(month)
                            store.add_new_time(timeid, str(year) + "-" + str_month + "-" + str_date)
                            timeid += 1
                    # print((i, str(date) + "/" + str(month) + "/" + str(year)))
                num_entity["time"] = timeid - 1
                print("creating time completed!")
                print(num_entity)
                # create location entities:
                print("starting create location")
                locid = 1
                for locid_town in range(1, 101):
                    for locid_dis in range(1, 18):
                        for locid_pro in range(1, 51):
                            # print((locid, location_town[0] + " " + location_town[locid_town] + " " +location_dis[0] + " " + location_dis[locid_dis]+ " "+ location_pro[0] + " " + location_pro[locid_pro]))
                            store.add_new_location(locid,
                                                   location_town[0] + " " + location_town[locid_town] + " " +
                                                   location_dis[0] + " " + location_dis[locid_dis] + " " +
                                                   location_pro[0] + " " + location_pro[locid_pro])
                            locid = locid + 1
                num_entity["location"] = locid - 1
                print("creating location completed!")
                print(num_entity)
                # print(n_entity_remain_each)
                # create person entities:
                print("starting create person")
                personid = 1
                for fid_name in range(1, 84):
                    for mid_name in range(1, 26):
                        for lid_name in range(1, 101):
                            store.add_new_person(personid,
                                                 first_name[fid_name] + " " + last_name[mid_name] + " " + last_name[
                                                     lid_name],
                                                 role1[random.randrange(0, 5)])
                            # print(role1[random.randrange(0, 5)])
                            personid += 1
                # print(personid)
                num_entity["person"] = personid - 1
                print("creating person completed!")
                print(num_entity)

                # create organization entities:
                print("Start create organization")
                orgid = 1
                for org_index in range(1, 49):
                    store.add_new_organization(orgid, organizations_tw[org_index])
                    orgid += 1
                for orgid_local in range(1, 39):
                    for loc_pro_index in range(1, 64):
                        # print((orgid, organizations_local[orgid_local] + " " + location_pro[0] + " " + location_pro[loc_pro_index]))
                        store.add_new_organization(orgid,
                                                   organizations_local[orgid_local] + " " + location_pro[0] + " " +
                                                   location_pro[loc_pro_index])
                        orgid = orgid + 1
                    for loc_dis_index in range(1, 161):
                        # print((orgid, organizations_local[orgid_local] + " " + location_dis[0] + " " + location_dis[loc_dis_index]))
                        store.add_new_organization(orgid,
                                                   organizations_local[orgid_local] + " " + location_dis[0] + " " +
                                                   location_dis[loc_dis_index])
                        orgid = orgid + 1
                for orgid_ngo in range(1, 163):
                    for cty_index in range(1, 225):
                        # print((orgid, organizations_ngo[orgid_ngo] + " " + " " +country_names[cty_index]))
                        store.add_new_organization(orgid, organizations_ngo[orgid_ngo] + " " + country_names[cty_index])
                        orgid = orgid + 1
                for index_uni in range(1, 4):
                    for index_field in range(1, 18):
                        for f_name in range(1, 30):
                            for mi_name in range(1, 111):
                                store.add_new_organization(orgid, organizations_uni[index_uni] + " " + organizations_field[
                                    index_field] +
                                                           " " + first_name[f_name] + " " + last_name[mi_name])
                                orgid += 1
                num_entity["organization"] = orgid - 1
                print("creating organization completed!")
                print(num_entity)
                # create agreement entities:
                print("Start create agreements!")
                agrid = 1
                for ty in range(1, 5):
                    for i in range(1, 51876):
                        # print((agrid, type_agr[ty] + " " + randomStringDigits(5)))
                        store.add_new_agreement(agrid, type_agr[ty] + " " + randomStringDigits(6))
                        agrid += 1
                num_entity["agreement"] = agrid - 1
                print("creating agreement completed!")
                print(num_entity)
                # create event entities:
                print("Start create events")
                eventid = 1
                for index in range(1, 84):
                    for ty in range(0, 5):
                        for to in range(1, 26):
                            for po in range(1, 21):
                                # print((eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[po]+ " lần "+ str(index)))
                                store.add_new_event(eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[
                                    po] + " lần " + str(index))
                                eventid += 1
                num_entity["event"] = eventid - 1
                print("creating event completed!")
                print(num_entity)
                # add relationships:
                # add_relationships_1M(store, book, num_entity, 6, 4, "Rules")
                add_relationships_5000(store, book, num_entity, 6, 4, "Rules")
                print("creating relationships completed!")
                # print(num_entity)
                #################################################################
                #################################################################
            elif store.number_entity == 15000000:
                # create country entities:
                print("starting create country")
                for ctyid in range(1, sheet_country.nrows):
                    store.add_new_country(ctyid, country_names[ctyid])
                    # pass
                num_entity["country"] = sheet_country.nrows - 1
                print("creating country completed!")
                print(num_entity)
                # create time entities:
                print("starting create time")
                timeid = 1
                for date in range(1, 29):
                    for month in range(1, 13):
                        for year in range(1600, 2020):
                            if date < 10:
                                str_date = "0" + str(date)
                            else:
                                str_date = str(date)
                            if month < 10:
                                str_month = "0" + str(month)
                            else:
                                str_month = str(month)
                            store.add_new_time(timeid, str(year) + "-" + str_month + "-" + str_date)
                            timeid += 1
                    # print((i, str(date) + "/" + str(month) + "/" + str(year)))
                num_entity["time"] = timeid - 1
                print("creating time completed!")
                print(num_entity)
                # create location entities:
                print("starting create location")
                locid = 1
                for locid_town in range(1, 300):
                    for locid_dis in range(1, 160):
                        for locid_pro in range(1, 64):
                            # print((locid, location_town[0] + " " + location_town[locid_town] + " " +location_dis[0] + " " + location_dis[locid_dis]+ " "+ location_pro[0] + " " + location_pro[locid_pro]))
                            store.add_new_location(locid,
                                                   location_town[0] + " " + location_town[locid_town] + " " +
                                                   location_dis[0] + " " + location_dis[locid_dis] + " " +
                                                   location_pro[0] + " " + location_pro[locid_pro])
                            locid = locid + 1
                num_entity["location"] = locid - 1
                print("creating location completed!")
                print(num_entity)
                # create person entities:
                print("starting create person")
                personid = 1
                for fid_name in range(1, 140):
                    for mid_name in range(1, 98):
                        for lid_name in range(1, 221):
                            store.add_new_person(personid,
                                                 first_name[fid_name] + " " + last_name[mid_name] + " " + last_name[
                                                     lid_name],
                                                 role1[random.randrange(0, 5)])
                            # print(role1[random.randrange(0, 5)])
                            personid += 1
                # print(personid)
                num_entity["person"] = personid - 1
                print("creating person completed!")
                print(num_entity)

                # create organization entities:
                print("Start create organization")
                orgid = 1
                for org_index in range(1, 49):
                    store.add_new_organization(orgid, organizations_tw[org_index])
                    orgid += 1
                for orgid_local in range(1, 39):
                    for loc_pro_index in range(1, 64):
                        # print((orgid, organizations_local[orgid_local] + " " + location_pro[0] + " " + location_pro[loc_pro_index]))
                        store.add_new_organization(orgid,
                                                   organizations_local[orgid_local] + " " + location_pro[0] + " " +
                                                   location_pro[loc_pro_index])
                        orgid = orgid + 1
                    for loc_dis_index in range(1, 161):
                        # print((orgid, organizations_local[orgid_local] + " " + location_dis[0] + " " + location_dis[loc_dis_index]))
                        store.add_new_organization(orgid,
                                                   organizations_local[orgid_local] + " " + location_dis[0] + " " +
                                                   location_dis[loc_dis_index])
                        orgid = orgid + 1
                for orgid_ngo in range(1, 163):
                    for cty_index in range(1, 225):
                        # print((orgid, organizations_ngo[orgid_ngo] + " " + " " +country_names[cty_index]))
                        store.add_new_organization(orgid, organizations_ngo[orgid_ngo] + " " + country_names[cty_index])
                        orgid = orgid + 1
                for index_uni in range(1, 5):
                    for index_field in range(1, 25):
                        for f_name in range(1, 140):
                            for mi_name in range(1, 220):
                                store.add_new_organization(orgid,
                                                           organizations_uni[index_uni] + " " + organizations_field[
                                                               index_field] +
                                                           " " + first_name[f_name] + " " + last_name[mi_name])
                                orgid += 1
                num_entity["organization"] = orgid - 1
                print("creating organization completed!")
                print(num_entity)
                # create agreement entities:
                print("Start create agreements!")
                agrid = 1
                for ty in range(1, 4):
                    for i in range(1, 988632):
                        # print((agrid, type_agr[ty] + " " + randomStringDigits(5)))
                        store.add_new_agreement(agrid, type_agr[ty] + " " + randomStringDigits(8))
                        agrid += 1
                num_entity["agreement"] = agrid - 1
                print("creating agreement completed!")
                print(num_entity)
                print("Start create events")
                eventid = 1
                for index in range(1, 491):
                    for ty in range(0, 5):
                        for to in range(1, 56):
                            for po in range(1, 23):
                                # print((eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[po]+ " lần "+ str(index)))
                                store.add_new_event(eventid, type_event[ty] + " " + topic_event[to] + " " + post_fix[
                                    po] + " lần " + str(index))
                                eventid += 1
                num_entity["event"] = eventid - 1
                print("creating event completed!")
                print(num_entity)
                # add relationships:
                # add_relationships_1M(store, book, num_entity, 6, 4, "Rules")
                add_relationships_5000(store, book, num_entity, 6, 4, "Rules")
                print("creating relationships completed!")

        store.close()
def add_new_person( personid, personname, personrole):
    line_data = "person" + str(personid) + ',"' + personrole + " " + personname + '",'\
                + '"' + personname + ' là ' + personrole + '",' + "Person" + "\n"
    print(line_data)
if __name__ == '__main__':
    # main((100, 200, "/home/phien/DatasetNeo4j/Dataset100/"))
    # main((5000, 7000, "/home/phien/DatasetNeo4j/Dataset5k/"))
    # main((15000000, 17000000, "/home/phien/.config/Neo4j Desktop/Application/neo4jDatabases/"
    #                   "database-d2edfdb8-d732-452d-afbd-675154fdd38d/installation-3.5.12/import/"))
    # main((60000, 80000, "/home/phien/.config/Neo4j Desktop/Application/neo4jDatabases/database-4a2a4e58-9147-4a34-9c5e-eb1e2a718602/installation-4.0.3/import/"))
    main((5000, 15000, "/home/phien/DatasetNeo4j/"))