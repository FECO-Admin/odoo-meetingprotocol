from odoo import fields, models


class MeetingActionItem(models.Model):
    _name = "meeting.action.item"
    _description = "Aufgabe aus Meeting"
    _order = "deadline, id"

    protocol_id = fields.Many2one(
        "meeting.protocol",
        string="Protokoll",
        required=True,
        ondelete="cascade",
    )
    name = fields.Char(string="Aufgabe", required=True)
    responsible_id = fields.Many2one("res.partner", string="Verantwortlich")
    deadline = fields.Date(string="Deadline")
    state = fields.Selection(
        [
            ("open", "Offen"),
            ("done", "Erledigt"),
            ("cancelled", "Storniert"),
        ],
        default="open",
        string="Status",
    )
