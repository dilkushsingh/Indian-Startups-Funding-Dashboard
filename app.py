import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide',page_title='StartUp Funding Analysis',page_icon='favicon.ico')


df = pd.read_csv('startup_cleaned.csv')

def load_investor_details(investor):
    st.title(investor)
    # Recent 5 investments
    recent_inv = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(recent_inv)

    col1, col2 = st.columns(2)
    with col1:
        # Biggest Investment
        biggest_inv = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investment')
        fig, ax = plt.subplots()
        ax.bar(biggest_inv.index, biggest_inv.values)
        st.pyplot(fig)
    with col2:
        # Sectors invested
        verticals = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(verticals, labels=verticals.index, autopct='%0.01f%%')
        st.pyplot(fig1)
    col3, col4 = st.columns(2)
    with col3:
        # Rounds in which investor investes
        rounds = df[df['investors'].str.contains(investor)].groupby('round')['amount'].count()
        st.subheader('Rounds in which Investor invested')
        fig2, ax2 = plt.subplots()
        ax2.pie(rounds, labels=rounds.index, autopct='%0.01f%%')
        st.pyplot(fig2)
    with col4:
        # Cities
        cities = df[df['investors'].str.contains(investor)].groupby('city')['city'].count()
        st.subheader(f'Cities in which {investor} invests')
        fig3, ax3 = plt.subplots()
        ax3.pie(cities, labels=cities.index, autopct='%0.01f%%')
        st.pyplot(fig3)
    st.subheader('YoY Investments')
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.pyplot(fig4)
    # Similar Investors
    selected_vertical = df[df['investors'].str.contains(investor)]['vertical'].mode(0).values[0]
    selected_subvertical = df[df['investors'].str.contains(investor)]['subvertical'].mode(0).values[0]
    similar_investors = df[(df['vertical'] == selected_vertical) & (df['subvertical'] == selected_subvertical)]
    if similar_investors.size == 0:
        similar_investors = df[(df['vertical'] == selected_vertical) | (df['subvertical'] == selected_subvertical)]
    similar_investors.head()
    st.subheader(f"Investors similar to {investor} in the {selected_vertical} vertical")
    st.write(similar_investors[['investors']].head())

def load_startup_details(startup):
    st.title(startup)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Industry')
        st.text(df[df['startup'] == startup]['vertical'].value_counts().index[0])
    with col2:
        st.subheader('SubIndustry')
        st.text(df[df['startup'] == startup]['subvertical'].value_counts().index[0])
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Location')
        st.text(df[df['startup'] == startup]['city'].mode().values[0])
    with col2:
        st.subheader('Total Funded Rounds')
        st.text(df[df['startup'] == "BYJU'S"]['round'].count())
    # Investments
    st.header('Investments')
    temp = df[df['startup'] == startup][['date', 'investors', 'round', 'amount']]
    st.dataframe(temp)
    # Top Investors
    st.subheader('Top Investors based on fundings')
    fig, ax = plt.subplots()
    ax.pie(temp['amount'], labels=temp.investors, autopct='%0.01f%%')
    st.pyplot(fig)
    # Similar Startups
    selected_vertical = df[df['startup'] == startup]['vertical'].mode(0).values[0]
    selected_subvertical = df[df['startup'] == startup]['subvertical'].mode(0).values[0]
    similar_startups = df[(df['vertical'] == selected_vertical) & (df['subvertical'] == selected_subvertical)]
    if similar_startups.size == 0:
        similar_startups = df[(df['vertical'] == selected_vertical) | (df['subvertical'] == selected_subvertical)]
    similar_startups['startup'].head(10)
    st.subheader(f"Startups similar to {startup} in the {selected_vertical} vertical")
    st.write(similar_startups[['startup']].head())

