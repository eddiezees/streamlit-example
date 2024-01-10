import streamlit as st
import pandas as pd

def load_data():
    # Replace this with your actual data loading logic
    # For demonstration purposes, we'll use a sample DataFrame
    data = {
        'Timestamp': [1, 2, 3, 4, 5],
        'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
        'Action': ['Allowed', 'Blocked', 'Allowed', 'Blocked', 'Allowed'],
        'Hostname': ['www.example.com', 'www.example.com', 'www.example.com', 'www.example.com', 'www.example.com']
    }
    return pd.DataFrame(data)

def main():
    st.title('Cortex Data Lake App')

    # Load data
    data = load_data()

    # Display data table
    st.dataframe(data)

    # Add filters
    st.sidebar.header('Filters')
    selected_hostname = st.sidebar.selectbox('Select Hostname', data['Hostname'].unique())
    filtered_data = data[data['Hostname'] == selected_hostname]

    # Display filtered data table
    st.subheader('Filtered Data')
    st.dataframe(filtered_data)

    # Add charts or other visualizations as needed

if __name__ == '__main__':
    main()
