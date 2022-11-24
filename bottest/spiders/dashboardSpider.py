import scrapy
import json
import requests

class SQLSpider(scrapy.Spider):
    name = 'dashboard'
    allowed_domains = ['dune.com']

    f = open('./payloads/dashboardPayload.json')
    pay_load = json.load(f)
        
    url = 'https://core-hsr.dune.com/v1/graphql'
    headers = {"x-hasura-api-key" : ""};
        

    def start_requests(self):
        seed_f = open("./dashboard_list.json", "r");
        # ignore first line, that is '['
        line = seed_f.readline();
        
        while line:
            line = seed_f.readline();
            
            if line == "":
                print(f"end of file!")
                break;
            line = line.strip();
            if line == ']' :
                break;
            
            q = json.loads(line.strip(','));
            
            # some case is Team only to do the work without user name
            if q["user"] is not None:
                user = q["user"]["name"];
            else:
                user = user = q["team"]["handle"];
           
            slug = q["slug"];
            self.pay_load["variables"]["user"] = user;
            self.pay_load["variables"]["slug"] = slug;
            #print(self.pay_load)
            yield scrapy.http.JsonRequest(url=self.url, method='POST', headers = self.headers , data = self.pay_load, callback=self.parse)
            

    def parse(self, response):
        
        yield json.loads(response.body);
     