import streamlit as st
import requests

#Fast API URL
BACKEND_URL = "http://127.0.0.1:8000"

# Adding Sidebar Navigation for better view
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose Module:", ["Test Suites", "Test Cases"])

if choice == "Test Suites":
    st.title("Test Management System - Test Suites")

    # Tabs for Test Suites
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "View ALL Test Suites",
        "View A particular Test Suite",
        "Add Test Suite",
        "Update Test Suite",
        "Delete Test Suite"
    ])

    # View All Test Suites
    with tab1:
        st.header("View All Test Suites")
        if st.button("Fetch All Test Suites"):
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
            except Exception as e:
                st.error(f"Failed to connect to the backend: {e}")

    #GET Test Suite
    with tab2:
        st.header("View A Particular Test Suites")
        suite_id = st.text_input("Enter Suite ID to Search")
        if st.button("Fetch The Test Suite"):
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
                        st.write("---")
                    else:
                        st.info("No test suites found.")
                else:
                    st.error(f"Error fetching test suites: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to the backend: {e}")

    # Add Test Suite
    with tab3:
        st.header("Add New Test Suite")
        name = st.text_input("Name")
        description = st.text_area("Description")
        if st.button("Add Test Suite"):
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
                except Exception as e:
                    st.error(f"Failed to connect to the backend: {e}")

    # Update Test Suite
    with tab4:
        st.header("Update Test Suite")
        suite_id = st.text_input("Enter Suite ID to Update")
        name = st.text_input("Updated Name")
        description = st.text_area("Updated Description")
        status = st.selectbox("Updated Status", ["Active", "Inactive"])
        if st.button("Update Test Suite"):
            if not suite_id or not name or not description or not status:
                st.warning("All fields are required. Please fill in all the details.")
            else:
                try:
                    payload = {"name": name, "description": description, "status": status}
                    response = requests.put(f"{BACKEND_URL}/test_suites/{suite_id}/", json=payload)
                    if response.status_code == 200:
                        st.success("Test suite updated successfully!")
                    else:
                        st.error(f"Error updating test suite: {response.status_code}")
                except Exception as e:
                    st.error(f"Failed to connect to the backend: {e}")

    # Delete Test Suite
    with tab5:
        st.header("Delete Test Suite")
        suite_id = st.text_input("Enter Suite ID to Delete")
        if st.button("Delete Test Suite"):
            try:
                response = requests.delete(f"{BACKEND_URL}/test_suites/{suite_id}/")
                if response.status_code == 200:
                    if response.json().get("message") == "Test Suit not found":
                        st.error("Not Found")
                    else:
                        st.success("Test suite deleted successfully!")
                else:
                    st.error(f"Error deleting test suite: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to the backend: {e}")

elif choice == "Test Cases":
    st.title("Test Management System - Test Cases")

    # Tabs for Test Cases
    tab1, tab2, tab3, tab4 = st.tabs([
        "View Test Cases",
        "Add Test Case",
        "Update Test Case",
        "Delete Test Case"
    ])

    with tab1:
        st.header("View All Test Cases")

    with tab2:
        st.header("Add New Test Case")

    with tab3:
        st.header("Update Test Case")

    with tab4:
        st.header("Delete Test Case")
