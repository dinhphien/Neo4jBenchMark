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
        self.fileEntityObject = open(dirname + 'entities'+ str(self.number_entity) + '.csv', "a+" )
        self.fileRelationObject = open(dirname + 'relationships' + str(self.number_entity) + '.csv', "a+")
        self.fileTimeEntityObject = open(dirname + 'time_entities' + str(self.number_entity )+ '.csv', "a+")
        self.fileNewsEntityObject = open(dirname + 'news_entities' + str(self.number_entity )+ '.csv', "a+")
        self.fileFactEntityObject = open(dirname + 'fact_entities' + str(self.number_entity )+ '.csv', "a+")

    def close(self):
        self.fileEntityObject.close()
        self.fileRelationObject.close()
        self.fileTimeEntityObject.close()

    def writeToFile(self, fileObject, line):
        fileObject.write(line)

    def add_new_person(self, personid, personname, personrole):
        line_data = "person" + str(personid) + ',"' + personrole + " " + personname + '",' \
                    + '"' + personname + ' là ' + personrole + '",' + "Person" + "\n"
        self.writeToFile(self.fileEntityObject, line_data)
        return personid


    def add_new_organization(self, orgid, orgname):
        line_data = "organization" + str(orgid) + ',"' + orgname + '",' \
                    + '"' + orgname + " là một tổ chức ....." + '",' + "Organization" + "\n"
        self.writeToFile(self.fileEntityObject, line_data)
        return orgid

    def add_new_location(self, locationid, locationname):
        line_data = "location" + str(locationid) + ',"' + locationname + '",' \
                    + '"' + locationname + ' là một địa danh ....' + '",' + "Location" + "\n"
        self.writeToFile(self.fileEntityObject, line_data)
        return locationid

    def add_new_country(self, countryid, countryname):
        population = random.randrange(10000000, 2000000000)
        squares = random.randrange(10000000, 2000000000)
        line_data = "country" + str(countryid) + ',"' + countryname + '",' \
                    + '"' + countryname + ' là quốc gia có dân số là ' + str(population) \
                                     + ' và diện tích là ' + str(squares) + '",' + "Country" + "\n"
        self.writeToFile(self.fileEntityObject, line_data)
        return countryid

    def add_new_time(self, timeid, time):
        line_data = "time" + str(timeid) + ',"' + time + '",' + time + "," + "Time" + "\n"
        self.writeToFile(self.fileTimeEntityObject, line_data)
        return timeid

    def add_new_event(self, eventid, eventname):
        line_data = "event" + str(eventid) + ',"' + eventname + '",' \
                    + '"' + eventname + ' là sự kiện được tổ chức .....' + '",' + "Event" + "\n"
        self.writeToFile(self.fileEntityObject, line_data)
        return eventid

    def add_new_agreement(self, agrid, agrname):
        line_data = "agreement" + str(agrid) + ',"' + agrname + '",' \
                    + '"' + agrname + ' được kí kết ....' + '",' + "Agreement" + "\n"
        self.writeToFile(self.fileEntityObject, line_data)
        return agrid
    def add_news (self, new_id):
        index_topic = random.randrange(0, len(TOPIC_NEWS))
        linkUrl = "http://samples.org/" + randomStringDigits(6, 4)
        new_data = "news" + str(new_id) + ',' + linkUrl + ',' + TOPIC_NEWS[index_topic] + ',' + "News" + '\n'
        self.writeToFile(self.fileNewsEntityObject, new_data)
        return new_id

    def add_fact_new_100(self, sub_index, obj_index, relation, time_id, location_id, location_type, fact_id, new_id):
        # create a new fact entity:
        fact_data = "fact" + str(fact_id) + ',' + "Fact" + '\n'
        self.writeToFile(self.fileFactEntityObject, fact_data)

        # add relationships:
        self.writeToFile(self.fileRelationObject,
                         "news"+ str(new_id) + ',' + "fact" + str(fact_id) + ',' + "HAS_FACT" + '\n')
        self.writeToFile(self.fileRelationObject,
                        "fact" + str(fact_id) + ',' + relation[0] + str(sub_index) + ',' + "HAS_SUBJECT_" +
                         relation[1].replace(" ", "_").upper()+ "\n" )
        self.writeToFile(self.fileRelationObject,
                         "fact" + str(fact_id) + ',' + relation[2] + str(obj_index) + ',' + "HAS_OBJECT_" +
                         relation[1].replace(" ", "_").upper()+ "\n" )
        if location_id != -1:
            self.writeToFile(self.fileRelationObject,
                         "fact" + str(fact_id) + ',' + location_type + str(location_id) + ',' + "OCURRED_IN" + '\n')
        if time_id != -1:
            self.writeToFile(self.fileRelationObject,
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
        if n_relations % 1000000 == 0:
            print(n_relations)

def main(argv=None):
    if not argv:
        pass
    else:
        store = Store(argv[0], argv[1], argv[2])
        print(argv[0])
        print(argv[1])
        num_entity = {}
        number_entity_each = math.floor(argv[0] / 7)

        # create country entity:
        for ctyid in range(1, number_entity_each + 1):
            country_name = "Nước " + randomStringDigits(6, 3) + " " + randomStringDigits(6, 4)
            store.add_new_country(ctyid, country_name)
        num_entity["country"] = ctyid
        # num_entity["country"] = 7142857

        # create person entity:
        prefix_person = ["Bộ trưởng ", "Thủ tướng ", "Chủ tịch nước " , ""
                         "Phó Thủ tướng ", "Chủ tịch Quốc hội ", "Phó chủ tịch nước "]
        for personid in range(1, number_entity_each + 1):
            person_name = randomStringDigits(6, 3) + " " + randomStringDigits(6, 4)
            store.add_new_person(personid, person_name, prefix_person[random.randrange(0, len(prefix_person))] )
        num_entity["person"] = personid
        # num_entity["person"] =7142857

        # create location entities:
        prefix_location = ["Tỉnh ", "Huyện ", "Xã ","Sông ", "Núi ", "Biển "]
        for locid in range(1, number_entity_each + 1):
            location_name = prefix_location[random.randrange(0, len(prefix_location))] + randomStringDigits(6, 3) + " " + randomStringDigits(6, 4)
            store.add_new_location(locid, location_name)
        num_entity["location"] = locid
        # num_entity["location"] = 7142857

        # create organization entities:
        prefix_org = ["Công ty ", "Bộ ", "Ủy Ban Nhân dân Huyện ", "Bệnh Viện ", "Trường tiểu học ",
                      "Tòa án Nhân dân huyện "]
        for orgid in range(1, number_entity_each + 1):
            organization_name = prefix_org[random.randrange(0, len(prefix_org))] + randomStringDigits(6, 3) + " " + randomStringDigits(6, 4)
            store.add_new_organization(orgid, organization_name)
        num_entity["organization"] = orgid
        # num_entity["organization"] = 7142857

        # create agreement entities:
        prefix_agr = ["Hội nghị ", "Hiệp ước ", "Hòa ước", "Hiệp định "]
        for agrid in range(1, number_entity_each + 1):
            agreement_name = prefix_agr[random.randrange(0, len(prefix_agr))] + randomStringDigits(6, 3) + " " + randomStringDigits(6, 4)
            store.add_new_agreement(agrid, agreement_name)
        num_entity["agreement"] = agrid
        # num_entity["agreement"] = 7142857

        # create event entities:
        event_prefix = ["Cuộc thi ", "Phong trào ", "Chiến dịch ", "Sự kiện ", "Cuộc vận động "]
        for eventid in range(1, number_entity_each + 1):
            event_name = event_prefix[random.randrange(0, len(event_prefix))] + randomStringDigits(6, 3) + " " + randomStringDigits(6, 4)
            store.add_new_event(eventid, event_name)
        num_entity["event"] = eventid
        # num_entity["event"] = 7142857

        # create time entities:
        for timeid in range(1, number_entity_each + 1):
            year = random.randrange(1900, 2060)
            date = random.randrange(1, 29)
            month = random.randrange(1, 13)
            if date < 10:
                str_date = "0" + str(date)
            else:
                str_date = str(date)
            if month < 10:
                str_month = "0" + str(month)
            else:
                str_month = str(month)
            store.add_new_time(timeid, str(year) + "-" + str_month + "-" + str_date)
        num_entity["time"] = timeid
        # num_entity["time"] = 7142857
        #
        # print(num_entity)
        # add relationships:
        print("creating relationships!")
        with xlrd.open_workbook('./data_entity.xlsx', on_demand=True) as book:
            add_relationships_100(store, book, num_entity, 6, 4, "RelationRules")
        print("finished creating relationships!")

if __name__ == '__main__':
    main((40000000, 60000000, "/home/phien/Neo4j_Server/Neo4jLargeDataSet/neo4j-enterprise-4.0.4_40M/import/"))



