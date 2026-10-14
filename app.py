
import streamlit as st

from analyzer import extract_resume_text, analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("AI Resume & Job Match Analyzer")
st.write(
    "Compare your resume with a job description "
    "and discover strengths, skill gaps, and improvements."
)

st.info(
    "The match score is an AI estimate, not an official ATS score "
    "or a prediction of hiring success."
)

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"],
)

job_description = st.text_area(
    "Paste the job description",
    height=220,
    placeholder="Paste the complete job description here...",
)

if st.button("Analyze Resume", type="primary"):
    if uploaded_file is None:
        st.error("Please upload a PDF resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    elif uploaded_file.size > 5 * 1024 * 1024:
        st.error("Please upload a PDF smaller than 5 MB.")

    else:
        try:
            with st.spinner("Analyzing your resume..."):
                resume_text = extract_resume_text(
                    uploaded_file.getvalue()
                )

                result = analyze_resume(
                    resume_text,
                    job_description.strip(),
                )

                st.session_state["analysis"] = result.model_dump()

        except ValueError as exc:
            st.error(str(exc))

        except Exception as exc:
            # Show a useful error while debugging locally.
            st.error(f"Analysis failed: {exc}")

if "analysis" in st.session_state:
    result = st.session_state["analysis"]

    st.divider()
    st.header("Your Analysis")

    left, right = st.columns([1, 2])

    with left:
        st.metric("Estimated Match", f"{result['match_score']}/100")
        st.progress(result["match_score"] / 100)

    with right:
        st.subheader("Summary")
        st.write(result["summary"])

    sections = [
        ("Matched Skills", "matched_skills"),
        ("Missing or Unclear Skills", "missing_or_unclear_skills"),
        ("Strengths", "strengths"),
        ("Improvement Suggestions", "improvement_suggestions"),
        ("Supporting Evidence", "evidence"),
    ]

    for title, key in sections:
        st.subheader(title)

        if result[key]:
            for item in result[key]:
                st.markdown(f"- {item}")
        else:
            st.write("No items identified.")

    report = "# AI Resume Analysis\n\n"
    report += f"**Estimated Match:** {result['match_score']}/100\n\n"
    report += f"## Summary\n{result['summary']}\n\n"

    for title, key in sections:
        report += f"## {title}\n"
        report += "\n".join(
            f"- {item}" for item in result[key]
        )
        report += "\n\n"

    report += (
        "Note: The match score is an AI estimate, "
        "not an official ATS score.\n"
    )

    st.download_button(
        "Download Analysis Report",
        data=report,
        file_name="resume_analysis.md",
        mime="text/markdown",
    )
