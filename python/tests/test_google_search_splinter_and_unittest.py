#!/usr/bin/env python

import sys
import unittest

from splinter import Browser

sys.path.append('./page_objects')

import pages

class TestGoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('chrome')
        cls.searchPage = pages.TestSearchPage()

    @classmethod
    def tearDownClass(cls):
        cls.browser.cookies.delete()
        cls.browser.quit()

    def test_filling_splinter_in_the_search_box_returns_splinter_website(self):
        self.browser.visit(self.searchPage.url)
        self.browser.fill(self.searchPage.nameSearchTextBox, 'Ninja Monkeys')
        button = self.browser.find_by_css(self.searchPage.dynamicSearchButton)
        button.click()
        self.assertTrue(self.browser.is_text_present('Ninja Monkeys'), 'No Ninja Monkeys here... :(')


unittest.main()