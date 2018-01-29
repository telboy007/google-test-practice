#!/usr/bin/env python

import sys

from splinter import Browser

sys.path.append('./page_objects')

import pages


def test_check_search_results():
    #set up
    searchPage = pages.TestSearchPage()
    browser = Browser('chrome')

    # load page
    browser.visit(searchPage.url)
    # perform search
    browser.fill(searchPage.nameSearchTextBox, 'Ninja Monkeys')
    #click dynamic search button
    button = browser.find_by_css(searchPage.dynamicSearchButton)
    button.click()
    # check results
    assert browser.is_text_present('Ninja Monkeys'), 'No Ninja Monkeys here... :('
    
    #tear down
    browser.cookies.delete()
    browser.quit()
