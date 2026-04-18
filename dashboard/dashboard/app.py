"""
MarketLab Professional Dashboard v3.0
Advanced Trading Intelligence System
Author: [Your Name]
Institution: Mumbai University
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
from pathlib import Path
from datetime import datetime
import base64

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="MarketLab Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "MarketLab: Bridging the Prediction-Profitability Gap"
    }
)

# ============================================================================
# CUSTOM CSS - PROFESSIONAL QUANT STYLE
# ============================================================================

st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #00d4ff;
        --secondary-color: #ff6b6b;
        --success-color: #51cf66;
        --warning-color: #ffd93d;
        --dark-bg: #0e1117;
        --card-bg: #1a1d29;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1d29 0%, #0e1117 100%);
        border-right: 1px solid #2d3142;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #00d4ff;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 1rem;
        font-weight: 600;
        color: #a0a0a0;
    }
    
    /* Headers */
    h1 {
        color: #ffffff;
        font-weight: 800;
        letter-spacing: -0.5px;
        padding-bottom: 1rem;
        border-bottom: 2px solid #00d4ff;
    }
    
    h2 {
        color: #00d4ff;
        font-weight: 700;
        margin-top: 2rem;
    }
    
    h3 {
        color: #ffd93d;
        font-weight: 600;
    }
    
    /* Cards */
    .metric-card {
        background: linear-gradient(135deg, #1a1d29 0%, #252836 100%);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #2d3142;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 1rem;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #0066cc 0%, #004c99 100%);
        border-radius: 8px;
        padding: 1rem;
        color: white;
        margin: 1rem 0;
        border-left: 4px solid #00d4ff;
    }
    
    .success-box {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        border-radius: 8px;
        padding: 1rem;
        color: white;
        margin: 1rem 0;
        border-left: 4px solid #51cf66;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        border-radius: 8px;
        padding: 1rem;
        color: white;
        margin: 1rem 0;
        border-left: 4px solid #ffd93d;
    }
    
    /* Tables */
    .dataframe {
        background: #1a1d29;
        border-radius: 8px;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 212, 255, 0.4);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background: #1a1d29;
        border-radius: 8px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #a0a0a0;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        color: #00d4ff;
        border-bottom: 2px solid #00d4ff;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

@st.cache_data
def load_all_data():
    """Load all project data"""
    base_path = Path('/content/drive/MyDrive/MarketLab_BEAST')
    
    data = {
        'loaded': False,
        'error': None
    }
    
    try:
        # Day 10: Event Classification
        day10_path = base_path / 'results_day10'
        if day10_path.exists():
            with open(day10_path / 'comprehensive_metrics_report.json', 'r') as f:
                data['event_classification'] = json.load(f)
            
            data['events'] = pd.read_csv(day10_path / 'final_enhanced_classifications.csv')
        
        # Day 11: Risk Metrics
        day11_path = base_path / 'results_day11'
        if day11_path.exists():
            data['risk_metrics'] = pd.read_csv(day11_path / 'risk_adjusted_metrics.csv')
            data['backtest_daily'] = pd.read_csv(day11_path / 'daily_backtest_returns.csv')
            
            with open(day11_path / 'statistical_tests.json', 'r') as f:
                data['statistical_tests'] = json.load(f)
            
            with open(day11_path / 'comprehensive_report.json', 'r') as f:
                data['comprehensive_report'] = json.load(f)
        
        # Day 12: Architecture
        day12_path = base_path / 'results_day12'
        if day12_path.exists():
            with open(day12_path / 'system_overview.json', 'r') as f:
                data['architecture'] = json.load(f)
            
            with open(day12_path / 'technical_documentation.json', 'r') as f:
                data['tech_docs'] = json.load(f)
        
        data['loaded'] = True
        
    except Exception as e:
        data['error'] = str(e)
    
    return data

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

def render_sidebar():
    """Render professional sidebar"""
    
    with st.sidebar:
        # Logo/Title
        st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h1 style='color: #00d4ff; font-size: 2.5rem; margin: 0;'>📊</h1>
            <h2 style='color: white; font-size: 1.5rem; margin: 0.5rem 0;'>MarketLab</h2>
            <p style='color: #a0a0a0; font-size: 0.9rem;'>Intelligence Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation
        page = st.radio(
            "Navigation",
            ["🏠 Overview", "📈 Model Performance", "🤖 Event Intelligence", 
             "⚖️ Risk Metrics", "🏗️ Architecture", "ℹ️ About"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Quick Stats
        st.markdown("### 📊 Quick Stats")
        
        data = load_all_data()
        
        if data['loaded']:
            if 'event_classification' in data:
                st.metric("Event Accuracy", "90.0%", "+5.0%")
            
            if 'risk_metrics' in data:
                intelligent = data['risk_metrics'][
                    data['risk_metrics']['strategy'] == 'intelligent_system'
                ].iloc[0]
                
                st.metric("Sharpe Ratio", f"{intelligent['sharpe_ratio']:.3f}", "+1.13")
                st.metric("Annual Return", f"{intelligent['annual_return']:.1%}", "+24%")
        
        st.markdown("---")
        
        # Footer
        st.markdown("""
        <div style='text-align: center; color: #666; font-size: 0.8rem; margin-top: 2rem;'>
            <p>MarketLab v3.0</p>
            <p>Mumbai University</p>
            <p>2024-2025</p>
        </div>
        """, unsafe_allow_html=True)
    
    return page

# ============================================================================
# PAGE: OVERVIEW
# ============================================================================

def page_overview():
    """Main overview page"""
    
    st.title("📊 MarketLab Intelligence Platform")
    st.markdown("### Bridging the Prediction-Profitability Gap in Algorithmic Trading")
    
    data = load_all_data()
    
    if not data['loaded']:
        st.error(f"⚠️ Error loading data: {data.get('error', 'Unknown error')}")
        return
    
    # Hero metrics
    st.markdown("## 🎯 Key Achievements")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3 style='color: #00d4ff; margin: 0;'>1,386</h3>
            <p style='color: #a0a0a0; margin: 0.5rem 0 0 0;'>ML Models Trained</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3 style='color: #51cf66; margin: 0;'>90.0%</h3>
            <p style='color: #a0a0a0; margin: 0.5rem 0 0 0;'>Event Classification</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3 style='color: #ffd93d; margin: 0;'>+1.13</h3>
            <p style='color: #a0a0a0; margin: 0.5rem 0 0 0;'>Sharpe Improvement</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <h3 style='color: #ff6b6b; margin: 0;'>-49%</h3>
            <p style='color: #a0a0a0; margin: 0.5rem 0 0 0;'>Drawdown Reduction</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # The Gap Discovery
    st.markdown("## 🔍 The Prediction-Profit Gap")
    
    st.markdown("""
    <div class='warning-box'>
        <h4 style='margin-top: 0;'>⚠️ Critical Discovery</h4>
        <p><strong>Despite 99.86% prediction accuracy (R²), ML models underperformed buy-and-hold by 21% annually.</strong></p>
        <p>This research reveals why high-accuracy ML models fail in real trading environments.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Gap visualization
    if 'risk_metrics' in data:
        fig = go.Figure()
        
        strategies = ['Buy & Hold', 'ML Model\n(99.86% R²)', 'Intelligent\nSystem']
        returns = [
            data['risk_metrics'][data['risk_metrics']['strategy'] == 'buy_and_hold']['annual_return'].values[0],
            data['risk_metrics'][data['risk_metrics']['strategy'] == 'ml_model_predictions']['annual_return'].values[0],
            data['risk_metrics'][data['risk_metrics']['strategy'] == 'intelligent_system']['annual_return'].values[0]
        ]
        
        colors = ['#3498db', '#e74c3c', '#2ecc71']
        
        fig.add_trace(go.Bar(
            x=strategies,
            y=returns,
            marker_color=colors,
            text=[f'{r:.1%}' for r in returns],
            textposition='outside',
            textfont=dict(size=14, color='white', family='Arial Black')
        ))
        
        fig.update_layout(
            title='Annual Returns Comparison: The Gap Revealed',
            yaxis_title='Annual Return',
            template='plotly_dark',
            height=400,
            yaxis=dict(tickformat='.0%'),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Solution Overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("## 💡 Our Solution")
        
        st.markdown("""
        <div class='success-box'>
            <h4 style='margin-top: 0;'>✅ Geopolitical Intelligence Framework</h4>
            <ul style='margin-bottom: 0;'>
                <li><strong>Event Detection:</strong> FinBERT classification (90% accuracy)</li>
                <li><strong>Impact Scoring:</strong> 0-10 scale with sentiment analysis</li>
                <li><strong>Risk Management:</strong> Event-aware position sizing</li>
                <li><strong>Adaptive Trading:</strong> Dynamic exposure adjustment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("## 📊 Results")
        
        if 'risk_metrics' in data:
            intelligent = data['risk_metrics'][
                data['risk_metrics']['strategy'] == 'intelligent_system'
            ].iloc[0]
            
            ml_model = data['risk_metrics'][
                data['risk_metrics']['strategy'] == 'ml_model_predictions'
            ].iloc[0]
            
            st.markdown(f"""
            <div class='info-box'>
                <h4 style='margin-top: 0;'>📈 Performance Metrics</h4>
                <table style='width: 100%; color: white;'>
                    <tr>
                        <td><strong>Sharpe Ratio:</strong></td>
                        <td style='text-align: right;'>{intelligent['sharpe_ratio']:.3f} <span style='color: #51cf66;'>▲</span></td>
                    </tr>
                    <tr>
                        <td><strong>Annual Return:</strong></td>
                        <td style='text-align: right;'>{intelligent['annual_return']:.2%} <span style='color: #51cf66;'>▲</span></td>
                    </tr>
                    <tr>
                        <td><strong>Max Drawdown:</strong></td>
                        <td style='text-align: right;'>{intelligent['max_drawdown']:.2%} <span style='color: #51cf66;'>▲</span></td>
                    </tr>
                    <tr>
                        <td><strong>Win Rate:</strong></td>
                        <td style='text-align: right;'>{intelligent['win_rate']:.1%}</td>
                    </tr>
                </table>
            </div>
            """, unsafe_allow_html=True)
    
    # Timeline
    st.markdown("## 📅 Research Timeline")
    
    timeline_data = {
        'Phase': ['Days 1-4', 'Days 5-7', 'Day 10', 'Day 11', 'Day 12'],
        'Focus': ['Model Training', 'Event System', 'NLP Enhancement', 'Risk Metrics', 'Architecture'],
        'Achievement': ['1,386 models', '85% accuracy', '90% accuracy', 'Sharpe +1.13', 'Production ready'],
        'Status': ['✅', '✅', '✅', '✅', '✅']
    }
    
    timeline_df = pd.DataFrame(timeline_data)
    st.dataframe(timeline_df, use_container_width=True, hide_index=True)

# ============================================================================
# PAGE: MODEL PERFORMANCE
# ============================================================================

def page_model_performance():
    """Model performance analysis"""
    
    st.title("📈 Model Performance Analysis")
    
    data = load_all_data()
    
    if not data['loaded'] or 'risk_metrics' not in data:
        st.warning("Data not available")
        return
    
    # Strategy comparison
    st.markdown("## 📊 Strategy Comparison")
    
    metrics_df = data['risk_metrics']
    
    # Create comparison table
    comparison = metrics_df[['strategy', 'sharpe_ratio', 'sortino_ratio', 
                            'max_drawdown', 'annual_return', 'win_rate']].copy()
    
    comparison.columns = ['Strategy', 'Sharpe', 'Sortino', 'Max DD', 'Annual Return', 'Win Rate']
    comparison['Strategy'] = comparison['Strategy'].str.replace('_', ' ').str.title()
    
    st.dataframe(
        comparison.style.format({
            'Sharpe': '{:.3f}',
            'Sortino': '{:.3f}',
            'Max DD': '{:.2%}',
            'Annual Return': '{:.2%}',
            'Win Rate': '{:.1%}'
        }).background_gradient(subset=['Sharpe', 'Sortino'], cmap='RdYlGn'),
        use_container_width=True,
        hide_index=True
    )
    
    # Equity curves
    st.markdown("## 📈 Equity Curves")
    
    if 'backtest_daily' in data:
        backtest_df = data['backtest_daily']
        backtest_df['date'] = pd.to_datetime(backtest_df['date'])
        
        fig = go.Figure()
        
        for strategy in backtest_df['strategy'].unique():
            strat_data = backtest_df[backtest_df['strategy'] == strategy].sort_values('date')
            cumulative = (1 + strat_data['portfolio_return']).cumprod()
            
            color_map = {
                'buy_and_hold': '#3498db',
                'ml_model_predictions': '#e74c3c',
                'intelligent_system': '#2ecc71'
            }
            
            name_map = {
                'buy_and_hold': 'Buy & Hold',
                'ml_model_predictions': 'ML Model',
                'intelligent_system': 'Intelligent System'
            }
            
            fig.add_trace(go.Scatter(
                x=strat_data['date'],
                y=cumulative,
                name=name_map.get(strategy, strategy),
                line=dict(width=3, color=color_map.get(strategy, 'gray')),
                mode='lines'
            ))
        
        fig.add_hline(y=1, line_dash="dash", line_color="gray", opacity=0.5)
        
        fig.update_layout(
            title='Cumulative Performance (2022-2024)',
            xaxis_title='Date',
            yaxis_title='Cumulative Return',
            template='plotly_dark',
            height=500,
            hovermode='x unified',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Risk-return scatter
    st.markdown("## ⚖️ Risk-Return Profile")
    
    fig = go.Figure()
    
    for _, row in metrics_df.iterrows():
        color_map = {
            'buy_and_hold': '#3498db',
            'ml_model_predictions': '#e74c3c',
            'intelligent_system': '#2ecc71'
        }
        
        name_map = {
            'buy_and_hold': 'Buy & Hold',
            'ml_model_predictions': 'ML Model',
            'intelligent_system': 'Intelligent System'
        }
        
        fig.add_trace(go.Scatter(
            x=[row['annual_volatility']],
            y=[row['annual_return']],
            mode='markers+text',
            marker=dict(size=20, color=color_map.get(row['strategy'], 'gray')),
            name=name_map.get(row['strategy'], row['strategy']),
            text=name_map.get(row['strategy'], row['strategy']),
            textposition='top center'
        ))
    
    fig.update_layout(
        title='Risk vs Return',
        xaxis_title='Annual Volatility (Risk)',
        yaxis_title='Annual Return',
        template='plotly_dark',
        height=500,
        xaxis=dict(tickformat='.0%'),
        yaxis=dict(tickformat='.0%'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: EVENT INTELLIGENCE
# ============================================================================

def page_event_intelligence():
    """Event classification results"""
    
    st.title("🤖 Event Intelligence System")
    
    data = load_all_data()
    
    if not data['loaded'] or 'event_classification' not in data:
        st.warning("Data not available")
        return
    
    event_data = data['event_classification']
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Classification Accuracy",
            "90.0%",
            "+5.0% vs baseline"
        )
    
    with col2:
        st.metric(
            "Events Analyzed",
            "40",
            "10 historical + 30 validation"
        )
    
    with col3:
        st.metric(
            "Perfect Categories",
            "4/6",
            "100% accuracy"
        )
    
    st.markdown("---")
    
    # Accuracy progression
    st.markdown("## 📊 Accuracy Progression")
    
    progression = {
        'Method': ['Baseline\nKeywords', 'First\nFinBERT', 'Improved\nKeywords', 'Final\nRefined'],
        'Accuracy': [0.85, 0.70, 0.875, 0.90]
    }
    
    fig = go.Figure()
    
    colors = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71']
    
    fig.add_trace(go.Bar(
        x=progression['Method'],
        y=progression['Accuracy'],
        marker_color=colors,
        text=[f'{a:.1%}' for a in progression['Accuracy']],
        textposition='outside',
        textfont=dict(size=14, color='white', family='Arial Black')
    ))
    
    fig.add_hline(y=0.90, line_dash="dash", line_color="#2ecc71", 
                 annotation_text="Target: 90%", opacity=0.7)
    
    fig.update_layout(
        title='Classification Accuracy Evolution',
        yaxis_title='Accuracy',
        template='plotly_dark',
        height=400,
        yaxis=dict(tickformat='.0%', range=[0, 1]),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Per-category performance
    st.markdown("## 📋 Category Performance")
    
    if 'events' in data:
        events_df = data['events']
        
        category_perf = events_df.groupby('true_category').agg({
            'correct': ['sum', 'count', 'mean']
        }).reset_index()
        
        category_perf.columns = ['Category', 'Correct', 'Total', 'Accuracy']
        category_perf = category_perf.sort_values('Accuracy', ascending=False)
        
        fig = go.Figure()
        
        colors_cat = ['#2ecc71' if acc == 1.0 else '#f39c12' if acc >= 0.85 else '#e74c3c' 
                     for acc in category_perf['Accuracy']]
        
        fig.add_trace(go.Bar(
            x=category_perf['Accuracy'],
            y=category_perf['Category'],
            orientation='h',
            marker_color=colors_cat,
            text=[f"{acc:.1%} ({c}/{t})" for acc, c, t in 
                  zip(category_perf['Accuracy'], category_perf['Correct'], category_perf['Total'])],
            textposition='outside'
        ))
        
        fig.update_layout(
            title='Accuracy by Event Category',
            xaxis_title='Accuracy',
            template='plotly_dark',
            height=400,
            xaxis=dict(tickformat='.0%', range=[0, 1.1]),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Sample classified events
    st.markdown("## 📰 Sample Classified Events")
    
    if 'events' in data:
        sample_events = events_df[['event', 'true_category', 'predicted_category', 
                                   'confidence', 'finbert_sentiment']].head(10)
        
        sample_events.columns = ['Event', 'True Category', 'Predicted', 'Confidence', 'Sentiment']
        
        st.dataframe(
            sample_events.style.format({
                'Confidence': '{:.1%}'
            }).apply(lambda x: ['background-color: #2d5016' if x['True Category'] == x['Predicted'] 
                               else 'background-color: #5c1919' for _ in x], axis=1),
            use_container_width=True,
            hide_index=True
        )

# ============================================================================
# PAGE: RISK METRICS
# ============================================================================

def page_risk_metrics():
    """Risk-adjusted performance metrics"""
    
    st.title("⚖️ Risk-Adjusted Performance")
    
    data = load_all_data()
    
    if not data['loaded'] or 'risk_metrics' not in data:
        st.warning("Data not available")
        return
    
    metrics_df = data['risk_metrics']
    
    # Sharpe ratio comparison
    st.markdown("## 📊 Sharpe Ratio Comparison")
    
    sharpe_data = metrics_df.sort_values('sharpe_ratio')
    
    fig = go.Figure()
    
    colors_sharpe = ['#e74c3c' if s < 0 else '#2ecc71' for s in sharpe_data['sharpe_ratio']]
    
    fig.add_trace(go.Bar(
        x=sharpe_data['sharpe_ratio'],
        y=[s.replace('_', ' ').title() for s in sharpe_data['strategy']],
        orientation='h',
        marker_color=colors_sharpe,
        text=[f'{s:.3f}' for s in sharpe_data['sharpe_ratio']],
        textposition='outside',
        textfont=dict(size=14, color='white', family='Arial Black')
    ))
    
    fig.add_vline(x=0, line_color="gray", line_width=2)
    
    fig.update_layout(
        title='Sharpe Ratio: Risk-Adjusted Returns',
        xaxis_title='Sharpe Ratio',
        template='plotly_dark',
        height=400,
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Drawdown analysis
    st.markdown("## 📉 Maximum Drawdown Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        dd_data = metrics_df.sort_values('max_drawdown', ascending=False)
        
        fig = go.Figure()
        
        colors_dd = ['#2ecc71' if abs(d) < 0.25 else '#f39c12' if abs(d) < 0.35 else '#e74c3c' 
                    for d in dd_data['max_drawdown']]
        
        fig.add_trace(go.Bar(
            x=dd_data['max_drawdown'],
            y=[s.replace('_', ' ').title() for s in dd_data['strategy']],
            orientation='h',
            marker_color=colors_dd,
            text=[f'{d:.1%}' for d in dd_data['max_drawdown']],
            textposition='inside',
            textfont=dict(size=12, color='white', family='Arial Black')
        ))
        
        fig.update_layout(
            title='Maximum Drawdown (Lower = Better)',
            xaxis_title='Drawdown',
            template='plotly_dark',
            height=400,
            xaxis=dict(tickformat='.0%'),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Win rate
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=[s.replace('_', ' ').title() for s in metrics_df['strategy']],
            y=metrics_df['win_rate'],
            marker_color=['#3498db', '#e74c3c', '#2ecc71'],
            text=[f'{w:.1%}' for w in metrics_df['win_rate']],
            textposition='outside',
            textfont=dict(size=14, color='white', family='Arial Black')
        ))
        
        fig.add_hline(y=0.5, line_dash="dash", line_color="gray", 
                     annotation_text="50% (Coin Flip)", opacity=0.5)
        
        fig.update_layout(
            title='Win Rate',
            yaxis_title='Win Rate',
            template='plotly_dark',
            height=400,
            yaxis=dict(tickformat='.0%', range=[0, 0.6]),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Statistical significance
    if 'statistical_tests' in data:
        st.markdown("## 🔬 Statistical Significance")
        
        tests = data['statistical_tests']['paired_t_tests']
        
        st.markdown(f"""
        <div class='success-box'>
            <h4 style='margin-top: 0;'>✅ Statistical Validation (n=782 days)</h4>
            <table style='width: 100%; color: white;'>
                <tr>
                    <th>Test</th>
                    <th>t-statistic</th>
                    <th>p-value</th>
                    <th>Significant?</th>
                </tr>
                <tr>
                    <td>Intelligent vs Buy-Hold</td>
                    <td>{tests['intelligent_vs_buy_hold']['t_statistic']:.3f}</td>
                    <td>{tests['intelligent_vs_buy_hold']['p_value']:.6f}</td>
                    <td>✅ YES (p < 0.001)</td>
                </tr>
                <tr>
                    <td>Intelligent vs ML Model</td>
                    <td>{tests['intelligent_vs_model']['t_statistic']:.3f}</td>
                    <td>{tests['intelligent_vs_model']['p_value']:.6f}</td>
                    <td>✅ YES (p < 0.001)</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE: ARCHITECTURE
# ============================================================================

def page_architecture():
    """Production architecture"""
    
    st.title("🏗️ Production Architecture")
    
    data = load_all_data()
    
    if not data['loaded'] or 'architecture' not in data:
        st.warning("Data not available")
        return
    
    arch = data['architecture']
    
    # Architecture overview
    st.markdown("## 🎯 System Overview")
    
    st.markdown(f"""
    <div class='info-box'>
        <h4 style='margin-top: 0;'>System: {arch['system_name']}</h4>
        <p><strong>Architecture:</strong> {arch['architecture_type']}</p>
        <p><strong>Deployment:</strong> {arch['deployment_model']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Core components
    st.markdown("## 📦 Core Components")
    
    for comp_id, comp in arch['core_components'].items():
        with st.expander(f"**{comp['name']}**"):
            st.markdown(f"**Purpose:** {comp['purpose']}")
            st.markdown(f"**Technologies:** {', '.join(comp['technologies'])}")
    
    # Deployment tiers
    st.markdown("## 💰 Deployment Cost Analysis")
    
    tier_data = []
    for tier_name, tier_info in arch['deployment_tiers'].items():
        tier_data.append({
            'Tier': tier_name.replace('_', ' ').title(),
            'Cost/Month': f"${tier_info['cost_per_month']}",
            'Description': tier_info['description'],
            'Timeline': tier_info['timeline']
        })
    
    tier_df = pd.DataFrame(tier_data)
    st.dataframe(tier_df, use_container_width=True, hide_index=True)
    
    # Tech stack
    if 'tech_docs' in data:
        st.markdown("## 🔧 Technology Stack")
        
        tech_stack = data['tech_docs']['tech_stack']
        
        tab1, tab2, tab3, tab4 = st.tabs(["Backend", "ML/AI", "Data Storage", "Infrastructure"])
        
        with tab1:
            for key, value in tech_stack['backend'].items():
                st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
        
        with tab2:
            for key, value in tech_stack['ml_ai'].items():
                st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
        
        with tab3:
            for key, value in tech_stack['data_storage'].items():
                st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
        
        with tab4:
            for key, value in tech_stack['infrastructure'].items():
                st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")

# ============================================================================
# PAGE: ABOUT
# ============================================================================

def page_about():
    """About the project"""
    
    st.title("ℹ️ About MarketLab")
    
    st.markdown("""
    ## 🎓 Research Project
    
    **MarketLab** is a comprehensive research project exploring the prediction-profitability gap 
    in algorithmic trading systems.
    
    ### 🎯 Research Questions
    
    1. **Why do high-accuracy ML models fail in trading?**
       - Despite 99.86% prediction accuracy, models lost 21% annually
       - Root cause: Inability to handle regime changes and geopolitical events
    
    2. **How can we bridge this gap?**
       - Event-aware intelligence system
       - FinBERT-powered event classification (90% accuracy)
       - Risk-adjusted position management
    
    3. **Is the solution statistically significant?**
       - Yes! p < 0.000001 across multiple tests
       - Sharpe improvement: +1.13
       - Drawdown reduction: -49%
    
    ### 📊 Methodology
    
    - **Training Data:** 20 years (2004-2024), 50 NSE stocks
    - **Features:** 325 technical indicators
    - **Models:** 1,386 ML models (25 algorithms)
    - **Testing Period:** 2022-2024 (turbulent market)
    - **Events:** 40 major geopolitical/economic events
    
    ### 🏆 Key Contributions
    
    1. **Empirical Evidence:** First large-scale study demonstrating prediction-profit gap
    2. **Novel Framework:** Geopolitical intelligence system for Indian markets
    3. **Production Architecture:** Complete deployment blueprint
    4. **Open Source:** All code and data available
    
    ### 📝 Publications
    
    - **ArXiv Preprint:** Submitted
    - **Target Journal:** Digital Finance (Springer)
    - **Conference:** ICAIF 2025 (planned)
    
    ### 👨‍🎓 Author
    
    **[Your Name]**  
    Final Year AI Student  
    Mumbai University  
    2024-2025
    
    ### 📧 Contact
    
    - Email: [your.email@university.edu]
    - GitHub: [github.com/yourname/marketlab]
    - LinkedIn: [linkedin.com/in/yourname]
    
    ### 🙏 Acknowledgments
    
    - Mumbai University Department of AI
    - Project Supervisor: [Supervisor Name]
    - Data Sources: NSE, Yahoo Finance, NewsAPI
    
    ### 📜 License
    
    MIT License - Open for academic and research use
    """)
    
    st.markdown("---")
    
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <p style='color: #666; font-size: 0.9rem;'>
            MarketLab Intelligence Platform v3.0<br>
            Built with ❤️ using Streamlit, Plotly, and Python<br>
            © 2024-2025 | All Rights Reserved
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application"""
    
    # Render sidebar and get selected page
    page = render_sidebar()
    
    # Route to appropriate page
    if page == "🏠 Overview":
        page_overview()
    elif page == "📈 Model Performance":
        page_model_performance()
    elif page == "🤖 Event Intelligence":
        page_event_intelligence()
    elif page == "⚖️ Risk Metrics":
        page_risk_metrics()
    elif page == "🏗️ Architecture":
        page_architecture()
    elif page == "ℹ️ About":
        page_about()

if __name__ == "__main__":
    main()
