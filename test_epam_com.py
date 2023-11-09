import re

from playwright.sync_api import Page, expect, Locator

from epam_page import EpamPage



def test_search_lviv_location(page: Page):
    epam_page = EpamPage(page)
    epam_page.open_epam_com()
    

    expect(page).to_have_title(re.compile("^EPAM"))

    epam_page.click_careers()

    expect(page).to_have_title(re.compile('Explore Professional Growth Opportunities | EPAM Careers'))

    epam_page.click_select()

    epam_page.click_city()

    expect(page.locator('.select2-selection__rendered')).to_have_text('Vienna')

    epam_page.click_find()

    expect(page.locator('h1')).to_have_text(re.compile('We found .* job openings for you'))

    




    


    



    # TODO:
    # 1) click Location dropdown
    # 2) select Lviv
    # 3) click Find
    # 4) check the phrase `We Found 26 Job Openings for You` <-- replace "26" by relevant regular expresion \d
