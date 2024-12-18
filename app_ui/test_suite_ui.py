import requests
import streamlit as st
from app.config import BACKEND_URL

def view_all_test_suites():
    st.header("View All Test Suites")
    if st.button("Fetch All Test Suites", key="fetch_all_suites"):
        try:
            response = requests.get(f"{BACKEND_URL}/test_suites/")
            if response.status_code == 200:
                test_suites = response.json()
                if test_suites:
                    for suite in test_suites:
                        st.subheader(f"Suite ID: {suite['id']}")
                        st.write(f"Name: {suite['name']}")
                        st.write(f"Description: {suite['description']}")
                        st.write(f"Status: {suite['status']}")
                        st.write(f"Created AT: {suite['created_at']}")
                        st.write(f"Updated AT: {suite['updated_at']}")
                        st.write("---")
                else:
                    st.info("No test suites found.")
            else:
                st.error(f"Error fetching test suites: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend")

def view_single_test_suite():
    st.header("View A Particular Test Suite")
    suite_id = st.text_input("Enter Suite ID to Search", key="fetch_a_suite")
    if st.button("Fetch The Test Suite", key="fetch_suite"):
        try:
            response = requests.get(f"{BACKEND_URL}/test_suites/{suite_id}")
            if response.status_code == 200:
                suite = response.json()
                if suite:
                    st.subheader(f"Suite ID: {suite['id']}")
                    st.write(f"Name: {suite['name']}")
                    st.write(f"Description: {suite['description']}")
                    st.write(f"Status: {suite['status']}")
                    st.write(f"Created AT: {suite['created_at']}")
                    st.write(f"Updated AT: {suite['updated_at']}")
                else:
                    st.info("Test suite not found.")
            elif response.status_code == 400 and response.json().get("detail") == "Invalid Input":
                st.error(f"Invalid Input: {response.status_code}")
            else:
                st.error(f"Error fetching test suite: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend")

def add_test_suite():
    st.header("Add New Test Suite")
    name = st.text_input("Name", key="add_suite_name")
    description = st.text_area("Description", key="add_suite_description")
    if st.button("Add Test Suite", key="add_suite"):
        if not name or not description:
            st.warning("All fields are required. Please fill in all the details.")
        else:
            try:
                payload = {"name": name, "description": description}
                response = requests.post(f"{BACKEND_URL}/test_suites/", json=payload)
                if response.status_code == 200:
                    st.success("Test suite created successfully!")
                else:
                    st.error(f"Error creating test suite: {response.status_code}")
            except Exception:
                st.error("Failed to connect to the backend")

def update_test_suite():
    st.header("Update Test Suite")
    suite_id = st.text_input("Enter Suite ID to Update", key="update_suite_id")
    name = st.text_input("Updated Name", key="update_suite_name")
    description = st.text_area("Updated Description", key="update_suite_description")
    status = st.selectbox("Updated Status", ["Active", "Inactive"], key="update_suite_status")
    if st.button("Update Test Suite", key="update_suite"):
        if not suite_id or not name or not description or not status:
            st.warning("All fields are required. Please fill in all the details.")
        else:
            try:
                payload = {"name": name, "description": description, "status": status}
                response = requests.put(f"{BACKEND_URL}/test_suites/{suite_id}/", json=payload)
                if response.status_code == 200:
                    st.success("Test suite updated successfully!")

                elif response.status_code == 400 and "not found" in response.json().get("detail"):
                    st.error(f"Invalid Input: {response.status_code}")
                else:
                    st.error(f"Error updating test suite: {response.status_code}")
            except Exception:
                st.error("Failed to connect to the backend")

def delete_test_suite():
    st.header("Delete Test Suite")
    suite_id = st.text_input("Enter Suite ID to Delete", key="delete_suite_id")
    if st.button("Delete Test Suite", key="delete_suite"):
        try:
            response = requests.delete(f"{BACKEND_URL}/test_suites/{suite_id}/")
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("message") == "Test Suite not found":
                    st.error("Test Suite not found")
                else:
                    st.success("Test suite deleted successfully!")
            else:
                st.error(f"Error deleting test suite: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend")
