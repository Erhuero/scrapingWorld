# -*- coding: utf-8 -*-
import scrapy
import json
from pprint import pprint

class MonsterSpiderSpider(scrapy.Spider):
    name = 'monster-spider'
    allowed_domains = ['monster.com']
    
    start_urls=['https://www.monster.com/jobs/search/pagination/'
                '?q=Product-Manager&where=USA&isDynamicPage=true&isMKPagination=true&page=2&total=26']
    
    
    def parse(self, response):
        results = json.loads(response.body_as_unicode().strip('()'))
        pprint(results)
        for result in results:
            try:
                print(result['MusangKingID'])
            except:
                print('Vide')
    
    """
    start_urls = ['https://www.monster.com/jobs/search/pagination/'
    '?q=Product-Manager&where=usa&intcid=skr_navigation_nhpso_searchMain&stpage=1&jobid=218258678&isDynamicPage=true&'
    'isMKPagination=true&page={}'.format(i + 1) for i in range(1)]
    #page=2 ou {}'.format(i+1) for i in range(2)]

    def parse(self, response):
        results= json.loads(response.body)
        for result in results:
            print(result['industryName'])
            job_id = result['JobID']
            next_url="https://job-openings.monster.com"
            "/v2/job/pure-json-view?&jobid={}".format(job_id)
            return response.follow(next_url, callback = self.parse_detail)
            #print(result['DatePostedText'])
        #pprint(results)
    
    def parse_details(self, response):
        
        result = json.loads(response.body)
        
        detail={}
        
        detail["title"] = ["companyInfo","CompanyHeader"]
        detail["description"] = result["jobDescription"]
        detail["job_id"] = result["jobId"]
        
        info = result["summary"]["info"]
        for i in info:
            detail[i['title']] = i['text']
            
        return detail
    """