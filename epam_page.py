

class EpamPage:

  def __init__(self, page):
      self.page = page


  def open_epam_com(self):
      self.page.goto("https://www.epam.com/")

  def click_careers(self):
      careers_link = self.page.locator('.top-navigation__item-text a[href="/careers"]')
      careers_link.click()

  def click_select(self):
      select_arrow = self.page.locator('.select2-selection__arrow')
      select_arrow.click()

  def click_city(self):
      select_option = self.page.locator('[aria-label="Austria"]')
      select_option.click();
      select_city = self.page.locator('.select2-results__option').get_by_role('option', name="Vienna")
      select_city.click();
  
  def click_find(self):
      find_button = self.page.get_by_role("button", name='Find')
      find_button.click()

