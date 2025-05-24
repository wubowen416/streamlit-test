import streamlit as st

st.title('Outro')

if 'uploaded' not in st.session_state:
    st.session_state['uploaded'] = False

if not st.session_state['uploaded']:
    st.warning('Do not close the tab! Data is uploading!')
    # Modify df
    df = st.session_state['df']
    for result in st.session_state['results']:
        column_name = f'{result["section"]}-{result["ref"]}'
        df.loc[df['group_id'] == result['group_id'], column_name] = result['value']
        df.loc[df['group_id'] == result['group_id'], 'done'] = 1
        df.loc[df['group_id'] == result['group_id'], 'user'] = st.session_state['user']
    # Write df to google sheet
    conn = st.session_state['conn']
    conn.update(data=df)
    st.session_state['uploaded'] = True
    st.rerun()
else:
    st.info('You can close the tab')
