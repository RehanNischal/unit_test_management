import requests
import streamlit as st
from app.config import BACKEND_URL

def add_new_test_case():
    st.header("Add New Test Case")
    name = st.text_input("Name", key="add_case_name")
    description = st.text_area("Description", key="add_case_description")
    priority = st.text_input("priority", key="add_case_priority")
    expected_outcome = st.text_input("expected_outcome", key="add_case_outcome")
    test_suite_id = st.text_input("test_suite_id", key="add_case_suite_id")

    if st.button("Add Test Case", key="add_case"):
        if not name or not description or not priority or not expected_outcome or not test_suite_id:
            st.warning("All fields are required. Please fill in all the details.")
        else:
            try:
                payload = {
                    "name": name,
                    "description": description,
                    "priority": priority,
                    "expected_outcome": expected_outcome,
                    "test_suite_id": test_suite_id
                }
                response = requests.post(f"{BACKEND_URL}/test_cases/", json=payload)
                if response.status_code == 200:
                    st.success("Test case created successfully!")
                elif response.status_code == 400 and "does not exist" in response.json().get("detail"):
                    st.error("Invalid Test Suit ID")
                else:
                    st.error(f"Error creating test case: {response.status_code}")
            except Exception:
                st.error("Failed to connect to the backend")

def get_cases_from_suite():
    st.header("View A Particular Test Suite")
    suite_id = st.text_input("Enter Suite ID to Search", key="fetch_cases")
    if st.button("Fetch All Test Suites", key="fetch_all_suites"):
        try:
            response = requests.get(f"{BACKEND_URL}/test_cases/", params={"test_suite_id": suite_id})
            if response.status_code == 200:
                test_cases = response.json()
                if test_cases:
                    for case in test_cases:
                        st.subheader(f"Case ID: {case['id']}")
                        st.write(f"Name: {case['name']}")
                        st.write(f"Description: {case['description']}")
                        st.write(f"Status: {case['status']}")
                        st.write(f"Priority: {case['priority']}")
                        st.write(f"Expected Outcome: {case['expected_outcome']}")
                        st.write(f"Created AT: {case['created_at']}")
                        st.write(f"Updated AT: {case['updated_at']}")
                        st.write("---")
                else:
                    st.info("No test cases found.")
            else:
                st.error(f"Error fetching test cases: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend")

def get_test_case_by_id():
    st.header("View Test Case By ID")
    test_case_id = st.text_input("Enter Test Case ID to Search", key="fetch_case_id")

    if st.button("Fetch Test Case", key="fetch_case"):
        try:
            response = requests.get(f"{BACKEND_URL}/test_cases/{test_case_id}")

            if response.status_code == 200:
                test_case = response.json()

                if test_case:
                    st.subheader(f"Case ID: {test_case['id']}")
                    st.write(f"Suite ID: {test_case['test_suite_id']}")
                    st.write(f"Name: {test_case['name']}")
                    st.write(f"Description: {test_case['description']}")
                    st.write(f"Status: {test_case['status']}")
                    st.write(f"Priority: {test_case['priority']}")
                    st.write(f"Expected Outcome: {test_case['expected_outcome']}")
                    st.write(f"Created AT: {test_case['created_at']}")
                    st.write(f"Updated AT: {test_case['updated_at']}")

            elif response.json().get("detail") == "Invalid Input" and response.status_code == 400:
                st.info("No test case found with the provided ID.")
            else:
                st.error(f"Error fetching test case: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend")


def update_test_case_by_id():
    st.header("Update Test Case By ID")
    test_case_id = st.text_input("Enter Test Case ID to Update", key="update_case_id")
    name = st.text_input("Name", key="update_case_name")
    description = st.text_area("Description", key="update_case_description")
    priority = st.selectbox("Priority", ["low", "medium", "high"], key="update_case_priority")
    expected_outcome = st.text_input("Expected Outcome", key="update_case_outcome")
    status = st.selectbox("Status", ["active", "inactive"], key="update_case_status")

    if st.button("Update Test Case", key="update_case_button"):
        if not test_case_id or not name or not description or not expected_outcome or not status or not priority:
            st.warning("All fields are required. Please fill in all the details.")
        else:
            try:
                payload = {
                    "name": name,
                    "description": description,
                    "priority": priority,
                    "expected_outcome": expected_outcome,
                    "status": status
                }
                response = requests.put(f"{BACKEND_URL}/test_cases/{test_case_id}", json=payload)
                if response.status_code == 200:
                    st.success(f"Test Run ID {test_case_id} updated successfully!")
                elif response.status_code == 400 and "not found" in response.json().get("detail"):
                    st.error(f"Invalid Input: {response.status_code}")
                else:
                    st.error(f"Error updating test case: {response.status_code}")
            except Exception:
                st.error("Failed to connect to the backend")


def search_test_cases_by_keyword():
    st.header("Search Test Cases By Keyword")
    keyword = st.text_input("Enter Keyword to Search for Test Cases", key="search_keyword")

    if st.button("Search Test Cases", key="search_case_button"):
        if not keyword:
            st.warning("Please enter a keyword to search")
        else:
            try:
                response = requests.get(f"{BACKEND_URL}/test_cases/search/", params={"keyword": keyword})
                if response.status_code == 200:
                    test_cases = response.json()
                    if test_cases:
                        if len(test_cases) == 0:
                            st.info("No test cases found for the given keyword")
                        else:
                            for case in test_cases:
                                st.subheader(f"Case ID: {case['id']}")
                                st.write(f"Name: {case['name']}")
                                st.write(f"Description: {case['description']}")
                                st.write(f"Status: {case['status']}")
                                st.write(f"Priority: {case['priority']}")
                                st.write(f"Expected Outcome: {case['expected_outcome']}")
                                st.write(f"Created AT: {case['created_at']}")
                                st.write(f"Updated AT: {case['updated_at']}")
                                st.write("---")
                    else:
                        st.info("No test cases found for the given keyword.")
                else:
                    st.error(f"Error fetching test cases: {response.status_code}")
            except Exception as e:
                st.error("Failed to connect to the backend")

def delete_test_case_by_id():
    st.header("Delete Test Case by ID")
    test_case_id = st.text_input("Enter Test Case ID to Delete", key="delete_case_id")

    if st.button("Delete Test Case", key="delete_case_button"):
        if not test_case_id:
            st.warning("Please enter a Test Case ID to delete.")
        else:
            try:
                response = requests.delete(f"{BACKEND_URL}/test_cases/{test_case_id}")
                if response.status_code == 200:
                    response_data = response.json()
                    if response_data.get("message") == "Test Case not found":
                        st.error("Test Case not found")
                    else:
                        st.success("Test Case deleted successfully!")
                else:
                    st.error(f"Error deleting test case: {response.status_code}")
            except Exception:
                st.error("Failed to connect to the backend")