def load_overall_analysis():
    st.title('Overall Analysis')
    total = round(df['amount'].sum())
    max = round(df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0])
    avg = round(df['amount'].mean(), 2)
    funded_startups = df['startup'].nunique()
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric('Total', str(total) +' Cr')
    with c2:
        st.metric('Maximum', str(max) +' Cr')
    with c3:
        st.metric('Average', str(avg) +' Cr')
    with c4:
        st.metric('Funded Startups', str(funded_startups))
    st.header('MoM Investments')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()    
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'], temp_df['amount'], marker='.')
    ax5.tick_params(axis='x', rotation=90, labelsize=5) 
    st.pyplot(fig5)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader('Top 10 Sectors based on number of investments')
        top10_verticals = df['vertical'].value_counts().nlargest(10)
        fig, ax = plt.subplots()
        ax.pie(top10_verticals, labels=top10_verticals.index, autopct='%0.01f%%', textprops={'fontsize': 7})
        st.pyplot(fig)
    with c2:
        st.subheader('Top 10 Sectors based on total amount invested')
        top10_verticals = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots()
        ax.pie(top10_verticals, labels=top10_verticals.index, autopct='%0.01f%%', textprops={'fontsize': 7})
        st.pyplot(fig)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader('Top 5 Funding Rounds by Number of Deals')
        funding_rounds = df.groupby('round')['amount'].sum().sort_values(ascending=False).head(5)
        fig, ax = plt.subplots()
        ax.pie(funding_rounds, labels=funding_rounds.index, autopct='%0.01f%%')
        st.pyplot(fig)
    with c2:
        st.subheader('Top 5 Funding Rounds by Amount Raised')
        funding_rounds = df.groupby('round')['amount'].count().sort_values(ascending=False).head(5)
        fig, ax = plt.subplots()
        ax.pie(funding_rounds, labels=funding_rounds.index, autopct='%0.01f%%')
        st.pyplot(fig)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader('Top 10 Cities having highest number of Fundings')
        top_cities = df['city'].value_counts().head(10)
        fig, ax = plt.subplots()
        ax.pie(top_cities, labels=top_cities.index, autopct='%0.01f%%')
        st.pyplot(fig)
    with c2:
        st.subheader('Top 10 Cities by Total Funding Amount')
        top_cities = df.groupby(['city'])['amount'].sum().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots()
        ax.pie(top_cities, labels=top_cities.index, autopct='%0.01f%%')
        st.pyplot(fig)
    c1, c2 = st.columns(2)
    with c1:
        # Top Startups of each year based on total amount raised
        st.subheader('Yearly Top Startups Based on Funding Amount')
        top_startups = df.groupby(['startup', 'year'])['amount'].sum().sort_values(ascending=False).reset_index().drop_duplicates('year', keep='first').sort_values('year', ascending=False)
        top_startups['x_axis'] =top_startups['startup'] + '-' + top_startups['year'].astype('str')
        fig, ax = plt.subplots()
        ax.bar(top_startups.x_axis, top_startups.amount)
        ax.tick_params(axis='x', rotation=90) 
        st.pyplot(fig)
    with c2:
        # Top Investors of each year based on total amount invested
        st.subheader('Yearly Top Investors Based on Invested Amount')
        top_investors = df.groupby(['investors', 'year'])['amount'].sum().sort_values(ascending=False).reset_index().drop_duplicates('year', keep='first').sort_values('year', ascending=False)
        top_investors['x_axis'] =top_investors['investors'] + '-' + top_investors['year'].astype('str')
        fig, ax = plt.subplots()
        ax.bar(top_investors.x_axis, top_investors.amount)
        ax.tick_params(axis='x', rotation=90) 
        st.pyplot(fig)
    # Funding Heatmap
    st.header('Funding Heatmap')
    funding_selected= st.selectbox('Select Heatmap', ['Total Amount', 'Total Investments'])
    if funding_selected == 'Total Amount':
        heatmap_data = pd.pivot_table(df, columns="year", index="month", values="amount", aggfunc='sum')
    elif funding_selected:
        heatmap_data = pd.pivot_table(df, columns="year", index="month", values="amount", aggfunc='count')
    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="cividis", ax=ax)
    st.pyplot(fig)


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()
elif option == 'StartUp':
    startup = st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    if btn1:
        load_startup_details(startup)
else:  
    investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(investor)