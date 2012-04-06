#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.desktop.base import Base
from selenium.webdriver.support.select import Select


class NewsletterPage(Base):

    _email_sel = (By.CSS_SELECTOR, ".email")
    _agree_to_privacy_policy_checkbox_sel = (By.CSS_SELECTOR, ".privacy-check")
    _submit_button_sel = (By.CSS_SELECTOR, "#content input[name=submit]")
    _privacy_policy_error_sel = (By.CSS_SELECTOR, ".privacy-field.field-error")
    _success_pane_sel = (By.CSS_SELECTOR, ".success-pane")

    def go_to_newsletter_page(self, url='/en-US/newsletter/'):
        self.selenium.get(self.base_url + url)

    def type_email(self, email):
        self.selenium.find_element(*self._email_sel).send_keys(email)

    def agree_to_privacy_policy(self):
        self.selenium.find_element(*self._agree_to_privacy_policy_checkbox_sel).click()

    def click_sign_me_up(self):
        self.selenium.find_element(*self._submit_button_sel).click()

    @property
    def is_privacy_policy_error_visible(self):
        return self.is_element_visible(*self._privacy_policy_error_sel)

    @property
    def is_success_visible(self):
        return self.is_element_visible(*self._success_pane_sel)


class MainNewsletterPage(NewsletterPage):

    _other_newsletters_sel = (By.CSS_SELECTOR, "#other-newsletters")

    #TODO:
    @property
    def is_success_visible(self):
        return self.is_element_present(*self._other_newsletters_sel)


class OtherNewsletterPage(Base):

    _email_sel = (By.CSS_SELECTOR, "input[name=email]")
    _country_sel = (By.CSS_SELECTOR, "select[name=country]")
    _lang_sel = (By.CSS_SELECTOR, "select[name=lang]")
    _mozilla_and_you_sel = (By.CSS_SELECTOR, "input[name=mozilla-and-you]")
    _submit_sel = (By.CSS_SELECTOR, "input[name=submit]")
    _form_sel = (By.CSS_SELECTOR, "#content form")
    _thanks_locator = (By.CSS_SELECTOR, "#main-feature > h2")

    def goto_page(self, email, country, lang, format):
        self._format_sel = (By.CSS_SELECTOR, "input[name=format][value=%s]" % format)
        self.selenium.get('%s/en-US/newsletter/new/?email=%s&country=%s&lang=%s&format=%s' % (self.base_url, email, country, lang, format))

    def get_email(self):
        return self.selenium.find_element(*self._email_sel).get_attribute('value')

    def get_country(self):
        element = self.selenium.find_element(*self._country_sel)
        return Select(element).first_selected_option.text

    def get_lang(self):
        element = self.selenium.find_element(*self._lang_sel)
        return Select(element).first_selected_option.text

    def get_format(self):
        return self.selenium.find_element(*self._format_sel).get_attribute('value')

    def click_submit(self):
        self.selenium.find_element(*self._submit_sel).click()

    @property
    def is_mozilla_and_you_selected(self):
        return self.selenium.find_element(*self._mozilla_and_you_sel).is_selected()

    @property
    def is_form_visible(self):
        return self.is_element_present(*self._form_sel)

    @property
    def thank_you_message(self):
        return self.selenium.find_element(*self._thanks_locator).text
