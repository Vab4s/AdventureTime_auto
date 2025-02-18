SEASON_TITLE = ('xpath', '//div[@id="content"]//h1')

SEASON_TEXT = ('xpath', '//div[@id="content"]//span[@itemtype="https://schema.org/BreadcrumbList"]')

CONTENT_FORM = ('xpath', '//div[@id="content"]')

EPISODES = ('xpath', '//a[@class="title_link"]')
EPISODE_NAME = ('xpath', '(//a[@class="title_link"])[{}]')
