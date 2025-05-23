# JobFit AI Agent

JobFit AI Agent is a Streamlit-powered tool that helps job seekers:

* Compare their resume with a job description
* Identify skill gaps and missing requirements
* Receive personalized project ideas to bridge those gaps
* Get actionable suggestions to improve their resume

---

## 🚀 Features

* Upload resume and job description (PDF, DOCX, TXT)
* Automatic keyword and skill extraction
* Skill gap analysis with matching checklist
* Personalized project recommendations
* Resume improvement suggestions
* Session history tracking

---

## 🛠️ Getting Started

### Prerequisites

* Python 3.9+
* [conda](https://docs.conda.io/en/latest/)

### Installation

```bash
# Clone the repository
$ git clone https://github.com/yourusername/jobfit-ai-agent
$ cd jobfit-ai-agent

# Set up the conda environment
$ conda env create -f environment.yml
$ conda activate jobfit-ai

# Launch the app
$ streamlit run main.py
```

---

## 📄 Usage

1. Upload your resume and the job description in the Streamlit app.
2. Wait for the analysis to complete.
3. Review:

   * Skills you already have
   * Missing skills
   * Suggested projects
   * Resume improvements

---

## ⚙️ Configuration

### `.env.template`

```
# Example .env.template file
# (copy to .env and fill in real values if external APIs are added in future)
OPENAI_API_KEY=
```

---

## 🧰 Project Structure

```
├── app/
│   ├── resume_parser.py
│   ├── job_parser.py
│   ├── gap_analyzer.py
│   ├── project_recommender.py
│   ├── resume_optimizer.py
│   └── session_state.py
├── logs/
├── main.py
├── requirements.txt
├── environment.yml
├── README.md
```

---

## 🐛 Troubleshooting

* **Text not extracting properly**:

  * Ensure the files are formatted well (not image-based PDFs)
* **Streamlit not launching**:

  * Make sure the `conda` environment is activated
* **Missing packages**:

  * Run `pip install -r requirements.txt` to catch any extras

---

## 📬 Feedback

Found a bug or want a new feature? Open an issue or submit a pull request!

---

## 📘 License

This project is licensed under the MIT License.