class countries:
    def __init__(self, page):
        self.page=page
        self.countries=page.locator('//select[@id="countrySelector"]')
        self.country_list=['UAE', 'USA', 'India']

    def country_list_options(self):
        for i in self.country_list:
            self.countries.click()
            self.countries.select_option(i)
            self.page.wait_for_timeout(3000)