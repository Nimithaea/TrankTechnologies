class technologies:
    def __init__(self,page):
        self.page=page

        self.tech=page.locator('(//a[text()="Technologies"])[1]')
        self.ecomm=page.locator('//li[@data-id="ecomm"]')
        self.mag_dev=page.locator('//a[text()="Magento Development"]')
        self.opn_dev=page.locator('(//a[text()="Opencart Development"])[1]')
        self.code_dev=page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.wdprs_dev=page.locator('(//a[text()="WordPress Development"])[1]')
        self.bigcomm=page.locator('(//a[text()="Big Commerce"])[1]')
        self.shp_dev=page.locator('(//a[text()="Shopify Development"])[1]')
        self.csc_dev=page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.njs_dev=page.locator('(//a[text()="Node JS Development"])[1]')
        self.nop_comm=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.woo_comm=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.lar_dev=page.locator('(//a[text()="Laravel Development"])[1]')
        self.pres_dev=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.dru_dev=page.locator('(//a[text()="Drupal Development"])[1]')
        self.wix_comm=page.locator('(//a[text()="Wix Development"])[1]')
        self.joo_comm=page.locator('(//a[text()="Joomla Development"])[1]')
        self.rjs_dev=page.locator('(//a[text()="React JS Development"])[1]')
        self.ejs_dev=page.locator('(//a[text()="Express JS Development"])[1]')

        self.tech_ecomm_options=[self.mag_dev,self.opn_dev,self.code_dev,self.wdprs_dev,self.bigcomm,self.shp_dev,self.csc_dev,
                                 self.njs_dev,self.nop_comm,self.woo_comm,self.lar_dev,self.pres_dev,self.dru_dev,self.wix_comm,self.joo_comm,self.rjs_dev,self.ejs_dev]

        # technologies -> mobile app development
        self.mobapp=page.locator('//li[@data-id="mobileApp"]')
        self.rnma_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.ema_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xam_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.ionic_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.swift_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.appint_book_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobapp_dev_options=[self.rnma_dev,self.ema_dev,self.xam_dev,self.kotlin_dev,self.flutter_dev,
                                         self.ionic_dev,self.swift_dev,self.appint_book_dev]
    def tech_ecomm_options_clicking(self):
        for i in self.tech_ecomm_options:
         self.tech.hover()
         self.ecomm.hover()
         i.click()
         self.page.wait_for_load_state('load')
         self.page.go_back()    
      

    def mobapp_dev_options_clicking(self):
        for i in self.mobapp_dev_options:
            self.tech.hover()
            self.mobapp.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back() 

