import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page config
st.set_page_config(
    page_title="MarketLab: Geopolitical Intelligence System",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
    }
    .finding-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_metrics():
    try:
        with open('metrics.json', 'r') as f:
            return json.load(f)
    except:
        return {}

@st.cache_data
def load_events():
    try:
        return pd.read_csv('historical_events.csv')
    except:
        return pd.DataFrame()

@st.cache_data
def load_taxonomy():
    try:
        with open('event_taxonomy.json', 'r') as f:
            return json.load(f)
    except:
        return {}

metrics = load_metrics()
events_df = load_events()
taxonomy = load_taxonomy()

# Sidebar
st.sidebar.markdown("## 🌍 MarketLab")
st.sidebar.markdown("**Geopolitical Intelligence for Stock Trading**")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🌍 Event Classifier", "📊 Research Findings", "🔬 Model Performance", "📄 About"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍🎓 Researcher")
st.sidebar.markdown("Final Year AI & Data Science Student")
st.sidebar.markdown("Mumbai University")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Quick Stats")
if metrics:
    st.sidebar.metric("Models Trained", f"{metrics.get('overall_statistics', {}).get('total_models_trained', 0):,}")
    st.sidebar.metric("Best Accuracy", f"{metrics.get('overall_statistics', {}).get('best_prediction_accuracy', 0)*100:.2f}%")
    st.sidebar.metric("Event Categories", metrics.get('day5_events', {}).get('event_categories', 6))

# HOME PAGE
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">MarketLab: Geopolitical Intelligence System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Bridging the Prediction-Profitability Gap in Stock Market AI</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🤖 Models Trained",
            value=f"{metrics.get('overall_statistics', {}).get('total_models_trained', 1386):,}",
            delta="1,386 total"
        )
    
    with col2:
        st.metric(
            label="🎯 Best Accuracy",
            value="99.86%",
            delta="R² = 0.9986"
        )
    
    with col3:
        st.metric(
            label="📉 Trading Gap",
            value="-21.5%",
            delta="Prediction ≠ Profit",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="🌍 Event Categories",
            value="6",
            delta="85% accuracy"
        )
    
    st.markdown("---")
    
    # Key Finding
    st.markdown("### 🔍 Key Discovery: The Prediction-Profit Gap")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="finding-box">
        <h4>⚠️ Critical Finding</h4>
        <p><strong>Despite achieving 99.86% prediction accuracy, ML models underperformed 
        buy-and-hold strategies by 21% annually when tested in real market conditions.</strong></p>
        
        <p><strong>Why?</strong> Models trained on historical patterns had no awareness of 
        geopolitical events that drive markets:</p>
        <ul>
            <li>Ukraine war (Feb 2022)</li>
            <li>Banking crisis (Mar 2023)</li>
            <li>Fed rate hikes (2022-2024)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="success-box">
        <h4>✅ Novel Solution: Geopolitical Intelligence Framework</h4>
        <p>Developed a hybrid system combining deep learning with real-time event classification:</p>
        <ul>
            <li>6-category event taxonomy (85% classification accuracy)</li>
            <li>Impact scoring (0-10 scale) with sentiment analysis</li>
            <li>Event-aware intelligent agent for risk assessment</li>
            <li><strong>Proof-of-concept: ITC stock improved +1.60%</strong></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 📊 Project Timeline")
        
        timeline_data = {
            'Phase': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5-6', 'Day 7'],
            'Task': ['Classical ML', 'Deep Learning', 'SHAP Analysis', 'Backtesting', 'Geopolitical AI', 'Integration'],
            'Models': [1326, 60, 0, 0, 0, 0]
        }
        
        fig = px.bar(
            timeline_data,
            x='Models',
            y='Phase',
            orientation='h',
            text='Task',
            title='Project Phases'
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    try:
        st.image('assets/architecture.png', caption='MarketLab System Architecture', use_container_width=True)
    except:
        st.info("Architecture diagram available in research repository")

# EVENT CLASSIFIER PAGE
elif page == "🌍 Event Classifier":
    st.markdown("# 🌍 Live Event Classifier")
    st.markdown("**Try the geopolitical intelligence system - type any event and see how it's classified!**")
    st.markdown("---")
    
    user_event = st.text_area(
        "Enter an event description:",
        placeholder="Example: Russia-Ukraine war escalates, oil prices surge",
        height=100
    )
    
    if st.button("🔍 Classify Event", type="primary"):
        if user_event:
            event_lower = user_event.lower()
            category_scores = {}
            
            for category, details in taxonomy.items():
                matches = sum(1 for keyword in details['keywords'] if keyword in event_lower)
                if matches > 0:
                    impact_weight = {'high': 3, 'medium': 2, 'low': 1}[details['typical_impact']]
                    category_scores[category] = matches * impact_weight
            
            if category_scores:
                sorted_categories = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)
                primary_category = sorted_categories[0][0]
                primary_score = sorted_categories[0][1]
                
                impact_map = {'high': 8, 'medium': 5, 'low': 3}
                base_impact = impact_map[taxonomy[primary_category]['typical_impact']]
                impact_score = min(10, base_impact + primary_score)
                
                negative_words = ['crisis', 'war', 'attack', 'crash', 'fall', 'decline', 'loss']
                positive_words = ['growth', 'rise', 'gain', 'profit', 'surge', 'breakthrough']
                
                neg_count = sum(1 for word in negative_words if word in event_lower)
                pos_count = sum(1 for word in positive_words if word in event_lower)
                
                if neg_count > pos_count:
                    sentiment = 'Negative'
                    sentiment_color = '🔴'
                elif pos_count > neg_count:
                    sentiment = 'Positive'
                    sentiment_color = '🟢'
                else:
                    sentiment = 'Neutral'
                    sentiment_color = '🟡'
                
                st.markdown("### 📊 Classification Results")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Category", primary_category.upper())
                
                with col2:
                    st.metric("Impact Score", f"{impact_score}/10")
                
                with col3:
                    st.metric("Sentiment", f"{sentiment_color} {sentiment}")
                
                with col4:
                    confidence = primary_score / sum(category_scores.values())
                    st.metric("Confidence", f"{confidence*100:.0f}%")
                
                st.markdown("---")
                st.markdown("### 🔍 Detailed Analysis")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Category Details:**")
                    st.info(f"**{primary_category.upper()}**\n\n{taxonomy[primary_category]['description']}")
                    
                    st.markdown("**Affected Sectors:**")
                    sectors = taxonomy[primary_category]['affected_sectors']
                    st.write(", ".join(sectors))
                
                with col2:
                    st.markdown("**All Categories (ranked):**")
                    for cat, score in sorted_categories:
                        st.write(f"• {cat.upper()}: {score} points")
            else:
                st.warning("No matching event categories found.")
        else:
            st.warning("Please enter an event description.")
    
    if not events_df.empty:
        st.markdown("---")
        st.markdown("### 📅 Historical Events Database (2022-2024)")
        st.dataframe(
            events_df[['date', 'event', 'category', 'impact']].sort_values('date', ascending=False),
            use_container_width=True
        )

