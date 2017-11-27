# This file is part of the party_supplier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import doctest_setup, doctest_teardown


class PartySupplierTestCase(ModuleTestCase):
    'Test Party Supplier module'
    module = 'party_supplier'


def suite():
    suite = trytond.tests.test_tryton.suite()
    from trytond.modules.company.tests import test_company
    for test in test_company.suite():
        if test not in suite and not isinstance(test, doctest.DocTestCase):
            suite.addTest(test)
    from trytond.modules.account.tests import test_account
    for test in test_account.suite():
        if test not in suite and not isinstance(test, doctest.DocTestCase):
            suite.addTest(test)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartySupplierTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_party_supplier.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='UTF-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
