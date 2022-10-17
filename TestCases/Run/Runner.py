from unittest import TestLoader, TextTestRunner, TestSuite
from TestCases.Clear_card_test_file import ClearCart
from TestCases.Search_functionality_test_file import SearchFunctionality
from TestCases.Sign_in_test_file import SignIn

# Todo Create Test Case That will add product to card "Meline"
# Todo Create Test Case that will clear card all products "Elen"

class RunnerClass:
    # Todo Organize unittest creating suite part "Nelli"
    pass


if __name__ == "__main__":
    # Todo get suite and run "Hayk"
    loader = TestLoader()


    suite = TestSuite((
        loader.loadTestsFromTestCase(ClearCart),
        loader.loadTestsFromTestCase(SearchFunctionality),
        loader.loadTestsFromTestCase(SignIn)
    ))
    # run test
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # Todo Generate HTML report "Vahagn"
