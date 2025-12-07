import pandas as pd
import numpy as np 
import plotly.express as px 
import streamlit as st 

df=pd.read_csv("egypt_real_estate_listings.csv")
cleaned_df = pd.read_csv("cleaned_df.csv")


st.set_page_config(
    page_title="Egypt Real Estate Analysis",
    page_icon="🏠",
    layout="wide"
)


page = st.sidebar.radio('Pages', ['Intro','Data','Data after cleaning','Univariate Analysis', 'Bivariate Analysis','MultiVariate Analysis'])


if page == 'Intro':
    
    st.image("background.jpg", use_container_width=True)
    
    # عنوان ونص ترحيبي
    st.markdown("<h1 style='text-align: center; color: white;'>🏡 Welcome to Egypt Real Estate Analysis</h1>", unsafe_allow_html=True)
    st.markdown("""
    Welcome!  
    This web app helps you explore and analyze real estate data in Egypt.  
    You can view property prices, locations, types, and other features with interactive charts and tables.
    """)

elif page == 'Data' :
    st.markdown("<h1 style='text-align: center; color: white;'>This is the real Data before Cleaning : </h1>", unsafe_allow_html=True)
    st.markdown("[Visit Data ](https://www.kaggle.com/datasets/hassankhaled21/egyptian-real-estate-listings)")
    df

elif page == 'Data after cleaning' :
    st.markdown("<h1 style='text-align: center; color: white;'>This is Data after Cleaning : </h1>", unsafe_allow_html=True)
    cleaned_df

elif page == 'Univariate Analysis':
    st.header("📊 Univariate Analysis")
    for col in cleaned_df.columns:
        st.plotly_chart(px.histogram(data_frame= cleaned_df, x= col, title= col))
    

elif page == 'Bivariate Analysis':
    st.header("📈 Bivariate Analysis")

    
    st.markdown("<h1 style='text-align: center; color: white;'>Distribution for price : </h1>", unsafe_allow_html=True)
    st.plotly_chart(px.box(cleaned_df, y="price", title="price Boxplot"))


    
    fig1 = px.box(cleaned_df , y="price", title="Price Boxplot (Log Scale)")
    fig1.update_yaxes(type="log")
    st.plotly_chart(fig1)



    st.markdown("<h1 style='text-align: center; color: white;'>Price Vs city </h1>", unsafe_allow_html=True)
    fig3 = px.scatter(cleaned_df, x="city", y="price", title="Price by City", height=600, width=1000)
    st.plotly_chart(fig3)
    

    st.markdown("<h1 style='text-align: center; color: white;'>price Vs location </h1>", unsafe_allow_html=True)
    fig4 = px.scatter(cleaned_df , x ="location" , y="price", title="Price by location", height=600, width=1000)
    st.plotly_chart(fig4)


    st.markdown("<h1 style='text-align: center; color: white;'>price Vs  size_sqm</h1>", unsafe_allow_html=True)
    fig5 =px.scatter(cleaned_df, x="size_sqm", y="price", title="Size_sqm vs Price")
    st.plotly_chart(fig5)

    
    st.markdown("<h1 style='text-align: center; color: white;'>price VS type</h1>", unsafe_allow_html=True)
    fig7 = px.histogram(cleaned_df, x="type" , y= "price" , title= "price Vs type" ,  opacity = 1)
    st.plotly_chart(fig7)




    
    st.markdown("<h1 style='text-align: center; color: white;'>Price vs Bedrooms</h1>", unsafe_allow_html=True)
    fig8 = px.scatter(cleaned_df , x="bedrooms" , y = "price" , title= "Bedrooms vs Price")
    st.plotly_chart(fig8)



    
    st.markdown("<h1 style='text-align: center; color: white;'>inconsistency between  size_sqm and  size_sqft</h1>", unsafe_allow_html=True)
    fig9 =px.scatter(cleaned_df, x="size_sqft", y="size_sqm",title="Sqft vs Sqm Relationship")
    st.plotly_chart(fig9)
    
    st.markdown("<h1 style='text-align: center; color: white;'>Payment Method vs type</h1>", unsafe_allow_html=True)
    fig10 = px.scatter(cleaned_df, x="type", y="price", facet_col= "payment_method", title="Price by Payment Method")
    st.plotly_chart(fig10)



    
elif page == 'MultiVariate Analysis':
    st.header("🔍 MultiVariate Analysis")

    
    st.markdown("<h1 style='text-align: center; color: white;'>average_price_per_city</h1>", unsafe_allow_html=True)
    average_price_per_city = cleaned_df.groupby("city")["price"].mean().reset_index()
    fig10 = px.bar(average_price_per_city ,x="city", y="price", title="Average Price per City")
    st.plotly_chart(fig10)   

    st.markdown("<h1 style='text-align: center; color: white;'>average_price_per_month</h1>", unsafe_allow_html=True)
    average_price_per_month = cleaned_df.groupby("available_from_month")["price"].mean().reset_index()
    fig11 = px.bar(average_price_per_month ,x="available_from_month", y="price", title="Average Price per month")
    st.plotly_chart(fig11) 


    st.markdown("<h1 style='text-align: center; color: white;'>corrolation between columns</h1>", unsafe_allow_html=True)
    num_cols = ["price", "size_sqm", "bedrooms", "bathrooms", "size_sqft"]
    corr = cleaned_df[num_cols].corr()
    fig12 = px.imshow(corr, text_auto=True)
    st.plotly_chart(fig12)


    st.markdown("<h1 style='text-align: center; color: white;'>total price per type per location </h1>", unsafe_allow_html=True)
    df_total_price_per_city_per_tyep = cleaned_df.groupby(["location" , "type"])["price"].sum().reset_index()
    fig13 = px.bar( df_total_price_per_city_per_tyep,x="type",y="price",
                    color="location",
                    color_discrete_sequence=px.colors.qualitative.Dark2,barmode="group",
                    title="total Price per type",hover_data=["type", "price"],
                    labels={"type":"type" , "price":"total price"}
                    )
    st.plotly_chart(fig13)
    st.markdown("<h1 style='text-align: center; color: white;'>total type saled per location per city</h1>", unsafe_allow_html=True)
    sales_per_location = cleaned_df.groupby(["location" , "city"] )["type"].count().reset_index(name = "count of type")
    fig14 = px.bar(
                    sales_per_location,
                    x="location",
                    y="count of type",
                    color = "city",
                    color_discrete_sequence=px.colors.qualitative.Dark2,
                    barmode="group",
                    title="count of type per location  " , 
                    labels= {"sum of count of type" : "count of type"}
                    )
    st.plotly_chart(fig14)
