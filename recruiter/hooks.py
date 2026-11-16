# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "recruiter"
app_title = "Frappe Ai Hr Recruiter"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Ai Hr Recruiter for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/recruiter/css/recruiter.bundle.css"
app_include_js = "/assets/recruiter/js/recruiter.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "recruiter.engine.on_document_submit",
        "on_cancel": "recruiter.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "recruiter.engine.daily_scheduled_sync"
    ]
}
