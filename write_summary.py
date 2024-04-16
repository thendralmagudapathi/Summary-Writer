import streamlit as st
import pandas as pd

# Load the DataFrame from a parquet file
df = pd.read_parquet("C:/Users/thend/Desktop/Pratik/final_data.parquet")

# Remove 'nan' values from the 'Article' column
df['Article'] = df['Article'].str.replace('nan', '')

# Convert tags to lowercase for consistency
df['Tags'] = df['Tags'].apply(lambda tags: [tag.lower() for tag in tags])

# Set page title and header
st.set_page_config(page_title="Article Summarizer", page_icon="✍️")
st.title("Article Summarizer App")

# Header section
st.header("🔍 Discover Relevant Articles")
st.subheader("Enter tags to find articles matching your interests")

# Get user input for tags
user_input_tags = st.text_input("Enter tags (comma-separated):")
user_input_tags = [tag.strip().lower() for tag in user_input_tags.split(',')]

if user_input_tags != "":

    # Filter the DataFrame based on user input tags
    filtered_df = df[df['Tags'].apply(lambda tags: any(input_tag in tag for input_tag in user_input_tags for tag in tags))]
    print(filtered_df)

else:

    filtered_df = pd.DataFrame() #empty dataframe

# Dummy summarizer function
def dummy_summarizer(article_text):

    # Split the article text into words
    words = article_text.split()
    
    # Extract the first 20 words or fewer
    summary = ' '.join(words[:20])
    
    return summary



if user_input_tags != "":

    print(user_input_tags)

    # Display the filtered articles and their summaries
    for index, row in filtered_df.iterrows():
        article_text = row['Article']
        summary = dummy_summarizer(article_text)


        # Display article details and summary
        st.write(f"Article ID: {row['id']}")
        st.write(f"Tags: {row['Tags']}")
        st.write("Summary:")
        st.write(summary)
        st.write('-' * 50)

    # Add footer
    st.write("---")
    st.write("📚 Article Summarizer by Justin")


# if user_input_tags and filtered_df.empty: 
else:

    st.warning("🙁 No articles found matching the entered tags.")
