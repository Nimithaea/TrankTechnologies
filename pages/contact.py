class contact:
    def __init__(self,page):
        self.page=page
        self.contactus=self.page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

        # self.page.locator('(//input[@placeholder="Your Name"])[2]').fill('Nimitha')
        # self.page.locator('(//input[@placeholder="Your Mail"])[2]').fill('abc@123@gmail.com')
        # self.page.locator('(//input[@placeholder="Enter OTP"])[2]').fill('1234')
        # self.page.locator('(//input[@placeholder="Your Company"])[2]').fill ('ABC Company')
        # self.page.locator('(//select[@name="service"])[2]').select_option('Graphic Design')
        # self.page.locator('(//input[@placeholder="Your Phone"])[2]').fill('980556789')
        # self.page.locator('(//textarea[@placeholder="Message"])[2]').fill('This is a test automation')

        self.cms_dev=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecomm_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.custom_web_dev=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.mob_app_desgn=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.res_web_desgn=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brand_ide_desgn=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.ios_dev=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.and_app_dev=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.hyd_app_dev=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.crss_plt_app_dev=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.pgs_web_app_dev=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.logo_design=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner_design=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packaging_design=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.business_card_design=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        self.contact_options=[self.cms_dev,self.ecomm_dev,self.custom_web_dev,self.mob_app_desgn,self.res_web_desgn,
                              self.brand_ide_desgn,self.ios_dev,self.and_app_dev,self.hyd_app_dev,self.crss_plt_app_dev,
                              self.pgs_web_app_dev,self.logo_design,self.banner_design,self.packaging_design,self.business_card_design]
    # #contact -> Social Media
    # self.fb=page.locator('//img[@alt="Facebook"]')
    # self.ln=page.locator('//img[@alt="LinkedIn"]')
    # self.insta=page.locator('(//img[@alt="Instagram"])[1]')
    # self.pintrest=page.locator('(//img[@alt="Instagram"])[2]')
    # self.twitter=page.locator('//img[@alt="Twitter"]')
    # self.yt=page.locator('//img[@alt="Youtube"]')
    # self.quora=page.locator('//img[@alt="Quora"]')
    def contact_options_clicking(self):
        for i in self.contact_options:
            self.contactus.click()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back() 