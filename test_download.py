#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#                 Dave Hunt <dhunt@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import urllib2

from BeautifulSoup import BeautifulStoneSoup
import pytest
from unittestzero import Assert
from urllib import FancyURLopener


@pytest.mark.skip_selenium

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2'


class TestDownload(object):

    def test_osx_download_button_returns_status_code_200(self, testsetup):
        html = BeautifulStoneSoup(urllib2.urlopen('%s/products/download.html' % testsetup.base_url))
        link = html.find('li', 'os_osx').a['href']
        print link
        response = urllib2.urlopen(link)
        Assert.equal(response.code, 200)

    def test_linux_download_button_returns_status_code_200(self, testsetup):
        html = BeautifulStoneSoup(urllib2.urlopen('%s/products/download.html' % testsetup.base_url))
        link = html.find('li', 'os_linux').a['href']
        print link
        response = urllib2.urlopen(link)
        Assert.equal(response.code, 200)

    def test_windows_download_button_returns_status_code_200(self, testsetup):
        html = BeautifulStoneSoup(urllib2.urlopen('%s/products/download.html' % testsetup.base_url))
        link = html.find('li', 'os_windows').a['href']
        print link
        response = urllib2.urlopen(link)
        Assert.equal(response.code, 200)

    def test_download_button_returns_status_code_200_using_chrome(self, testsetup):
        '''https://bugzilla.mozilla.org/show_bug.cgi?id=672713'''
        myopener = MyOpener()
        html = BeautifulStoneSoup(myopener.open('%s/products/download.html' % testsetup.base_url))
        link = html.find('li', 'os_windows').a['href']
        print link
        response = urllib2.urlopen(link)
        Assert.equal(response.code, 200)
