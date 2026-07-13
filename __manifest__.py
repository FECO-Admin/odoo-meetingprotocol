{
    "name": "Meetingprotokolle",
    "version": "19.0.1.0.0",
    "category": "Productivity",
    "license": "LGPL-3",
    "author": "FE Gruppe",
    "summary": "Meetingprotokolle mit Teilnehmern, Tagesordnung und Aufgaben",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/meeting_protocol_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
