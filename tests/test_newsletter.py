#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.newsletter import (NewsletterPage, MainNewsletterPage,
                                      OtherNewsletterPage)
import pytest
xfail = pytest.mark.xfail


class TestNewsletter:

    def test_newsletter(self, mozwebqa):
        pg = MainNewsletterPage(mozwebqa)
        pg.go_to_newsletter_page()
        self.signup_workflow(pg)

    def test_other_newsletters(self, mozwebqa):
        pg = OtherNewsletterPage(mozwebqa)
        pg.goto_page('me@testmozilla.com', 'us', 'en', 'text')

        # Make sure it pre-filled the format correctly
        Assert.equal(pg.get_email(), 'me@testmozilla.com')
        Assert.equal(pg.get_country(), 'United States')
        Assert.equal(pg.get_lang(), 'English')
        Assert.equal(pg.get_format(), 'text')
        Assert.true(pg.is_mozilla_and_you_selected)

        pg.click_submit()

        Assert.false(pg.is_form_visible)
        Assert.equal("Thanks for updating your email preferences.", pg.thank_you_message)

    def test_newsletter_fr(self, mozwebqa):
        pg = NewsletterPage(mozwebqa)
        pg.go_to_newsletter_page('/fr/newsletter/')
        self.signup_workflow(pg)

    def test_newsletter_de(self, mozwebqa):
        pg = NewsletterPage(mozwebqa)
        pg.go_to_newsletter_page('/de/newsletter/')
        self.signup_workflow(pg)

    def test_newsletter_pt(self, mozwebqa):
        pg = NewsletterPage(mozwebqa);
        pg.go_to_newsletter_page('/pt-BR/newsletter/')
        self.signup_workflow(pg)

    def signup_workflow(self, pg):
        """Submits the form with errors, and then with values that
        should be a success"""

        pg.click_sign_me_up()

        Assert.true(pg.is_privacy_policy_error_visible)
        Assert.false(pg.is_success_visible)

        pg.type_email('me@testmozilla.com')
        pg.agree_to_privacy_policy()
        pg.click_sign_me_up()
