class Portfolio:
    def __init__(self,page):
        self.page=page
        self.portfolio=page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]').click()
        self.ics_homework=page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wings_pharma=page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena_animation=page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360=page.locator('//a[@href="https://home360stores.com/"]')
        self.club_meetings=page.locator('//h4[text()="Club Meetings"]')
        self.cord_cable=page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')
    

