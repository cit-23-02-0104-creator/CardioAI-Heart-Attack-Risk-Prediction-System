from pathlib import Path
import json
import html

import joblib
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CardioAI | Heart Risk Intelligence",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROJECT PATHS / MODEL CONFIG
# ============================================================

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "best_model.joblib"
METRICS_PATH = ROOT / "results" / "metrics.json"

DEFAULT_FEATURES = [
    "age",
    "sex",
    "total_cholesterol",
    "ldl",
    "hdl",
    "systolic_bp",
    "diastolic_bp",
    "smoking",
    "diabetes",
]

FEATURE_LABELS = {
    "age": "Age",
    "sex": "Sex",
    "total_cholesterol": "Total Cholesterol",
    "ldl": "LDL Cholesterol",
    "hdl": "HDL Cholesterol",
    "systolic_bp": "Systolic BP",
    "diastolic_bp": "Diastolic BP",
    "smoking": "Smoking",
    "diabetes": "Diabetes",
}


# ============================================================
# HELPERS
# ============================================================

def load_metrics():
    if not METRICS_PATH.exists():
        return {}
    try:
        return json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


@st.cache_resource

def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)


metrics_data = load_metrics()

try:
    model = load_model()
    model_error = None
except Exception as exc:
    model = None
    model_error = str(exc)


# Prefer the feature order saved inside the trained estimator.
if model is not None and hasattr(model, "feature_names_in_"):
    FEATURES = list(model.feature_names_in_)
elif metrics_data.get("features"):
    FEATURES = list(metrics_data["features"])
else:
    FEATURES = DEFAULT_FEATURES


best_model_name = metrics_data.get("best_model", "Logistic Regression")
all_model_metrics = metrics_data.get("metrics", {})
best_metrics = all_model_metrics.get(best_model_name, {})

accuracy = float(best_metrics.get("accuracy", 0.0))
precision = float(best_metrics.get("precision", 0.0))
recall = float(best_metrics.get("recall", 0.0))
f1 = float(best_metrics.get("f1", 0.0))
roc_auc = float(best_metrics.get("roc_auc", 0.0))
dataset_rows = int(metrics_data.get("dataset_rows", 0))


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
<style>

:root {
    --bg: #050812;
    --panel: rgba(15, 23, 42, 0.72);
    --panel-strong: rgba(13, 20, 37, 0.94);
    --border: rgba(148, 163, 184, 0.13);
    --muted: #7f8da5;
    --text: #f8fafc;
    --cyan: #4de7ff;
    --blue: #5b8cff;
    --pink: #ff5f9d;
    --green: #28e0a2;
}

.stApp {
    background:
        radial-gradient(circle at 7% 4%, rgba(77,231,255,.10), transparent 22%),
        radial-gradient(circle at 92% 8%, rgba(255,95,157,.09), transparent 23%),
        radial-gradient(circle at 52% 92%, rgba(91,140,255,.08), transparent 28%),
        var(--bg);
    color: var(--text);
}

.main .block-container {
    max-width: 1480px;
    padding: 1.8rem 2.2rem 4rem;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #070b16 0%, #050812 100%);
    border-right: 1px solid rgba(148,163,184,.10);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.6rem;
}

/* Inputs */
div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"] {
    background: rgba(255,255,255,.025);
    border: 1px solid rgba(148,163,184,.10);
    border-radius: 17px;
    padding: 13px 13px 8px;
    margin-bottom: 10px;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,.045) !important;
    border: 1px solid rgba(148,163,184,.12) !important;
    border-radius: 11px !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="select"] > div:focus-within {
    border-color: rgba(77,231,255,.55) !important;
    box-shadow: 0 0 0 3px rgba(77,231,255,.07) !important;
}

label {
    color: #b9c4d6 !important;
    font-size: 12px !important;
    font-weight: 650 !important;
}

/* Buttons */
div.stButton > button {
    min-height: 58px;
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 15px;
    background: linear-gradient(105deg, #087ff5, #08c9e8 48%, #755cff);
    color: white;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: .2px;
    box-shadow: 0 18px 45px rgba(15,130,240,.23);
    transition: .2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 23px 55px rgba(15,160,255,.32);
}

/* Metrics */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(255,255,255,.055), rgba(255,255,255,.018));
    border: 1px solid var(--border);
    border-radius: 19px;
    padding: 18px;
    min-height: 116px;
    box-shadow: 0 20px 55px rgba(0,0,0,.16);
}

