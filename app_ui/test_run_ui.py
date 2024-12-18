from datetime import datetime
import requests
import streamlit as st
from app.config import BACKEND_URL

def create_test_run():
    st.header("Create New Test Run")
    test_suite_id = st.number_input("Test Suite ID", min_value=1, step=1, key="create_run_test_suite_id")
    run_status = st.selectbox("Run Status", ["in_progress", "completed", "failed"], key="create_run_status")

    if st.button("Create Test Run", key="create_run_button"):
        if not test_suite_id or not run_status:
            st.warning("Please fill in all fields.")
        else:
            try:
                payload = {
                    "test_suite_id": test_suite_id,
                    "run_status": run_status
                }
                response = requests.post(f"{BACKEND_URL}/test_runs", json=payload)
                if response.status_code == 200:
                    st.success("Test run created successfully!")
                elif response.status_code == 400 and "does not exist" in response.json().get("detail"):
                    st.error("Invalid Test Suit ID")
                else:
                    st.error(f"Error creating test run: {response.status_code}")
            except Exception:
                st.error("Failed to connect to the backend")


def view_all_test_runs():
    st.header("View All Test Runs")
    if st.button("Fetch All Test Runs", key="fetch_all_runs"):
        try:
            response = requests.get(f"{BACKEND_URL}/test_runs/")
            if response.status_code == 200:
                test_runs = response.json()
                if test_runs:
                    for run in test_runs:
                        st.subheader(f"Run ID: {run['id']}")
                        st.write(f"Test Suite ID: {run['test_suite_id']}")
                        st.write(f"Run Status: {run['run_status']}")
                        st.write(f"Started At: {run['start_time']}")
                        st.write(f"Ended At: {run['end_time'] if 'end_time' in run else 'N/A'}")
                        st.write(f"Test Results: {run['test_results']}")
                        st.write("---")
                else:
                    st.info("No test runs found.")
            else:
                st.error(f"Error fetching test runs: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend. Error")

def view_single_test_run():
    st.header("View A Particular Runs")
    run_id = st.text_input("Enter Test Run ID", key="run_id_fetch")
    if st.button("Fetch Test Run", key="fetch_run"):
        try:
            response = requests.get(f"{BACKEND_URL}/test_runs/{run_id}")
            if response.status_code == 200:
                run = response.json()
                if run:
                    st.subheader(f"Run ID: {run['id']}")
                    st.write(f"Test Suite ID: {run['test_suite_id']}")
                    st.write(f"Run Status: {run['run_status']}")
                    st.write(f"Started At: {run['start_time']}")
                    st.write(f"Ended At: {run['end_time'] if 'end_time' in run else 'N/A'}")
                    st.write(f"Test Results: {run['test_results']}")
                    st.write("---")
                else:
                    st.info("Test suite not found.")
            elif response.status_code == 400 and response.json().get("detail") == "Invalid Input":
                st.error(f"Invalid Input: {response.status_code}")
            else:
                st.error(f"Error fetching test run: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend")


def update_test_run():
    st.header("Update Test Run")
    run_id = st.text_input("Enter Test Run ID", key="run_id_update")

    result = st.selectbox("Test Run Result", ["Passed", "Failed", "In Progress", "Not Run"], key="result")
    end_time = st.text_input("End Time (e.g. 2024-12-16T17:38:43.970Z)", value=str(datetime.utcnow().isoformat()),
                             key="end_time")
    run_status = st.selectbox("Run Status", ["In Progress", "Complete", "Not Started"], key="run_status")

    if st.button("Update Test Run", key="update_run"):
        if not run_id or not result or not end_time or not run_status :
            st.warning("All fields are required. Please fill in all the details.")
        else:
            try:
                payload = {
                    "result": result,
                    "end_time": end_time,
                    "run_status": run_status
                }
                response = requests.put(f"{BACKEND_URL}/test_runs/{run_id}", json=payload)
                if response.status_code == 200:
                    st.success(f"Test Run ID {run_id} updated successfully!")
                elif response.status_code == 400 and "not found" in response.json().get("detail"):
                    st.error(f"Invalid Input: {response.status_code}")
                else:
                    st.error(f"Error updating test run: {response.status_code}")
            except Exception:
                st.error(f"Failed to connect to the backend")

def delete_test_run():
    st.header("Delete Test Run")
    run_id = st.text_input("Enter Run ID to Delete", key="delete_run_id")
    if st.button("Delete Test Run", key="delete_run"):
        try:
            response = requests.delete(f"{BACKEND_URL}/test_runs/{run_id}/")
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("message") == "Test Run not found":
                    st.error("Test Run not found")
                else:
                    st.success("Test Run deleted successfully!")
            else:
                st.error(f"Error deleting test run: {response.status_code}")
        except Exception:
            st.error("Failed to connect to the backend")
