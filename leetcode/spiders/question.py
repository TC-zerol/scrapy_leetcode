# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class QuestionSpider(scrapy.Spider):
    name = 'question'
    allowed_domains = ['leetcode-cn.com']


    def start_requests(self):
        self.res = pd.DataFrame(columns=('title', 'content', 'difficulty', 'accepted', 'submit'))
        self.index = 0
        base_url = 'https://leetcode-cn.com/problems/two-sum/'
        yield scrapy.Request(url=base_url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//*[@id="lc-home"]/div/div[1]/div[2]/div/div[1]/h4/a//text()').extract()
        content = response.xpath('//*[@id="question-detail-main-tabs"]/div[2]/div/div[1]/div//text()').extract()
        difficulty = response.xpath('//*[@id="lc-home"]/div/div[1]/div[2]/div/div[1]/div/span[2]//text()').extract()
        accepted = response.xpath('//*[@id="lc-home"]/div/div[1]/div[2]/div/div[1]/h4/a//text()').extract()
        submit = response.xpath('//*[@id="lc-home"]/div/div[1]/div[2]/div/div[2]/div[3]/p[2]//text()').extract()
        next_url = response.xpath('//*[@id="lc-home"]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[3]/a[2]//@href').extract_first()
        print('https://leetcode-cn.com'+str(next_url))
        self.res.append([{'title': str(title), 'content': str(content),
                          'difficulty': str(difficulty), 'accepted': str(accepted), 'submit': str(submit)}])
        if next_url is not None:
            if self.index%10==0:
                self.res.to_csv('question'+str(self.index)+'.csv')
            yield scrapy.Request('https://leetcode-cn.com'+str(next_url), callback=self.parse)
        else:
            self.res.to_csv('question.csv')