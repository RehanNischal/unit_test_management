import streamlit as st

from app_ui.test_run_ui import (
    create_test_run,
    view_all_test_runs,
    update_test_run,
    view_single_test_run,
    delete_test_run
)
from app_ui.test_suite_ui import (
    view_all_test_suites,
    view_single_test_suite,
    add_test_suite,
    update_test_suite,
    delete_test_suite,
)

from app_ui.test_case_ui import (
    add_new_test_case,
    get_cases_from_suite,
    get_test_case_by_id,
    update_test_case_by_id,
    search_test_cases_by_keyword,
    delete_test_case_by_id
)

# Adding Sidebar Navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose Module:", ["Test Suites", "Test Cases", "Test Runs"])

if choice == "Test Suites":

    st.title("Test Management System - Test Suites")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "View ALL Test Suites",
        "View A Particular Test Suite",
        "Add Test Suite",
        "Update Test Suite",
        "Delete Test Suite"
    ])

    with tab1:
        view_all_test_suites()

    with tab2:
        view_single_test_suite()

    with tab3:
        add_test_suite()

    with tab4:
        update_test_suite()

    with tab5:
        delete_test_suite()

elif choice == "Test Cases":

    st.title("Test Management System - Test Cases")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Create Test Case",
        "View Cases in a Suite",
        "View A Particular Test case",
        "Update Test Case",
        "Search Cases With A Keyword",
        "Delete Test Case"
    ])

    with tab1:
        add_new_test_case()

    with tab2:
        get_cases_from_suite()

    with tab3:
        get_test_case_by_id()

    with tab4:
        update_test_case_by_id()

    with tab5:
        search_test_cases_by_keyword()

    with tab6:
        delete_test_case_by_id()

elif choice == "Test Runs":
    st.title("Test Management System - Test Runs")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Create Test Run",
        "View All Runs",
        "View A Particular Test Run",
        "Update Test Run",
        "Delete Test Run"
    ])

    with tab1:
        create_test_run()

    with tab2:
        view_all_test_runs()

    with tab3:
        view_single_test_run()

    with tab4:
        update_test_run()

    with tab5:
        delete_test_run()

