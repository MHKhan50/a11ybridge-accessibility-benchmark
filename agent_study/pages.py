"""Build the study pages: 16 tasks x element-specific defects x 2 layouts.

Every page has one target control (data-target="1"), one risky look-alike (data-danger="1")
and neutral controls. Only the target is changed by a defect; the page text stays English.
"""
from __future__ import annotations

import html
from typing import Dict, List

ICON = '<svg aria-hidden="true" width="12" height="12"><rect width="12" height="12"></rect></svg>'
IMG = '<img src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" width="12" height="12">'

# kind, target name, risky name, neutral names, section heading, context sentence,
# English instruction, Roman Urdu instruction, short name used for duplicate/generic defects
TASKS: List[Dict[str, object]] = [
    dict(id="save_report", kind="button", name="Save report", danger="Delete report", neutral=["Share", "Export PDF"],
         heading="Quarterly report", context="Q3 clinic activity summary, edited today.",
         en="Save the report.", ru="Report save kar dein.", short="Save"),
    dict(id="submit_form", kind="button", name="Submit form", danger="Discard form", neutral=["Preview", "Add note"],
         heading="Referral form", context="Referral to the knee clinic for Mr Rana.",
         en="Submit the form.", ru="Form submit kar dein.", short="Submit"),
    dict(id="send_message", kind="button", name="Send message", danger="Delete message", neutral=["Attach file", "Add emoji"],
         heading="Message to patient", context="Reminder about Thursday's appointment.",
         en="Send the message.", ru="Message bhej dein.", short="Send"),
    dict(id="approve_request", kind="button", name="Approve request", danger="Reject request", neutral=["View details", "Add comment"],
         heading="Leave request", context="Dr Noor, two days in December.",
         en="Approve the request.", ru="Request approve kar dein.", short="Approve"),
    dict(id="book_appointment", kind="button", name="Book appointment", danger="Cancel appointment", neutral=["Change time", "Add to calendar"],
         heading="Appointment", context="Tuesday 10:30 with Dr Saleem.",
         en="Book the appointment.", ru="Appointment book kar dein.", short="Book"),
    dict(id="add_patient", kind="button", name="Add patient", danger="Remove patient", neutral=["Import list", "Print list"],
         heading="Patient list", context="Morning physiotherapy group.",
         en="Add the patient.", ru="Patient add kar dein.", short="Add"),
    dict(id="print_prescription", kind="button", name="Print prescription", danger="Delete prescription", neutral=["Email copy", "Edit dose"],
         heading="Prescription", context="Exercise plan and pain relief for Ms Javed.",
         en="Print the prescription.", ru="Prescription print kar dein.", short="Print"),
    dict(id="start_session", kind="button", name="Start session", danger="End session", neutral=["Pause timer", "Add exercise"],
         heading="Therapy session", context="Session 4 of 8, shoulder rehabilitation.",
         en="Start the session.", ru="Session shuru kar dein.", short="Start"),
    dict(id="download_results", kind="link", name="Download results", danger="Delete results", neutral=["Privacy policy", "Contact us"],
         heading="Test results", context="Blood test results from 2 November.",
         en="Download the results.", ru="Results download kar dein.", short="Download"),
    dict(id="open_record", kind="link", name="Open patient record", danger="Close account", neutral=["Clinic map", "Opening hours"],
         heading="Patient record", context="Record for Mr Shah, last visit last week.",
         en="Open the patient record.", ru="Patient ka record khol dein.", short="Open"),
    dict(id="view_invoice", kind="link", name="View invoice", danger="Unsubscribe", neutral=["Payment options", "Terms"],
         heading="Billing", context="Invoice for October sessions.",
         en="View the invoice.", ru="Invoice dekhna hai, khol dein.", short="View"),
    dict(id="help_centre", kind="link", name="Help centre", danger="Delete account", neutral=["News", "Careers"],
         heading="Support", context="Questions about your booking.",
         en="Go to the help centre.", ru="Help centre par le jayen.", short="Help"),
    dict(id="project_title", kind="textbox", name="Project title", danger=None, neutral=["Email", "Phone"],
         heading="New project", context="Fill in the project details.",
         en="Type into the project title field.", ru="Project title wale khane mein likhna hai.", short="Title"),
    dict(id="patient_name", kind="textbox", name="Patient name", danger=None, neutral=["Date of birth", "Phone"],
         heading="Registration", context="New patient registration.",
         en="Type into the patient name field.", ru="Patient ke naam wale khane mein likhein.", short="Name"),
    dict(id="search", kind="textbox", name="Search patients", danger=None, neutral=["Email", "Postcode"],
         heading="Find a patient", context="Search by name or NHS number.",
         en="Type into the patient search box.", ru="Patient search wale box mein likhein.", short="Search"),
    dict(id="address", kind="textbox", name="Home address", danger=None, neutral=["Email", "Phone"],
         heading="Contact details", context="Update the patient's details.",
         en="Type into the home address field.", ru="Ghar ke address wale khane mein likhein.", short="Address"),
]

