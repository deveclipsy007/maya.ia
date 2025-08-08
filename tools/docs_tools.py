from agno.tools import tool

class DocsTools:
    @tool
    def issue_report(self, appointment_id: str, text: str, kind: str = "laudo") -> dict:
        # Geraria e armazenaria um PDF/HTML; aqui mock
        return {"doc_id": "DOC123", "url": "https://example.com/doc.pdf", "kind": kind}