div[data-testid="stMetricLabel"] { color: #71819b !important; }
div[data-testid="stMetricValue"] { color: white !important; font-weight: 800 !important; }

/* Alerts */
div[data-testid="stAlert"] { border-radius: 16px !important; }

/* Expanders */
details[data-testid="stExpander"] {
    background: rgba(255,255,255,.025);
    border: 1px solid rgba(148,163,184,.10);
    border-radius: 15px;
}

/* Progress */
div[data-testid="stProgressBar"] {
    margin: 8px 0 14px;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid rgba(148,163,184,.10);
    border-radius: 14px;
    overflow: hidden;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.html(
        """
        <div style="padding:4px 2px 18px;">
            <div style="font-size:25px;font-weight:850;color:#fff;letter-spacing:-.7px;">
                ❤️ Cardio<span style="color:#4de7ff;">AI</span>
            </div>
            <div style="font-size:9px;letter-spacing:2.4px;color:#60718c;margin-top:5px;text-transform:uppercase;">
                Heart Risk Intelligence
            </div>
        </div>
        """
    )

    st.markdown("---")

    status_text = "AI ENGINE ONLINE" if model is not None else "MODEL OFFLINE"
    status_color = "#28e0a2" if model is not None else "#ff647c"

    st.html(
        f"""
        <div style="
            padding:18px;
            border-radius:19px;
            background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018));
            border:1px solid rgba(148,163,184,.11);
            box-shadow:0 18px 45px rgba(0,0,0,.20);
            margin-bottom:14px;
        ">
            <div style="font-size:9px;letter-spacing:1.8px;color:#657895;text-transform:uppercase;margin-bottom:9px;">
                System Status
            </div>
            <div style="font-size:14px;font-weight:800;color:#fff;">
                <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:{status_color};box-shadow:0 0 14px {status_color};margin-right:8px;"></span>
                {status_text}
            </div>
        </div>
        """
    )

    st.html(
        f"""
        <div style="
            padding:18px;
            border-radius:19px;
            background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018));
            border:1px solid rgba(148,163,184,.11);
            margin-bottom:14px;
        ">
            <div style="font-size:9px;letter-spacing:1.8px;color:#657895;text-transform:uppercase;margin-bottom:9px;">
                Prediction Engine
            </div>
            <div style="font-size:14px;font-weight:800;color:#fff;">
                {html.escape(best_model_name)}
            </div>
            <div style="font-size:10px;color:#657895;margin-top:6px;">
                Trained classification pipeline
            </div>
        </div>
        """
    )

    st.html(
        f"""
        <div style="
            padding:18px;
            border-radius:19px;
            background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018));
            border:1px solid rgba(148,163,184,.11);
        ">
            <div style="font-size:9px;letter-spacing:1.8px;color:#657895;text-transform:uppercase;margin-bottom:12px;">
                Validation Snapshot
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:13px;">
                <div><div style="font-size:20px;font-weight:850;color:#fff;">{accuracy:.1%}</div><div style="font-size:9px;color:#667893;">ACCURACY</div></div>
                <div><div style="font-size:20px;font-weight:850;color:#fff;">{roc_auc:.1%}</div><div style="font-size:9px;color:#667893;">ROC-AUC</div></div>
                <div><div style="font-size:20px;font-weight:850;color:#fff;">{recall:.1%}</div><div style="font-size:9px;color:#667893;">RECALL</div></div>
                <div><div style="font-size:20px;font-weight:850;color:#fff;">{dataset_rows:,}</div><div style="font-size:9px;color:#667893;">ROWS</div></div>
            </div>
        </div>
        """
    )

    st.html(
        """
        <div style="margin-top:26px;padding:0 2px;color:#46556d;font-size:9px;line-height:1.8;letter-spacing:1px;">
            CARDIOAI V1.0<br>
            MACHINE LEARNING DEMONSTRATION
        </div>
        """
    )


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div style="
        position:relative;
        overflow:hidden;
        padding:42px 46px;
        border-radius:30px;
        background:
            radial-gradient(circle at 87% 25%,rgba(77,231,255,.12),transparent 24%),
            radial-gradient(circle at 78% 90%,rgba(255,95,157,.08),transparent 22%),
            linear-gradient(135deg,rgba(15,28,53,.94),rgba(7,12,25,.96));
        border:1px solid rgba(148,163,184,.14);
        box-shadow:0 35px 90px rgba(0,0,0,.30);
    ">
        <div style="
            display:inline-block;
            padding:7px 13px;
            border-radius:999px;
            background:rgba(77,231,255,.07);
            border:1px solid rgba(77,231,255,.22);
            color:#64eaff;
            font-size:9px;
            font-weight:800;
            letter-spacing:1.7px;
        ">
            ✦ AI-POWERED CARDIOVASCULAR INTELLIGENCE
        </div>

        <div style="font-size:clamp(35px,4.2vw,61px);line-height:1.02;font-weight:900;letter-spacing:-3px;color:#fff;margin-top:20px;">
            Heart Attack<br>
            <span style="background:linear-gradient(90deg,#4de7ff,#8f7dff,#ff6b9f);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                Risk Prediction
            </span>
        </div>

        <div style="max-width:760px;color:#8e9db4;font-size:14px;line-height:1.8;margin-top:17px;">
            Analyze cardiovascular indicators with a trained machine-learning model
            and receive an instant risk-class prediction with probability insights.
        </div>

        <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:24px;">
            <span style="padding:7px 11px;border-radius:10px;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.07);color:#aebbd0;font-size:10px;">9 HEALTH SIGNALS</span>
            <span style="padding:7px 11px;border-radius:10px;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.07);color:#aebbd0;font-size:10px;">REAL-TIME PREDICTION</span>
            <span style="padding:7px 11px;border-radius:10px;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.07);color:#aebbd0;font-size:10px;">EDUCATIONAL ML</span>
        </div>
    </div>
    """
)


# ============================================================
# OVERVIEW METRICS
# ============================================================

st.html(
    """
    <div style="margin:34px 0 17px;">
        <div style="font-size:23px;font-weight:850;color:#fff;">Model Intelligence</div>
        <div style="font-size:11px;color:#657792;margin-top:4px;">Validation performance from the trained model</div>
    </div>
    """
)

m1, m2, m3, m4 = st.columns(4, gap="medium")

with m1:
    st.metric("ACCURACY", f"{accuracy:.1%}", "test set")
with m2:
    st.metric("ROC-AUC", f"{roc_auc:.1%}", "discrimination")
with m3:
    st.metric("RECALL", f"{recall:.1%}", "positive class")
with m4:
    st.metric("F1 SCORE", f"{f1:.1%}", "balanced score")


# ============================================================
# MODEL ERROR
# ============================================================

if model_error:
    st.error(f"Model loading failed: {model_error}")

if model is None:
    st.warning(
        f"The trained model was not found. Expected: {MODEL_PATH}. "
        "Run `python src/train.py` first."
    )
    st.stop()


# ============================================================
# PATIENT INPUTS
# ============================================================

st.html(
    """
    <div style="margin:38px 0 17px;">
        <div style="font-size:23px;font-weight:850;color:#fff;">Patient Assessment</div>
        <div style="font-size:11px;color:#657792;margin-top:4px;">Enter the cardiovascular profile used by the prediction model</div>
    </div>
    """
)

left, right = st.columns(2, gap="large")

with left:
    st.html(
        """
        <div style="padding:20px 22px 4px;border:1px solid rgba(148,163,184,.10);border-radius:21px 21px 0 0;background:linear-gradient(145deg,rgba(20,35,61,.72),rgba(8,14,27,.72));">
            <div style="font-size:9px;letter-spacing:1.8px;font-weight:850;color:#4de7ff;">01 · PERSONAL PROFILE</div>
            <div style="font-size:11px;color:#61738e;margin-top:5px;">Basic patient characteristics</div>
        </div>
        """
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=120,
        value=50,
        step=1,
        help="Patient age in years.",
    )

    sex = st.selectbox(
        "Sex",
        options=[0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male",
        help="Encoded as 0 = Female, 1 = Male.",
    )

    smoking = st.selectbox(
        "Smoking",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes",
        help="Encoded as 0 = No, 1 = Yes.",
    )

    diabetes = st.selectbox(
        "Diabetes",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes",
        help="Encoded as 0 = No, 1 = Yes.",
    )

with right:
    st.html(
        """
        <div style="padding:20px 22px 4px;border:1px solid rgba(148,163,184,.10);border-radius:21px 21px 0 0;background:linear-gradient(145deg,rgba(38,23,45,.72),rgba(10,13,25,.72));">
            <div style="font-size:9px;letter-spacing:1.8px;font-weight:850;color:#ff6b9f;">02 · CARDIOVASCULAR PROFILE</div>
            <div style="font-size:11px;color:#61738e;margin-top:5px;">Cholesterol and blood pressure</div>
        </div>
        """
    )

    total_cholesterol = st.number_input(
        "Total Cholesterol",
        min_value=50.0,
        max_value=500.0,
        value=200.0,
        step=1.0,
        help="Total cholesterol measurement.",
    )

    ldl = st.number_input(
        "LDL Cholesterol",
        min_value=20.0,
        max_value=400.0,
        value=120.0,
        step=1.0,
        help="Low-density lipoprotein cholesterol.",
    )

    hdl = st.number_input(
        "HDL Cholesterol",
        min_value=10.0,
        max_value=150.0,
        value=50.0,
        step=1.0,
        help="High-density lipoprotein cholesterol.",
    )


bp1, bp2 = st.columns(2, gap="large")

with bp1:
    systolic_bp = st.number_input(
        "Systolic Blood Pressure",
        min_value=60.0,
        max_value=250.0,
        value=120.0,
        step=1.0,
        help="Systolic blood pressure.",
    )

with bp2:
    diastolic_bp = st.number_input(
        "Diastolic Blood Pressure",
        min_value=30.0,
        max_value=180.0,
        value=80.0,
        step=1.0,
        help="Diastolic blood pressure.",
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

predict_clicked = st.button(
    "⚡  RUN CARDIOAI RISK ANALYSIS",
    use_container_width=True,
    type="primary",
)


# ============================================================
# PREDICTION
# ============================================================

if predict_clicked:
    values = {
        "age": age,
        "sex": sex,
        "total_cholesterol": total_cholesterol,
        "ldl": ldl,
        "hdl": hdl,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "smoking": smoking,
        "diabetes": diabetes,
    }

    missing_features = [feature for feature in FEATURES if feature not in values]

    if missing_features:
        st.error(
            "The loaded model expects feature(s) that are not supported by this interface: "
            + ", ".join(missing_features)
        )
        st.stop()

    input_data = pd.DataFrame(
        [[values[feature] for feature in FEATURES]],
        columns=FEATURES,
    )

    try:
        prediction = int(model.predict(input_data)[0])

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            classes = list(getattr(model, "classes_", [0, 1]))

            if 1 in classes:
                positive_index = classes.index(1)
                risk_probability = float(probabilities[positive_index])
            else:
                risk_probability = 1.0 if prediction == 1 else 0.0
        else:
            risk_probability = float(prediction)

        risk_probability = max(0.0, min(1.0, risk_probability))
        risk_percent = risk_probability * 100

        # ----------------------------------------------------
        # RESULT HEADER
        # ----------------------------------------------------

        st.html(
            """
            <div style="margin:42px 0 17px;">
                <div style="font-size:23px;font-weight:850;color:#fff;">Risk Assessment</div>
                <div style="font-size:11px;color:#657792;margin-top:4px;">Model output generated from the submitted profile</div>
            </div>
            """
        )

        # ----------------------------------------------------
        # RESULT CARD
        # ----------------------------------------------------

        if prediction == 1:
            result_title = "Higher Predicted Risk"
            result_label = "HIGHER RISK"
            result_color = "#ff5f78"
            result_bg = "rgba(255,70,100,.09)"
            result_border = "rgba(255,95,120,.24)"
            result_icon = "⚠️"
            result_text = "The model classified this profile into the positive risk class."
        else:
            result_title = "Lower Predicted Risk"
            result_label = "LOWER RISK"
            result_color = "#28e0a2"
            result_bg = "rgba(40,224,162,.08)"
            result_border = "rgba(40,224,162,.22)"
            result_icon = "✓"
            result_text = "The model classified this profile into the lower-risk class."

        gauge_degree = risk_percent * 3.6

        st.html(
            f"""
            <div style="
                padding:30px;
                border-radius:27px;
                background:
                    radial-gradient(circle at 50% 0%,rgba(77,231,255,.05),transparent 36%),
                    linear-gradient(145deg,rgba(15,25,45,.94),rgba(7,12,24,.97));
                border:1px solid rgba(148,163,184,.13);
                box-shadow:0 30px 80px rgba(0,0,0,.28);
            ">
                <div style="display:flex;align-items:center;justify-content:center;gap:9px;color:{result_color};font-size:10px;font-weight:850;letter-spacing:1.8px;">
                    <span>{result_icon}</span>{result_label}
                </div>

                <div style="text-align:center;font-size:32px;font-weight:900;color:#fff;margin-top:10px;">
                    {result_title}
                </div>

                <div style="text-align:center;color:#71819a;font-size:12px;margin-top:7px;">
                    {result_text}
                </div>

                <div style="display:flex;justify-content:center;margin:28px 0 22px;">
                    <div style="
                        width:190px;
                        height:190px;
                        border-radius:50%;
                        padding:13px;
                        background:conic-gradient({result_color} 0deg {gauge_degree:.1f}deg, rgba(255,255,255,.065) {gauge_degree:.1f}deg 360deg);
                        box-shadow:0 0 45px {result_color}18;
                    ">
                        <div style="
                            width:100%;height:100%;border-radius:50%;
                            display:flex;flex-direction:column;align-items:center;justify-content:center;
                            background:#080e1b;
                            border:1px solid rgba(255,255,255,.06);
                        ">
                            <div style="font-size:42px;line-height:1;font-weight:900;color:#fff;letter-spacing:-2px;">{risk_percent:.1f}%</div>
                            <div style="font-size:9px;letter-spacing:1.7px;color:#687993;margin-top:8px;">RISK PROBABILITY</div>
                        </div>
                    </div>
                </div>

                <div style="max-width:650px;margin:auto;height:7px;border-radius:999px;background:rgba(255,255,255,.06);overflow:hidden;">
                    <div style="height:100%;width:{risk_percent:.2f}%;border-radius:999px;background:linear-gradient(90deg,#28e0a2,#4de7ff,#ff5f78);"></div>
                </div>

                <div style="display:flex;justify-content:space-between;max-width:650px;margin:8px auto 0;color:#52637c;font-size:9px;">
                    <span>LOW</span><span>MODEL PROBABILITY</span><span>HIGH</span>
                </div>
            </div>
            """
        )

        # ----------------------------------------------------
        # RESULT METRICS
        # ----------------------------------------------------

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        r1, r2, r3 = st.columns(3, gap="medium")

        with r1:
            st.metric("PREDICTION", result_label)
        with r2:
            st.metric("RISK PROBABILITY", f"{risk_percent:.1f}%")
        with r3:
            st.metric("ENGINE", best_model_name)

        # ----------------------------------------------------
        # PROFILE SUMMARY
        # ----------------------------------------------------

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        with st.expander("📊  VIEW SUBMITTED HEALTH PROFILE"):
            display_values = []
            for feature in FEATURES:
                value = values[feature]
                if feature == "sex":
                    value = "Female" if value == 0 else "Male"
                elif feature in {"smoking", "diabetes"}:
                    value = "No" if value == 0 else "Yes"

                display_values.append(
                    {
                        "Health Indicator": FEATURE_LABELS.get(feature, feature.replace("_", " ").title()),
                        "Value": value,
                    }
                )

            st.dataframe(
                pd.DataFrame(display_values),
                use_container_width=True,
                hide_index=True,
            )

    except Exception as exc:
        st.error("Prediction failed. Please check the model and input feature configuration.")
        st.exception(exc)


# ============================================================
# MODEL DETAILS
# ============================================================

st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

with st.expander("🧠  MODEL & DATASET DETAILS"):
    c1, c2 = st.columns(2)

    with c1:
        st.write("**Best model**")
        st.code(best_model_name)

        st.write("**Dataset size**")
        st.code(f"{dataset_rows:,} rows")

        st.write("**Target**")
        st.code(str(metrics_data.get("target", "heart_attack")))

    with c2:
        st.write("**Features used**")
        st.code("\n".join(FEATURES))

        st.write("**Model file**")
        st.code(str(MODEL_PATH))


# ============================================================
# DISCLAIMER / FOOTER
# ============================================================

st.html(
    """
    <div style="
        margin-top:48px;
        padding:24px 10px 5px;
        border-top:1px solid rgba(148,163,184,.08);
        text-align:center;
        color:#46556d;
        font-size:10px;
        line-height:1.9;
    ">
        <div style="color:#70819a;font-weight:800;letter-spacing:1px;">
            CARDIOAI · HEART RISK INTELLIGENCE
        </div>
        <div style="margin-top:7px;">
            ⚠️ Educational machine-learning demonstration only. Not a medical device or diagnostic tool.
        </div>
        <div>
            Do not use this prediction for medical decisions or emergencies. Consult a qualified healthcare professional.
        </div>
    </div>
    """
)
