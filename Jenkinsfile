pipeline {
  agent any
  environment {
    VENV_DIR = ".venv"
  }
  stages {
    stage("Setup") {
      steps {
        sh "python3 -m venv ${VENV_DIR}"
        sh ". ${VENV_DIR}/bin/activate && pip install -r requirements.txt"
        sh ". ${VENV_DIR}/bin/activate && python -m playwright install --with-deps"
      }
    }
    stage("Smoke") {
      when {
        expression { return params.SUITE == "smoke" }
      }
      steps {
        sh ". ${VENV_DIR}/bin/activate && pytest -m smoke --html=artifacts/report.html --self-contained-html --alluredir=artifacts/allure"
      }
    }
    stage("Regression") {
      when {
        expression { return params.SUITE == "regression" }
      }
      steps {
        sh \". ${VENV_DIR}/bin/activate && pytest -m 'regression and not smoke' --html=artifacts/report.html --self-contained-html --alluredir=artifacts/allure\"
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: "artifacts/**", allowEmptyArchive: true
    }
  }
}
