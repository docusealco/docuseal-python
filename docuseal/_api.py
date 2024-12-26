from docuseal._http import DocusealHttp


class DocusealApi:
    def __init__(self, key=None, url="https://api.docuseal.com", read_timeout=60, open_timeout=60):
        self.config = {}

        self.config["key"] = key
        self.config["url"] = url
        self.config["read_timeout"] = read_timeout
        self.config["open_timeout"] = open_timeout

        self.http = DocusealHttp(self.config)

    @property
    def key(self):
        return self.config["key"]

    @key.setter
    def key(self, value):
        self.config["key"] = value

    @property
    def url(self):
        return self.config["url"]

    @url.setter
    def url(self, value):
        self.config["url"] = value

    @property
    def read_timeout(self):
        return self.config["read_timeout"]

    @read_timeout.setter
    def read_timeout(self, value):
        self.config["read_timeout"] = value

    @property
    def open_timeout(self):
        return self.config["open_timeout"]

    @open_timeout.setter
    def open_timeout(self, value):
        self.config["open_timeout"] = value

    def list_templates(self, params=None):
        if params is None:
            params = {}
        return self.http.get("/templates", params)

    def get_template(self, template_id, params=None):
        if params is None:
            params = {}
        return self.http.get(f"/templates/{template_id}", params)

    def create_template_from_docx(self, data):
        return self.http.post("/templates/docx", data)

    def create_template_from_html(self, data):
        return self.http.post("/templates/html", data)

    def create_template_from_pdf(self, data):
        return self.http.post("/templates/pdf", data)

    def merge_templates(self, data):
        return self.http.post("/templates/merge", data)

    def clone_template(self, template_id, data):
        return self.http.post(f"/templates/{template_id}/clone", data)

    def update_template(self, template_id, data):
        return self.http.put(f"/templates/{template_id}", data)

    def update_template_documents(self, template_id, data):
        return self.http.put(f"/templates/{template_id}/documents", data)

    def archive_template(self, template_id):
        return self.http.delete(f"/templates/{template_id}")

    def permanently_delete_template(self, template_id):
        return self.http.delete(f"/templates/{template_id}", {"permanently": True})

    def list_submissions(self, params=None):
        if params is None:
            params = {}
        return self.http.get("/submissions", params)

    def get_submission(self, submission_id, params=None):
        if params is None:
            params = {}
        return self.http.get(f"/submissions/{submission_id}", params)

    def create_submission(self, data):
        return self.http.post("/submissions/init", data)

    def create_submission_from_emails(self, data):
        return self.http.post("/submissions/emails", data)

    def archive_submission(self, submission_id):
        return self.http.delete(f"/submissions/{submission_id}")

    def permanently_delete_submission(self, submission_id):
        return self.http.delete(f"/submissions/{submission_id}", {"permanently": True})

    def list_submitters(self, params=None):
        if params is None:
            params = {}
        return self.http.get("/submitters", params)

    def get_submitter(self, submitter_id, params=None):
        if params is None:
            params = {}
        return self.http.get(f"/submitters/{submitter_id}", params)

    def update_submitter(self, submitter_id, data):
        return self.http.put(f"/submitters/{submitter_id}", data)

