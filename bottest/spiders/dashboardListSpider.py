import scrapy
import json
import requests
import os 

class ListSpider(scrapy.Spider):
    name = 'dashboardlist'
    allowed_domains = ['dune.com']
    print(os.getcwd())
    
    
    
    f = open('./payloads/dashboardListPayload.json')
    pay_load = json.load(f)
        
    url = 'https://core-hsr.dune.com/v1/graphql'
    headers = {"x-hasura-api-key" : ""};
        

    def start_requests(self):
        while(self.pay_load["variables"]["offset"] <= 44840):
            yield scrapy.http.JsonRequest(url=self.url, method='POST', headers = self.headers , data = self.pay_load, callback=self.parse)
            self.pay_load["variables"]["offset"] = self.pay_load["variables"]["offset"] + 20

    def parse(self, response):
        data = ((json.loads(response.body)))['data'];
        
        dbs = data['dashboards'];
        for q in dbs:
            yield q
        
        
 