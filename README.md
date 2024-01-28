
*******************     Terminal      **********************

    -v: see detail result
    -s: see print()
    -h: list of all the props of pytest
    -n: number of // threads you want to run (xdist)


*******************     pytest.ini      **********************

python_files = test_*.py
python_classes = *Tests
python_functions = test_*
addopts = -p no:warnings


*******************     Mark       ******************* 

pytest -m the_name_of_the_mark  # runs the marked tests
pytest -m "smt and smtelse"     #in the same file
pytest -m "smt or smtelse"      #in the same root folder
pytest -m "not smt"             #all but this

A good habits it's to create a class with the name of the tested product and add a mark
@mark.body
class BodyClassTests

* SKIP/FAILED:
@mark.skip(reason= "not yet updat") * this gonna skip the designeted function/test
@mark.xfail(reason= "to be deprecated") * it expect to fail

* PARAMS:
@mark.parametrize('tv_brand', [     #for every injected params it runs 1 time
    ('Samsung'),
    ('Sony'),
    ('Vizio')
])

Multiple browsers automation: THE FILE MUST BE CALLED "conftest.py"
@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()
     

*******************     Fixture     ******************* 

@fixture(scope='')
    function: open browser, run and close. open new(!) browser, run and close (list)
    session: open browser, run and close. open same(!) browser, run and close (gen object)


pytest-html
place: pytest --html="result.html"   #place and name of the file
       pytest --junitxml="result.xml" (need Jenkins!)


It gives you new oppy in the cli:
def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Enviroment to run test")


pytest-xdist for // testing
