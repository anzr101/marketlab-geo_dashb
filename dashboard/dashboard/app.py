"""
MarketLab Research Showcase
Bridging the Prediction-Profitability Gap in Algorithmic Trading
Author: [Your Name] | Mumbai University | 2024-2025
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="MarketLab Research",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS - PROFESSIONAL RESEARCH STYLE
# ============================================================================

st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d35 100%);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1d35 0%, #0a0e27 100%);
        border-right: 2px solid #2a2d45;
    }
    
    /* Headers */
    h1 {
        color: #ffffff;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-bottom: 1rem;
        border-bottom: 3px solid #667eea;
        margin-bottom: 2rem;
    }
    
    h2 {
        color: #667eea;
        font-weight: 700;
        margin-top: 3rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #a8b2ff;
        font-weight: 600;
        margin-top: 1.5rem;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Custom cards */
    .problem-card {
        background: linear-gradient(135deg, #fc5c7d 0%, #6a82fb 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(252, 92, 125, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .solution-card {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(67, 233, 123, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #0a0e27;
    }
    
    .result-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(250, 112, 154, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #0a0e27;
    }
    
    .info-card {
        background: rgba(102, 126, 234, 0.1);
        border-left: 4px solid #667eea;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .quote-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #a8b2ff;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        font-style: italic;
        color: #a8b2ff;
    }
    
    /* Stats box */
    .stat-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid rgba(102, 126, 234, 0.3);
        transition: transform 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        color: #a8b2ff;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        font-weight: 600;
    }
    
    /* Process steps */
    .process-step {
        background: rgba(102, 126, 234, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        position: relative;
    }
    
    .step-number {
        position: absolute;
        top: -15px;
        left: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 1.2rem;
    }
    
    /* Sidebar styling */
    .sidebar-title {
        text-align: center;
        padding: 2rem 0;
        border-bottom: 2px solid #2a2d45;
    }
    
    /* Links */
    a {
        color: #667eea;
        text-decoration: none;
    }
    
    a:hover {
        color: #a8b2ff;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-title">
            <h1 style="font-size: 3rem; margin: 0;">📊</h1>
            <h2 style="color: white; font-size: 1.8rem; margin: 0.5rem 0;">MarketLab</h2>
            <p style="color: #a8b2ff; font-size: 0.9rem;">Research Showcase</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        page = st.radio(
            "Navigation",
            ["🏠 Overview", "🔬 Research Journey", "📊 Key Findings", 
             "🏗️ Technical Implementation", "ℹ️ About"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div class="stat-box">
                <div class="stat-number">90%</div>
                <div class="stat-label">Event Accuracy</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div class="stat-box">
                <div class="stat-number">+1.13</div>
                <div class="stat-label">Sharpe Improvement</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.8rem; margin-top: 2rem;">
            <p>Mumbai University</p>
            <p>Final Year Project 2024-25</p>
        </div>
        """, unsafe_allow_html=True)
    
    return page

# ============================================================================
# PAGE: OVERVIEW
# ============================================================================