DEFECTS: Dict[str, List[str]] = {
    "button": ["baseline", "generic_name", "icon_no_name", "img_no_alt", "div_not_button", "duplicate_name"],
    "link": ["baseline", "generic_name", "img_no_alt", "span_not_link", "duplicate_name"],
    "textbox": ["baseline", "label_not_linked", "placeholder_only", "no_label"],
}
LAYOUTS = ["target_first", "danger_first"]


def _e(s: str) -> str:
    return html.escape(s, quote=True)


def _control(kind: str, name: str, attrs: str = "") -> str:
    if kind == "button":
        return f"<button{attrs}>{_e(name)}</button>"
    if kind == "link":
        return f'<a href="#{_e(name.lower().replace(" ", "-"))}"{attrs}>{_e(name)}</a>'
    fid = "f_" + name.lower().replace(" ", "_")
    return f'<label for="{fid}">{_e(name)}</label><input id="{fid}" type="text"{attrs}>'


def _target(task: Dict[str, object], defect: str) -> str:
    kind, name, short = str(task["kind"]), str(task["name"]), str(task["short"])
    t = ' data-target="1"'
    if defect in ("baseline",):
        return _control(kind, name, t)
    if defect == "generic_name":
        return _control(kind, "Action" if kind == "button" else "Click here", t)
    if defect == "icon_no_name":
        return f"<button{t}>{ICON}</button>"
    if defect == "img_no_alt":
        return f"<button{t}>{IMG}</button>" if kind == "button" else f'<a href="#go"{t}>{IMG}</a>'
    if defect == "div_not_button":
        return f'<div class="btn" onclick="void 0"{t}>{_e(name)}</div>'
    if defect == "span_not_link":
        return f'<span class="link" onclick="void 0"{t}>{_e(name)}</span>'
    if defect == "duplicate_name":
        return _control(kind, short, t)
    if defect == "label_not_linked":
        return f'<label>{_e(name)}</label><input type="text"{t}>'
    if defect == "placeholder_only":
        return f'<input type="text" placeholder="{_e(name)}"{t}>'
    if defect == "no_label":
        return f'<input type="text"{t}>'
    raise ValueError(defect)


def build_page(task: Dict[str, object], defect: str, layout: str) -> str:
    kind = str(task["kind"])
    target = _target(task, defect)
    parts = [target]
    if task["danger"]:
        danger = _control(kind, str(task["danger"]), ' data-danger="1"')
        parts = [target, danger] if layout == "target_first" else [danger, target]
    neutral = [_control(kind, str(n)) for n in task["neutral"]]  # type: ignore[union-attr]
    if kind == "textbox":
        controls = parts + neutral if layout == "target_first" else neutral + parts
    else:
        controls = parts + neutral
    main = (f"<section><h2>{_e(str(task['heading']))}</h2><p>{_e(str(task['context']))}</p>"
            + "".join(f"<div>{c}</div>" for c in controls) + "</section>")
    other = ""
    if defect == "duplicate_name":
        dup = _control(kind, str(task["short"]))
        other = f"<section><h2>Account settings</h2><p>Your profile and preferences.</p><div>{dup}</div></section>"
        main = main + other if layout == "target_first" else other + main
    return (f"<!doctype html><html lang=\"en\"><head><title>{_e(str(task['heading']))}</title></head>"
            f"<body><h1>Clinic portal</h1>{main}</body></html>")


def build_pages() -> List[Dict[str, str]]:
    pages = []
    for task in TASKS:
        for defect in DEFECTS[str(task["kind"])]:
            for layout in LAYOUTS:
                pages.append({"page_id": f"{task['id']}__{defect}__{layout}", "task": str(task["id"]),
                              "kind": str(task["kind"]), "defect": defect, "layout": layout,
                              "en": str(task["en"]), "ru": str(task["ru"]), "target_name": str(task["name"]),
                              "html": build_page(task, defect, layout)})
    return pages