# RESEARCH FINDINGS PAGE
elif page == "📊 Research Findings":
    st.markdown("# 📊 Research Findings")
    st.markdown("**Complete analysis of the prediction-profitability gap**")
    st.markdown("---")
    
    st.markdown("### 🎯 The Prediction-Profit Gap")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 📈 Prediction Success
        - **Best R²**: 0.9986 (99.86% accuracy)
        - **Method**: Random Forest
        - **Models**: 1,386 trained
        """)
        st.success("✅ State-of-the-art prediction accuracy")
    
    with col2:
        st.markdown("""
        #### 📉 Trading Reality
        - **Average Return**: -3.14% annually
        - **Buy-Hold Average**: +18.31%
        - **Underperformance**: -21.46%
        """)
        st.error("❌ High accuracy ≠ profitable trading")
    
    try:
        st.image('assets/summary.png', caption='Research Summary', use_container_width=True)
    except:
        st.info("Summary available in repository")

# MODEL PERFORMANCE PAGE
elif page == "🔬 Model Performance":
    st.markdown("# 🔬 Model Performance Analysis")
    st.markdown("**Detailed breakdown of all 1,386 models**")
    st.markdown("---")
    
    if metrics:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🤖 Classical ML")
            day1 = metrics.get('day1_classical_ml', {})
            st.metric("Total Models", f"{day1.get('total_models', 0):,}")
            st.metric("Best R²", f"{day1.get('best_r2', 0):.4f}")
        
        with col2:
            st.markdown("#### 🧠 Deep Learning")
            day2 = metrics.get('day2_deep_learning', {})
            st.metric("Total Models", f"{day2.get('total_models', 0):,}")
            st.metric("Best R²", f"{day2.get('best_r2', 0):.4f}")

# ABOUT PAGE
elif page == "📄 About":
    st.markdown("# 📄 About This Research")
    st.markdown("---")
    
    st.markdown("""
    ## 🎓 Researcher
    
    **Final Year Student**  
    B.E. AI & Data Science  
    Mumbai University  
    
    ## 🔬 Key Contributions
    
    1. **Scale**: 1,386 models trained across 50 NSE stocks
    2. **Discovery**: Prediction accuracy ≠ profitable trading
    3. **Innovation**: First geopolitical event framework for Indian markets
    4. **Solution**: Hybrid intelligence system
    
    ## 🔓 Open Source
    
    All code, data, and findings will be open-sourced.
    
    ---
    
    *Last updated: January 2025*
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>MarketLab: Geopolitical Intelligence System</strong></p>
    <p>Mumbai University • Final Year Research Project • 2025</p>
</div>
""", unsafe_allow_html=True)
