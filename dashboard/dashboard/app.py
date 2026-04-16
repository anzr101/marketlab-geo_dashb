import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go
import plotly.express as px

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="MarketLab | AI Trading Research",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# PROFESSIONAL CUSTOM CSS
# ============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 100%);
        color: #ffffff;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .hero-container {
        padding: 4rem 2rem;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #e0e0e0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: rgba(255, 255, 255, 0.9);
        font-weight: 300;
        margin-bottom: 2rem;
    }
    
    .hero-stat {
        display: inline-block;
        margin: 1rem 2rem;
        text-align: center;
    }
    
    .hero-stat-number {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    .hero-stat-label {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.7);
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 3rem 0 1.5rem 0;
        color: #ffffff;
        border-left: 5px solid #667eea;
        padding-left: 1.5rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a3e 100%);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(102, 126, 234, 0.3);
        transition: transform 0.3s ease;
        margin: 1rem 0;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-label {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.6);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .discovery-box {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        border-radius: 15px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(245, 158, 11, 0.4);
    }
    
    .discovery-title {
        font-size: 2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    
    .discovery-text {
        font-size: 1.2rem;
        line-height: 1.8;
        color: rgba(255, 255, 255, 0.95);
    }
    
    .insight-box {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a3e 100%);
        border-left: 5px solid #667eea;
        border-radius: 10px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .insight-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #667eea;
        margin-bottom: 1rem;
    }
    
    .insight-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: rgba(255, 255, 255, 0.8);
    }
    
    .timeline-item {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a3e 100%);
        border-left: 3px solid #667eea;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 10px;
    }
    
    .timeline-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .timeline-desc {
        color: rgba(255, 255, 255, 0.7);
        line-height: 1.6;
    }
    
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .hero-stat-number {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD DATA
# ============================================================================

@st.cache_data
def load_metrics():
    try:
        with open('metrics.json', 'r') as f:
            return json.load(f)
    except:
        return {}

@st.cache_data
def load_backtest():
    try:
        df = pd.read_csv('backtest_data.csv')
        return df
    except:
        return pd.DataFrame()

metrics = load_metrics()
backtest_df = load_backtest()

# ============================================================================
# NAVIGATION
# ============================================================================

query_params = st.query_params
page = query_params.get("page", ["home"])[0] if isinstance(st.query_params.get("page", ["home"]), list) else st.query_params.get("page", "home")

cols = st.columns(5)
with cols[0]:
    if st.button("🏠 Home", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = "home"
        st.rerun()
with cols[1]:
    if st.button("🔍 Discovery", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = "discovery"
        st.rerun()
with cols[2]:
    if st.button("📊 Evidence", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = "evidence"
        st.rerun()
with cols[3]:
    if st.button("💡 Solution", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = "solution"
        st.rerun()
with cols[4]:
    if st.button("👨‍🎓 About", use_container_width=True):
        st.query_params.clear()
        st.query_params["page"] = "about"
        st.rerun()

st.markdown("---")

# ============================================================================
# HOME PAGE
# ============================================================================

if page == "home":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">MarketLab</div>
        <div class="hero-subtitle">Why 99.86% Accurate AI Still Loses Money</div>
        <div>
            <div class="hero-stat">
                <span class="hero-stat-number">1,386</span>
                <span class="hero-stat-label">Models Trained</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">99.86%</span>
                <span class="hero-stat-label">Best Accuracy</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">-21%</span>
                <span class="hero-stat-label">Trading Gap</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="discovery-box">
        <div class="discovery-title">⚠️ The Prediction-Profit Gap</div>
        <div class="discovery-text">
            Despite achieving 99.86% prediction accuracy across 1,386 machine learning models, 
            trading strategies underperformed simple buy-and-hold by 21% annually when 
            tested on real market conditions (2022-2024).
            <br><br>
            <strong>Why?</strong> Models trained on historical patterns had zero awareness of 
            geopolitical events that actually drive markets: wars, banking crises, interest rate changes.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # The Gap Chart
    if not backtest_df.empty:
        st.markdown('<div class="section-title">The Gap: Prediction vs Reality</div>', unsafe_allow_html=True)
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Buy & Hold',
            x=backtest_df['Stock'],
            y=backtest_df['BH_Return_%'],
            marker_color='#10b981',
            text=backtest_df['BH_Return_%'].round(1).astype(str) + '%',
            textposition='outside',
        ))
        
        fig.add_trace(go.Bar(
            name='AI Models',
            x=backtest_df['Stock'],
            y=backtest_df['Strategy_Return_%'],
            marker_color='#ef4444',
            text=backtest_df['Strategy_Return_%'].round(1).astype(str) + '%',
            textposition='outside',
        ))
        
        fig.update_layout(
            title={'text': 'Annual Returns: Buy-Hold vs AI (2022-2024)', 'font': {'size': 24, 'color': 'white'}},
            xaxis_title='Stock',
            yaxis_title='Annual Return (%)',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', size=14),
            barmode='group',
            height=500,
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', zeroline=True, zerolinecolor='rgba(255,255,255,0.3)'),
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Stats
    st.markdown('<div class="section-title">Research at Scale</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1,386</div>
            <div class="metric-label">Models Trained</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">50</div>
            <div class="metric-label">NSE Stocks</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">20</div>
            <div class="metric-label">Years of Data</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">325</div>
            <div class="metric-label">Features Engineered</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# DISCOVERY PAGE
# ============================================================================

elif page == "discovery":
    st.markdown('<div class="section-title">🔍 The Discovery</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">What We Found</div>
        <div class="insight-text">
            After training 1,386 machine learning models across 25 algorithms on 50 NSE stocks 
            with 20 years of historical data, we achieved exceptional prediction accuracy 
            (R² = 0.9986 or 99.86%).
            <br><br>
            <strong>However, when deployed in backtesting on real market conditions (2022-2024), 
            every single model underperformed a simple buy-and-hold strategy by an average of 21%.</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">✅ Prediction Success</div>
            <div class="insight-text">
                • Best R²: 0.9986 (99.86%)<br>
                • Algorithm: Random Forest<br>
                • 37 universal features identified<br>
                • Ensemble methods validated<br>
                • State-of-the-art accuracy
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">❌ Trading Reality</div>
            <div class="insight-text">
                • Average return: -3.14% annually<br>
                • Buy-hold average: +18.31%<br>
                • Gap: -21.46% underperformance<br>
                • Success rate: 0/5 stocks<br>
                • Transaction costs included
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="discovery-box">
        <div class="discovery-title">💡 Key Insight</div>
        <div class="discovery-text">
            <strong>R² measures prediction accuracy, not directional accuracy.</strong>
            <br><br>
            A model can predict ₹1,250 when actual is ₹1,255 (high R²) but still signal 
            "sell" when the price actually goes up, resulting in trading losses.
            <br><br>
            More critically: Models trained on 2004-2021 patterns failed during 2022-2024 
            because they couldn't account for unprecedented geopolitical events.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# EVIDENCE PAGE
# ============================================================================

elif page == "evidence":
    st.markdown('<div class="section-title">📊 The Evidence</div>', unsafe_allow_html=True)
    
    if metrics:
        st.markdown('<div class="section-title">Model Performance</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="timeline-item">
                <div class="timeline-title">Classical Machine Learning</div>
                <div class="timeline-desc">
                    • Models: 1,326 total<br>
                    • Algorithms: 25 (RF, XGBoost, LightGBM, etc.)<br>
                    • Best R²: 0.9986<br>
                    • Average R²: -2.79 (many overfitted)
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="timeline-item">
                <div class="timeline-title">Deep Learning</div>
                <div class="timeline-desc">
                    • Models: 60 total<br>
                    • Architectures: LSTM, GRU, Transformer, etc.<br>
                    • Best R²: 0.9104<br>
                    • Sequence length: 60 days
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('<div class="section-title">Feature Analysis (SHAP)</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">Universal Features Discovered</div>
            <div class="insight-text">
                Out of 325 engineered features, only 37 showed consistent importance across all stocks:
                <br><br>
                <strong>Top 3 Features:</strong><br>
                1. EMA_3 (3-day exponential moving average)<br>
                2. SMA_3 (3-day simple moving average)<br>
                3. VWAP_5 (5-day volume weighted average price)
                <br><br>
                <strong>Insight:</strong> Stock prices depend heavily on very recent history (2-5 days), 
                confirming market efficiency hypothesis.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Architecture Image
    try:
        st.markdown('<div class="section-title">System Architecture</div>', unsafe_allow_html=True)
        st.image('assets/architecture.png', use_container_width=True)
    except:
        pass

# ============================================================================
# SOLUTION PAGE
# ============================================================================

elif page == "solution":
    st.markdown('<div class="section-title">💡 The Solution</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="discovery-box">
        <div class="discovery-title">Geopolitical Intelligence Framework</div>
        <div class="discovery-text">
            To address the prediction-profit gap, we developed a novel framework that combines 
            machine learning predictions with real-time geopolitical event awareness.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-title">1. Event Classification System</div>
        <div class="timeline-desc">
            • 6 categories: Geopolitical, Economic Policy, Corporate, Regulatory, Natural Disaster, Tech Disruption<br>
            • 85% classification accuracy<br>
            • Impact scoring (0-10 scale)<br>
            • Sentiment analysis (positive/negative/neutral)
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-title">2. Intelligent Risk Agent</div>
        <div class="timeline-desc">
            • Monitors events within 7-day trading window<br>
            • Assesses market risk based on event impact<br>
            • Adjusts trading signals accordingly<br>
            • Risk thresholds: High (>7), Medium (4-7), Low (<4)
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-title">3. Risk Management Rules</div>
        <div class="timeline-desc">
            • High risk (impact > 7): Stay in cash, avoid trading<br>
            • Medium risk (4-7): Reduce position size to 50%<br>
            • Low risk (<4): Follow model predictions normally
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Results</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">✅ Proof of Concept</div>
            <div class="insight-text">
                • ITC: +1.60% improvement<br>
                • 34 high-risk days identified (4.6%)<br>
                • 102 trades avoided during volatility<br>
                • Framework validated successfully
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">🚀 Next Steps</div>
            <div class="insight-text">
                • Real-time news feed integration<br>
                • Advanced NLP for event detection<br>
                • Multi-asset class extension<br>
                • Production deployment with live data
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# ABOUT PAGE
# ============================================================================

elif page == "about":
    st.markdown('<div class="section-title">👨‍🎓 About This Research</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">Researcher</div>
        <div class="insight-text">
            <strong>Final Year Student</strong><br>
            B.E. Artificial Intelligence & Data Science<br>
            Mumbai University
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Research Contributions</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-title">1. Comprehensive Scale Analysis</div>
        <div class="timeline-desc">
            One of the largest student-led studies of ML-based stock prediction on Indian markets. 
            1,386 models across 50 NSE stocks with 20 years of historical data.
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-title">2. Prediction-Profit Gap Discovery</div>
        <div class="timeline-desc">
            Empirical demonstration that high prediction accuracy does not guarantee trading profitability. 
            Identified the disconnect between R² metrics and real-world returns.
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-title">3. Geopolitical Intelligence Framework</div>
        <div class="timeline-desc">
            First comprehensive event classification system for Indian stock markets. Novel integration 
            of machine learning with geopolitical event awareness.
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-title">4. Open Source Contribution</div>
        <div class="timeline-desc">
            Complete methodology, code, and findings open-sourced for research community. 
            Reproducible framework for event-aware algorithmic trading.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">6</div>
            <div class="metric-label">Months Duration</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">150+</div>
            <div class="metric-label">Compute Hours</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">5,000+</div>
            <div class="metric-label">Lines of Code</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">📚 Citation</div>
        <div class="insight-text">
            If you use this research, please cite:<br><br>
            <code>MarketLab: Geopolitical Intelligence for Stock Market Prediction<br>
            Mumbai University, 2025</code>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: rgba(255, 255, 255, 0.5); padding: 2rem;'>
    <p><strong>MarketLab</strong> | Mumbai University | 2025</p>
    <p>Bridging the Prediction-Profitability Gap in AI Trading</p>
</div>
""", unsafe_allow_html=True)
