class blog:
    def __init__(self,page):
        self.page=page
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.appdev_blog=page.locator('//a[@href="/blog/category/app-development/"]')
        self.ai_blog=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.contmkt_blog=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.crmdev_blog=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digmakt_blog=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommdev_blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[1]')
        self.emailmarkt_blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"])[1]')
        self.gd_blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[1]')
        self.sit_blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"])[1]')
        self.sdev_blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"])[1]')
        self.uiux_blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[1]')
        self.webdev_blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[1]')
        self.blog_options=[self.appdev_blog,self.ai_blog,self.contmkt_blog,self.crmdev_blog,self.digmakt_blog,
                           self.ecommdev_blog,self.emailmarkt_blog,self.gd_blog,self.sit_blog,self.sdev_blog,
                           self.uiux_blog,self.webdev_blog]

    def blog_options_clicking(self):
        for i in self.blog_options:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back() 



        