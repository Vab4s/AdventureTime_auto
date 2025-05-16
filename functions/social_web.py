from locators.episode_page_locators import (VK_BUTTON, OK_BUTTON, MOI_MIR_BUTTON, TWITTER_BUTTON, VIBER_BUTTON,
                                            WATSUP_BUTTON, SKYPE_BUTTON, TELEGRAM_BUTTON)


def social_web(web_name: str) -> tuple:
    if web_name == 'vk.com':
        return VK_BUTTON
    elif web_name == 'ok.ru':
        return OK_BUTTON
    elif web_name == 'mail.ru':
        return MOI_MIR_BUTTON
    elif web_name == 'x.com':
        return TWITTER_BUTTON
    elif web_name == 'viber':
        return VIBER_BUTTON
    elif web_name == 'whatsapp.com':
        return WATSUP_BUTTON
    elif web_name == 'teams':
        return SKYPE_BUTTON
    elif web_name == 't.me':
        return TELEGRAM_BUTTON

