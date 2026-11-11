class vertical:
    def __init__(self,page):
        self.page=page
        #vertical locator
        self.vert=page.locator('(//a[text()="Verticals"])[1]')
        self.trd=page.locator('//li[@data-id="trading"]')
        self.stktrd=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.paptrd=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cfdtrd=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.tddappdev=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algtrd=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.cstmtrd=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webprttrd=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.trading_options=[self.stktrd,self.paptrd,self.cfdtrd,self.tddappdev,self.algtrd,self.cstmtrd,self.webprttrd]

        #verticals-> Retail and Ecommerce
        self.re=page.locator('//li[@data-id="retailEcommerce"]')
        self.ecomm_appdev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.re_options=[self.ecomm_appdev]

        # #verticals -> HealthCare
        self.helt=page.locator('//li[@data-id="healthcare"]')
        self.dn=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.hta=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.health_options=[self.dn,self.hta]

        #vertical -> Fintech
        self.ft=page.locator('//li[@data-id="fintech"]')
        self.pos=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto = page.locator('(//a[text()="Crypto"])[1]')
        self.fintech_options=[self.pos,self.crypto]

        #vertical ->Custom App
        self.ca=page.locator('//li[@data-id="customApp"]')
        self.dad=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrm=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.trv=page.locator('(//a[text()="Travel"])[1]')
        self.dat_app_dev=page.locator('(//a[text()="Dating App Development"])[1]')
        self.crm=page.locator('(//a[text()="CRM Development"])[1]')
        self.erp=page.locator('(//a[text()="ERP App Development"])[1]')
        self.elern=page.locator('(//a[text()="E-Learning"])[1]')
        self.rest=page.locator('(//a[text()="Real Estate"])[1]')
        self.custom_options=[self.dad,self.hrm,self.trv,self.dat_app_dev,self.crm,self.erp,self.elern,self.rest]

    def trading_options_clicking(self):
        for i in self.trading_options:
         self.vert.hover()
         self.trd.hover()
         i.click()
         self.page.wait_for_load_state('load')
         self.page.go_back()

    def rande_options_clicking(self):
       for i in self.re_options:
          self.vert.hover()
          self.re.hover()
          i.click()
          self.page.wait_for_load_state('load')
          self.page.go_back()

    def healthcare_options_clicking(self):
       for i in self.health_options:
          self.vert.hover()
          self.helt.hover()
          i.click()
          self.page.wait_for_load_state('load')
          self.page.go_back()

    def fintech_options_clicking(self):
           for i in self.fintech_options:
              self.vert.hover()
              self.ft.hover()
              i.click()
              self.page.wait_for_load_state('load')
              self.page.go_back()

    def customapp_options_clicking(self):
            for i in self.custom_options:
                self.vert.hover()
                self.ca.hover()
                i.click()
                self.page.wait_for_load_state('load')
                self.page.go_back()