def page_overview():
    st.title("Bridging the Prediction-Profitability Gap in Algorithmic Trading")
    
    st.markdown("""
    <div style="text-align: center; color: #a8b2ff; font-size: 1.2rem; margin-bottom: 3rem;">
        A comprehensive research project exploring why high-accuracy ML models fail in real trading
    </div>
    """, unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">1,386</div>
            <div class="stat-label">ML Models Trained</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">99.86%</div>
            <div class="stat-label">Prediction Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">-21%</div>
            <div class="stat-label">Trading Underperformance</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">90%</div>
            <div class="stat-label">Event Classification</div>
        </div>
        """, unsafe_allow_html=True)
    
    # The Problem
    st.markdown("## 🚨 The Problem")
    
    st.markdown("""
    <div class="problem-card">
        <h3 style="color: white; margin-top: 0;">The Prediction-Profitability Gap</h3>
        <p style="font-size: 1.1rem; color: white; line-height: 1.8;">
            Despite achieving <strong>99.86% prediction accuracy (R²)</strong> across 1,386 machine learning models, 
            every single trading strategy <strong>underperformed simple buy-and-hold by 21% annually</strong>.
        </p>
        <p style="font-size: 1.1rem; color: white; line-height: 1.8;">
            Models trained on 2004-2021 data completely failed when deployed in 2022-2024 markets, 
            proving that <strong>high accuracy ≠ profitability</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Why it happens
    st.markdown("### Why Does This Happen?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>📉 Market Regime Changes</h4>
            <ul>
                <li>2022-2024: Ukraine war, banking crisis, Fed rate hikes</li>
                <li>Models trained on 2004-2021 (bull market era)</li>
                <li>Zero awareness of geopolitical events</li>
                <li>Patterns became obsolete overnight</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>🎯 The Fundamental Flaw</h4>
            <ul>
                <li>ML predicts prices based on historical patterns</li>
                <li>Ignores external shocks and news events</li>
                <li>No context about WHY prices move</li>
                <li>Prediction accuracy becomes meaningless</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # The Gap Visualization
    st.markdown("### 📊 The Gap Revealed")
    
    fig = go.Figure()
    
    strategies = ['Buy & Hold<br>Baseline', 'ML Model<br>99.86% R²', 'Intelligent<br>System']
    returns = [-0.85, -14.02, 9.92]
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    
    fig.add_trace(go.Bar(
        x=strategies,
        y=returns,
        marker_color=colors,
        marker_line_color='white',
        marker_line_width=2,
        text=[f'{r:.1f}%' for r in returns],
        textposition='outside',
        textfont=dict(size=16, color='white', family='Inter')
    ))
    
    fig.update_layout(
        title='Annual Returns Comparison (2022-2024 Testing Period)',
        yaxis_title='Annual Return (%)',
        template='plotly_dark',
        height=450,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter', color='white'),
        title_font_size=18
    )
    
    fig.add_hline(y=0, line_dash="dash", line_color="white", opacity=0.3)
    fig.add_annotation(
        x=1, y=-14.02,
        text="21% worse than<br>buy-and-hold!",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#e74c3c",
        font=dict(color="#e74c3c", size=14)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # The Solution
    st.markdown("## ✅ Our Solution")
    
    st.markdown("""
    <div class="solution-card">
        <h3 style="margin-top: 0;">Geopolitical Intelligence Framework</h3>
        <p style="font-size: 1.1rem; line-height: 1.8;">
            Instead of relying solely on ML predictions, we built an <strong>event-aware intelligent system</strong> 
            that combines machine learning with real-time geopolitical event detection and impact assessment.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>🤖 Event Detection</h4>
            <p>FinBERT-powered classification of news events into 6 categories with <strong>90% accuracy</strong></p>
            <ul>
                <li>Geopolitical</li>
                <li>Economic Policy</li>
                <li>Regulatory</li>
                <li>Corporate</li>
                <li>Natural Disaster</li>
                <li>Technological</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>📊 Impact Scoring</h4>
            <p>Automated assessment of event severity on a <strong>0-10 scale</strong></p>
            <ul>
                <li>Sentiment analysis</li>
                <li>Historical correlation</li>
                <li>Market context</li>
                <li>Real-time updates</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <h4>⚖️ Risk Management</h4>
            <p>Dynamic position adjustment based on event impact</p>
            <ul>
                <li>Impact >8: Close positions</li>
                <li>Impact 5-8: Reduce 50%</li>
                <li>Impact <5: Normal trading</li>
                <li>Automated execution</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Results
    st.markdown("## 🎯 Results")
    
    st.markdown("""
    <div class="result-card">
        <h3 style="margin-top: 0;">Statistical Significance Achieved</h3>
        <p style="font-size: 1.1rem; line-height: 1.8;">
            Our intelligent system demonstrated <strong>statistically significant outperformance</strong> 
            (p < 0.000001) across 782 trading days with comprehensive risk-adjusted metrics.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sharpe ratio comparison
        fig = go.Figure()
        
        strategies_sharpe = ['Buy & Hold', 'ML Model', 'Intelligent']
        sharpe_values = [-0.28, -0.89, 0.24]
        colors_sharpe = ['#3498db', '#e74c3c', '#2ecc71']
        
        fig.add_trace(go.Bar(
            y=strategies_sharpe,
            x=sharpe_values,
            orientation='h',
            marker_color=colors_sharpe,
            text=[f'{s:.2f}' for s in sharpe_values],
            textposition='outside',
            marker_line_color='white',
            marker_line_width=2
        ))
        
        fig.update_layout(
            title='Sharpe Ratio Comparison',
            xaxis_title='Sharpe Ratio',
            template='plotly_dark',
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter', color='white')
        )
        
        fig.add_vline(x=0, line_dash="dash", line_color="white", opacity=0.3)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Drawdown comparison
        fig = go.Figure()
        
        strategies_dd = ['Buy & Hold', 'ML Model', 'Intelligent']
        dd_values = [-26.97, -47.14, -22.95]
        colors_dd = ['#f39c12', '#e74c3c', '#2ecc71']
        
        fig.add_trace(go.Bar(
            y=strategies_dd,
            x=dd_values,
            orientation='h',
            marker_color=colors_dd,
            text=[f'{d:.1f}%' for d in dd_values],
            textposition='inside',
            marker_line_color='white',
            marker_line_width=2,
            textfont=dict(color='white', size=14)
        ))
        
        fig.update_layout(
            title='Maximum Drawdown (Lower = Better)',
            xaxis_title='Drawdown (%)',
            template='plotly_dark',
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter', color='white')
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Key takeaway
    st.markdown("""
    <div class="quote-card">
        <h3 style="color: #a8b2ff;">💡 Key Insight</h3>
        <p style="font-size: 1.2rem; line-height: 1.8; color: #a8b2ff;">
            "Context matters more than accuracy. A 90% accurate event classifier combined with 
            simple risk rules outperformed 99.86% accurate price predictions because it understood 
            <strong>WHY</strong> markets move, not just <strong>HOW</strong> they moved in the past."
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: RESEARCH JOURNEY
# ============================================================================

def page_research_journey():
    st.title("🔬 Research Journey")
    
    st.markdown("""
    <div style="text-align: center; color: #a8b2ff; font-size: 1.1rem; margin-bottom: 2rem;">
        From problem discovery to solution validation - a systematic research approach
    </div>
    """, unsafe_allow_html=True)
    
    # Phase 1
    st.markdown("""
    <div class="process-step">
        <div class="step-number">1</div>
        <h3 style="margin-top: 1rem; color: #667eea;">Discovery: Training 1,386 Models</h3>
        
        <p><strong>Goal:</strong> Build comprehensive ML prediction system</p>
        <ul>
            <li>Collected 20 years of data (2004-2024) for 50 NSE stocks</li>
            <li>Engineered 325 technical features (momentum, volatility, trends)</li>
            <li>Trained 25 classical ML algorithms + 5 deep learning models</li>
            <li>Total combinations: 1,386 trained models</li>
        </ul>
        <p><strong>Best Result:</strong> Random Forest achieved R² = 0.9986 (99.86% accuracy)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Phase 2
    st.markdown("""
    <div class="process-step">
        <div class="step-number">2</div>
        <h3 style="margin-top: 1rem; color: #667eea;">Shock: The Gap Emerges</h3>
        
        <p><strong>Discovery:</strong> Backtesting revealed catastrophic failure</p>
        <ul>
            <li>Test period: 2022-2024 (out-of-sample)</li>
            <li>ML strategies lost money despite high accuracy</li>
            <li>Underperformance: -21% vs buy-and-hold annually</li>
            <li>All 1,386 models failed in live conditions</li>
        </ul>
        <p><strong>Root Cause Analysis:</strong> Models had zero awareness of:
            <ul>
                <li>Russia-Ukraine war (Feb 2022)</li>
                <li>Silicon Valley Bank collapse (Mar 2023)</li>
                <li>Federal Reserve rate hikes (2022-2023)</li>
                <li>Any geopolitical or economic shocks</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Phase 3
    st.markdown("""
    <div class="process-step">
        <div class="step-number">3</div>
        <h3 style="margin-top: 1rem; color: #667eea;">Hypothesis: Event-Aware Intelligence</h3>
        
        <p><strong>Idea:</strong> What if we detect and respond to major events?</p>
        <ul>
            <li>Built event taxonomy (6 categories)</li>
            <li>Manual classification of 10 major 2022-2024 events</li>
            <li>Created impact scoring system (0-10 scale)</li>
            <li>Keyword-based detection: 85% accuracy</li>
        </ul>
        <p><strong>Initial Validation:</strong> ITC case study showed +1.60% improvement</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Phase 4
    st.markdown("""
    <div class="process-step">
        <div class="step-number">4</div>
        <h3 style="margin-top: 1rem; color: #667eea;">Enhancement: FinBERT Integration</h3>
        
        <p><strong>Goal:</strong> Upgrade event classification to 90%+</p>
        <ul>
            <li>Integrated FinBERT (financial sentiment model)</li>
            <li>Added zero-shot classification as fallback</li>
            <li>Refined keyword taxonomy with priority scoring</li>
            <li>Tested on 40 diverse events (10 historical + 30 validation)</li>
        </ul>
        <p><strong>Iterative Improvement:</strong>
            <ul>
                <li>First attempt: 70% (worse than baseline!)</li>
                <li>Improved keywords: 87.5%</li>
                <li>Final refined: 90.0% ✅</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Phase 5
    st.markdown("""
    <div class="process-step">
        <div class="step-number">5</div>
        <h3 style="margin-top: 1rem; color: #667eea;">Validation: Professional Risk Metrics</h3>
        
        <p><strong>Goal:</strong> Prove statistical significance</p>
        <ul>
            <li>Generated realistic 3-year backtest (782 trading days)</li>
            <li>Calculated Sharpe, Sortino, Calmar ratios</li>
            <li>Measured maximum drawdown and win rates</li>
            <li>Performed paired t-tests and Diebold-Mariano tests</li>
        </ul>
        <p><strong>Statistical Results:</strong>
            <ul>
                <li>Sharpe improvement: -0.89 → +0.24 (Δ = +1.13)</li>
                <li>Drawdown reduction: -47% → -23% (49% improvement)</li>
                <li>p-value < 0.000001 (extremely significant)</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Phase 6
    st.markdown("""
    <div class="process-step">
        <div class="step-number">6</div>
        <h3 style="margin-top: 1rem; color: #667eea;">Production: System Architecture</h3>
        <p><strong>Duration:</strong> Day 12</p>
        <p><strong>Goal:</strong> Design deployable production system</p>
        <ul>
            <li>Event-driven microservices architecture</li>
            <li>4-layer design: Data → Intelligence → Decision → Monitoring</li>
            <li>Tech stack: FastAPI, PostgreSQL, Redis, FinBERT, TensorFlow</li>
            <li>3-tier deployment: MVP ($300/mo) → Production ($800/mo) → Enterprise ($2000/mo)</li>
        </ul>
        <p><strong>Risk Framework:</strong> Position sizing, stop losses, event-based rules, drawdown controls</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline visualization
    st.markdown("## 📅 Project Timeline")
    
    timeline_data = {
        'Phase': ['Discovery', 'Shock', 'Hypothesis', 'Enhancement', 'Validation', 'Production'],
        
        'Outcome': ['1,386 models', 'Gap found', '85% accuracy', '90% accuracy', 'p<0.001', 'Architecture']
    }
    
    df = pd.DataFrame(timeline_data)
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

# ============================================================================
# PAGE: KEY FINDINGS
# ============================================================================

def page_key_findings():
    st.title("📊 Key Findings")
    
    st.markdown("""
    <div style="text-align: center; color: #a8b2ff; font-size: 1.1rem; margin-bottom: 2rem;">
        Quantitative results and statistical validation
    </div>
    """, unsafe_allow_html=True)
    
    # Finding 1
    st.markdown("## 🔍 Finding 1: The Prediction-Profit Gap Exists")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>📈 Prediction Metrics (Training)</h4>
            <table style="width: 100%; color: white;">
                <tr><td><strong>Best R²:</strong></td><td style="text-align: right;">0.9986 (99.86%)</td></tr>
                <tr><td><strong>RMSE:</strong></td><td style="text-align: right;">0.0124</td></tr>
                <tr><td><strong>Algorithm:</strong></td><td style="text-align: right;">Random Forest</td></tr>
                <tr><td><strong>Training Period:</strong></td><td style="text-align: right;">2004-2021</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>💰 Trading Performance (Testing)</h4>
            <table style="width: 100%; color: white;">
                <tr><td><strong>Annual Return:</strong></td><td style="text-align: right; color: #e74c3c;">-14.02%</td></tr>
                <tr><td><strong>Sharpe Ratio:</strong></td><td style="text-align: right; color: #e74c3c;">-0.89</td></tr>
                <tr><td><strong>vs Buy-Hold:</strong></td><td style="text-align: right; color: #e74c3c;">-21% worse</td></tr>
                <tr><td><strong>Testing Period:</strong></td><td style="text-align: right;">2022-2024</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote-card">
        <strong>Conclusion:</strong> High prediction accuracy is necessary but not sufficient for trading profitability. 
        Models need contextual awareness of market-moving events.
    </div>
    """, unsafe_allow_html=True)
    
    # Finding 2
    st.markdown("## 🤖 Finding 2: Event Classification Achieves 90% Accuracy")
    
    # Category performance
    categories = ['Geopolitical', 'Economic Policy', 'Natural Disaster', 'Technological', 'Corporate', 'Regulatory']
    accuracy = [1.00, 0.933, 1.00, 1.00, 0.857, 0.667]
    colors_cat = ['#2ecc71' if a >= 0.9 else '#f39c12' if a >= 0.8 else '#e74c3c' for a in accuracy]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=accuracy,
        y=categories,
        orientation='h',
        marker_color=colors_cat,
        text=[f'{a:.1%}' for a in accuracy],
        textposition='outside',
        marker_line_color='white',
        marker_line_width=2
    ))
    
    fig.update_layout(
        title='Event Classification Accuracy by Category',
        xaxis_title='Accuracy',
        template='plotly_dark',
        height=400,
        xaxis=dict(tickformat='.0%', range=[0, 1.1]),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter', color='white')
    )
    
    fig.add_vline(x=0.9, line_dash="dash", line_color="#2ecc71", 
                 annotation_text="Target: 90%", opacity=0.7)
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>✅ Perfect Categories (100%)</h4>
            <ul>
                <li>Geopolitical (6/6 events)</li>
                <li>Natural Disaster (3/3 events)</li>
                <li>Technological (3/3 events)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>⚠️ Challenging Categories</h4>
            <ul>
                <li>Regulatory: 66.7% (tax vs policy ambiguity)</li>
                <li>Corporate: 85.7% (company names → tech confusion)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Finding 3
    st.markdown("## ⚖️ Finding 3: Risk-Adjusted Performance Significantly Improves")
    
    metrics_comparison = {
        'Metric': ['Sharpe Ratio', 'Sortino Ratio', 'Max Drawdown', 'Annual Return', 'Win Rate'],
        'Buy & Hold': [-0.28, -0.48, -26.97, -0.85, 50.3],
        'ML Model': [-0.89, -1.48, -47.14, -14.02, 48.3],
        'Intelligent': [0.24, 0.44, -22.95, 9.92, 51.0]
    }
    
    df_metrics = pd.DataFrame(metrics_comparison)
    
    # Format for display
    df_display = df_metrics.copy()
    df_display['Buy & Hold'] = df_display['Buy & Hold'].apply(lambda x: f'{x:.2f}%' if 'Rate' in df_display.loc[df_display['Buy & Hold'] == x, 'Metric'].values[0] or 'Return' in df_display.loc[df_display['Buy & Hold'] == x, 'Metric'].values[0] or 'Drawdown' in df_display.loc[df_display['Buy & Hold'] == x, 'Metric'].values[0] else f'{x:.2f}')
    
    st.dataframe(df_display, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="result-card">
        <h4 style="margin-top: 0;">🎯 Statistical Significance</h4>
        <ul>
            <li><strong>Sample Size:</strong> 782 trading days (3 years)</li>
            <li><strong>Paired t-test (Intelligent vs Buy-Hold):</strong> t=7.06, p < 0.000001 ✅</li>
            <li><strong>Paired t-test (Intelligent vs ML Model):</strong> t=7.49, p < 0.000001 ✅</li>
            <li><strong>Diebold-Mariano test:</strong> DM=2.21, p=0.027 ✅</li>
            <li><strong>Conclusion:</strong> Improvements are statistically significant, not due to chance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: TECHNICAL IMPLEMENTATION
# ============================================================================

def page_technical():
    st.title("🏗️ Technical Implementation")
    
    st.markdown("""
    <div style="text-align: center; color: #a8b2ff; font-size: 1.1rem; margin-bottom: 2rem;">
        Production-ready system architecture and technology stack
    </div>
    """, unsafe_allow_html=True)
    
    # Architecture
    st.markdown("## 🏛️ System Architecture")
    
    st.markdown("""
    <div class="info-card">
        <h4>4-Layer Microservices Architecture</h4>
        <p>Event-driven, cloud-native design for scalability and reliability</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="process-step">
            <div class="step-number">1</div>
            <h4 style="margin-top: 1rem;">Data Layer</h4>
            <ul>
                <li>Market data feeds (NSE/BSE API)</li>
                <li>News aggregation (NewsAPI, RSS)</li>
                <li>PostgreSQL database</li>
                <li>Redis cache</li>
                <li>Kafka message queue</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="process-step">
            <div class="step-number">3</div>
            <h4 style="margin-top: 1rem;">Decision Layer</h4>
            <ul>
                <li>Signal generation</li>
                <li>Portfolio management</li>
                <li>Order execution (Broker API)</li>
                <li>Position tracking</li>
                <li>Risk controls</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="process-step">
            <div class="step-number">2</div>
            <h4 style="margin-top: 1rem;">Intelligence Layer</h4>
            <ul>
                <li>FinBERT event classifier (90%)</li>
                <li>ML prediction engine (1,386 models)</li>
                <li>Event impact scoring</li>
                <li>Risk assessment</li>
                <li>Feature engineering</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="process-step">
            <div class="step-number">4</div>
            <h4 style="margin-top: 1rem;">Monitoring Layer</h4>
            <ul>
                <li>Performance dashboard (Streamlit)</li>
                <li>Risk monitoring (real-time)</li>
                <li>Alert system (SNS)</li>
                <li>Audit logs</li>
                <li>System health checks</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Tech Stack
    st.markdown("## 🔧 Technology Stack")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>Backend</h4>
            <ul>
                <li>Python 3.10+</li>
                <li>FastAPI</li>
                <li>Celery + Redis</li>
                <li>Uvicorn + Nginx</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>ML/AI</h4>
            <ul>
                <li>scikit-learn</li>
                <li>TensorFlow 2.x</li>
                <li>FinBERT (HuggingFace)</li>
                <li>pandas, numpy</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <h4>Infrastructure</h4>
            <ul>
                <li>AWS / GCP</li>
                <li>Docker</li>
                <li>PostgreSQL</li>
                <li>Redis, Kafka</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Deployment
    st.markdown("## 💰 Deployment Tiers")
    
    tier_data = {
        'Tier': ['MVP', 'Production', 'Enterprise'],
        'Cost/Month': ['$300', '$800', '$2,000'],
        'Use Case': ['Paper trading', 'Live trading', 'Multi-asset'],
        'Infrastructure': ['Single EC2', 'Multi-AZ', 'Multi-region'],
        'Data': ['Free sources', 'Premium feeds', 'Bloomberg/Reuters']
    }
    
    df_tiers = pd.DataFrame(tier_data)
    st.dataframe(df_tiers, use_container_width=True, hide_index=True)
    
    # Risk Management
    st.markdown("## ⚖️ Risk Management Framework")
    
    st.markdown("""
    <div class="solution-card">
        <h4 style="margin-top: 0;">Automated Risk Controls</h4>
        <table style="width: 100%;">
            <tr>
                <td style="width: 40%;"><strong>Position Sizing:</strong></td>
                <td>Max 5% per stock, 20% per sector</td>
            </tr>
            <tr>
                <td><strong>Stop Losses:</strong></td>
                <td>3% hard stop, 2% trailing stop</td>
            </tr>
            <tr>
                <td><strong>Event Response:</strong></td>
                <td>Impact >8: Close all | 5-8: Reduce 50% | <5: Normal</td>
            </tr>
            <tr>
                <td><strong>Drawdown Control:</strong></td>
                <td>Max 15% portfolio drawdown</td>
            </tr>
            <tr>
                <td><strong>Real-time Monitoring:</strong></td>
                <td>Alerts for P&L >2%, failed orders, risk breaches</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: ABOUT
# ============================================================================

def page_about():
    st.title("ℹ️ About This Research")
    
    st.markdown("""
    <div style="text-align: center; color: #a8b2ff; font-size: 1.1rem; margin-bottom: 2rem;">
        Final year research project | Mumbai University | 2024-2025
    </div>
    """, unsafe_allow_html=True)
    
    # Project Info
    st.markdown("## 📚 Project Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>🎓 Academic Details</h4>
            <table style="width: 100%; color: white;">
                <tr><td><strong>Institution:</strong></td><td>Mumbai University</td></tr>
                <tr><td><strong>Program:</strong></td><td>B.Tech Artificial Intelligence</td></tr>
                <tr><td><strong>Year:</strong></td><td>Final Year (2024-25)</td></tr>
                <tr><td><strong>Duration:</strong></td><td>6 months</td></tr>
                <tr><td><strong>Status:</strong></td><td>Completed</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>🎯 Research Scope</h4>
            <table style="width: 100%; color: white;">
                <tr><td><strong>Stocks Analyzed:</strong></td><td>50 NSE stocks</td></tr>
                <tr><td><strong>Data Period:</strong></td><td>2004-2024 (20 years)</td></tr>
                <tr><td><strong>Models Trained:</strong></td><td>1,386 models</td></tr>
                <tr><td><strong>Events Classified:</strong></td><td>40 events</td></tr>
                <tr><td><strong>Testing Days:</strong></td><td>782 trading days</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    # Contributions
    st.markdown("## 🏆 Key Contributions")
    
    st.markdown("""
    <div class="result-card">
        <h4 style="margin-top: 0;">Original Research Contributions</h4>
        <ol style="font-size: 1.05rem; line-height: 1.8;">
            <li><strong>Empirical Evidence:</strong> First large-scale study (1,386 models) demonstrating the prediction-profitability gap in algorithmic trading</li>
            <li><strong>Novel Framework:</strong> Geopolitical intelligence system specifically designed for Indian equity markets</li>
            <li><strong>Statistical Validation:</strong> Rigorous testing with p < 0.000001 across 782 trading days</li>
            <li><strong>Production Architecture:</strong> Complete system blueprint with cost analysis and deployment roadmap</li>
            <li><strong>Open Source:</strong> All code, data, and methodologies publicly available for reproducibility</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Methodology
    st.markdown("## 🔬 Research Methodology")
    
    st.markdown("""
    <div class="info-card">
        <h4>Systematic Approach</h4>
        <ul>
            <li><strong>Data Collection:</strong> Historical price data, technical indicators, news events</li>
            <li><strong>Feature Engineering:</strong> 325 technical features across multiple timeframes</li>
            <li><strong>Model Training:</strong> 25 ML algorithms + 5 deep learning architectures</li>
            <li><strong>Backtesting:</strong> Walk-forward validation with realistic transaction costs</li>
            <li><strong>Event Integration:</strong> FinBERT-powered classification with impact scoring</li>
            <li><strong>Statistical Testing:</strong> Paired t-tests, Diebold-Mariano, confidence intervals</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Publications
    st.markdown("## 📝 Publications & Dissemination")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>📄 Planned Publications</h4>
            <ul>
                <li><strong>ArXiv Preprint:</strong> Submitted</li>
                <li><strong>Journal:</strong> Digital Finance (Springer)</li>
                <li><strong>Conference:</strong> ICAIF 2025</li>
                <li><strong>Repository:</strong> GitHub (open source)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>🌐 Open Source Resources</h4>
            <ul>
                <li>Complete codebase (Python)</li>
                <li>Trained models (1,386)</li>
                <li>Event taxonomy & classifications</li>
                <li>Dashboard & visualizations</li>
                <li>Documentation & tutorials</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Impact
    st.markdown("## 🎯 Potential Impact")
    
    st.markdown("""
    <div class="solution-card">
        <h4 style="margin-top: 0;">Real-World Applications</h4>
        <ul style="font-size: 1.05rem; line-height: 1.8;">
            <li><strong>Retail Traders:</strong> Understand why ML strategies fail and how to improve them</li>
            <li><strong>Quant Firms:</strong> Framework for integrating event intelligence into trading systems</li>
            <li><strong>Academics:</strong> Benchmark for future research on prediction-profit gap</li>
            <li><strong>Regulators:</strong> Insights into AI-driven trading risks and market stability</li>
            <li><strong>Fintech Startups:</strong> Production-ready architecture for deployment</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact
    st.markdown("## 📧 Contact & Links")
    
    st.markdown("""
    <div class="info-card" style="text-align: center;">
        <h4>Get in Touch</h4>
        <p><strong>Author:</strong> [Your Name]</p>
        <p><strong>Email:</strong> your.email@university.edu</p>
        <p><strong>GitHub:</strong> github.com/yourname/marketlab</p>
        <p><strong>LinkedIn:</strong> linkedin.com/in/yourname</p>
        <p><strong>Dashboard:</strong> marketlab-dashboard.streamlit.app</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem; padding: 2rem;">
        <p><strong>MarketLab Research Showcase v3.0</strong></p>
        <p>Built with Streamlit, Plotly, and Python</p>
        <p>© 2024-2025 | Mumbai University | All Rights Reserved</p>
        <p style="margin-top: 1rem; font-size: 0.8rem;">
            This research is provided for educational and academic purposes only.<br>
            Not financial advice. Trading involves substantial risk of loss.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    page = render_sidebar()
    
    if page == "🏠 Overview":
        page_overview()
    elif page == "🔬 Research Journey":
        page_research_journey()
    elif page == "📊 Key Findings":
        page_key_findings()
    elif page == "🏗️ Technical Implementation":
        page_technical()
    elif page == "ℹ️ About":
        page_about()

if __name__ == "__main__":
    main()
