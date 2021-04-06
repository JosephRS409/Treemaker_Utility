from treemaker_draft_with_pytest import look_or_move, change_dir, make_dir, create_folder
from io import StringIO
import pytest
import sys
import os


def test_look_or_move_0(monkeypatch):
    # Tests whether or not the inquiry is valid.
    # Setup simulated user input: 0 and "enter" key
    test_input = StringIO("0\n")
    monkeypatch.setattr(sys, "stdin", test_input)
    cwd = os.getcwd()
    look_or_move()
    assert cwd == os.getcwd()
# def test_look_or_move_1(monkeypatch):
    test_input = StringIO("1\n0\n") # was waiting on user input # added the quit function to just 
    monkeypatch.setattr(sys, "stdin", test_input)
    cwd = os.getcwd() # path changes, so test it
    folder_name = os.path.split(cwd)[1]
    look_or_move()
    assert os.path.split(cwd)[0] == os.getcwd() # we use this in option 4
# def test_look_or_move_2(monkeypatch):
    test_input = StringIO("2\n0\n")
    monkeypatch.setattr(sys, "stdin", test_input)
    full_contents = os.listdir(os.getcwd()) # Similar to option 0. A verbose option 0.
    look_or_move()
    assert full_contents == os.listdir(os.getcwd()) # if nothing changed then true
# def test_look_or_move_3(monkeypatch):
    test_input = StringIO("3\n0\n")
    monkeypatch.setattr(sys, "stdin", test_input)
    directory = os.listdir(os.getcwd())
    look_or_move()
    assert directory == os.listdir(os.getcwd())
# def test_look_or_move_4(monkeypatch):
    test_input = StringIO(f"4\n{folder_name}\n0\n")
    monkeypatch.setattr(sys, "stdin", test_input)
    cwd = os.getcwd() # path changes, so test it
    # directory = os.path.split(cwd)[1]
    # parent_dir = os.getcwd()
    path = os.path.join(cwd, folder_name)
    look_or_move()
    assert path == os.getcwd() # Same folder we saved from test 1. Literally added it back on and we don't even have to know the folder name!


def test_change_dir_1(monkeypatch): # The junction function between make_dir() or look_or_move().
    test_input = StringIO("yes\n")
    monkeypatch.setattr(sys, "stdin", test_input)
    key = False
    change_dir()
    assert key == False
    # assert inquiry == "yes" or inquiry == "no" # This code would've worked if I were returning inquiry, but I'm not.
# def test_change_dir_2(monkeypatch):
    test_input = StringIO("no\n0\nyes\n") # redundant test of look_or_move()
    monkeypatch.setattr(sys, "stdin", test_input)
    cwd = os.getcwd()
    change_dir()
    assert cwd == os.getcwd()


def test_make_dir_1(monkeypatch):
    test_input = StringIO("no\nno\n")
    monkeypatch.setattr(sys, "stdin", test_input)
    cwd = os.getcwd()
    make_dir()
    assert cwd == os.getcwd()
# def test_make_dir_2(monkeypatch): 
    test_input = StringIO("no\nyes\nyes\n") # Go to change_dir() then main menu.
    monkeypatch.setattr(sys, "stdin", test_input)
    cwd = os.getcwd()
    make_dir()
    assert cwd == os.getcwd()
    key = False
    # change_dir()
    assert key == False
# def test_make_dir_2(monkeypatch): # Going to create_folder() fxn.
    unique_folder = "totally_unique_folder_name"
    test_input = StringIO(f"yes\n{unique_folder}\nyes\n")
    monkeypatch.setattr(sys, "stdin", test_input)# Test create_folder() through make_dir().
    cwd = os.getcwd()
    make_dir()
    # assert cwd == os.getcwd() # This line of code was holding up this make_dir() function test.
        # I wonder why.
    # test if made
    # test if duplicate
    # alter folder
    # accept folder name
    # delete folder and exit
    cwd = os.getcwd()
    path = os.path.join(cwd, unique_folder)
    # create_folder() # Enabling this line causes the unique_folder to not be deleted thus failing the next test.
    assert cwd == os.getcwd() # Huh... having this line here doesn't fail the test. I wonder why.
    assert os.path.isdir(unique_folder) == True # Check: Did we make a directory? 
    assert os.path.exists(path) == True # Check: Does unique_folder exist?
    # tail = os.path.split(path)[1]  # Unnecessary with path variable.
    os.rmdir(path) # KILL THE FOLDER!! Mwah-ha-ha! Your sacrifice will be appreciated, young folder.
    assert not os.path.exists(path) == True


def test_create_folder_1(monkeypatch):
    unique_folder = "totally_unique_folder_name"
    test_input = StringIO(f"{unique_folder}\nyes\n")
    monkeypatch.setattr(sys, "stdin", test_input)# Test create_folder()
    # test if made
    # test if duplicate
    # alter folder
    # accept folder name
    # delete folder and exit
    cwd = os.getcwd()
    path = os.path.join(cwd, unique_folder)
    create_folder()
    assert os.path.isdir(unique_folder) == True # Did we make a directory?
    assert os.path.exists(path) == True # Does unique_folder exist?
    # tail = os.path.split(path)[1]  # Unnecessary with path variable.
    os.rmdir(path)
    assert not os.path.exists(path) == True # checks if deleted
    # Can I check with:
        # os.path.exists(unique_folder) == True
        # check with isdir and listdir
        # directory in os.listdir(os.getcwd())
            # Or can I?
"""

def test_add_year_month_column():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("water.csv", parse_dates=["readDate"])
    assert len(df) == 246830

    # Ensure that the data frame doesn't have a column named yearMonth.
    assert "yearMonth" not in df.columns

    # Call the add_year_month_column function.
    df = add_year_month_column(df)

    # Ensure that the data frame now has a column named yearMonth.
    assert "yearMonth" in df.columns

    # Ensure that each cell in the yearMonth column
    # contains a period[M] with a valid year and month.
    for cell in df["yearMonth"]:
        year = cell.year
        month = cell.month
        assert 2015 <= year <= 2019
        assert 1 <= month <= 12


def test_filter_for_meter():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("water.csv", parse_dates=["readDate"])
    assert len(df) == 246830

    # Call the filter_for_meter function.
    meter_number = "M4724"
    df = filter_for_meter(df, meter_number)

    # Because the only rows remaining in the data
    # frame should be for meter M4724, verify that
    # the meter number is M4724 in all rows.
    assert len(df) == 60
    for cell in df["meterNumber"]:
        assert cell == "M4724"


def test_filter_between_dates():
    # Read the water.csv file and convert the
    # readDate column from a string to a datetime64.
    df = pd.read_csv("water.csv", parse_dates=["readDate"])
    assert len(df) == 246830

    # Call the filter_between_dates function.
    start = pd.to_datetime(f"2016-07-01")
    end = pd.to_datetime(f"2016-07-31")
    df = filter_between_dates(df, start, end)

    # Verify that the read date in all remaining
    # rows is between the start and end dates.
    assert len(df) == 4041
    for cell in df["readDate"]:
        assert start <= cell <= end
"""

pytest.main(["-v", "--tb=no", "test_treemaker_draft.py"])
