# DocuSeal Python

The DocuSeal Python library provides seamless integration with the DocuSeal API, allowing developers to interact with DocuSeal's electronic signature and document management features directly within Python applications. This library is designed to simplify API interactions and provide tools for efficient implementation.

## Documentation

Detailed documentation is available at [DocuSeal API Docs](https://www.docuseal.com/docs/api?lang=python).

## Requirements

Python 3.5 and later.

## Installation

```sh
pip install --upgrade docuseal
```

Install from source with:

```sh
python setup.py install
```

## Usage

### Configuration

Set up the library with your DocuSeal API key based on your deployment. Retrieve your API key from the appropriate location:

#### Global Cloud

API keys for the global cloud can be obtained from your [Global DocuSeal Console](https://console.docuseal.com/api).

```python
from docuseal import docuseal

docuseal.key = "API_KEY"
```

#### EU Cloud

API keys for the EU cloud can be obtained from your [EU DocuSeal Console](https://console.docuseal.eu/api).

```python
from docuseal import docuseal

docuseal.key = "API_KEY"
docuseal.url = "https://api.docuseal.eu"
```

#### On-Premises

For on-premises installations, API keys can be retrieved from the API settings page of your deployed application, e.g., https://yourdocusealapp.com/settings/api.

```python
from docuseal import docuseal

docuseal.key = "API_KEY"
docuseal.url = "https://yourdocusealapp.com/api"
```

## API Methods

### list_submissions(params)

[Documentation](https://www.docuseal.com/docs/api?lang=python#list-all-submissions)

Provides the ability to retrieve a list of available submissions.


```python
docuseal.list_submissions({ "limit": 10 })
```

### get_submission(id)

[Documentation](https://www.docuseal.com/docs/api?lang=python#get-a-submission)

Provides the functionality to retrieve information about a submission.


```python
docuseal.get_submission(1001)
```

### create_submission(data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#create-a-submission)

This API endpoint allows you to create signature requests (submissions) for a document template and send them to the specified submitters (signers).

**Related Guides:**<br>
[Send documents for signature via API](https://www.docuseal.com/guides/send-documents-for-signature-via-api)
[Pre-fill PDF document form fields with API](https://www.docuseal.com/guides/pre-fill-pdf-document-form-fields-with-api)


```python
docuseal.create_submission({
  "template_id": 1000001,
  "send_email": True,
  "submitters": [
    {
      "role": "First Party",
      "email": "john.doe@example.com"
    }
  ]
})
```

### create_submission_from_emails(data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#create-submissions-from-emails)

This API endpoint allows you to create submissions for a document template and send them to the specified email addresses. This is a simplified version of the POST /submissions API to be used with Zapier or other automation tools.


```python
docuseal.create_submission_from_emails({
  "template_id": 1000001,
  "emails": "hi@docuseal.com, example@docuseal.com"
})
```

### archive_submission(id)

[Documentation](https://www.docuseal.com/docs/api?lang=python#archive-a-submission)

Allows you to archive a submission.


```python
docuseal.archive_submission(1001)
```

### list_submissions(params)

[Documentation](https://www.docuseal.com/docs/api?lang=python#list-all-submitters)

Provides the ability to retrieve a list of submitters.


```python
docuseal.list_submissions({ "limit": 10 })
```

### get_submitter(id)

[Documentation](https://www.docuseal.com/docs/api?lang=python#get-a-submitter)

Provides the functionality to retrieve information about a submitter.


```python
docuseal.get_submitter(500001)
```

### update_submitter(id, data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#update-a-submitter)

Allows you to update submitter details, pre-fill or update field values and re-send emails.

**Related Guides:**<br>
[Automatically sign documents via API](https://www.docuseal.com/guides/pre-fill-pdf-document-form-fields-with-api#automatically_sign_documents_via_api)


```python
docuseal.update_submitter(500001, {
  "email": "john.doe@example.com",
  "fields": [
    {
      "name": "First Name",
      "default_value": "Acme"
    }
  ]
})
```

### list_submissions(params)

[Documentation](https://www.docuseal.com/docs/api?lang=python#list-all-templates)

Provides the ability to retrieve a list of available document templates.


```python
docuseal.list_submissions({ "limit": 10 })
```

### get_template(id)

[Documentation](https://www.docuseal.com/docs/api?lang=python#get-a-template)

Provides the functionality to retrieve information about a document template.


```python
docuseal.get_template(1000001)
```

### create_template_from_docx(data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#create-a-template-from-word-docx)

Provides the functionality to create a fillable document template for existing Microsoft Word document. Use `{{Field Name;role=Signer1;type=date}}` text tags to define fillable fields in the document. See [https://www.docuseal.com/examples/fieldtags.docx](https://www.docuseal.com/examples/fieldtags.docx) for more text tag formats. Or specify the exact pixel coordinates of the document fields using `fields` param.

**Related Guides:**<br>
[Use embedded text field tags to create a fillable form](https://www.docuseal.com/guides/use-embedded-text-field-tags-in-the-pdf-to-create-a-fillable-form)


```python
docuseal.create_template_from_docx({
  "name": "Test DOCX",
  "documents": [
    {
      "name": "string",
      "file": "base64"
    }
  ]
})
```

### create_template_from_html(data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#create-a-template-from-html)

Provides the functionality to seamlessly generate a PDF document template by utilizing the provided HTML content while incorporating pre-defined fields.

**Related Guides:**<br>
[Create PDF document fillable form with HTML](https://www.docuseal.com/guides/create-pdf-document-fillable-form-with-html-api)


```python
docuseal.create_template_from_html({
  "html": """<p>Lorem Ipsum is simply dummy text of the
<text-field
  name=\"Industry\"
  role=\"First Party\"
  required=\"false\"
  style=\"width: 80px; height: 16px; display: inline-block; margin-bottom: -4px\">
</text-field>
and typesetting industry</p>
""",
  "name": "Test Template"
})
```

### merge_templates(data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#merge-templates)

Allows you to merge multiple templates with documents and fields into a new combined template.


```python
docuseal.merge_templates({
  "template_ids": [
    321,
    432
  ],
  "name": "Merged Template"
})
```

### create_template_from_pdf(data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#create-a-template-from-existing-pdf)

Provides the functionality to create a fillable document template for existing PDF file. Use `{{Field Name;role=Signer1;type=date}}` text tags to define fillable fields in the document. See [https://www.docuseal.com/examples/fieldtags.pdf](https://www.docuseal.com/examples/fieldtags.pdf) for more text tag formats. Or specify the exact pixel coordinates of the document fields using `fields` param.

**Related Guides:**<br>
[Use embedded text field tags to create a fillable form](https://www.docuseal.com/guides/use-embedded-text-field-tags-in-the-pdf-to-create-a-fillable-form)


```python
docuseal.create_template_from_pdf({
  "name": "Test PDF",
  "documents": [
    {
      "name": "string",
      "file": "base64",
      "fields": [
        {
          "name": "string",
          "areas": [
            {
              "x": 0,
              "y": 0,
              "w": 0,
              "h": 0,
              "page": 1
            }
          ]
        }
      ]
    }
  ]
})
```

### clone_template(id, data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#clone-a-template)

Allows you to clone existing template into a new template.


```python
docuseal.clone_template(1000001, {
  "name": "Cloned Template"
})
```

### update_template(id, data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#update-a-template)

Provides the functionality to move a document template to a different folder and update the name of the template.


```python
docuseal.update_template(1000001, {
  "name": "New Document Name",
  "folder_name": "New Folder"
})
```

### update_template_documents(id, data)

[Documentation](https://www.docuseal.com/docs/api?lang=python#update-template-documents)

Allows you to add, remove or replace documents in the template with provided PDF/DOCX file or HTML content.


```python
docuseal.update_template_documents(1000001, {
  "documents": [
    {
      "file": "string"
    }
  ]
})
```

### archive_template(id)

[Documentation](https://www.docuseal.com/docs/api?lang=python#archive-a-template)

Allows you to archive a document template.


```python
docuseal.archive_template(1000001)
```

### Configuring Timeouts

Set timeouts to avoid hanging requests:

```ruby
docuseal.open_timeout = 30
docuseal.read_timeout = 30
```

## Support

For feature requests or bug reports, visit our [GitHub Issues page](https://github.com/docusealco/docuseal-python/issues).


## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
